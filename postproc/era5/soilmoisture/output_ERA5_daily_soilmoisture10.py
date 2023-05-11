import importlib
import xarray as xr
import numpy as np
import sys

datpath1="/project/mojave/observations/ERA5_daily/soilmoisture1/"
datpath2="/project/mojave/observations/ERA5_daily/soilmoisture2/"
datpathout="/project/mojave/observations/ERA5_daily/soilmoisture_10cm/"

#ystart=1980
#yend=2020
ystart=1959
yend=1978

for iyear in np.arange(ystart,yend+1,1):
    fname1 = datpath1+"soilmoisture1_"+str(iyear)+".nc"
    fname2 = datpath2+"soilmoisture2_"+str(iyear)+".nc"

    dat1 = xr.open_dataset(fname1)
    dat2 = xr.open_dataset(fname2)

    soilmoisture10 = dat1['soilmoisture1'].load() + (3./21.)*dat2['soilmoisture2'].load()
    soilmoisture10 = soilmoisture10 * 1000. * 0.1
    soilmoisture10 = soilmoisture10.rename('soilmoisture10')
#    soilmoisture10 = soilmoisture10.rename({'g0_lon_2':'lon', 'g0_lat_1':'lat', 
#                      'initial_time0_hours':'time'})
    soilmoisture10.attrs={'units':'kg m**-2'}
    soilmoisture10.to_netcdf("/project/mojave/observations/ERA5_daily/soilmoisture_10cm/"+
               "soilmoisture_10cm_"+str(iyear)+".nc")
