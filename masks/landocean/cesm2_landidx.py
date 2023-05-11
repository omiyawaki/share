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
lm,om=pickle.load(open('%s/%s.pickle'%(odir,varn),'rb'))

# flatten array to 1d
lm1=lm.flatten()
lmi=np.arange(lm1.size) # indices of flattened array
lmi=lmi[~np.isnan(lm1)] # original indices for land points only

om1=om.flatten()
omi=np.arange(om1.size) # indices of flattened array
omi=omi[~np.isnan(om1)] # original indices for land points only

pickle.dump([lmi,omi], open('%s/lomi.pickle'%(odir),'wb'),protocol=5)
