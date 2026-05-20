# Structure-Informed Modeling of Electrophile-Sensitive Residues in the PTEN–PI3K/Akt Axis

## Overview

This repository contains a structure-informed residue prioritisation workflow centred on PTEN, a tumour suppressor and negative regulator of PI3K/Akt signalling.

The project is built around a specific computational question:

> Which PTEN residues combine structural exposure, residue chemistry, conservation, and functional-region context in a way that makes them reasonable candidates for follow-up analysis under lipid electrophile-associated oxidative stress?

The workflow ranks selected PTEN residues using transparent proxy features and places the output in the biological context of PTEN-regulated PI3K/Akt signalling.

This is not a docking project and does not attempt to model electrophile binding.

## Biological Rationale

Oxidative stress can promote lipid peroxidation and generate electrophilic lipid-derived aldehydes such as 4-HNE and MDA. These species can modify nucleophilic amino acid side chains under suitable biochemical conditions.

PTEN is relevant in this context because perturbation of PTEN activity can affect PI3K/Akt signalling, a major growth, survival, and tumour-associated signalling axis.

A residue-level prioritisation workflow can help define which PTEN sites should be examined more closely in future structural, proteomic, biochemical, or cell-based experiments.

## Methodological Scope

This repository performs structure-informed prioritisation, not biochemical validation.

The current prioritisation score combines:

- relative solvent accessibility
- conservation score
- residue-class weighting
- PTEN functional-region annotation
- PI3K/Akt pathway context

The output is a ranked list of PTEN residues for follow-up investigation. It should not be interpreted as evidence that a residue is electrophile-modified, redox-reactive, functionally inhibited, or causally linked to PI3K/Akt activation.

## Data Provenance

This repository contains two PTEN residue-feature workflows.

The first workflow uses an example proxy-feature table to demonstrate residue-level scoring logic. That table is not presented as a validated catalogue of PTEN redox-modified residues, experimentally measured biochemical susceptibility, or fully structure-derived solvent-accessibility output.

The second workflow downloads an AlphaFold PTEN mmCIF structure model and derives model-based residue-level structural features, including relative solvent accessibility and mean residue-level pLDDT.

Feature provenance and interpretation limits are documented in:

```text
metadata/feature_sources.md
```

The structural-input status is documented in:

```text
data/structures/README.md
```

## Why Classical Docking Is Not Used

Standard molecular docking is not appropriate for the central question addressed here.

Lipid electrophile modification is a covalent, chemistry-dependent process. Reversible non-covalent docking scores do not model adduct formation, reaction kinetics, residue nucleophilicity, or electrophile-specific chemistry.

For that reason, this repository does not report:

- docking poses
- binding affinities
- covalent adduct geometries
- electrophile-protein interaction models

The analysis is limited to interpretable residue-level prioritisation.

Detailed evidence-boundary and biological-rationale statements are provided in:

```text
docs/methodological_boundaries.md
docs/pten_pi3kakt_rationale.md
```

## Analytical Workflow

1. Prepare PTEN residue-level feature input
2. Validate and process structural-proxy features
3. Assign conservative residue-class weights
4. Compute a structure-informed prioritisation score
5. Generate residue-ranking and feature-profile visualisations
6. Contextualise PTEN within the PI3K/Akt tumour-signalling axis

## Repository Layout

- `data/raw/` — Input tables for the example PTEN residue workflow and PI3K/Akt pathway context.
- `data/processed/` — Processed PTEN feature tables from the example and AlphaFold-derived workflows.
- `results/tables/` — Residue prioritisation score outputs from example and AlphaFold-derived workflows.
- `results/figures/` — Visual summaries of PTEN residue scores and feature profiles.
- `src/feature_engineering/` — Feature validation and preparation scripts.
- `src/scoring/` — Residue prioritisation score calculation.
- `src/visualization/` — Figure-generation scripts.
- `src/structure_processing/` — AlphaFold structure download and structure-derived feature extraction scripts.
- `data/structures/` — AlphaFold PTEN mmCIF structure model and structural-data status documentation.
- `metadata/` — Feature provenance documentation.
- `environment/` — Conda and pip environment specifications.
- `docs/` — Methodological boundary documentation and PTEN-PI3K/Akt biological rationale.
- `run_pipeline.sh` — One-command pipeline runner.

## Inputs

### PTEN residue feature table

```text
data/raw/pten_residue_features_example.csv
```

This table contains selected PTEN residues with residue identity, relative solvent accessibility, conservation score, functional-region annotation, and residue-level context.

