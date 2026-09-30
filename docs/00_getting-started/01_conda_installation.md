# Miniconda installation

All tools in this tutorial are installed with **conda**, which creates isolated
environments so that the tools and their dependencies don't interfere with
anything else on your computer. We use **Miniconda**, a lightweight version of conda.

## 1. Download and install Miniconda

Download the installer for your operating system from the
[Miniconda website](https://www.anaconda.com/download/success) and follow the
installation instructions.

```{todo}
Add screenshots or notes for any installer options users should pay attention to.
```

## 2. Open a conda terminal

Windows
: Search for **Anaconda Powershell Prompt (miniconda3)** in the start menu and open it.

macOS
: Open a new **Terminal** window.

Linux
: Open a new terminal window.

You should now see `(base)` in front of your prompt. This means conda is active.

## 3. Check the installation

```bash
conda --version
```

This should print a version number, e.g. `conda 25.x.x`.

:::{tip}
Always use this conda terminal (not the normal command prompt on Windows) for
all commands in this tutorial.
:::

## Next steps

Install the two environments used in this tutorial:

- {doc}`02_apscale_env_installation` – read processing and taxonomic assignment
- {doc}`03_TTT_env_installation` – data analysis
