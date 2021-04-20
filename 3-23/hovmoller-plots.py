import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np
import datetime as dt

data = Dataset("/Users/brownscholar/Desktop/BridgeUp_Internship/data/atlantic-data.nc")
w_array = data.variables["w"][:]
lat = 150 
latslice = w_array[:,lat,:,0]
rotation = np.rot90(latslice) #.reshape((118,lat,1352,0))


#date = 0
#timeslice = w_array[date,:,:,0]



top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')


longitude_values = data.variables['longitude'][:]
for i in range(len(longitude_values)):
    longitude_values[i] = longitude_values[i] - 360
print(longitude_values)




startdate = dt.date(1950,1,1)
oritime = data.variables['time'][:]

yearlist = []
for i in (range(0, len(oritime), 52)):
	yearss = startdate + dt.timedelta(hours = int(oritime[i]))
	yearlist.append(yearss.year)
print(yearlist)



min = 0
max = 1355

fig, ax = plt.subplots()

ax.set_yticks(np.arange(0, 118, 20))
ax.set_yticklabels(longitude_values[0::20])

ax.set_xticks(np.arange(0,1355,52))
ax.set_xticklabels(yearlist, rotation = 90)

#ax.pcolormesh(latslice, cmap = newcmp, vmin = -1, vmax = 1)

#ax.set_xticks(np.arange(0, 1355, 52))

plt.xlabel("Years")
plt.ylabel('Longitude •West')




p = plt.pcolormesh(rotation[2:-2,2:-2], cmap = newcmp, vmax = 1, vmin = -1)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Hovmoller Diagram at " + str(lat) + " Latitude and 50.625°")
plt.scatter([],[], color = "blue", label = "going down")
plt.scatter([],[], color = "red", label = "going up")
plt.legend(bbox_to_anchor=[1.0,1.0])



plt.colorbar()
plt.show()

#insert netcdf data into a variable
#cut a time splice using same method from density.py
# create plot with this time slice