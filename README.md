# Structure-Informed Modeling of Electrophile-Sensitive Residues in the PTEN–PI3K/Akt Axis

## Overview

This repository implements a structure-informed computational framework for prioritising PTEN residues that may merit downstream investigation in the context of lipid electrophile-associated oxidative stress and PI3K/Akt tumour-signalling biology.

The project is designed to support a disciplined computational entry point into the question:

> Which PTEN residues combine structural exposure, residue chemistry, and functional conservation features that make them rational candidates for downstream experimental evaluation under lipid electrophile-associated oxidative stress?

## Biological Context

PTEN is a tumour suppressor and negative regulator of PI3K/Akt signalling. Oxidative stress and lipid peroxidation can generate reactive lipid electrophiles such as 4-HNE and MDA, which may modify nucleophilic protein residues under appropriate biochemical conditions.

This project focuses on PTEN because perturbation of PTEN function can alter PI3K/Akt pathway regulation, a central axis in tumour biology.

## Scientific Positioning

This repository does **not** claim to demonstrate electrophile-mediated PTEN modification.

Instead, it provides a reproducible residue-prioritisation framework using interpretable proxy features:

- relative solvent accessibility

- conservation score

- residue-class weighting

- PTEN functional-region annotation

- PI3K/Akt pathway context

The output should be interpreted as a hypothesis-prioritisation signal, not as direct biochemical evidence.

## Why This Project Avoids Classical Docking

Classical molecular docking is not used because lipid electrophiles such as 4-HNE and MDA can form covalent adducts through reaction chemistry that is not captured by standard reversible non-covalent docking scores.

This project therefore avoids claims about:

- binding affinity

- docking poses

- covalent adduct geometry

- electrophile-protein interaction mechanisms

Instead, it uses structure-informed residue features to prioritise PTEN sites for future experimental or higher-resolution computational investigation.

A detailed evidence-boundary statement is provided in:

```text

docs/methodological\_boundaries.md

