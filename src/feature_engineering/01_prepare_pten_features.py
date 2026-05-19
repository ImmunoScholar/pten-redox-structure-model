"""
01_prepare_pten_features.py

Purpose:
Prepare PTEN residue-level features for structure-informed prioritisation.

Scientific boundary:
This script does not predict covalent binding, electrophile adduction, or biochemical
reactivity. It prepares proxy features such as relative solvent accessibility,
conservation, and residue class for downstream prioritisation.

Input:
data/raw/pten_residue_features_example.csv

Output:
data/processed/pten_prepared_features.csv
"""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "pten_residue_features_example.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"
OUTPUT_FILE = OUTPUT_DIR / "pten_prepared_features.csv"


REQUIRED_COLUMNS = {
    "protein",
    "gene",
    "residue_position",
    "residue",
    "residue_label",
    "region",
    "relative_sasa",
    "conservation_score",
    "known_functional_relevance",
}


def validate_columns(df: pd.DataFrame) -> None:
    """Ensure all expected feature columns are present."""
    missing = REQUIRED_COLUMNS.difference(df.columns)

    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def residue_class_weight(residue: str) -> float:
    """
    Assign a conservative residue-class weight.

    Biological reasoning:
    Cysteine is weighted highest because thiol chemistry is central to many
    redox-sensitive protein modifications. Lysine and histidine are retained as
    context-dependent residues relevant to electrophile-associated modification,
    but are not treated as equivalent to cysteine.
    """
    residue = residue.upper()

    if residue == "C":
        return 1.00
    if residue == "H":
        return 0.65
    if residue == "K":
        return 0.55

    return 0.00


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    validate_columns(df)

    df["residue_class_weight"] = df["residue"].apply(residue_class_weight)

    # Ensure numeric feature columns are valid.
    df["relative_sasa"] = pd.to_numeric(df["relative_sasa"], errors="raise")
    df["conservation_score"] = pd.to_numeric(df["conservation_score"], errors="raise")

    # Clip to expected 0-1 range for conservative scoring.
    df["relative_sasa"] = df["relative_sasa"].clip(0, 1)
    df["conservation_score"] = df["conservation_score"].clip(0, 1)

    df = df.sort_values(["protein", "residue_position"]).reset_index(drop=True)

    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Prepared PTEN feature table written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
