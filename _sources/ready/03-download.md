# Downloading the data

All data files used in the lecture are available on the [QCR webserver](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/).

Links and info to be added here as the course unfolds.

(era5-075)=
## ERA5 data (global)

### Ready to use, global low resolution NetCDF files

[ERA5](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5) is an atmospheric reanalysis product. Note that you can download the data yourself (I provide some sample scripts below), but for a start you can download some files I prepared for you:

**Invariant (2D) data:**

- [ERA5_LowRes_Invariant.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes/ERA5_LowRes_Invariant.nc)

**Monthly surface (3D) data:**

- [ERA5_LowRes_Monthly_t2m.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes/ERA5_LowRes_Monthly_t2m.nc): 2m temperature
- [ERA5_LowRes_Monthly_tp.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes/ERA5_LowRes_Monthly_tp.nc): total precipitation

**File naming conventions**:

- `LowRes` means that I asked for a lower spatial resolution than available (0.75° instead of the 0.25° default).
- `Monthly` means that I averaged the data to calendar months
- `MonthlyAvg` means that I averaged the data to all months (annual cycle)
- `4D` means that the data is also available on pressure levels
- `t2m` or `tp` are variable names
- `Invariant` means that this file contains time invariant fields such as topography or land-sea mask.

### Additional ERA5 data from the CDS servers (optional)

You may want to download ERA5 data yourself if:

- you'd like additional variables not listed above
- you'd like to use high resolution data (0.25°) instead of the low resolution (0.75°) that I provided
- you'd like to download hourly or daily data instead of monthly data

If you want to go this path (**optional**), you'll need an account at the [Copernicus Data Store](https://cds.climate.copernicus.eu)

You may want to use their online platform to analyze/download the data, or you can use a script.

Here are a few example scripts to get you started:

- script I used to download all the data listed above: [download_era5.ipynb](https://nbviewer.org/urls/cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/download_era5.ipynb)
- script I used to download the "ultra low res" data listed in the CMIP6 section - the only change is the grid resolution: [download_era5_lr.ipynb](https://nbviewer.org/urls/cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/download_era5.ipynb)
- script I used to download the high resolution data (0.25°) over West Africa: [download_era5_hr_wa.ipynb](https://nbviewer.org/urls/cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/download_era5_hr_wa.ipynb)
