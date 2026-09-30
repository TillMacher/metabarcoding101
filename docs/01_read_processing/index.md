# Overview

**Goal:** turn raw Illumina reads into an ESV/OTU table.

| Step | Tool | Input | Output |
|------|------|-------|--------|
| Demultiplexing | {doc}`01_demultiplexer2` | Raw `.fastq.gz` files (one pair per library) | One `.fastq.gz` pair per sample |
| Processing | {doc}`02_apscale` | Demultiplexed `.fastq.gz` files | ESV/OTU read table + `.fasta` |

**Environment:** `conda activate apscale4`

:::{note}
Skip demultiplexing if your sequencing provider already delivered one file
pair per sample, and go straight to {doc}`02_apscale`.
:::

:::{seealso}
Prefer a graphical interface? See {doc}`../04_apscale_gui/01_read_processing`.
:::
