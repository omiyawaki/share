import importlib
import xarray as xr
import numpy as np
from metpy.units import units
from metpy.calc import specific_humidity_from_dewpoint as td2q
import sys
from tqdm import tqdm

idirp="/project/mojave/observations/ERA5_daily/PS/"
idirtd="/project/mojave/observations/ERA5_daily/TD2m/"
idirq="/project/mojave/observations/ERA5_daily/Q2m/"

ystart=1959
yend=1978

for iyear in tqdm(np.arange(ystart,yend+1,1)):
    fnamep = idirp+"ps_"+str(iyear)+".nc"
    fnametd = idirtd+"td2m_"+str(iyear)+".nc"

    dps = xr.open_dataset(fnamep)
    dtd = xr.open_dataset(fnametd)
    ps=dps['ps']*units.pascal
    td=dtd['td2m']*units.kelvin
    # calculate specific humidity
    q2m = td2q(ps,td)

    q2m = q2m.rename('q2m')
    q2m.attrs={'units':'kg kg**-1'}
    q2m.to_netcdf("/project/mojave/observations/ERA5_daily/Q2m/"+
               "q2m_"+str(iyear)+".nc")
