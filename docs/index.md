# Metabarcoding 101

A hands-on tutorial for analysing DNA metabarcoding data, from raw Illumina
reads to taxon tables, figures and statistics.

## The workflow

```text
 raw reads (FASTQ)
        │
        ▼
 1. Read processing         Demultiplexer2 → APSCALE
        │                   → ESV / OTU table + sequences
        ▼
 2. Taxonomic assignment    APSCALE-blast  and/or  BOLDigger3
        │                   → taxon table
        ▼
 3. Data analysis           TaxonTableTools2
                            → figures, diversity, statistics
```

Steps 1 and 2 can also be run in a single graphical app,
the {doc}`APSCALE-GUI <04_apscale_gui/index>`.

## Tools at a glance

| Tool | What it does | Source |
|------|--------------|--------|
| **Demultiplexer2** | Sorts paired-end Illumina reads into samples by their inline tags | [GitHub](https://github.com/DominikBuchner/demultiplexer2) |
| **APSCALE** | Turns raw reads into ESV/OTU tables (merging, trimming, filtering, denoising, clustering) | [GitHub](https://github.com/DominikBuchner/apscale) |
| **APSCALE-blast** | Assigns taxonomy using BLAST against a range of reference databases | [GitHub](https://github.com/TillMacher/apscale_blast) |
| **BOLDigger3** | Assigns taxonomy against the BOLD Systems v5 database | [GitHub](https://github.com/DominikBuchner/boldigger3) |
| **APSCALE-GUI** | Graphical interface bundling Demultiplexer2, APSCALE, APSCALE-blast and BOLDigger3 | [GitHub](https://github.com/TillMacher/apscale_gui) |
| **TaxonTableTools2** | Explores, filters and visualises taxon tables (diversity, ordination, plots, export) | [GitHub](https://github.com/TillMacher/TaxonTableTools2) |

:::{note}
The tools are installed into **two conda environments**:

- `APSCALE4` – read processing and taxonomic assignment ({doc}`setup <00_getting-started/02_apscale_env_installation>`)
- `TTT` – data analysis with TaxonTableTools2 ({doc}`setup <00_getting-started/03_TTT_env_installation>`)
:::

:::{tip}
New here? Start with {doc}`00_getting-started/00_introduction` and follow the
pages in order. Every step uses the same {doc}`example dataset
<00_getting-started/04_example_data>`, so you can reproduce all outputs yourself.
:::

```{toctree}
:hidden:
:caption: Getting started

00_getting-started/00_introduction
00_getting-started/index
00_getting-started/04_example_data
```

```{toctree}
:hidden:
:caption: 1 · Read processing

01_read_processing/index
01_read_processing/01_demultiplexer2
01_read_processing/02_apscale
```

```{toctree}
:hidden:
:caption: 2 · Taxonomic assignment

02_taxonomic_assignment/index
02_taxonomic_assignment/01_apscale_blast
02_taxonomic_assignment/02_boldigger3
```

```{toctree}
:hidden:
:caption: 3 · Data analysis

03_data_analysis/index
03_data_analysis/01_taxontabletools2
03_data_analysis/02_apscale_data_analysis
```

```{toctree}
:hidden:
:caption: APSCALE-GUI

04_apscale_gui/index
04_apscale_gui/01_read_processing
04_apscale_gui/02_taxonomic_assignment
```

```{toctree}
:hidden:
:caption: Help

05_help/faq
05_help/glossary
05_help/citation
```
