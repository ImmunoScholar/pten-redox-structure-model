"""
05_extract_pten_structure_features.py

Purpose:
Extract structure-derived residue features from the AlphaFold PTEN mmCIF model.

Input:
data/structures/AF-P60484-F1-model_v6.cif

Outputs:
data/processed/pten_alphafold_structure_features.csv
results/tables/pten_alphafold_residue_priority_scores.csv

Scientific boundary:
The input structure is an AlphaFold predicted model, not an experimentally
determined PTEN structure. Solvent accessibility and pLDDT values are therefore
model-derived features, not experimental measurements. The resulting score is a
prioritisation score, not evidence of electrophile modification or biochemical
reactivity.
"""

from pathlib import Path
from typing import Dict

import pandas as pd
from Bio.PDB import MMCIFParser, ShrakeRupley
from Bio.PDB.Polypeptide import protein_letters_3to1

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_CIF = PROJECT_ROOT / "data" / "structures" / "AF-P60484-F1-model_v6.cif"
OUTPUT_FEATURES = PROJECT_ROOT / "data" / "processed" / "pten_alphafold_structure_features.csv"
OUTPUT_SCORES = PROJECT_ROOT / "results" / "tables" / "pten_alphafold_residue_priority_scores.csv"

# Tien et al./commonly used maximum ASA scale approximations are used here as
# pragmatic normalization constants for relative SASA calculation.
MAX_ASA: Dict[str, float] = {
    "A": 129.0,
    "R": 274.0,
    "N": 195.0,
    "D": 193.0,
    "C": 167.0,
    "Q": 225.0,
    "E": 223.0,
    "G": 104.0,
    "H": 224.0,
    "I": 197.0,
    "L": 201.0,
    "K": 236.0,
    "M": 224.0,
    "F": 240.0,
    "P": 159.0,
    "S": 155.0,
    "T": 172.0,
    "W": 285.0,
    "Y": 263.0,
    "V": 174.0,
}

def residue_class_weight(residue_one_letter: str) -> float:
    """Assign conservative residue-class weights for Cys, His, and Lys."""
    if residue_one_letter == "C":
        return 1.00
    if residue_one_letter == "H":
        return 0.65
    if residue_one_letter == "K":
        return 0.55
    return 0.00

def parse_structure_features() -> pd.DataFrame:
    if not INPUT_CIF.exists():
        raise FileNotFoundError(
            f"Missing AlphaFold mmCIF file: {INPUT_CIF}. "
            "Run src/structure_processing/04_download_alphafold_pten.py first."
        )

    parser = MMCIFParser(QUIET=True)
    structure = parser.get_structure("PTEN_ALPHAFOLD", INPUT_CIF)

    shrake_rupley = ShrakeRupley()
    shrake_rupley.compute(structure, level="R")

    rows = []

    for model in structure:
        for chain in model:
            for residue in chain:
                hetflag, residue_position, insertion_code = residue.id

                if hetflag.strip():
                    continue

                residue_name_3 = residue.get_resname().upper()

                if residue_name_3 not in protein_letters_3to1:
                    continue

                residue_one_letter = protein_letters_3to1[residue_name_3]

                atom_b_factors = [
                    atom.get_bfactor()
                    for atom in residue.get_atoms()
                ]

                mean_plddt = sum(atom_b_factors) / len(atom_b_factors)

                absolute_sasa = getattr(residue, "sasa", None)

                max_asa = MAX_ASA.get(residue_one_letter)

                if absolute_sasa is None or max_asa is None:
                    relative_sasa = None
                else:
                    relative_sasa = min(absolute_sasa / max_asa, 1.0)

                rows.append(
                    {
                        "protein": "PTEN",
                        "gene": "PTEN",
                        "uniprot_accession": "P60484",
                        "structure_source": "AlphaFold/RCSB AF_AFP60484F1",
                        "residue_position": residue_position,
                        "residue": residue_one_letter,
                        "residue_label": f"{residue_one_letter}{residue_position}",
                        "absolute_sasa": absolute_sasa,
                        "relative_sasa": relative_sasa,
                        "mean_plddt": mean_plddt,
                        "target_residue": residue_one_letter in {"C", "K", "H"},
                        "residue_class_weight": residue_class_weight(residue_one_letter),
                    }
                )

    df = pd.DataFrame(rows)

    if df.empty:
        raise RuntimeError("No protein residues were parsed from the AlphaFold mmCIF file.")

    return df

def score_target_residues(df: pd.DataFrame) -> pd.DataFrame:
    targets = df[df["target_residue"]].copy()

    targets["alphafold_priority_score"] = (
        0.45 * targets["relative_sasa"].fillna(0)
        + 0.25 * targets["residue_class_weight"]
        + 0.30 * (targets["mean_plddt"] / 100)
    )

    targets["priority_rank"] = (
        targets["alphafold_priority_score"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )

    targets = targets.sort_values(
        ["priority_rank", "residue_position"]
    ).reset_index(drop=True)

    return targets

def main() -> None:
    OUTPUT_FEATURES.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_SCORES.parent.mkdir(parents=True, exist_ok=True)

    features = parse_structure_features()
    scores = score_target_residues(features)

    features.to_csv(OUTPUT_FEATURES, index=False)
    scores.to_csv(OUTPUT_SCORES, index=False)

    print(f"Structure-derived PTEN features written to: {OUTPUT_FEATURES}")
    print(f"Structure-derived PTEN priority scores written to: {OUTPUT_SCORES}")
    print(f"Total residues parsed: {len(features)}")
    print(f"Target C/K/H residues scored: {len(scores)}")
    print("\nTop-ranked AlphaFold-derived target residues:")
    print(
        scores[
            [
                "residue_label",
                "relative_sasa",
                "mean_plddt",
                "residue_class_weight",
                "alphafold_priority_score",
                "priority_rank",
            ]
        ].head(10).to_string(index=False)
    )

if __name__ == "__main__":
    main()