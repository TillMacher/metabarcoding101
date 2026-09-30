# Installation

We recommend installing everything into a dedicated
[conda](https://docs.conda.io/en/latest/miniconda.html) environment.

## 1. Create a conda environment

```bash
conda create -n metabarcoding python=3.12
conda activate metabarcoding
```

## 2. Install APSCALE

```bash
pip install apscale
```

<!-- TODO: add APSCALE's external dependencies (e.g. vsearch, cutadapt) and how to install them -->

## 3. Install TaxonTableTools

```bash
pip install taxontabletools2
```

<!-- TODO: add the dependency installer step (blast+, vsearch, swarm, playwright) if needed -->

## 4. Check the installation

```bash
apscale --help
```

<!-- TODO: add the command that launches TTT -->

:::{admonition} Troubleshooting
:class: warning
Installation problems? See the {doc}`../faq`.
:::
