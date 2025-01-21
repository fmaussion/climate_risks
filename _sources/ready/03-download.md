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

## Reading data from an url

You can also open files without downloading them locally. This is very inefficient (it will download all data in memory each time you run the notebook), but might be useful if you can't store files. You will need the `h5netcdf` library to be installed for the following to work:

```python
import xarray as xr
import urllib, io

url = 'https://cluster.klima.uni-bremen.de/~fmaussion/teaching/qcr/ERA5_LowRes_Invariant.nc'

req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    ds = xr.open_dataset(io.BytesIO(resp.read()))

ds
```
