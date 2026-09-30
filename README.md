# Metabarcoding 101

Source for the tutorial website on DNA metabarcoding with **APSCALE** and **TaxonTableTools**.

📖 **Read it here:** https://metabarcoding101.readthedocs.io

## Editing

Pages are Markdown files in `docs/`. The menu order is set in `docs/index.md`.
Every push to `main` rebuilds the website automatically on Read the Docs.

## Preview locally

```bash
pip install -r docs/requirements.txt
sphinx-build docs docs/_build/html
# open docs/_build/html/index.html
```
