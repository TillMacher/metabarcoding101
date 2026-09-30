# FAQ & troubleshooting

## Installation

**`conda` command not found**
: Install Miniconda (see {doc}`../00_getting-started/01_conda_installation`) and
  use the conda terminal (on Windows: *Anaconda Powershell Prompt*).

**A command is not found (e.g. `apscale`, `taxontabletools2`)**
: Check that the right environment is active: `conda activate apscale4` or
  `conda activate TTT`.

**`vsearch`, `swarm` or `blastn` not found**
: Run `apscale_installer` inside the `apscale4` environment. On Linux and macOS
  (Intel) you can use conda instead, see {doc}`../00_getting-started/02_apscale_env_installation`.

**Creating the environment from the `.yml` file fails**
: Use the manual installation described on the environment pages.

## APSCALE

**My old APSCALE project doesn't work**
: Projects created with APSCALE 3 or older are not compatible with APSCALE 4.
  Create a new project.

**Files or folders don't show up in the APSCALE-GUI**
: Click **Refresh files and folders**.

**Paired-end files are not recognised**
: File names must end with `_R1.fastq.gz` and `_R2.fastq.gz`.

## Taxonomic assignment

**BOLDigger3 asks for a username and password**
: Downloading the BOLD database requires a free account at
  [boldsystems.org](https://www.boldsystems.org). Identifications don't.

**BOLDigger3 stopped in the middle of a run**
: Run the same command again. BOLDigger3 continues where it left off.

**APSCALE-blast is very slow**
: Use the `megablast` task (default) and reduce `-max_target_seqs` if needed.

## TaxonTableTools2

**My table doesn't appear**
: Click **Refresh**, then **Load Table**. This is also needed after each
  processing step, because every step creates a new table version.

```{todo}
Add problems as users report them.
```

## Still stuck?

Open an issue in the repository of the tool (links on the {doc}`home page <../index>`).
