#!/usr/bin/env bash

set -euo pipefail

echo "Running PTEN redox structure-informed prioritisation pipeline..."

python src/feature_engineering/01_prepare_pten_features.py
python src/scoring/02_score_electrophile_sensitive_residues.py
python src/visualization/03_visualize_pten_scores.py

echo "Pipeline completed successfully."
