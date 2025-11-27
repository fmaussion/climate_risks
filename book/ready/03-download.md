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
- [ERA5_LowRes_Monthly_pet.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes/ERA5_LowRes_Monthly_pet.nc): potential evapotranspiration
- [ERA5_LowRes_Monthly_spei.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes/ERA5_LowRes_Monthly_spei.nc): SPEI

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

The [national river flow archive](https://nrfa.ceh.ac.uk) is a great resource for hydrologist. I downloaded the daily streamflow and precipitation data ([search tool](https://nrfa.ceh.ac.uk/data/search)) for the Chew river near Bristol ([station 53004](https://nrfa.ceh.ac.uk/data/station/meanflow/53004)) and provide it here:

- Chew at Compton Dando - Gauged Daily Flow (gdf): [53004_gdf.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/53004_gdf.csv)
- Chew at Compton Dando - Catchment daily rainfall (cdr): [53004_cdr.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/csv/53004_cdr.csv)

Documentation:

- [Gauged Daily Flow](https://nrfa.ceh.ac.uk/gauged-daily-flow-data)
- [Catchment daily rainfall](https://nrfa.ceh.ac.uk/catchment-rainfall)

### Data for Workshop 04's assignment (future climate at Heathrow)

For this workshop, we will use the following timeseries at Heathrow airport:
- [W5E5v2.0_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/W5E5v2.0_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_historical_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_historical_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp126_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp126_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp370_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp370_tas_lhr_daily.csv)
- [gfdl-esm4_r1i1p1f1_w5e5_ssp585_tas_lhr_daily.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/lhr/csv/tas/gfdl-esm4_r1i1p1f1_w5e5_ssp585_tas_lhr_daily.csv)

The content of these files is explained in the assignment.

### Daily timeseries from ISIMIP

[ISIMIP](https://www.isimip.org/) stands for the "Inter-Sectoral Impact Model Intercomparison Project". I downloaded global daily data for the years 1979-2019 (W5E5) and for 1850-2100 (GFDL-ESM4, MRI-ESM2, UKESM1-0LL) for the variables `tas` (2m temperature), `pr` (precipitation), `tasmax` (max temperature), `tasmin` (min temperature), and `hurs` (relative humidity). This alltogether represents a bit more than 1.6TB of data globally. Therefore, I extracted a number of timeseries for you to download. **Let me know if you need more locations, or perhaps a specific region!**.

The timeseries are available for a number of locations, **together with ERA5 daily data for precipitation and temperature**. Visit the following webpage to explore them all:

- [ISIMIP Timeseries](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/)

If you feel ambitious and want to download global datasets, they are available here:

- [ISIMIP Global Dataset on WCR server](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/raw_dl/).

**Note also that the ISIMIP data download portal is very good and relatively intuitive to use: [data.isimip.org](https://data.isimip.org/).**

## Monthly CMIP6 data (global)

CMIP6 stands for the [Coupled Model Intercomparison Project Phase 6](https://pcmdi.llnl.gov/CMIP6/). It is a large collection of climate model simulations from many different models and institutions that formed the basis of IPCC AR6. The data is stored on the [ESGF](https://esgf-node.llnl.gov/projects/cmip6/) (Earth System Grid Federation) servers. Here I provide a subset of the data on my webserver for you to download.

The data below is regridded to a common grid (2° and 0.75°) and averaged to monthly values.

### Regridded to 2° resolution

At 2° resolution, all CMIP6 temperature and precipitation files represent **9.2GB** of data. With the addition of PET and SPEI, the total is 28GB.

#### Projections

This is the list of Earth System Models (ESMs), sometimes still called Global Circulation Models (GCMs) and scenarios for which I provide temperature data. The data is regridded to a common 2° grid and averaged to monthly values:

```{include} cmip6-list-2deg.md
```

**If you want to avoid having to click on all files and want to download all files at once**, you can use [wget](https://en.wikipedia.org/wiki/Wget). After downloading the list of files provided below, you can use the following command to download all files at once:

```bash
wget -i cmip6-tas-list-2deg.txt
```

- list of temperature files: [cmip6-tas-list-2deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-tas-list-2deg.txt)
- list of precipitation files: [cmip6-pr-list-2deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-pr-list-2deg.txt)
- list of PET files: [cmip6-pet-list-2deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-pet-list-2deg.txt)
- list of SPEI files: [cmip6-spei-list-2deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-spei-list-2deg.txt)

#### 2° resolution ERA5 data

This is the same ERA5 data as you've used so far, but at an even lower resolution of 2°. I've coarsened the data even more to match the CMIP6 data available above:

- [ERA5_UltraLowRes_Invariant.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes/ERA5_UltraLowRes_Invariant.nc): invariant data at 2° resolution
- [ERA5_UltraLowRes_Monthly_t2m.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes/ERA5_UltraLowRes_Monthly_t2m.nc): 2m temperature data at 2° resolution
- [ERA5_UltraLowRes_Monthly_tp.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes/ERA5_UltraLowRes_Monthly_tp.nc): precipitation data at 2° resolution
- [ERA5_UltraLowRes_Monthly_pet.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes/ERA5_UltraLowRes_Monthly_pet.nc): potential evapotranspiration data at 2° resolution
- [ERA5_UltraLowRes_Monthly_spei.nc](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_UltraLowRes/ERA5_UltraLowRes_Monthly_spei.nc): SPEI data at 2° resolution

### Regridded to 0.75° resolution

At 0.75° resolution, all CMIP6 temperature and precipitation files represent **65GB** of data. With the addition of PET and SPEI, the total is 193GB.

#### Projections

The data is regridded to a common 0.75° grid and averaged to monthly values:

```{include} cmip6-list-075deg.md
```

**If you want to avoid having to click on all files and want to download all files at once**, you can use [wget](https://en.wikipedia.org/wiki/Wget). After downloading the list of files provided below, you can use the following command to download all files at once:

```bash
wget -i cmip6-tas-list-075deg.txt
```

- list of temperature files: [cmip6-tas-list-075deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-tas-list-075deg.txt)
- list of precipitation files: [cmip6-pr-list-075deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-pr-list-075deg.txt)
- list of PET files: [cmip6-pet-list-075deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-pet-list-075deg.txt)
- list of SPEI files: [cmip6-spei-list-075deg.txt](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/notebooks/cmip6-spei-list-075deg.txt)

#### 0.75° resolution ERA5 data

See [](era5-075).

### CMIP6 data at their original resolution

See this server for the original resolution files: [OGGM server](https://cluster.klima.uni-bremen.de/~oggm/cmip6/).

(glacier-data)=
## Glacier data

For Workshop 06, we will use data from the [OGGM standard projections](https://github.com/OGGM/oggm-standard-projections-csv-files). We will use the data organised in river basins, which is a bit more hidden than the globally aggregated files.

All 75 river basins (see workshop 06, lesson 02) are available in a single folder: [https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/). Basins are numbered, and I recommend to download the tar file for the basin you are interested in. These folders contain projection data for the scenarios ssp126 and ssp585.

**For workshop 06 Lesson 01, you will need**:

- glacier projections for the Rhone basin (id 6243), a netCDF file: [6243.tar.gz](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/6243.tar.gz)

**For workshop 06 Lesson 02, you will need**:
- statistics for all glaciers in the world (a csv file): [rgi60_stats.csv](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/rgi60_stats.csv)
- the river basins outlines (a shapefile): [glacier_basins.zip](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/glacier_basins.zip)

**For workshop 06's Assignment, you will also need**:

- glacier projections for the Aral Sea catchment (id 2902), a netCDF file: [2902.tar.gz](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/glaciers/projections_per_basin/2309.tar.gz)

## Flood workshop data

For the flood workshop, we prepared a set of dataset for you to download. The data is available in a single zip file, on Sharepoint (access for UoB students only):

[Zip file](https://uob-my.sharepoint.com/:u:/g/personal/uu23343_bristol_ac_uk/EWsR68oAPkJNleVNc-vhg1UBKoP608MyvvnzBnAe2pVhag?e=z0noy2)

Download the file and extract it in the `data` folder of your repository. The content of the zip file is explained in the assignment.
