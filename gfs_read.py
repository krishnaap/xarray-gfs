#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 19:03:08 2020

@author: krishna

"""

import xarray as xr

ds = xr.open_dataset('/media/MediaCentre/Dataset/gdas1.fnl0p25.2019081300.f00.grib2',engine='cfgrib',backend_kwargs={'filter_by_keys': {'typeOfLevel': 'isobaricInPa'}})
