# Taxonomic assignment

## BLASTn (APSCALE-blast)

![APSCALE-GUI BLASTn](https://raw.githubusercontent.com/TillMacher/apscale_gui/master/_figures/Apscale_gui_4.png)

1. **Download databases.** Download single databases, or use
   **Download All Latest Databases**. They are stored in
   `APSCALE_projects/APSCALE_databases`.
2. **Select** your `.fasta` file and a database.
3. **Start** the BLAST search.

:::{tip}
For large datasets and large databases (e.g. COI), select the task
**megablast**. It is much faster.
:::

Results are written to `11_read_table/data`. See
{doc}`../02_taxonomic_assignment/01_apscale_blast` for how hits are filtered.

## BOLDigger3

![APSCALE-GUI BOLDigger3](https://raw.githubusercontent.com/TillMacher/apscale_gui/master/_figures/Apscale_gui_5.png)

1. **Select** your `.fasta` file and the BOLD database.
2. **Start** the BOLDigger3 search.

Results are written to `11_read_table/data`. See
{doc}`../02_taxonomic_assignment/02_boldigger3` for databases, operating
modes and flags.

```{todo}
Add the database/mode settings and screenshots for the example dataset.
```

## Next step

{doc}`Data analysis <../03_data_analysis/index>`
