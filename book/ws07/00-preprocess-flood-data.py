import geopandas as gpd
import pandas as pd
import xarray as xr
from rioxarray.raster_array import Resampling
from rasterio.features import rasterize
from rasterio.enums import MergeAlg
import os
import numpy as np
import re

#   Define top directory + list data folders
wd = "C:/Users/Hamish/Desktop/PhD/TSR/data/raw/"
od = "C:/Users/Hamish/Desktop/PhD/TSR/data/processed/"
folders = os.listdir(wd)

#   Use to build paths
dem_pth = wd + folders[0]+"/"
new_dem_pth = od + folders[0]+"/"

pop_pth = wd + folders[1]+"/"
new_pop_pth = od + folders[1]+"/"

sfincs_pth = wd+folders[2]+"/"
new_sfincs_pth = od+folders[2]+"/"

#   Build pop file paths
pop = os.listdir(pop_pth)
pop_proj_pth = [gpkg for gpkg in pop if "stripped" in gpkg][0]
new_pop_proj_pth = new_pop_pth + "cropped_" + re.sub(".gpkg", ".nc", pop_proj_pth)
pop_proj_pth = pop_pth + pop_proj_pth
worldpop_pth = [tif for tif in pop if ".tif" in tif][0]
new_worldpop_pth =  new_pop_pth + "cropped_" + worldpop_pth
worldpop_pth =  pop_pth + worldpop_pth

#   Build dem pths
dem = os.listdir(dem_pth)
new_nsi_pth = new_dem_pth + "cropped_" + re.sub(".gpkg", ".nc", dem[0])
nsi_pth = dem_pth + dem[0]
new_adi_pth = new_dem_pth + "cropped_" + re.sub(".csv", ".gpkg", dem[1])
adi_pth = dem_pth + dem[1]
census_pth = dem_pth + dem[2]

#   Build sfincs runs file paths
sfincs_runs = os.listdir(sfincs_pth)
sfincs_runs_new = [new_sfincs_pth + "epsg_4326_" +s_r for s_r in sfincs_runs]
sfincs_runs = [sfincs_pth + s_r for s_r in sfincs_runs]

#   Reformat sfincs to be user friendly
for i in range(len(sfincs_runs)):
    print("Working on SFINCS output " + str(i+1) + " of " + str(len(sfincs_runs)) + "..")
    target = xr.open_dataset(sfincs_runs[i])
    #target["zsmax"].plot() # Note spatial dims are indexs
    
    #   Clarity
    target = target.rename({"n" : "y_ind",
                            "m" : "x_ind"})
    
    # Extract unique x and y values (flatten to give shape)
    x_1d = np.unique(target["x"].values)
    y_1d = np.unique(target["y"].values)
    
    #   Assign spatial coordinates to the indexes
    target = target.assign_coords({"x_ind": x_1d, "y_ind": y_1d})
    #target["zsmax"].plot() # Better
    target = target.drop_vars(["x", "y", "corner_x", "corner_y"])
    target = target.rename({"y_ind" : "y", "x_ind" : "x"}) # Reflect change
    
    #   Reproject to epsg 4326 for ease of use
    old_crs = "EPSG:"+str(target.crs.values)  # UTM code - we want wgs84
    target = target.rio.write_crs(old_crs)
    target = target.rio.reproject("EPSG:4326")
    target = target.rio.write_crs("EPSG:4326")
    
    #   Write to disk
    target.to_netcdf(sfincs_runs_new[i])

#   Fetch bbox from flood map
bbox = target.rio.bounds()

#   Crop / resample spatial data 

#   Worldpop (tif)
worldpop = xr.open_dataset(worldpop_pth)

#   Crop
worldpop = worldpop.rio.clip_box(minx=bbox[0], miny=bbox[1],
                                 maxx=bbox[2], maxy=bbox[3])

#   Resample (aka regrid) - sum all values
np.sum(worldpop["band_data"]) # To check 
worldpop = worldpop.rio.reproject_match(target, resampling=Resampling.sum)
np.sum(worldpop["band_data"]) # To check
worldpop["band_data"].plot() # To see
#   Note we actually loss some pop here- potentially grid misalignment. For the
#   purpose of this exercise I am not fussed.
worldpop["band_data"].rio.to_raster(new_worldpop_pth)

#   Pop projections
pop_proj = gpd.read_file(pop_proj_pth) # Read
pop_proj.crs # Check projecton system
pop_proj = pop_proj.to_crs(crs=4326) # Transform to wgs84
pop_proj = pop_proj.clip(mask = bbox)
pop_proj.plot() # check

