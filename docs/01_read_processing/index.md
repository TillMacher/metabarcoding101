# Read processing – overview

**Goal:** turn raw Illumina reads into an ESV/OTU table.

| Step | Tool | Input | Output |
|------|------|-------|--------|
| Demultiplexing | {doc}`01_demultiplexer2` | Raw FASTQ files (one per lane/library) | One FASTQ pair per sample |
| Processing | {doc}`02_apscale` | Demultiplexed FASTQ files | ESV/OTU table + FASTA |

**Environment:** `conda activate APSCALE4`

:::{seealso}
Prefer a graphical interface? See {doc}`../04_apscale_gui/01_read_processing`.
:::
