# Installing JupyterLab (all platforms)

This chapter contains the instructions about how to install additional useful tools which will enhance your python installation a great deal!

```{note}
Installing JupyterLab and the python packages need to be done **only once** on the computer you are using! If you are using a workstation in a lab, you will have to do it again if you change for another workstation or if the workstation is reset.
```

## Prerequisites

 I'll assume that the [python installation instructions](01-installation) have worked for you (or that you are using a university workstation), and that you:

- are able to start a miniforge prompt
- can type `mamba list` successfully (`conda list` on the university's workstations)
- can type `python` and open a python interpreter.

For a primer on the different prompts and interpreters, see [my beginners' programming class notes](https://fabienmaussion.info/intro_to_programming/week_02/01-Install-jupyter.html#explanation-the-difference-between-the-command-prompt-the-miniforge-prompt-and-the-python-interpreter)

## Installation instructions

Open a miniforge prompt (or a terminal on Linux/macOS) and type:

`````{tab-set}
:sync-group: compcategory

````{tab-item} On university workstations / Anaconda
:sync: university

```
conda create --name qcr --channel conda-forge python=3.12 jupyterlab numpy scipy matplotlib xarray netcdf4 cartopy cftime geopandas seaborn rioxarray
```

````

````{tab-item} On your personal computer / Miniforge
:sync: forge

```
mamba create --name qcr --channel conda-forge jupyterlab numpy scipy matplotlib xarray netcdf4 cartopy cftime geopandas seaborn rioxarray
```

````

`````

This will install jupyter-lab and all the packages at the same time. Say "yes" to the install question. To check if it worked, type `ipython
` in the terminal, which should display something like:

```none
Python 3.9.7 | packaged by conda-forge | (default, Sep 29 2021, 19:15:42) [MSC v.1916 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

The only *visual* difference between the `ipython` and `python` interpreters is that `>>>` has been replaced by `In [1]:`. More on this in class if you are interested.

Exit `ipython` (remember how? Use `exit()`) and move on to the next step.

```{note}
The packages `cftime`, `geopandas` and `rioxarray` have been added as a requirement for Workshop 7. To install them *in an existing `qcr` environment*, start by activating the environment with `conda activate qcr` and then type `mamba install --channel conda-forge cftime geopandas rioxarray` or, if `mamba` is not available, `conda install --channel conda-forge cftime geopandas rioxarray`.
```

## Opening JupyterLab in the qcr environment and folder

```{note}
This needs to be done every time you want to work on your notebooks!
```

From now on, and regardless of the computer you are using, you will have to activate the `qcr` environment before starting `jupyter-lab`. I **strongly** recommend to start `jupyter-lab` from the folder where you want to work (i.e. where you have saved your notebooks and data).

The steps are as follows:

1. Open a miniforge prompt (or a terminal on Linux/macOS)
2. Navigate to the folder where you want to work by typing:

    ```none
    cd C:\path\to\folder
    ```

    I recommend copying the path from the file explorer - see video below for an example.

3. Activate the `qcr` environment by typing:

    ```none
    conda activate qcr
    ```

4. Start `jupyter-lab` by typing:

    ```none
    jupyter-lab
    ```

This is best explained with a simple video:

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1048667583?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Open the prompt, navigate to a folder and start JupyterLab"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

If you are new to JupyterLab, ou can [watch this video on my beginners class](https://fabienmaussion.info/intro_to_programming/week_03/01-Intro-notebooks.html).

## Learning checklist

<label><input type="checkbox" id="week05_01" class="box"> I know how to install jupyter on any computer and start jupyter-lab from a specific folder.</input></label>
<label><input type="checkbox" id="week05_02" class="box"> I know how to activate an environment and start `jupyter-lab` from the prompt.</input></label>