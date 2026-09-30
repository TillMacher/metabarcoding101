# BOLDigger3

[BOLDigger3](https://github.com/DominikBuchner/boldigger3) identifies
sequences against the **BOLD Systems v5** databases. It automates BOLD's
online identification engine (which only accepts small batches), adds
metadata and selects the best-fitting hit for each sequence.

**Input:** `.fasta` file with ESV/OTU sequences · **Output:** identification
table (`.xlsx` and `.parquet`)

- Up to about **10,000 sequences per hour**, depending on the operating mode
- **Resumes** where it stopped if a run is interrupted
- A **BOLD account** is needed once, to download the public database

## 1. Download the BOLD database

Register for a free account at [boldsystems.org](https://www.boldsystems.org), then run:

```bash
boldigger3 download_db PATH_TO_OUTPUT_DIR
```

BOLDigger3 asks for your BOLD username and password, and downloads the latest
public data package as a DuckDB file (`.ddb`). If your local copy is already
up to date, nothing is downloaded.

## 2. Run the identification

```bash
boldigger3 identify PATH_TO_FASTA PATH_TO_DATABASE --db DATABASE_NR --mode OPERATING_MODE
```

`PATH_TO_DATABASE`
: The `.ddb` file from step 1

`--db` – which BOLD library to search
: 1 · Animal library (public)
: 2 · Animal species-level library (public + private)
: 3 · Animal library (public + private)
: 4 · Validated Canadian arthropod library
: 5 · Plant library (public)
: 6 · Fungi library (public)
: 7 · Animal secondary markers (public)
: 8 · Validated animal Red List library

`--mode` – how BOLD searches
: 1 · Rapid species search
: 2 · Genus and species search
: 3 · Exhaustive search

```{todo}
Add the recommended `--db` and `--mode` for the example dataset (e.g. COI →
`--db 1 --mode 2`?) and the expected runtime.
```

### Custom thresholds

The default similarity thresholds are **species 97 %, genus 95 %, family 90 %,
order 85 %, class 75 %, phylum 50 %**. You can change up to five of them
(species, genus, family, order, class) in order:

```bash
boldigger3 identify PATH_TO_FASTA PATH_TO_DATABASE --db 1 --mode 2 --thresholds 99 97
```

## 3. How the top hit is chosen

For each sequence, BOLDigger3 looks at the top 100 hits, keeps those above the
threshold of the best hit, and picks the **most common classification without
missing data**. If none is found, it moves one taxonomic level up. For hits below
the species threshold, the taxonomic resolution is reduced accordingly
(e.g. a 96 % hit is reported at genus level).

## 4. Flags

Flags mark hits that deserve a closer look:

| Flag | Meaning |
|------|---------|
| 1 · Reverse BIN taxonomy | All supporting hits use reverse BIN taxonomy |
| 2 · Differing taxonomy | The selected hit represents < 90 % of the hits |
| 3 · Private data | All supporting hits are private |
| 4 · Unique hit | The top hit is a unique hit among the top 100 |
| 5 · Multiple BINs | The species-level hit spans more than one BIN |

```{todo}
Add guidance on how to handle flagged hits in practice.
```

## 5. Outputs

```{todo}
Describe the output files (names, where they are written, key columns) and add
an excerpt for the example dataset.
```

The identification table is the file you need for {doc}`Data analysis <../03_data_analysis/index>`.

## Updating

```bash
pip install --upgrade boldigger3
```