#   We are going to use this to linearly increase the more granular worldpop
#   / NSI values. So we actually want the value to be increase from baseline
#   (in this case 2010)
pop_proj.columns # have a look at col names
pop_proj["ssp585_scaler"] = pop_proj["hadgem2_es_ssp5_rcp85_2080"] / pop_proj["TOTALPOP10"]
pop_proj["ssp245_scaler"] = pop_proj["hadgem2_es_ssp2_rcp45_2080"] / pop_proj["TOTALPOP10"]

#   We will now rasterise this dataset (so we can use array calcs with worldpop)
grid_transform = worldpop.rio.transform()
grid_shape = worldpop.rio.shape

#   We have to rasterise col by col, so loop here
cols = list(pop_proj.columns)
cols = [c for c in cols if "geometry" not in c]
#   We dont really need all these, but I am keeping them as a handy ref

store = dict() # to store the rasters
for i in range(len(cols)):
    
    rasterized = rasterize(
        shapes=zip(pop_proj.geometry, pop_proj[cols[i]]),  # Burn the column values
        out_shape=grid_shape,      # Shape of the output raster
        transform=grid_transform,  # Affine transform from the template raster
        fill=np.nan,               # Background value (non numeric so we dont screw calcs)
        all_touched=True,          # Include all pixels touched by geometries
        dtype=np.float32     # Data type of the output raster
    )
    
    rasterized = xr.DataArray(
    rasterized,
    dims=("y", "x"),
    coords={"y": worldpop.y,
            "x": worldpop.x},
    attrs={"crs": 4326}
    )
    
    #   Store with name
    store[cols[i]] = rasterized
    
#   Stack to create xarray dataset
pop_proj =  xr.Dataset(store)
pop_proj["TOTALPOP10"].plot() # check
#   Write to disk
pop_proj.to_netcdf(new_pop_proj_pth)
#   Good stuff

#   Now demographics data
census = gpd.read_file(census_pth)
adi = pd.read_csv(adi_pth)

#   Join the csv file to the spatial file via the unique identifier code
adi = census.merge(adi, on="GISJOIN")
del census # clean

#   CRS shenanagins 
adi.crs
adi = adi.to_crs(crs=4326) # Transform to wgs84
adi = adi.clip(mask = bbox) # clip to area of interest
adi.columns # Lets look
adi.plot() # lets look

#   Make ranks numeric
adi["ADI_NATRANK"] = pd.to_numeric(adi["ADI_NATRANK"], errors="coerce") # Error values become nan
adi["ADI_STATERNK"] = pd.to_numeric(adi["ADI_STATERNK"], errors="coerce")
adi = adi.drop("FIPS", axis=0)

#   Write to disk
adi.to_file(new_adi_pth)

#   Now NSI value index. Dense points dataset. Lets build a grid from
#   our flood map and concentrate to these to cut down excessive size

#   First parse for relevent info
nsi = gpd.read_file(nsi_pth)
nsi.columns # Look
nsi = nsi[["Val_Struct", "Val_Cont", "Val_Other", "Val_Vehic", "geometry"]] #   Lets only keep value information
nsi["total_val"] = nsi[["Val_Struct", "Val_Cont", "Val_Other", "Val_Vehic"]].sum(axis=1) #   Further simplify to total value
nsi["properties"] = 1 # As one property for each point
nsi.head() # check

#   Now rasterise total val and properties taking the sum
target_vars = ["total_val", "properties"]
store = dict()
for i in range(len(target_vars)):
        
    nsi_grid = rasterize(
        shapes=zip(nsi.geometry, nsi[target_vars[i]]),  # Burn the column values
        out_shape=grid_shape,      # Shape of the output raster
        transform=grid_transform,  # Affine transform from the template raster
        fill=0,               # Background value (we require 0 here as add must add to this)
        all_touched=False,          # Only points within cells (avoid edge case double count)
        dtype=np.float32,           # Data type of the output raster
        merge_alg=MergeAlg.add  # Sum the values if more than one point in each cell     
    )
    
    #   Convert to xarray
    nsi_grid = xr.DataArray(
        nsi_grid,
        dims=("y", "x"),
        coords={
            "y": target.y,
            "x": target.x
        },
        attrs={"crs": 4326}
    )
    
    #   mask zeros
    nsi_grid = nsi_grid.where(nsi_grid!=0,np.nan)
    
    #   Store with name
    store[target_vars[i]] = nsi_grid

#   Combine datasets + write to disk
nsi_grid = xr.Dataset(store)
nsi_grid = nsi_grid.rio.write_crs("EPSG:4326")
#nsi_grid["properties"].plot() # Check
nsi_grid.to_netcdf(new_nsi_pth)

#   Note that there are ICLUS datasets on landuse available which could be used
#   to further analysis on vunerability / exposure. In the interest of brevity I
#   have excluded them.