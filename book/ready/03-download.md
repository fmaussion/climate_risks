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

CMIP6 stands for the [Coupled Model Intercomparison Project Phase 6](https://pcmdi.llnl.gov/CMIP6/). It is a large collection of climate model simulations from many different models and institutions that formed the basis of IPCC AR6. The data is stored on the [ESGF](https://esgf-node.llnl.gov/projects/cmip6/) (Earth System Grid Federation) servers. Here I provide a subset of the data on my webserver for you to download. The data is already regridded to a common 2° grid and averaged to monthly values.

### "Ultra" low resolution ERA5 data

This is the same ERA5 data as you've used so far, but at an even lower resolution of 2°. I've coarsened the data even more to reduce the volume of climate projection data you'll have to manipulate for the assignments. **These datasets should only be used as reference historical data for the CMIP assignments.**

- [ERA5_UltraLowRes_Invariant.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Invariant.nc): invariant data at 2° resolution
- [ERA5_UltraLowRes_Monthly_t2m.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Monthly_t2m.nc): 2m temperature data at 2° resolution
- [ERA5_UltraLowRes_Monthly_tp.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes_Monthly_tp.nc): precipitation data at 2° resolution

### CMIP6 1979-2100 temperature data

This is the list of Earth System Models (ESMs), sometimes still called Global Circulation Models (GCMs) and scenarios for which I provide temperature data. The data is already regridded to a common 2° grid and averaged to monthly values.

```{include} cmip6-list.md
```

## Timeseries data

### Weather station data

The "[Global Surface Summary of the Day](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00516)"
database is managed by NOAA. It contains daily weather station data from all over the world.
These data are open access by the way! You can download them yourself from the page linked above.

I downloaded the data for the Heathrow weather station near London and provide it here:
- [gsod-heathrow.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/gsod-heathrow.csv)

I also downloaded Bristol and Cardiff data if you are interested:

- [gsod-bristol.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/gsod-bristol.csv)
- [gsod-cardiff.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/gsod-cardiff.csv)

Since we can't trust the current US adminstration to keep this infrastructure
running for the duration of the class, I mirred the GSOD readme on our server -
you'll find it [here](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/readme.txt).

### Daily precipitation and streamflow from the national river flow archive

The [national river flow archive](https://nrfa.ceh.ac.uk) is a great resource for hydrologists. I downloaded the daily streamflow and precipitation data for the Chew river near Bristol ([station 53004](https://nrfa.ceh.ac.uk/data/station/meanflow/53004)) and provide it here:

- Chew at Compton Dando - Gauged Daily Flow (gdf): [53004_gdf.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/53004_gdf.csv)
- Chew at Compton Dando - Catchment daily rainfall (cdr): [53004_cdr.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/53004_cdr.csv)

Documentation:

- [Gauged Daily Flow](https://nrfa.ceh.ac.uk/gauged-daily-flow-data)
- [Catchment daily rainfall](https://nrfa.ceh.ac.uk/catchment-rainfall)

### Daily timeseries from ISIMIP

[ISIMIP](https://www.isimip.org/) stands for the "Inter-Sectoral Impact Model Intercomparison Project".
It is a community-driven modelling effort to understand the impacts of climate change across sectors.
It aims at providing a consistent set of climate change projections for impacts assessments, and coordinates
the development and application of global and regional impact models.

ISIMIP also provides a set of gridded daily data for a number of climate variables. This represents a lot of data, and therefore I provide only a selection of timeseries here. **Do not hesitate to keep in touch if you would like me to prepare more data for you**.

The timeseries for precipitation and temperature are available for a number of locations. Visit the following webpage to explore them all:

- [ISIMIP Timeseries](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/)

#### Data for Workshop 06 (Heathrow)

For this workshop, we will use the following timeseries at Heathrow airport:
- [W5E5v2.0_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/W5E5v2.0_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_historical_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_historical_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp126_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp126_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp370_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp370_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp585_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp585_tas_lhr_daily.csv)

The content of these files is explained in the assignment.

## Glacier data

For Workshop 07, we will use data from the [OGGM standard projections](https://github.com/OGGM/oggm-standard-projections-csv-files). We will use the data organised in river basins, which is a bit more hidden than the globally aggregated files.

All 75 river basins (see workshop 07, lesson 02) are available in a single folder: [https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/). Basins are numbered, and I recommend to download the tar file for the basin you are interested in. These folder contain projection data for the scenarios ssp126 and ssp585.

**For workshop 07, you will need three files to get started**:

- glacier projections for the Rhone basin (id 6243), a netCDF file: [6243.tar.gz](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/6243.tar.gz)
- statistics for all glaciers in the world (a csv file): [rgi60_stats.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/rgi60_stats.csv)
- the river basins outlines (a shapefile): [glacier_basins.zip](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/glacier_basins.zip)

## Flood workshop data

For the flood workshop, we prepared a set of dataset for you to download. The data is available in a single zip file, on Sharepoint (access for UoB students only):

[Zip file](https://uob-my.sharepoint.com/:u:/g/personal/uu23343_bristol_ac_uk/EWsR68oAPkJNleVNc-vhg1UBKoP608MyvvnzBnAe2pVhag?e=ah3ONe)

Download the file and extract it in the `data` folder of your repository. The content of the zip file is explained in the assignment.
