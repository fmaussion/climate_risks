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

[ISIMIP](https://www.isimip.org/) stands for the "Inter-Sectoral Impact Model Intercomparison Project". I downloaded global daily data for the years 1979-2019 (W5E5) and for 1850-2100 (GFDL-ESM4) for the variables `tas` (2m temperature), `pr` (precipitation), `tasmax` (max temperature), `tasmin` (min temperature), and `hurs` (relative humidity). This alltogether represents a bit more than 0.5TB of data. Therefore, I extracted a number of timeseries for you to download. **Let me know if you need more locations, or perhaps a specific region!**.

The timeseries are available for a number of locations. Visit the following webpage to explore them all:

- [ISIMIP Timeseries](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ISIMIP/timeseries/)
