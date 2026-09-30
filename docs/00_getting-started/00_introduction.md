# What is metabarcoding?

**DNA metabarcoding** identifies many species at once from a single sample
(e.g. water, soil, a bulk insect sample) by sequencing a short, standardised
DNA marker region and comparing the sequences to a reference database.

```{todo}
Add a short, beginner-friendly introduction (2–3 paragraphs) and an overview figure.
```

## Typical applications

```{todo}
List typical applications, e.g. biodiversity monitoring, water quality assessment,
detection of invasive or rare species, diet analysis.
```

## Marker genes

| Marker | Typical target groups |
|--------|----------------------|
| COI | Invertebrates (e.g. insects) |
| 12S | Fish, vertebrates |
| 16S | Bacteria |
| 18S | Eukaryotes (e.g. protists) |
| ITS | Fungi |

```{todo}
Check and adjust the marker table; add the primer pairs used in the example dataset.
```

## From sample to result

1. **Sampling** – collect water, soil, bulk samples, …
2. **Lab work** – DNA extraction, PCR amplification with tagged primers, library preparation
3. **Sequencing** – usually paired-end Illumina sequencing
4. **Bioinformatics** – demultiplexing, read processing, taxonomic assignment
5. **Analysis** – diversity, community composition, statistics

:::{note}
This tutorial covers steps **4 and 5**: the bioinformatics and analysis.
:::

## Key terms

Reads, ESVs, OTUs and taxon tables are explained in the {doc}`../05_help/glossary`.
