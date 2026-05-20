# PTEN-PI3K/Akt Rationale

## Purpose

This document explains the biological rationale for centring this repository on PTEN residue prioritisation in the context of PI3K/Akt tumour-signalling biology and lipid electrophile-associated oxidative stress.

## Biological rationale

PTEN is a tumour suppressor and negative regulator of PI3K/Akt signalling. Perturbation of PTEN function can affect pathway regulation, making PTEN a relevant protein for tumour-biology-focused prioritisation.

Oxidative stress can generate lipid-derived electrophiles such as 4-HNE and MDA. These molecules can modify nucleophilic amino acid side chains under suitable biochemical conditions. This provides a rationale for focusing on residue classes such as cysteine, lysine, and histidine.

## Computational rationale

This repository does not test PTEN modification experimentally. Instead, it builds a residue-prioritisation workflow that combines PTEN pathway context with residue-level structural features derived from a declared AlphaFold predicted structure model.

The AlphaFold-derived workflow extracts model-based relative solvent accessibility and pLDDT values and combines them with residue-class weighting to rank PTEN Cys, Lys, and His residues for downstream experimental consideration.

## Interpretation boundary

The workflow does not demonstrate lipid electrophile adduction, PTEN inhibition, PI3K/Akt activation, tumour-cell signalling changes, or causal tumour biology effects.

The strongest defensible interpretation is that the repository provides a reproducible computational foundation for prioritising PTEN residues that may merit downstream testing in lipid electrophile-associated oxidative stress models.

## Experimental translation

Downstream validation would require controlled electrophile exposure, residue-specific mass spectrometry, PTEN activity assays, mutagenesis, and PI3K/Akt signalling readouts such as AKT phosphorylation or downstream pathway markers.
