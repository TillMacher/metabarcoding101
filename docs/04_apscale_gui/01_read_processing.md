# Read processing

![APSCALE-GUI main window](https://raw.githubusercontent.com/TillMacher/apscale_gui/master/_figures/Apscale_gui_2.png)

## Demultiplexing

Only needed if your reads are in `01_raw_data/data` (not yet demultiplexed).
The GUI uses {doc}`Demultiplexer2 <../01_read_processing/01_demultiplexer2>`.

1. **Create a primer set** with the number of primers used in your project.
2. **Create a tagging scheme** based on the primer set. The Excel file opens
   automatically: fill in the tag combinations and sample names of your library.
3. **Start demultiplexing.**

When it has finished, the original files are moved from `01_raw_data/data` to
`01_raw_data/processed`, and the demultiplexing option disappears from the GUI.

```{todo}
Add screenshots of the primer set and tagging scheme for the example dataset.
```

## Raw data processing

![APSCALE-GUI raw data processing](https://raw.githubusercontent.com/TillMacher/apscale_gui/master/_figures/Apscale_gui_3.png)

Most settings can stay at their defaults. You must set:

- **Primer sequences** (forward and reverse)
- **Minimum and maximum fragment length**

Choose how to run APSCALE:

Basic mode
: Runs all modules **except** replicate merging and negative control removal.

Complete mode
: Runs all modules. Check that the **replicate delimiter** and **negative
  control prefix** match your sample names.

Individual commands
: Run each module separately.

The read tables and `.fasta` files are written to `11_read_table/data`.

For details on the settings, see {doc}`../01_read_processing/02_apscale` and the
[APSCALE manual (PDF)](https://github.com/DominikBuchner/apscale/blob/main/manual/apscale_manual.pdf).

```{todo}
Add the settings used for the example dataset and a screenshot of a finished run.
```

## Next step

{doc}`02_taxonomic_assignment`
