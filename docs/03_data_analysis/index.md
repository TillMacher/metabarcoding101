# Overview

**Goal:** add metadata, explore, filter and visualise your data.

| Tool | Use it for | Environment |
|------|------------|-------------|
| {doc}`01_taxontabletools2` | Combining read + taxonomy tables, filtering, diversity analyses, plots | `conda activate TTT` |
| {doc}`02_apscale_data_analysis` | Adding sample/sequence metadata, GBIF name checks, ENA upload preparation, filtered table export | `conda activate apscale4` |

**Input:** the read table from {doc}`APSCALE <../01_read_processing/02_apscale>` and the taxonomy table from
{doc}`APSCALE-blast <../02_taxonomic_assignment/01_apscale_blast>` or
{doc}`BOLDigger3 <../02_taxonomic_assignment/02_boldigger3>`

```{todo}
Explain when to use which tool, and whether the APSCALE analyze module should
be run before TTT (e.g. to add metadata first).
```
