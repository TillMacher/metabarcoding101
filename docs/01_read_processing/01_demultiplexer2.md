# Demultiplexer2

[Demultiplexer2](https://github.com/DominikBuchner/demultiplexer2) sorts
paired-end Illumina reads into samples by identifying the **inline tags** at
the start of each read.

**Input:** gzipped `.fastq.gz` file pairs · **Output:** one gzipped `.fastq.gz`
pair per sample

:::{important}
Demultiplexer2 has been succeeded by
[demultiplexer3](https://github.com/DominikBuchner/demultiplexer3), which is
faster and uses the same three steps (replace `demultiplexer2` with
`demultiplexer3` in the commands). The `apscale4` environment and the
APSCALE-GUI currently still use Demultiplexer2.
:::

```{todo}
Decide whether this page should use demultiplexer2 or demultiplexer3.
```

The workflow has three steps:

1. **Primer set:** which primers and tags were used
2. **Tagging scheme:** which tag combination belongs to which sample
3. **Demultiplex**

## Step 1: Create a primer set

A *primer set* is an Excel file describing the primers and tags of your
dataset. It is saved in the `demultiplexer2/data` folder so you can reuse it.

```bash
demultiplexer2 create_primerset --name NameOfPrimerset --n_primers NumberOfPrimers
```

`--name`
: Name of the primer set (e.g. `fwh2F2-fwhR2n`)

`--n_primers`
: Number of primers in your dataset

Open the Excel file and fill in its three sheets:

1. **General information** – the primers used for amplification
2. **Forward tags** – names and sequences of the forward tags
3. **Reverse tags** – names and sequences of the reverse tags

```{todo}
Add a screenshot of a filled-in primer set for the example dataset.
```

## Step 2: Create a tagging scheme

The *tagging scheme* links each input file and tag combination to a sample name.

```bash
demultiplexer2 create_tagging_scheme --name NameOfTaggingScheme --data_dir InputDirectory --primerset_path PathToPrimerset
```

`--name`
: Name of the tagging scheme (e.g. `MyFirstStudy`)

`--data_dir`
: Folder containing the `.fastq.gz` files to demultiplex

`--primerset_path`
: Path to the primer set from step 1

The tagging scheme is saved to the current folder. Open it and **add your
sample names** before continuing.

```{todo}
Add a screenshot of a filled-in tagging scheme.
```

## Step 3: Demultiplex

```bash
demultiplexer2 demultiplex --primerset_path PathToPrimerset --tagging_scheme_path PathToTaggingScheme --output_dir OutputDirectory
```

`--output_dir`
: Folder to write the demultiplexed files to

Demultiplexer2 reports how many reads matched a tag combination for each input
file pair. Unmatched reads are discarded.

```text
08:58:58: TEST_001_r1.fastq.gz - TEST_001_r2.fastq.gz: 16865 of 100000 sequences matched the provided tag sequences (16.86 %)
```

```{todo}
Add the output for the example dataset and explain what a "good" match rate looks like.
```

## Next step

Copy the demultiplexed files into your APSCALE project: {doc}`02_apscale`.
