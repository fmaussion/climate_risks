# Installing Python (optional)


```{figure} https://www.python.org/static/community_logos/python-logo.png
---
figclass: margin
---
```

This chapter provides instructions on how to install Python on your personal computer.

Installing Python on your device is optional. All class exercises can be completed using the university’s workstations. However, installing Python on your own device allows you to work on exercises at home and can be a valuable learning experience.

There are multiple ways to install Python on your computer. While most methods work, some are more practical than others. Unless you are experienced with Python installations (i.e., you have done this before), please follow these instructions carefully.


```{admonition} What to do if you **already** have python installed on your laptop
:class: warning, dropdown

**If you already have Anaconda, Conda, or Miniconda installed from a previous class:**

You can keep your installation if it works for you. If you'd prefer to start fresh, uninstall Anaconda and follow the instructions below.

---

**If you're unsure what this means:**

Follow the instructions below.
```

```{admonition} For Windows 7 or Chromebook users
:class: warning, dropdown

Do not attempt to install Python on a Windows 7 computer. This operating system is no longer supported. You can use the university's workstations for the exercises instead.

Installing Python on a Chromebook is not straightforward, and I cannot provide support for this. You can still use the university's workstations to complete the exercises.
```

## Install Miniconda

We will use an installation option with a minimal footprint on your computer: [Miniforge](https://github.com/conda-forge/miniforge)

`````{tab-set}
:sync-group: oscategory

````{tab-item} On Windows
:sync: win

Download [the Windows installer](https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Windows-x86_64.exe) amd double-click the `.exe` file to execute it.

Follow the prompts, taking note of the options to "Create start menu shortcuts" and "Add Miniforge3 to my PATH environment variable".
I'd recommend you to **not** add Miniforge3 to the PATH environment variable, as it can cause conflicts with other software (it is ticked off per default).
Without Miniforge3 on the path, the most convenient way to use the installed software (such as commands conda and mamba) will be via the "Miniforge Prompt" installed to the start menu (see [](test-install) below).

```{admonition} Important! About the installation location
:class: warning

Choose a folder located in where there is enough space available, for example in your user directory (e.g. `C:\Users\yourname\Miniforge3`). Do not install in a folder with special characters in the name (e.g. french accents), as this can cause issues with conda.
```

````

````{tab-item} On Mac OS and Linux
:sync: os

For these platforms, no need to download the files yourself, but you need to run a script. See the instructions [here](https://github.com/conda-forge/miniforge?tab=readme-ov-file#unix-like-platforms-macos--linux).

````
`````

(test-install)=
### Testing your installation

To see if everything worked well, open a terminal prompt.

`````{tab-set}
:sync-group: oscategory

````{tab-item} On Windows
:sync: win

On Windows, open the `miniforge prompt` (from the Start menu, search for and open "miniforge prompt"):

```{image} ../img/miniforge.png
:alt: miniforge prompt
:class: bg-primary mb-1
:width: 400px
```

<br>

The prompt you opened should display a line like this:

```none
(base) C:\Windows\System32>
```

````

````{tab-item} On Mac OS and Linux
:sync: os

For these platforms, the terminal is available by default. You can open it by searching for "terminal" in the search bar.

````

`````

Now you should have a terminal window open. In the terminal, type:

```none
mamba list
```

You should see a long list of package names.

If you type:

```none
python
```

A new python prompt should appear, with something like:

```none
Python 3.12.7 | packaged by Anaconda, Inc. | (main, Oct  4 2024, 13:17:27) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can type ``exit()`` to get out of the python interpreter.

```{admonition} Optional: a brief explanation of what we've just done
:class: note, dropdown

The steps above should work in nearly all situations and prepare you for the class. Here's a brief explanation in case you're curious or need to search for more information:

We installed [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a minimal installer for the larger Anaconda project. Anaconda is a scientific Python distribution, but it includes more tools than you will need.

**Additionally, we made some default configurations:**
- We set [Conda-Forge](https://conda-forge.org/) as the default channel for downloading Python packages (instead of the default Anaconda channel).
- We replaced `conda` with [Mamba](https://mamba.readthedocs.io) as the default package manager. `mamba install` works the same way as `conda install` but is significantly faster.
```

## Learning checklist

<label><input type="checkbox" id="week05_01" class="box"> I learned how to install Python on my computer.</input></label>
<label><input type="checkbox" id="week05_02" class="box"> I know how to open a Python interpreter from the Miniforge Prompt (or the terminal on Linux/macOS) and close it using exit().</input></label>
