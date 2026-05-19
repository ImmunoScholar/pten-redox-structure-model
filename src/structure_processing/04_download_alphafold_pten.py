"""
04_download_alphafold_pten.py

Purpose:
Download the AlphaFold computed structure model for human PTEN using UniProt
accession P60484.

Data provenance:
- Protein: PTEN_HUMAN
- UniProt accession: P60484
- RCSB computed model entry: AF_AFP60484F1
- AlphaFold coordinate file: AF-P60484-F1-model_v6.cif
- File type: mmCIF coordinate file

Scientific boundary:
This is a computationally predicted AlphaFold model, not an experimentally
determined PTEN structure. It is used here only to derive reproducible
structure-derived features for residue-level prioritisation.
"""

from pathlib import Path
from urllib.request import urlretrieve

PROJECT_ROOT = Path(__file__).resolve().parents[2]

OUTPUT_DIR = PROJECT_ROOT / "data" / "structures"
OUTPUT_FILE = OUTPUT_DIR / "AF-P60484-F1-model_v6.cif"

ALPHAFOLD_CIF_URL = "https://alphafold.ebi.ac.uk/files/AF-P60484-F1-model_v6.cif"

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading AlphaFold PTEN mmCIF: {ALPHAFOLD_CIF_URL}")
    urlretrieve(ALPHAFOLD_CIF_URL, OUTPUT_FILE)

    if not OUTPUT_FILE.exists() or OUTPUT_FILE.stat().st_size == 0:
        raise RuntimeError("Downloaded mmCIF file is missing or empty.")

    print(f"AlphaFold PTEN mmCIF written to: {OUTPUT_FILE}")
    print("Source entry: RCSB AF_AFP60484F1 / AlphaFold P60484")
    print("Scientific boundary: predicted model, not experimental structure.")

if __name__ == "__main__":
    main()