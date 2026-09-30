# APSCALE data analysis

APSCALE 4 includes an **analyze module**: a browser-based interface to add
metadata to your project, check species names against GBIF, prepare data for
publication and export filtered read tables.

**Input:** a finished APSCALE project (`11_read_table`) · **Output:** files in
`12_analyze/data`

## Start the analyze module

```bash
conda activate apscale4
apscale --analyze
```

Run this inside the project folder, or add the project path:
`apscale --analyze PATH/TO/PROJECT`. The interface opens in your web browser.

```{todo}
Add a screenshot of the analyze start page.
```

## Modules

1. **Add sample metadata** – e.g. site, date, habitat, replicate
2. **Add sequence metadata** – e.g. taxonomy from APSCALE-blast or BOLDigger3
3. **Search GBIF species names** – harmonise species names with the GBIF backbone taxonomy
4. **Perform GBIF validation** – validate species names via a GBIF occurrence record search
5. **Prepare ENA upload** – prepare your data for submission to the European Nucleotide Archive
6. **Export read tables** – filter by sample or sequence metadata and export, optionally split by metadata

```{todo}
Add a short walkthrough for each module with the example dataset (inputs,
settings, outputs).
```
