# TaxonTableTools2

[TaxonTableTools2](https://github.com/TillMacher/TaxonTableTools2) (TTT) is a
graphical app for analysing and visualising DNA metabarcoding data, made for
users without programming experience.

**Input:** read table (APSCALE) + taxonomy table (APSCALE-blast or BOLDigger3)
· **Output:** Taxon tables, plots (`.pdf` + interactive `.html`) and the data
behind each plot

:::{warning}
TTT2 is under active development. Check your results carefully and
[report bugs](https://github.com/TillMacher/TaxonTableTools2/issues).
:::

## 1. Start TTT

```bash
conda activate TTT
taxontabletools2
```

The interface opens in your web browser.

```{todo}
Add a screenshot of the start screen.
```

## 2. Create or select a project

1. Enter the path to your **APSCALE projects folder**.
2. TTT creates a `TTT_projects` folder there.
3. Select your project in the dropdown and click **Open Active Project**.

Each project has two subfolders:

```text
TTT_projects/
└── My_project/
    ├── Import/         ← put your input tables here
    └── TaXon_tables/   ← Taxon tables created by TTT
```

## 3. Import your data

Copy your **read table** and **taxonomy table** into the `Import` folder.
Supported formats: `.xlsx` and `.parquet.snappy`.

```{todo}
Show which files from the APSCALE and APSCALE-blast/BOLDigger3 outputs to copy
(exact file names for the example dataset).
```

## 4. Create a Taxon table

Open **🧬 Create Taxon Table**:

1. Select your read table (import format: *APSCALE*).
2. Select your taxonomy table (import format: *APSCALE* for APSCALE-blast, or *BOLDigger*).
3. Enter a name and create the table.

TTT merges both into a **Taxon table** (with a metadata sheet) and saves it
to `TaXon_tables`.

## 5. Load and process the table

Load the table with **Load Table** (click **Refresh** if it doesn't show up).

In **🛠️ Table Processing** you can:

- Merge replicates
- Subtract or remove negative controls
- Filter by reads (absolute or relative), taxa, samples or traits
- Normalise (rarefy) read numbers

:::{note}
Each processing step creates a **new version** of the Taxon table. Refresh and
reload the table before continuing with the next step.
:::

```{todo}
Walk through the processing steps for the example dataset, with the chosen
settings and why.
```

## 6. Analyse and plot

| Section | What you can do |
|---------|-----------------|
| 🖥️ Basic Stats | Reads and ESVs/OTUs per sample, taxonomic resolution |
| 📈 Metabarcoding Basics | Read distribution per taxon, circular taxonomy plots, rarefaction curves |
| 🌱 Alpha Diversity | Richness, Shannon diversity, Heip / Pielou evenness |
| 🌎 Beta Diversity | Jaccard / Bray-Curtis (dis)similarity, PCoA, NMDS |
| 🧪 Sample Comparison | Venn diagrams |
| 🔍 Population Dynamics | Haplotype / intraspecific variation |
| 📍 Biogeography, 📆 Time Series | Spatial and temporal patterns |
| 🌿 GBIF Modules | Species name and occurrence checks via GBIF |
| 🟢 Ecological Status Classes | Assessment indices (e.g. fish or diatom indices) |

```{todo}
Check the section descriptions and add one worked example per section
(settings + resulting figure) using the example dataset.
```

All plots are saved automatically as `.pdf` and interactive `.html`, together
with a table of the underlying data.

## 7. Customise plots

Use the **sidebar** to change plot size, fonts, colours, layout template,
legend and more. Click **💾 Save Settings** to keep them for next time.

## 8. Export

```{todo}
Describe how to export Taxon tables (`.xlsx` / `.h5`) and use them in other
software (e.g. R).
```
