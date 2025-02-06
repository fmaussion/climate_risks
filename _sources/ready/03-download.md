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

TODO

```{dropdown} BCC-CSM2-MR
**Temperature** (`tas`)
- [BCC-CSM2-MR_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/BCC-CSM2-MR/BCC-CSM2-MR_ssp126_regridded_tas.nc)
- [BCC-CSM2-MR_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/BCC-CSM2-MR/BCC-CSM2-MR_ssp245_regridded_tas.nc)
- [BCC-CSM2-MR_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/BCC-CSM2-MR/BCC-CSM2-MR_ssp370_regridded_tas.nc)
- [BCC-CSM2-MR_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/BCC-CSM2-MR/BCC-CSM2-MR_ssp585_regridded_tas.nc)
```

```{dropdown} CAMS-CSM1-0
**Temperature** (`tas`)
- [CAMS-CSM1-0_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CAMS-CSM1-0/CAMS-CSM1-0_ssp126_regridded_tas.nc)
- [CAMS-CSM1-0_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CAMS-CSM1-0/CAMS-CSM1-0_ssp245_regridded_tas.nc)
- [CAMS-CSM1-0_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CAMS-CSM1-0/CAMS-CSM1-0_ssp370_regridded_tas.nc)
- [CAMS-CSM1-0_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CAMS-CSM1-0/CAMS-CSM1-0_ssp585_regridded_tas.nc)
```

```{dropdown} CESM2
**Temperature** (`tas`)
- [CESM2_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2/CESM2_ssp126_regridded_tas.nc)
- [CESM2_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2/CESM2_ssp245_regridded_tas.nc)
- [CESM2_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2/CESM2_ssp370_regridded_tas.nc)
- [CESM2_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2/CESM2_ssp585_regridded_tas.nc)
```

```{dropdown} CESM2-WACCM
**Temperature** (`tas`)
- [CESM2-WACCM_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2-WACCM/CESM2-WACCM_ssp126_regridded_tas.nc)
- [CESM2-WACCM_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2-WACCM/CESM2-WACCM_ssp245_regridded_tas.nc)
- [CESM2-WACCM_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2-WACCM/CESM2-WACCM_ssp370_regridded_tas.nc)
- [CESM2-WACCM_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/CESM2-WACCM/CESM2-WACCM_ssp585_regridded_tas.nc)
```

```{dropdown} EC-Earth3
**Temperature** (`tas`)
- [EC-Earth3_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3/EC-Earth3_ssp126_regridded_tas.nc)
- [EC-Earth3_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3/EC-Earth3_ssp245_regridded_tas.nc)
- [EC-Earth3_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3/EC-Earth3_ssp370_regridded_tas.nc)
- [EC-Earth3_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3/EC-Earth3_ssp585_regridded_tas.nc)
```

```{dropdown} EC-Earth3-Veg
**Temperature** (`tas`)
- [EC-Earth3-Veg_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3-Veg/EC-Earth3-Veg_ssp126_regridded_tas.nc)
- [EC-Earth3-Veg_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3-Veg/EC-Earth3-Veg_ssp245_regridded_tas.nc)
- [EC-Earth3-Veg_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3-Veg/EC-Earth3-Veg_ssp370_regridded_tas.nc)
- [EC-Earth3-Veg_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/EC-Earth3-Veg/EC-Earth3-Veg_ssp585_regridded_tas.nc)
```

```{dropdown} FGOALS-f3-L
**Temperature** (`tas`)
- [FGOALS-f3-L_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/FGOALS-f3-L/FGOALS-f3-L_ssp126_regridded_tas.nc)
- [FGOALS-f3-L_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/FGOALS-f3-L/FGOALS-f3-L_ssp245_regridded_tas.nc)
- [FGOALS-f3-L_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/FGOALS-f3-L/FGOALS-f3-L_ssp370_regridded_tas.nc)
- [FGOALS-f3-L_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/FGOALS-f3-L/FGOALS-f3-L_ssp585_regridded_tas.nc)
```

```{dropdown} GFDL-ESM4
**Temperature** (`tas`)
- [GFDL-ESM4_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/GFDL-ESM4/GFDL-ESM4_ssp126_regridded_tas.nc)
- [GFDL-ESM4_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/GFDL-ESM4/GFDL-ESM4_ssp245_regridded_tas.nc)
- [GFDL-ESM4_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/GFDL-ESM4/GFDL-ESM4_ssp370_regridded_tas.nc)
- [GFDL-ESM4_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/GFDL-ESM4/GFDL-ESM4_ssp585_regridded_tas.nc)
```

```{dropdown} INM-CM4-8
**Temperature** (`tas`)
- [INM-CM4-8_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM4-8/INM-CM4-8_ssp126_regridded_tas.nc)
- [INM-CM4-8_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM4-8/INM-CM4-8_ssp245_regridded_tas.nc)
- [INM-CM4-8_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM4-8/INM-CM4-8_ssp370_regridded_tas.nc)
- [INM-CM4-8_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM4-8/INM-CM4-8_ssp585_regridded_tas.nc)
```

```{dropdown} INM-CM5-0
**Temperature** (`tas`)
- [INM-CM5-0_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM5-0/INM-CM5-0_ssp126_regridded_tas.nc)
- [INM-CM5-0_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM5-0/INM-CM5-0_ssp245_regridded_tas.nc)
- [INM-CM5-0_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM5-0/INM-CM5-0_ssp370_regridded_tas.nc)
- [INM-CM5-0_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/INM-CM5-0/INM-CM5-0_ssp585_regridded_tas.nc)
```

```{dropdown} MPI-ESM1-2-HR
**Temperature** (`tas`)
- [MPI-ESM1-2-HR_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MPI-ESM1-2-HR/MPI-ESM1-2-HR_ssp126_regridded_tas.nc)
- [MPI-ESM1-2-HR_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MPI-ESM1-2-HR/MPI-ESM1-2-HR_ssp245_regridded_tas.nc)
- [MPI-ESM1-2-HR_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MPI-ESM1-2-HR/MPI-ESM1-2-HR_ssp370_regridded_tas.nc)
- [MPI-ESM1-2-HR_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MPI-ESM1-2-HR/MPI-ESM1-2-HR_ssp585_regridded_tas.nc)
```

```{dropdown} MRI-ESM2-0
**Temperature** (`tas`)
- [MRI-ESM2-0_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MRI-ESM2-0/MRI-ESM2-0_ssp126_regridded_tas.nc)
- [MRI-ESM2-0_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MRI-ESM2-0/MRI-ESM2-0_ssp245_regridded_tas.nc)
- [MRI-ESM2-0_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MRI-ESM2-0/MRI-ESM2-0_ssp370_regridded_tas.nc)
- [MRI-ESM2-0_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/MRI-ESM2-0/MRI-ESM2-0_ssp585_regridded_tas.nc)
```

```{dropdown} NorESM2-MM
**Temperature** (`tas`)
- [NorESM2-MM_ssp126](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/NorESM2-MM/NorESM2-MM_ssp126_regridded_tas.nc)
- [NorESM2-MM_ssp245](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/NorESM2-MM/NorESM2-MM_ssp245_regridded_tas.nc)
- [NorESM2-MM_ssp370](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/NorESM2-MM/NorESM2-MM_ssp370_regridded_tas.nc)
- [NorESM2-MM_ssp585](https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/CMIP6/NorESM2-MM/NorESM2-MM_ssp585_regridded_tas.nc)
```
