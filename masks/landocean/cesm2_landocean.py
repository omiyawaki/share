import os,sys
import copy
import pickle
import numpy as np
import xarray as xr

varn='lomask'
odir='/project/amp/miyawaki/data/share/%s/cesm2' % (varn)

if not os.path.exists(odir):
    os.makedirs(odir)

# load cesm land fraction data
ds=xr.open_dataset('/project/amp/miyawaki/data/share/lfrac/sftlf_fx_CESM2_historical_r1i1p1f1_gn.nc')
lf=ds['sftlf']/100
dlf=np.heaviside(lf-0.5,1).data # binary land fraction
lm=copy.copy(dlf) # keep land mask
lm[dlf==0]=np.nan 
om=copy.copy(dlf) # keep ocean mask
om[om==1]=np.nan
om[om==0]=1

pickle.dump([lm,om], open('%s/%s.pickle'%(odir,varn),'wb'),protocol=5)
