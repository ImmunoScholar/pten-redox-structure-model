# Feature Provenance and Interpretation

## Purpose

This document defines the provenance and interpretation status of the residue-level features used in this repository.

## Current data status

The current PTEN residue feature table is an example input used to demonstrate the computational workflow:

`data/raw/pten_residue_features_example.csv`

The table contains selected PTEN residues with proxy features including relative solvent accessibility, conservation score, residue identity, PTEN region annotation, and functional-context notes.

## Critical interpretation boundary

The current feature values should not be interpreted as experimentally validated PTEN redox-modification sites, newly calculated structural measurements, publication-grade solvent-accessibility values, validated conservation scores, biochemical susceptibility measurements, evidence of electrophile adduction, evidence of PTEN functional inhibition, or evidence of PI3K/Akt pathway activation.

They are included to make the pipeline executable and to demonstrate how residue-level features can be processed, scored, and visualised.

## Current acceptable use

The current feature table is acceptable for testing the computational pipeline, demonstrating residue-level prioritisation logic, showing how structure-informed proxy features can be combined, and generating example tables and figures.

It is not sufficient for claiming actual PTEN electrophile modification, residue-level biochemical reactivity, PTEN inhibition, PI3K/Akt pathway activation, or tumour-cell causal effects.

## Required upgrade for stronger biological claims

For stronger claims, the current example features should be replaced or supplemented with explicitly sourced or computed values, such as solvent accessibility calculated from a defined PDB or AlphaFold PTEN structure, conservation scores generated from a documented multiple-sequence alignment, experimentally observed redox or electrophile-modified residues from curated redox-proteomics datasets, and PTEN functional annotations linked to primary literature or curated databases.

