# TaxonTableTools2 environment

The `TTT` environment contains
[TaxonTableTools2](https://github.com/TillMacher/TaxonTableTools2), which is
used for {doc}`data analysis <../03_data_analysis/index>`.

**Requirements:** Windows 10/11 or macOS (Apple silicon) · Python 3.10 or
higher (installed automatically). On Linux, use the
[manual installation](#manual-installation-linux) below.

## 1. Download the environment file

Download
[taxontabletools2_env.yml](https://github.com/TillMacher/TaxonTableTools2/blob/main/environments/taxontabletools2_env.yml)
and save it somewhere you can find it.

## 2. Create the environment

```bash
conda env create -f taxontabletools2_env.yml
```

## 3. Activate the environment

```bash
conda activate TTT
```

## 4. Start TaxonTableTools2

```bash
taxontabletools2
```

The graphical interface opens automatically in your web browser.

```{todo}
Add a screenshot of the TTT start screen.
```

## Manual installation (Linux)

```bash
conda create -n TTT python=3.13
conda activate TTT
pip install taxontabletools2
conda install -c conda-forge scikit-bio
taxontabletools2
```

## Updating

```bash
conda activate TTT
pip install --upgrade taxontabletools2
```

TTT also shows a notice in its sidebar when a new version is available.
