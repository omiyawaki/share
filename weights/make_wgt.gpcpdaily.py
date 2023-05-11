import xesmf as xe
import xarray as xr

# creates regridder weight file for regridding
# GPCP daily (1 deg) grid to CESM2 grid (288 x 192)

idata='gpcpdaily'
odata='cesm2'
rgdir='/project/amp/miyawaki/data/share/regrid'
rfile='%s/f.e11.F1850C5CNTVSST.f09_f09.002.cam.h0.PHIS.040101-050012.nc'%rgdir
ofile='%s/wgt.%s.%s.nc'%(rgdir,idata,odata)
ifile='/project/mojave/observations/OBS-PR/GPCP_DAILY/gpcp.v01r03.daily.1996.nc'

# open up CESM data to get the output grid.
rdat=xr.open_dataset(rfile)

# open reference CERES data
idat=xr.open_dataset(ifile)

# create regridder
rgrd=xe.Regridder(idat,rdat,'bilinear',periodic=True)
rgrd.to_netcdf(ofile)
