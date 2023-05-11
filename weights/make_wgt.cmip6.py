import os,sys
sys.path.append('/home/miyawaki/scripts/common')
sys.path.append('/home/miyawaki/scripts/p004/scripts/hist_hotdays/cmip6/data')
import glob
import xesmf as xe
import xarray as xr
from tqdm import tqdm
from cmip6util import mods,simu,emem
from glade_utils import grid

# creates regridder weight file for regridding
# a CMIP model grid to CESM2 grid (288 x 192)

# information about input data to read input grid
idata='cmip6'
ty='2d'
vn='tas'
fq='day'
fo='historical'
cl='his'

# destination grid info
odata='cesm2'
rgdir='/project/amp/miyawaki/data/share/regrid'
rfile='%s/f.e11.F1850C5CNTVSST.f09_f09.002.cam.h0.PHIS.040101-050012.nc'%rgdir

# open up CESM data to get the output grid.
rdat=xr.open_dataset(rfile)

# create weights for list of models specified by mods
lmd=mods(fo)
for md in tqdm(lmd):
    ens=emem(md)
    grd=grid(fo,cl,md)

    ofile='%s/wgt.%s.%s.%s.%s.nc'%(rgdir,idata,md,ty,odata)
    idir='/project/mojave/cmip6/%s/%s/%s/%s/%s/%s' % (fo,fq,vn,md,ens,grd)
    lfn=glob.glob('%s/%s_%s_%s_%s_%s_%s_*.nc' % (idir,vn,fq,md,fo,ens,grd)) 
    # open one reference model data
    idat=xr.open_dataset(lfn[0])

    # create regridder
    rgrd=xe.Regridder(idat,rdat,'bilinear',periodic=True)
    rgrd.to_netcdf(ofile)
