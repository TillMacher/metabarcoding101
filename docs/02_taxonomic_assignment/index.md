# Overview

**Goal:** assign a taxonomic name to each ESV/OTU sequence by comparing it
to a reference database.

| Tool | Reference database | Runs | Best for |
|------|--------------------|------|----------|
| {doc}`01_apscale_blast` | Pre-compiled local databases (MIDORI2, SILVA, PR2, UNITE, diat.barcode, …) | Locally, offline | Any marker with a matching database |
| {doc}`02_boldigger3` | BOLD Systems v5 | Online (BOLD ID engine) | COI (animals), also plants & fungi |

**Input:** the `.fasta` file from APSCALE (`11_read_table/data`)
**Environment:** `conda activate apscale4`

```{todo}
Add a recommendation which tool to use for which marker / dataset, and whether
to combine both (APSCALE-blast can re-BLAST good hits with BOLDigger3, see
`-reblast_db`).
```

:::{seealso}
Prefer a graphical interface? See {doc}`../04_apscale_gui/02_taxonomic_assignment`.
:::
