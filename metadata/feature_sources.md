# Feature Provenance and Interpretation

## Purpose

This document defines the provenance and interpretation status of the residue-level features used in this repository.

## Current data status

This repository now contains two PTEN residue-feature workflows.

### 1. Example proxy-feature workflow

The file data/raw/pten_residue_features_example.csv is an example input used to demonstrate the original scoring workflow.

Its relative_sasa and conservation_score columns should not be interpreted as newly calculated, experimentally validated, or publication-grade structural measurements.

The corresponding outputs are:

- data/processed/pten_prepared_features.csv
- results/tables/pten_residue_susceptibility_scores.csv

### 2. AlphaFold-derived structure-feature workflow

The file data/structures/AF-P60484-F1-model_v6.cif is downloaded from AlphaFold/RCSB for human PTEN, UniProt accession P60484.

The script src/structure_processing/05_extract_pten_structure_features.py derives residue-level features from this predicted structure model, including absolute SASA, relative SASA, mean residue-level pLDDT, target residue identity, and residue-class weight.

The corresponding outputs are:

- data/processed/pten_alphafold_structure_features.csv
- results/tables/pten_alphafold_residue_priority_scores.csv

## Critical interpretation boundary

The AlphaFold-derived features are model-derived, not experimental structural measurements.

The prioritisation scores should not be interpreted as evidence of experimentally validated PTEN redox-modification sites, biochemical susceptibility, electrophile adduction, PTEN functional inhibition, PI3K/Akt pathway activation, or tumour-cell causal effects.

The valid interpretation is that selected Cys, Lys, and His residues are ranked by transparent residue-level features derived from a declared predicted PTEN structure model.

## Required upgrade for stronger biological claims

For stronger biological claims, this workflow should be supplemented with experimentally determined structures where appropriate, redox-proteomics evidence, targeted mass spectrometry, PTEN activity assays, mutagenesis, controlled electrophile exposure experiments, and downstream PI3K/Akt signalling readouts.
