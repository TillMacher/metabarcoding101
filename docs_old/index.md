# Metabarcoding 101

Welcome! This site is a hands-on tutorial for analysing DNA metabarcoding data,
from raw sequencing reads to ecological results, using two open-source tools:

| Environment | Step                | Tool                    | What it does                                                                                           | Repository                                                 |
|-------------|---------------------|--------------------------|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| APSCALE4    | Raw Data Processing | **Demultiplexer2**       | Demultiplexes paired-end Illumina sequencing reads by identifying and sorting inline tags.             | [GitHub](https://github.com/DominikBuchner/demultiplexer2) |
| APSCALE4    | Raw Data Processing | **APSCALE**              | Processes raw reads into ESV/OTU tables (merging, trimming, filtering, denoising, clustering)          | [GitHub](https://github.com/DominikBuchner/apscale)        |
| APSCALE4    | Raw Data Processing | **APSCALE-GUI**          | Graphical-User-Interface of APSCALE4 (including Demutliplexer2, APSCALE, APSCALE-blast, and BOLDigger3 | [GitHub](https://github.com/TillMacher/apscale_gui)        |
| APSCALE4    | Raw Data Processing | **APSCALE-blast**        | Assigns taxonomy to sequences against various available databases                                      | [GitHub](https://github.com/TillMacher/apscale_blast)      |
| APSCALE4    | Raw Data Processing | **BOLDigger3**           | Assigns taxonomy to sequences against the BOLDsystemsv5 database                                       | [GitHub](https://github.com/DominikBuchner/boldigger3)     |
| TTT         | Data Analysis       | **TaxonTableTools (TTT)** | Explores, filters and visualises taxon tables (diversity, ordination, plots, export)                   | [GitHub](https://github.com/TillMacher/TaxonTableTools2)   |


:::{tip}
New here? Start with {doc}`00_getting-started/00_introduction`, then follow the pages
in order. Every step uses the same small example dataset, so you can reproduce
all outputs yourself.
:::

```{toctree}
:maxdepth: 2
:hidden:
:caption: Getting started

00_getting-started/00_introduction
00_getting-started/01_conda_installation
00_getting-started/02_apscale_env_installation
00_getting-started/03_TTT_env_installation
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Read processing

01_read_processing/00_introduction
01_read_processing/01_demultiplexer2
01_read_processing/02_apscale
01_read_processing/03_apscale_gui
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Taxonomic assignment

02_taxonomic_assignment/00_introduction
02_taxonomic_assignment/01_apscale_blast
02_taxonomic_assignment/02_boldigger3
02_taxonomic_assignment/03_apscale_gui
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: Taxonomic assignment

03_data_analysis/00_introduction
03_data_analysis/01_taxontabletools2
03_data_analysis/02_apscale_data_analysis
```