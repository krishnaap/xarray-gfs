# gfs-xarray
Script for reading gfs file or any grib file using xarray and cfgrib

xarray uses cfgrib to read the grib or grib2 files. cfgrib have to explicitly give in what type of level you are reading the data, especially in the case of NCEP GFS data. GFS contains data in variety of types of levels.
The type of levels are: 
hybrid,atmosphere,surface,unknown,isobaricInPa,isobaricInhPa,meanSea,depthBelowLandLayer,heightAboveGround,heightAboveGroundLayer,tropopause,maxWind,heightAboveSea,isothermZero,pressureFromGroundLayer,sigmaLayer,sigma,potentialVorticity.

In detail, the each variables are given in different type of levls in GFS. Most frequently used variables are given down below with their corresponding type of levels. So when you want to read a specific variable from GFS, you have to specify the suitable type of level.

hybrid
Data variables:
    clwmr, icmr,rwmr, snmr, grle      


Atmosphere

Data variables:
    refc        


Surface

Data variables:
    vis,gust,hindex,sp,orog,t,sdwe,sde,cpofp,prate,csnow,cicep,cfrzr,crain,wilt,fldcp,SUNSD,lftx,cape,cin,4lftx,hpbl,lsm,siconc

unknown

Data variables:
    u,v,VRATE,pwat,cwat,r,tozne ,gh


isobaricInPa

Data variables:
    gh,t ,absv,o3mr


isobaricInhPa

Data variables:
    gh,t              (isobaricInhPa, latitude, longitude)
	

meanSea

Data variables:
    mslet,prmsl
    
