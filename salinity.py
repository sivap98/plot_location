# -*- coding: utf-8 -*-
"""
Created on Thu May 13 11:40:22 2021

@author: Dell
"""

from datetime import datetime,timedelta
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import dates as mpl_dates
data=Dataset(r'D:/myi/my_selection.nc')
lats=data.variables['LATITUDE'][:]
lons=data.variables['LONGITUDE'][:]
temp=data.variables['TEMP'][:]
salinity=data.variables['PSAL'][:]
pressure=data.variables['PRES'][:]
sec=data.variables['TIME'][:]
dates=[]
ref_date=datetime(2017,10,1,0,56,59)
m=np.arange(25460)
for i in m:
    date=ref_date+timedelta(seconds=float(sec[i]))
    dates.append(date)
   
x,y=dates,salinity
plt.title('PRACTICAL SALINITY in Oct-Nov of 2017')
plt.ylabel('sea_water_salinity in psu')
plt.tight_layout()

plt.plot(x,y)
plt.gcf().autofmt_xdate()