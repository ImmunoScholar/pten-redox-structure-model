# Structure Data Status

This directory contains the AlphaFold computed structure model used for the structure-derived PTEN feature workflow.

## Current structure file

data/structures/AF-P60484-F1-model_v6.cif

## Source

The structure file is downloaded by src/structure_processing/04_download_alphafold_pten.py.

The file corresponds to human PTEN:

- UniProt accession: P60484
- Protein: PTEN_HUMAN
- RCSB computed model entry: AF_AFP60484F1
- Source coordinate file: AlphaFold AF-P60484-F1-model_v6.cif

## Scientific boundary

This structure is a computational AlphaFold prediction, not an experimentally determined PTEN structure.

The structure is used to derive reproducible model-based features, including relative solvent accessibility and mean residue-level pLDDT. These values should not be interpreted as experimental structural measurements.

The resulting structure-derived prioritisation output is intended for hypothesis prioritisation only. It does not provide evidence of electrophile adduction, biochemical reactivity, PTEN inhibition, PI3K/Akt activation, or tumour-cell causal effects.
