# Downloading the data

All data files used in the lecture are available on [this webserver](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/).

## ERA5 data

### Ready to use, low resolution NetCDF files

[ERA5](https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5) is an atmospheric reanalysis product. We will use it a lot! Note that you can download the data yourself (I provide some sample scripts below), but for a start you can download some files I prepared for you:

**Invariant (2D) data:**
- [ERA5_LowRes_Invariant.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes_Invariant.nc)

**Monthly surface (3D) data:**

- [ERA5_LowRes_Monthly_t2m.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes_Monthly_t2m.nc): 2m temperature
- [ERA5_LowRes_Monthly_tp.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes_Monthly_tp.nc): total precipitation

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
- you'd like to download hourly or daily

If you want to go this path (**optional**), you'll need an account at the [Copernicus Data Store](https://cds.climate.copernicus.eu)

You may want to use their online platform to analyze/download the data, or you can use a script. To get you started, [here](https://nbviewer.org/urls/cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/download_era5.ipynb) is the script I use to download all the data listed above.

## CMIP6 data

CMIP6 stands for the Coupled Model Intercomparison Project Phase 6. It is a large collection of climate model simulations from many different models and institutions that formed the basis of IPCC AR6. The data is stored on the [ESGF](https://esgf-node.llnl.gov/projects/cmip6/) (Earth System Grid Federation) servers. I provide a subset of the data on my webserver for you to download. The data is already regridded to a common 2° grid and averaged to monthly values.

### "Ultra" low resolution ERA5 data

This is the same data as you've used so far, but at an even lower resolution of 2°. I've coarsened the data even more to reduce the volume of climate projection data you'll have to manipulate for the assignments. **These datasets should only be used as reference historical data for the CMIP assignments.**

- [ERA5_UltraLowRes_Invariant.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Invariant.nc): invariant data at 2° resolution
- [ERA5_UltraLowRes_Monthly_t2m.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Monthly_t2m.nc): 2m temperature data at 2° resolution
- [ERA5_UltraLowRes_Monthly_tp.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Monthly_tp.nc): precipitation data at 2° resolution

### CMIP6 1979-2100 temperature data

This is the list of Earth System Models (ESMs, sometimes still called Global Circulation Models GCMs) and scenarios for which I provide temperature data. The data is already regridded to a common 2° grid and averaged to monthly values.

```{include} cmip6-list.md
```