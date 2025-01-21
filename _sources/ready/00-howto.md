# How to use this website and prepare for each week

## Install Python and JupyterLab

You have several options available for this class. You can even switch between them depending on your daily mood!

1. **Install Python and JupyterLab on your personal computer**
   This is the recommended option if you have a computer you can use for the entire term, but it is not mandatory. Installing Python and JupyterLab on your personal device allows you to work on assignments and projects without relying on the university's workstations. Follow the instructions on this website to install [Python](01-installation) and [JupyterLab](02-install-jupyter) on your computer.

2. **Use the university's workstations**
   Python is already set up on these machines. However, you will need to install [JupyterLab and the required packages](02-install-jupyter) for each workstation you use. This is a good option if you don’t have a compatible computer or prefer not to carry one around.

3. **Use OGGM Classroom**
   This is a free service that allows you to run Jupyter Notebooks on the OGGM servers. You won’t need to install anything, but it requires a stable internet connection. We will call this "Plan C", and I’ll recommend it only if you have no other option.

## Jupyter notebooks

Jupyter Notebooks have become a central tool in the scientific Python ecosystem. The advantage of Jupyter Notebooks over traditional code scripts in text files is that they can include text, code, and plots in the same document. Notebooks are a fantastic tool to explore data or models and to communicate science.

Notebooks are an ideal playground for learning Python and writing your assignments without having to jump between several documents! We will use notebooks for the entire class. In fact, this website is written with Jupyter Notebooks!

## Organizing your notebooks

The notebooks are central to this lecture. We won’t use anything other than notebooks to write code (and text!), and you will have to submit notebooks as your final project report as well.

Each week’s notebooks should be downloaded and run on your machine. You will also be asked to download data files ([](03-download)). I recommend organizing your code and data so that you can easily access both wherever you are. Your university OneDrive account is perfect for this: create a "QCR" folder and store all your notebooks and data there. I recommend organizing your notebooks in weekly folders, and alongside my weekly folders, there is a `data` folder where my data is stored. This way, the paths to data files in my notebooks look like:

```python
ds = xr.open_dataset(r'../data/ERA5_LowRes_Monthly_t2m.nc')
```

The `../` navigates to the parent folder, and from there I can find the data file.

## Preparing for each week

Most weeks are organized around two notebooks:

- A "lesson," where you will learn new tools. It is mostly "click-through" code that I wrote (and that you'll reuse later) with some understanding questions in between.
- An "assignment," where you'll apply the tools you've learned before.

```{note}
The **main objective of the practicals is to learn about climate risks and their quantification**. Learning to use the notebooks and coding is important as well, but only secondary!
```

## Tips for the presenting group

Each week, a volunteer group will present their results to the rest of the class. This part is not marked and will have no negative effect whatsoever on the rest of the class. The main objective of the group presentations is for me to focus on what is really creating problems for students (as opposed to me assuming what will).

Here are a few suggestions to prepare your contributions:

- Make sure that you have managed to do parts of the requested analyses. It doesn't have to be all of them or be 100% perfect (nothing is!), but if you have substantial problems with one exercise, please contact me beforehand.
- In your presentations, focus on the "assignment" notebook. If one of the points or questions in the "lesson" notebook was unclear to you, feel free to discuss it as well!
- Focus on the main plots/analyses and what you didn’t understand well. There are no stupid questions or comments! If you don’t understand something, feel free to address it in your presentation: it is very likely that all of us have the same issues.
