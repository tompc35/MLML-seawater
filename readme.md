# Interannual variability at Moss Landing seawater intake

Analysis of water property anomalies since 2010. Data is available at http://seawater.mlml.calstate.edu

View analysis in an [IPython notebook] (MLML_shorestation_interannual.ipynb)

### Packages

Code uses the following, in addition to standard Python packages:

* xarray http://xarray.pydata.org

* MLML physoce https://github.com/tompc35/physoce

### Downloading data and creating NetCDF file

* Edit mlml_data_path.py to specify the directories where you want the data stored

* Run get_mlml_data.py

* All csv files will automatically be downloaded and converted to NetCDF format