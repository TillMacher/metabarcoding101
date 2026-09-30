# APSCALE4 environment

The `apscale4` environment contains everything for read processing and
taxonomic assignment:

- [APSCALE](https://github.com/DominikBuchner/apscale) and [APSCALE-GUI](https://github.com/TillMacher/apscale_gui)
- [APSCALE-blast](https://github.com/TillMacher/apscale_blast)
- [BOLDigger3](https://github.com/DominikBuchner/boldigger3)
- [Demultiplexer2](https://github.com/DominikBuchner/demultiplexer2)
- the `apscale_installer` helper, which installs vsearch, swarm and blast+

**Requirements:** Windows, macOS or Linux · Python 3.12 (installed automatically)

## 1. Download the environment file

Download
[apscale_env.yml](https://github.com/TillMacher/apscale_installer/blob/main/environments/apscale_env.yml)
(Windows & macOS) and save it somewhere you can find it, e.g. your Downloads folder.

## 2. Create the environment

In your conda terminal, run (adjust the path to where you saved the file):

```bash
conda env create -f apscale_env.yml
```

## 3. Activate the environment

```bash
conda activate apscale4
```

## 4. Install vsearch, swarm and blast+

vsearch and blast+ can't be installed automatically via conda on Windows and
macOS (Apple silicon), so use the installer script:


**Windows and macOS:**

```bash
apscale_installer
```

**Linux and macOS (Intel):**

```bash
conda install bioconda::vsearch
conda install bioconda::blast
conda install bioconda::swarm
playwright install
```

## 5. Check the installation

```bash
vsearch --version
swarm --version
blastn -h
cutadapt --version
```

Each command should print a version number or help text without errors.

```{todo}
Add a screenshot of a successful check, or the expected output.
```

## Alternative: manual installation

If creating the environment from the `.yml` file fails:

```bash
conda create -n apscale4 python=3.12 ipython
conda activate apscale4
pip install apscale apscale_gui apscale_installer apscale_blast boldigger3 demultiplexer2
apscale_installer
```

## Updating

```bash
conda activate apscale4
pip install --upgrade apscale apscale_gui apscale_blast boldigger3 demultiplexer2
```

:::{warning}
The old `apscale` environment (Python 3.10) is outdated. Remove it with
`conda remove -n apscale --all` and use `apscale4` instead.
:::

:::{seealso}
There is also a [video tutorial](https://www.youtube.com/watch?v=c6pm0FhcINI)
showing the installation on Windows and macOS.
:::
