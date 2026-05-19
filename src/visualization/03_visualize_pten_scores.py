"""
03_visualize_pten_scores.py

Purpose:
Generate visual outputs for PTEN residue prioritisation analysis.

Scientific boundary:
Figures show structure-informed prioritisation features and scores.
They do not demonstrate covalent electrophile adduction, biochemical reactivity,
or pathway activation.

Input:
results/tables/pten_residue_susceptibility_scores.csv

Outputs:
results/figures/pten_residue_priority_scores.png
results/figures/pten_feature_profiles.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "results" / "tables" / "pten_residue_susceptibility_scores.csv"
OUTPUT_DIR = PROJECT_ROOT / "results" / "figures"

SCORE_PLOT = OUTPUT_DIR / "pten_residue_priority_scores.png"
FEATURE_PLOT = OUTPUT_DIR / "pten_feature_profiles.png"


def plot_priority_scores(df: pd.DataFrame) -> None:
    """Plot PTEN residue prioritisation scores."""
    ordered = df.sort_values("electrophile_sensitivity_priority_score", ascending=True)

    plt.figure(figsize=(8, 5))
    plt.barh(
        ordered["residue_label"],
        ordered["electrophile_sensitivity_priority_score"],
    )
    plt.xlabel("Structure-informed prioritisation score")
    plt.ylabel("PTEN residue")
    plt.title("PTEN Residue Prioritisation Under Lipid Electrophile-Associated Oxidative Stress")
    plt.tight_layout()
    plt.savefig(SCORE_PLOT, dpi=300)
    plt.close()


def plot_feature_profiles(df: pd.DataFrame) -> None:
    """Plot interpretable feature profiles for ranked PTEN residues."""
    ordered = df.sort_values("priority_rank")

    x_labels = ordered["residue_label"].tolist()
    x_positions = range(len(x_labels))

    plt.figure(figsize=(9, 5))
    plt.plot(x_positions, ordered["relative_sasa"], marker="o", label="Relative SASA")
    plt.plot(x_positions, ordered["conservation_score"], marker="o", label="Conservation score")
    plt.plot(x_positions, ordered["residue_class_weight"], marker="o", label="Residue-class weight")

    plt.xticks(x_positions, x_labels, rotation=45)
    plt.ylabel("Feature value")
    plt.title("Feature Profiles for PTEN Residue Prioritisation")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FEATURE_PLOT, dpi=300)
    plt.close()


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)

    plot_priority_scores(df)
    plot_feature_profiles(df)

    print(f"Priority score plot written to: {SCORE_PLOT}")
    print(f"Feature profile plot written to: {FEATURE_PLOT}")


if __name__ == "__main__":
    main()
