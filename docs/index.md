# Metabarcoding 101

Welcome! This site is a hands-on tutorial for analysing DNA metabarcoding data,
from raw sequencing reads to ecological results, using two open-source tools:

| Tool | What it does | Repository |
|------|--------------|------------|
| **APSCALE** | Processes raw reads into ESV/OTU tables (merging, trimming, filtering, denoising, clustering) | [GitHub](https://github.com/DominikBuchner/apscale) |
| **TaxonTableTools (TTT)** | Explores, filters and visualises taxon tables (diversity, ordination, plots, export) | [GitHub](https://github.com/YOUR-GITHUB-USERNAME/TaxonTableTools2) |

## How the workflow fits together

```text
raw FASTQ reads
      │
      ▼
  APSCALE  ──►  ESV / OTU table + sequences
                        │
                        ▼
              taxonomic assignment
                        │
                        ▼
                      TTT  ──►  figures, statistics, reports
```

:::{tip}
New here? Start with {doc}`getting-started/installation`, then follow the pages
in order. Every step uses the same small example dataset, so you can reproduce
all outputs yourself.
:::

```{toctree}
:maxdepth: 2
:hidden:
:caption: Getting started

getting-started/introduction
getting-started/installation
getting-started/example-data
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: APSCALE – read processing

apscale/index
apscale/project-setup
apscale/running
apscale/outputs
```

```{toctree}
:maxdepth: 2
:hidden:
:caption: TTT – data analysis

ttt/index
ttt/import
ttt/analysis
ttt/export
```

```{toctree}
:maxdepth: 1
:hidden:
:caption: Help

faq
```

## Contents

1. **Getting started:** {doc}`getting-started/introduction` · {doc}`getting-started/installation` · {doc}`getting-started/example-data`
2. **APSCALE:** {doc}`apscale/index` · {doc}`apscale/project-setup` · {doc}`apscale/running` · {doc}`apscale/outputs`
3. **TTT:** {doc}`ttt/index` · {doc}`ttt/import` · {doc}`ttt/analysis` · {doc}`ttt/export`
