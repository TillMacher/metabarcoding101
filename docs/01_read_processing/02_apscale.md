# APSCALE

[APSCALE](https://github.com/DominikBuchner/apscale) (**A**dvanced **P**ipeline
for **S**imple yet **C**omprehensive **A**na**L**ys**E**s of DNA metabarcoding
data) turns demultiplexed reads into ESV/OTU tables. It runs all common
processing steps and is configured through a single Excel settings file.

**Input:** demultiplexed `.fastq.gz` files · **Output:** ESV/OTU read tables,
`.fasta` files, log files and a project report

APSCALE uses [vsearch](https://github.com/torognes/vsearch),
[cutadapt](https://github.com/marcelm/cutadapt) and
[swarm](https://github.com/torognes/swarm) in the background.

:::{seealso}
Full details on all settings are in the
[APSCALE manual (PDF)](https://github.com/DominikBuchner/apscale/blob/main/manual/apscale_manual.pdf).
:::

## 1. Create a project

```bash
apscale --create_project NAME
```

This creates a project folder with one subfolder per processing step:

```text
NAME_apscale
├── 01_raw_data
├── 02_demultiplexing
├── 03_PE_merging
├── 04_primer_trimming
├── 05_quality_filtering
├── 06_dereplication
├── 07_denoising
├── 08_swarm_clustering
├── 09_replicate_merging
├── 10_nc_removal
├── 11_read_table
├── 12_analyze
└── Settings_NAME.xlsx
```

## 2. Add your data

Copy your **demultiplexed** `.fastq.gz` files into `02_demultiplexing/data`.

:::{note}
APSCALE works with compressed (`.gz`) files only.
:::

## 3. Configure the settings

Open `Settings_NAME.xlsx` in the project folder. It has one sheet per module
plus a `0_general_settings` sheet.

**General settings**

cores to use
: Default: all cores − 2. Lower it if you need your computer for other work.

compression level
: Default: 6. Higher = smaller files but slower; lower = faster.

**Settings you must set yourself**

- **Primer sequences** (forward and reverse) in the primer trimming sheet
- **Expected fragment length** (excluding primers), used for quality filtering

All other settings have sensible defaults.

```{todo}
Add the settings for the example dataset (primers, min/max length) and a
screenshot of the settings file.
```

## 4. Run APSCALE

Run the complete pipeline from inside the project folder:

```bash
apscale --run_apscale
```

Or from anywhere, by giving the project path:

```bash
apscale --run_apscale PATH/TO/PROJECT
```

### Running modules individually

Each step can also be run on its own (optionally followed by the project path):

| Command | Step |
|---------|------|
| `apscale --pe_merging` | Paired-end merging |
| `apscale --primer_trimming` | Primer trimming |
| `apscale --quality_filtering` | Quality filtering |
| `apscale --dereplication` | Dereplication |
| `apscale --denoising` | Denoising (ESVs) |
| `apscale --swarm_clustering` | Swarm clustering (OTUs) |
| `apscale --replicate_merging` | Replicate merging |
| `apscale --nc_removal` | Negative control removal |
| `apscale --generate_read_table` | Read table generation |

Run `apscale -h` to see all options.

### Replicates and negative controls

Replicate merging and negative control removal rely on your **sample names**:

replicate delimiter (`09_replicate_merging` sheet)
: Separates the sample name from the replicate number. Default: `_`
  (e.g. `Site1_A` and `Site1_B` are replicates of `Site1`).

minimum replicate presence
: In how many replicates an ESV/OTU must occur to be kept. Default: `2`.

negative control prefix (`10_nc_removal` sheet)
: Samples starting with this prefix are treated as negative controls. Default: `NC_`.

```{todo}
Explain how the example dataset is named and how negative controls are handled
(what exactly is removed).
```

## 5. Outputs

The main results are written to `11_read_table/data`:

- **Read table** – ESVs/OTUs × samples with read counts
- **`.fasta` file** – the ESV/OTU sequences, used for {doc}`taxonomic assignment <../02_taxonomic_assignment/index>`

Each step also writes a log file, and a **project report** summarises how many
reads passed each step.

```{todo}
Describe the output files for the example dataset and how to check the report
for problems (e.g. low merging rate).
```

## Next step

{doc}`Taxonomic assignment <../02_taxonomic_assignment/index>`
