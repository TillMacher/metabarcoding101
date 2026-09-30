# Overview

The **[APSCALE-GUI](https://github.com/TillMacher/apscale_gui)** bundles
Demultiplexer2, APSCALE, APSCALE-blast and BOLDigger3 in one graphical app.
It runs the same steps as the command-line chapters, so you can use either route.

| Step | Command line | GUI |
|------|--------------|-----|
| Read processing | {doc}`Read processing <../01_read_processing/index>` | {doc}`01_read_processing` |
| Taxonomic assignment | {doc}`Taxonomic assignment <../02_taxonomic_assignment/index>` | {doc}`02_taxonomic_assignment` |

![APSCALE-GUI start window](https://raw.githubusercontent.com/TillMacher/apscale_gui/master/_figures/Apscale_gui_1.png)

## Start the GUI

```bash
conda activate apscale4
apscale_gui
```

The interface opens in your web browser.

## Set up your projects folder

1. Create a folder for all your projects, e.g. `APSCALE_projects` on your desktop.
2. Paste the path to this folder into the GUI. You can tick the option to remember it.
3. Click the button to create the **database** and **tagging scheme** folders inside it.

:::{tip}
If new files or folders don't show up, click **Refresh files and folders**.
:::

## Create a project

Type a project name and click the button to create it. This creates the same
folder structure and settings file as the command-line version
(see {doc}`../01_read_processing/02_apscale`).

## Add your data

Non-demultiplexed reads
: Copy to `01_raw_data/data`

Already demultiplexed reads
: Copy to `02_demultiplexing/data`

:::{important}
File names of paired-end reads must end with `_R1.fastq.gz` and `_R2.fastq.gz`.
:::

:::{warning}
Projects created with APSCALE 3 or older are not compatible with APSCALE 4.
Create a new project instead.
:::

```{todo}
Add screenshots of the project setup for the example dataset.
```
