# -*- coding: utf-8 -*-

"""
edit this file to define paths to MLML data

example:
-------

import mlml_data_path

data_dir = mlml_data_path.seawater()
"""

# csv files
def seawater():
    datadir = '/Users/tomconnolly/work/Data/MLML/seawater/'
    return datadir

def weather():
    datadir = '/Users/tomconnolly/work/Data/MLML/weather/'
    return datadir

# NetCDF files (created from csv files in get_mlml_data.py)
def netcdf():
    datadir = '/Users/tomconnolly/work/Data/MLML/netcdf/'
    return datadir