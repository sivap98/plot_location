# -*- coding: utf-8 -*-
"""
Created on Sun May  9 23:02:37 2021

@author: Dell
"""
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import datetime
import glob
lons=[]
lats=[]
dates=[]
months=[]
#importing all nc files
for file in glob.glob('*.nc'):
    data=Dataset(file,'r')
#listing dates
    jd=data.variables['JULD'][:]
    ref_date=datetime.datetime(1950,1,1,0,0,0)
    date=ref_date+datetime.timedelta(days=jd[0])
    dates.append(date)
    months.append(date.month)
#listing latitude and longitude    
    lons.append(data.variables['LONGITUDE'][:])
    lats.append(data.variables['LATITUDE'][:])
#basemap setup            
mp=Basemap(projection="merc",llcrnrlat=2,llcrnrlon=54,urcrnrlat=30,urcrnrlon=96,resolution='f')
mp.drawcoastlines()
mp.drawlsmask(land_color='coral',ocean_color='aqua',lakes=True)
parallels = np.arange(0.,81,5.)
meridians = np.arange(10.,351.,5.)
mp.drawparallels(parallels,labels=[True,False,False,False])
mp.drawmeridians(meridians,labels=[False,False,False,True])
mp.scatter(lons,lats,latlon=True,s=50,c=months,marker='.',cmap="summer")
cbar=mp.colorbar()
cbar.set_label('deployed month')
#annotating all points
#for i in range(len(lons)):
#    x,y=mp(lons[i],lats[i])
#    plt.text(x,y,str(dates[i]))
plt.title('FLOAT LOCATIONS-'+str(date.year))
plt.figure(figsize=(8,8))
plt.show()