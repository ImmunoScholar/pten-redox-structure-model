"""
02_score_electrophile_sensitive_residues.py

Purpose:
Calculate a conservative structure-informed prioritisation score for PTEN residues
that may merit downstream investigation under lipid electrophile-associated
oxidative stress.

Scientific boundary:
This score is NOT a prediction of covalent adduction, biochemical reactivity,
binding affinity, or functional perturbation.

It is a hypothesis-prioritisation score based on interpretable proxy features:
- relative solvent accessibility
- conservation
- residue-class weighting

Input:
data/processed/pten_prepared_features.csv

Output:
results/tables/pten_residue_susceptibility_scores.csv
"""

from pathlib import Path
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "pten_prepared_features.csv"
OUTPUT_DIR = PROJECT_ROOT / "results" / "tables"
OUTPUT_FILE = OUTPUT_DIR / "pten_residue_susceptibility_scores.csv"


def compute_prioritisation_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute an interpretable residue prioritisation score.

    Score design:
    - relative_sasa captures structural exposure proxy
    - conservation_score captures potential functional constraint
    - residue_class_weight gives chemically conservative residue emphasis

    The score is intentionally simple and transparent.
    """

    df = df.copy()

    df["electrophile_sensitivity_priority_score"] = (
        0.40 * df["relative_sasa"]
        + 0.35 * df["conservation_score"]
        + 0.25 * df["residue_class_weight"]
    )

    df["priority_rank"] = (
        df["electrophile_sensitivity_priority_score"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )

    df = df.sort_values(
        ["priority_rank", "residue_position"]
    ).reset_index(drop=True)

    return df


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    scored = compute_prioritisation_score(df)

    scored.to_csv(OUTPUT_FILE, index=False)

    print(f"PTEN residue prioritisation scores written to: {OUTPUT_FILE}")
    print("\nTop-ranked residues:")
    print(
        scored[
            [
                "residue_label",
                "region",
                "relative_sasa",
                "conservation_score",
                "residue_class_weight",
                "electrophile_sensitivity_priority_score",
                "priority_rank",
            ]
        ].head(5).to_string(index=False)
    )


if __name__ == "__main__":
    main()