The current input is an example feature table for demonstrating the workflow. It is not presented as a complete experimentally validated redox-site catalogue.

### PI3K/Akt pathway context table

```text
data/raw/pi3k_akt_axis_context.csv
```

This table records the biological role of PTEN and selected PI3K/Akt pathway components, including PI3K, AKT, PDK1, and mTOR.

## Scoring Strategy

The example proxy-feature prioritisation score is deliberately simple and interpretable:

```text
priority score =
0.40 × relative solvent accessibility
+ 0.35 × conservation score
+ 0.25 × residue-class weight
```

### Feature rationale

- Relative solvent accessibility — Proxy for structural exposure in the example workflow.
- Conservation score — Proxy for functional constraint in the example workflow.
- Residue-class weight — Conservative weighting of residue chemistry.
- Functional-region annotation — Biological context within PTEN.
- PI3K/Akt context — Pathway-level relevance.

Cysteine receives the highest residue-class weight because thiol chemistry is central to many redox-sensitive mechanisms. Histidine and lysine are retained as context-dependent residues relevant to lipid electrophile-associated modification but are not treated as equivalent to cysteine.

The AlphaFold-derived workflow uses a separate model-based prioritisation score combining relative SASA, residue-class weight, and mean residue-level pLDDT. This score is structure-informed but remains a prioritisation metric, not biochemical evidence.

## Outputs

### Tables

- `data/processed/pten_prepared_features.csv` — Cleaned example PTEN residue feature table with residue-class weights.
- `results/tables/pten_residue_susceptibility_scores.csv` — Ranked prioritisation scores from the example proxy-feature workflow.
- `data/processed/pten_alphafold_structure_features.csv` — PTEN residue-level features derived from the AlphaFold predicted structure model, including SASA and pLDDT.
- `results/tables/pten_alphafold_residue_priority_scores.csv` — Ranked Cys/Lys/His residue prioritisation scores derived from AlphaFold model-based structural features.

### Figures

- `results/figures/pten_residue_priority_scores.png` — Ranked PTEN residue prioritisation scores from the example proxy-feature workflow.
- `results/figures/pten_feature_profiles.png` — Feature profiles for ranked PTEN residues from the example proxy-feature workflow.

## Usage

Create the Conda environment:

```bash
conda env create -f environment/environment.yml
```

Activate the environment:

```bash
conda activate pten-redox-structure
```

Run the full pipeline:

```bash
./run_pipeline.sh
```

This executes both workflows:

1. example proxy-feature preparation, scoring, and visualisation
2. AlphaFold PTEN mmCIF download
3. AlphaFold-derived structure-feature extraction
4. AlphaFold-derived Cys/Lys/His residue prioritisation

Individual scripts are available in `src/` for stepwise inspection.

## Interpretation and Evidence Boundary

The prioritisation scores are intended to rank PTEN residues using either example proxy features or AlphaFold-derived model-based structural features.

The strongest defensible interpretation is:

> Higher-ranked PTEN residues are candidates for downstream experimental or higher-resolution computational evaluation under lipid electrophile-associated oxidative stress.

The output does not prove that a residue is:

- electrophile-modified
- oxidized
- redox-reactive
- functionally inhibited
- causally involved in PI3K/Akt pathway activation

Claims about actual PTEN modification, PI3K/Akt signalling consequences, or tumour-cell causal effects require orthogonal validation, including redox proteomics, targeted mass spectrometry, mutagenesis, PTEN activity assays, controlled electrophile exposure experiments, and signalling readouts.

## Current Scope

The current version contains two linked workflows:

1. an example proxy-feature workflow for demonstrating PTEN residue-prioritisation logic
2. an AlphaFold-derived structure-feature workflow that downloads the PTEN P60484 predicted mmCIF model and extracts residue-level SASA and pLDDT features

The repository establishes a reproducible Python workflow, PTEN-centred Cys/Lys/His residue prioritisation, PI3K/Akt tumour-signalling context, explicit methodological limits, and no unsupported docking, binding, adduction, or pathway-activation claims.

This is not an experimentally validated PTEN lipoxidation study. Future versions should add experimentally determined structures where relevant, documented conservation analysis, redox-proteomics evidence, targeted mass spectrometry, PTEN activity assays, mutagenesis, controlled electrophile exposure experiments, and downstream PI3K/Akt signalling readouts.

## Intended Use

This repository is intended as a disciplined computational foundation for investigating PTEN residue-level vulnerability under lipid electrophile-associated oxidative stress.

It is designed to support rational experimental prioritisation, not to replace biochemical or cellular validation.

