# gfs-xarray
Script for reading gfs file or any grib file using xarray and cfgrib

xarray uses cfgrib to read the grib or grib2 files. cfgrib have to explicitly give in what type of level you are reading the data, especially in the case of NCEP GFS data. GFS contains data in variety of types of levels.
The type of levels are: 
hybrid,atmosphere,surface,unknown,isobaricInPa,isobaricInhPa,meanSea,depthBelowLandLayer,heightAboveGround,heightAboveGroundLayer,tropopause,maxWind,heightAboveSea,isothermZero,pressureFromGroundLayer,sigmaLayer,sigma,potentialVorticity.

In detail, the each variables are given in different type of levls in GFS. Most frequently used variables are given down below with thier corresponding type of levels. So when you want to read a specific variable from GFS, you have to specify the suitable type of level.

hybrid
Data variables:
    clwmr       (latitude, longitude)    
    icmr        (latitude, longitude)
    rwmr        (latitude, longitude)
    snmr        (latitude, longitude)
    grle        (latitude, longitude)


Atmosphere

Data variables:
    refc        (latitude, longitude)


Surface

Data variables:
    vis         (latitude, longitude)
    gust        (latitude, longitude)
    hindex      (latitude, longitude)
    sp          (latitude, longitude)
    orog        (latitude, longitude)
    t           (latitude, longitude)
    sdwe        (latitude, longitude)
    sde         (latitude, longitude)
    cpofp       (latitude, longitude)
    prate       (latitude, longitude)
    csnow       (latitude, longitude)
    cicep       (latitude, longitude)
    cfrzr       (latitude, longitude)
    crain       (latitude, longitude)
    wilt        (latitude, longitude)
    fldcp       (latitude, longitude)
    SUNSD       (latitude, longitude)
    lftx        (latitude, longitude)
    cape        (latitude, longitude)
    cin         (latitude, longitude)
    4lftx       (latitude, longitude)
    hpbl        (latitude, longitude)
    lsm         (latitude, longitude)
    siconc      (latitude, longitude)
    

unknown

Data variables:
    u           (latitude, longitude)
    v           (latitude, longitude)
    VRATE       (latitude, longitude)
    pwat        (latitude, longitude)
    cwat        (latitude, longitude)
    r           (latitude, longitude)
    tozne       (latitude, longitude)
    gh          (latitude, longitude)


isobaricInPa

Data variables:
    gh            (latitude, longitude)
    t             (latitude, longitude)
    absv          (latitude, longitude)
    o3mr          (latitude, longitude)


isobaricInhPa

Data variables:
    gh             (isobaricInhPa, latitude, longitude)
    t              (isobaricInhPa, latitude, longitude)
	

meanSea

Data variables:
    mslet       (latitude, longitude)
    prmsl       (latitude, longitude)
    
