# Which dataset should I use for my project?

Choosing the right dataset is crucial, as it determines the type of analysis you can perform. Some datasets are better suited for certain types of analyses than others. Below, I provide a guide to help you select the most appropriate dataset for your needs.

## ERA5 Data

ERA5 is the most widely used reanalysis dataset, making it a convenient choice for analyzing past climate risks. It covers the period **1940 to present** at **0.25° spatial resolution**, with multiple temporal resolutions (hourly, daily, and monthly). ERA5 data is freely available from the **Copernicus Climate Data Store (CDS)** and can be easily accessed using the `cdsapi` Python package. You can find examples of how to download ERA5 data in the [download section](../ready/03-download). The QCR server has some data at 0.75° resolution for you to download directly.

```{admonition} ERA5 is a good choice if ...
:class: note

- You need **historical climate data** (1919400 to present) and do not require bias-corrected projections (or can perform bias correction yourself).
- You need **upper-level atmospheric data** (e.g., 500 hPa winds) or other specialized variables (e.g., snowfall, evaporation).
- You require **relatively high spatial resolution** data (0.25°).
- You are conducting a **global study** or working over a **larger region**.
- You want to download data for a specific **region or variable**, as accessing ERA5 through the CDS API is straightforward.
```

## W5E5 Data

W5E5 is a **bias-corrected version of ERA5**, available at **daily resolution** and **0.5° spatial resolution**. Developed by the **ISIMIP project**, it contains only **surface variables** (temperature, precipitation, etc.). W5E5 data is freely available from the **ISIMIP data portal** and is also preloaded on the QCR server for selected variables (`tas`, `pr`, `tasmax`, `tasmin`, `hurs`) and a selected climate model.

```{admonition} W5E5 is a good choice if ...
:class: note

- You plan to use it alongside **ISIMIP6 projections** for future climate analysis (as ISIMIP6 projections are bias-corrected to W5E5).
- You need **daily resolution** surface climate data at select locations. While ERA5 also offers daily data, W5E5 is readily available on the QCR server and I can prepare timeseries or small regional subsets for you.
- You want quick access to **temperature, precipitation, and humidity** data from the QCR server.
```

## ISIMIP6 Climate Projections

ISIMIP6 provides **bias-corrected climate projections** at **daily resolution** and **0.5° spatial resolution**, using the W5E5 dataset as the historical reference. These projections are freely available from the **ISIMIP data portal** and cover three **future scenarios** (SSP126, SSP370, SSP585) using **five climate models** (though only one model is available on the QCR server).

```{admonition} ISIMIP6 is a good choice if ...
:class: note

- You are working with **W5E5 data for historical periods** and need consistent **future climate projections**.
- You require **daily-resolution** climate projections.
- You are okay with using **only one climate model** for future projections (while multiple models are recommended for robust climate studies, using a single model is acceptable for daily-resolution studies).
- You need **time-series data** or data for a **specific region** (but not global-scale analyses at daily resolution).
```

## CMIP6 Climate Projections

CMIP6 represents the **latest generation of climate model projections**, with outputs at **various spatial resolutions** and **multiple temporal scales**. CMIP6 data is freely available from the **Earth System Grid Federation (ESGF)** and the **Copernicus Climate Data Store (CDS)**. On the QCR server, monthly precipitation and temperature data are provided at their original resolution and at **0.75° and 2° regridded resolution**.

```{admonition} CMIP6 is a good choice if ...
:class: note

- You need **monthly-resolution data** rather than daily.
- You want to work with **raw (uncorrected) climate model outputs** rather than bias-corrected projections.
- You want to analyze the **full range of climate models and emission scenarios**.
- You are primarily working with **temperature and precipitation** (other variables must be downloaded separately from ESGF or CDS).
- You are conducting **large-scale analyses** (e.g., global, continental, or regional studies).
```

## Global Summary of the Day (GSOD) Data

GSOD is a **station-based dataset** compiled by the **National Climatic Data Center (NCDC)** of NOAA. It provides **daily observational data** from weather stations worldwide. GSOD data is freely available from **NOAA servers**, and a small selection of stations is accessible on the QCR server. I can help with downloading these data.

```{admonition} GSOD is a good choice if ...
:class: note

- You are conducting a **local-scale study** and need observational data from a specific weather station.
- You need **daily-resolution observations** and prefer **measured data** over reanalysis or climate model outputs.
- You can **handle data gaps** and **quality issues**, as station data can be incomplete.
- You understand that while **station data provides actual observations**, it may have spatial limitations compared to gridded datasets.
```

## National River Flow Archive (NRFA) Data

The [national river flow archive](https://nrfa.ceh.ac.uk) is a valuable resource for **hydrological applications in the UK**. It provides **daily streamflow** data for many UK rivers, along with **daily catchment rainfall totals** from a network of rain gauges. The data is freely available and can be downloaded via the NRFA website ([search tool](https://nrfa.ceh.ac.uk/data/search)). I can assist with downloading and processing these data.

```{admonition} NRFA is a good choice if ...
:class: note

- You are analyzing a **past flood event in the UK** and need streamflow data.
- You are interested in the **relationship between rainfall and streamflow** in the UK.
- You require **daily-resolution data** for a specific river or catchment.
- You plan to link past streamflow data with **ISIMIP6 daily climate projections**, but keep in mind that this may require **bias correction**.
```

## Summary of Recommendations

| Dataset            | Type                     | Resolution  | Temporal Scale | Best For |
|--------------------|-------------------------|-------------|---------------|----------|
| **ERA5**          | Reanalysis               | 0.25°       | Hourly-daily-monthly | Past climate risks, global studies, specialized variables |
| **W5E5**          | Bias-corrected reanalysis | 0.5°       | Daily          | Historical data with bias correction, ISIMIP6 projections |
| **ISIMIP6**       | Bias-corrected projections | 0.5°       | Daily          | Future projections, time-series analysis |
| **CMIP6**         | Climate projections      | Various (often 0.5°-2°) | Monthly        | Multi-model comparisons, projections |
| **GSOD**          | Observational (station)  | Point data  | Daily          | Local-scale studies, observed climate data |
| **NRFA**          | Observational (streamflow) | Point data (catchments) | Daily | UK hydrology, flood studies, streamflow-rainfall relationships |
