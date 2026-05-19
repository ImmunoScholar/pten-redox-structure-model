# Methodological Boundaries

## Purpose

This document defines the scientific interpretation limits of this repository.

The project investigates PTEN residue prioritisation in the context of lipid electrophile-associated oxidative stress and PI3K/Akt tumour-signalling biology.

## What This Project Does

This repository provides a structure-informed computational framework for prioritising PTEN residues using interpretable proxy features:

- relative solvent accessibility
- conservation score
- residue-class weighting
- PTEN functional-region annotation

The output is a residue-level prioritisation score intended to nominate sites for downstream structural or experimental investigation.

## What This Project Does Not Do

This project does not perform or claim:

- classical docking of lipid electrophiles
- covalent docking
- binding affinity prediction
- electrophile adduction prediction
- biochemical reactivity prediction
- PTEN functional inhibition
- PI3K/Akt pathway activation
- tumour-cell causal inference

## Why Classical Docking Is Not Used

Lipid-derived electrophiles such as 4-HNE and MDA can form covalent adducts with nucleophilic residues under appropriate biochemical conditions.

Classical molecular docking is designed primarily for reversible non-covalent ligand-binding models and does not, by itself, model covalent reaction chemistry, adduct formation, reaction kinetics, or residue-specific electrophile chemistry.

Therefore, this repository avoids interpreting docking poses or binding scores as evidence of lipid electrophile-protein modification.

## Interpretation Framework

The prioritisation score should be interpreted as:

> A structure-informed hypothesis-prioritisation signal.

It should not be interpreted as:

> Direct evidence that a residue is modified, reactive, or functionally perturbed.

## Evidence Required for Stronger Claims

Claims of actual electrophile-mediated PTEN modification would require orthogonal validation such as:

- redox proteomics
- targeted mass spectrometry
- site-directed mutagenesis
- PTEN activity assays
- controlled 4-HNE/MDA exposure experiments
- PI3K/Akt signalling readouts
- tumour-cell functional assays

## Current Role of the Pipeline

The current pipeline is designed to support rational experimental prioritisation by identifying PTEN residues that combine interpretable structural and biological proxy features.
