# APSCALE-blast

[APSCALE-blast](https://github.com/TillMacher/apscale_blast) assigns
taxonomy to ESVs/OTUs with a local **BLASTn** search against pre-compiled
reference databases, then filters the hits to one taxonomy per sequence.

**Input:** `.fasta` file with ESV/OTU sequences · **Output:** taxonomy table
(`.xlsx`) and log files

## 1. Download a reference database

Pre-compiled databases are available on the
[APSCALE database server](https://seafile.rlp.net/d/c172d076de1e4c45b594/)
and are updated regularly. Download the database that fits your marker and
unzip it.

| Database | Marker / group |
|----------|----------------|
| MIDORI2 | Eukaryotic mitochondrial markers (e.g. COI, 12S, 16S) |
| SILVA | rRNA (16S / 18S) |
| PR2 | Protists (18S) |
| UNITE | Fungi / eukaryotes (ITS) |
| diat.barcode | Diatoms (rbcL) |
| CRUX | Plants (trnL) |

```{todo}
Check the database table against the current server contents and state which
database is used for the example dataset.
```

:::{important}
Please cite the database you use. References are on the
[APSCALE-blast page](https://github.com/TillMacher/apscale_blast#databases)
and under {doc}`../05_help/citation`.
:::

Custom databases can be built with the
[db_creator scripts](https://github.com/TillMacher/apscale_blast/tree/main/db_creator).

## 2. Run APSCALE-blast

```bash
apscale_blast -db PATH/TO/DATABASE -q PATH/TO/ESVs.fasta
```

If you run `apscale_blast` without arguments, it asks for the database and
FASTA paths interactively. Use **full paths**, e.g.
`/Users/you/Downloads/MIDORI2_UNIQ_NUC_GB260_srRNA_BLAST`.

What happens:

1. The FASTA file is split into subsets (default: 100 sequences each).
2. Subsets are BLASTed in parallel.
3. Hits are filtered to one taxonomy per sequence (see below).
4. Results are written to a new Excel file.

## 3. How hits are filtered

- **By e-value:** the hit(s) with the lowest e-value are kept.
- **By similarity thresholds:** the taxonomic level is adjusted to the similarity
  (default: species ≥ 97 %, genus ≥ 95 %, family ≥ 90 %, order ≥ 87 %, class ≥ 85 %).
- **Conflicts:** hits with conflicting taxonomy are set to their most recent common taxon.
- Sequences without any hit are added as **No Match**.

```{todo}
Double-check the default thresholds (the README text and the options table
list different values) and add an example of how a conflict is resolved.
```

## 4. Outputs

```text
ESVs.fasta
ESVs/
├── ESVs_taxonomy.xlsx        ← filtered result: one taxonomy per ESV
├── ESVs.parquet.snappy
├── IDs.txt
├── log.txt
└── subsets/                  ← raw and filtered BLAST hits per subset
```

`ESVs_taxonomy.xlsx` is the file you need for {doc}`Data analysis <../03_data_analysis/index>`.

```{todo}
Add a screenshot/excerpt of the taxonomy table for the example dataset.
```

## Options

### Main settings

| Argument | Description | Default |
|----------|-------------|---------|
| `-database`, `-db` | Path to the local reference database | *required* |
| `-query_fasta`, `-q` | Path to the query FASTA file | *required* |
| `-out`, `-o` | Output directory | `./blastn` |

### BLASTn settings

| Argument | Description | Default |
|----------|-------------|---------|
| `-n_cores` | Number of CPU cores | CPU count − 2 |
| `-task` | `blastn`, `megablast` or `dc-megablast` | `megablast` |
| `-subset_size` | Sequences per FASTA subset | `100` |
| `-max_target_seqs` | Maximum hits kept per query | `20` |

### Filter settings

| Argument | Description | Default |
|----------|-------------|---------|
| `-thresholds` | Similarity thresholds (comma-separated) | `97,95,90,87,85` |
| `-filter` | `1` = e-value → similarity, `2` = similarity → e-value, `3` = similarity | `2` |
| `-masking` | Pass to disable masking | enabled |
| `-rating_range` | Range of allowed rating values | `5` |
| `-sim_range` | Subtracted from the highest similarity to retain hits | `0` |

### Re-BLAST settings

| Argument | Description | Default |
|----------|-------------|---------|
| `-reblast_db`, `-db2` | Optional second database. Use `"boldigger"` for BOLDigger3 | — |
| `-reblast_sim` | Similarity threshold for re-BLASTing hits against `-db2` | `98` |

### Misc

| Argument | Description | Default |
|----------|-------------|---------|
| `-blastn_exe` | Path to the BLASTn executable | `blastn` |

:::{tip}
For large datasets and large databases (e.g. COI), keep the default task
`megablast`. It is much faster than `blastn`.
:::
