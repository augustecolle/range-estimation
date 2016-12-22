import numpy as np
import geopy
from geopy.distance import vincenty

#-----------------Import data----------------
text_file = open("./routes/mont_ventoux.txt", "r")
lines = text_file.readlines()
#---------------------------------------------

lat_long_alt = [x.split()[1:] for x in lines if (len(x.split()) == 4 and x.split()[0] == 'T')] #get data only if it starts with 'T' and we should check if the list is not empty because otherwise we will get an error when trying to index the empty list in search for 'T'
lat = [float(x[0]) for x in lat_long_alt] #convert string to floating point values
long = [float(x[1]) for x in lat_long_alt]
heights = [float(x[2]) for x in lat_long_alt]
height_diff = np.array([(heights[x] - heights[x-1]) for x in range(1, len(heights))]) #we need difference in height for two points since we want the slope between these points


#---------------Calculate distances between lats en longs---------------
start = tuple([lat[0], long[0]])
distances = []

for x in zip(lat[1:], long[1:]):
    distance = vincenty(x, start).meters
    if distance > 0:
        distances.append(distance)
    else:
        distances.append(1e-9) #if we would end up somehow by having twice the same point (can't devide by zero)
    start = x
#-----------------------------------------------------------------------

slopes = [y/x*100 for y,x in zip(height_diff, distances)] #calculate slope in percentages
print(max(slopes), min(slopes)) #check maxima

cum_distances = np.cumsum(distances)

#-----------make a plot-------------
#import matplotlib.pyplot as plt
#import numpy as np
#
#
#plt.scatter(cum_distances/1000.0, heights[1:], label=r'height profile')
#plt.legend(loc = 'upper right')
#plt.show()
#plt.plot(np.cumsum(distances), slopes, label=r'Slopes')
#plt.legend(loc = 'upper right')
#plt.show()
#-----------------------------------


#-----------do some smoothing and caculate derivative (as slope)------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

slope_avg_distance = 100 #22120 #in meter

deltax = 0.1 #don't change
slope_index = int(slope_avg_distance*1.0/deltax) #slope index for advancing slope_avg_distance
x = cum_distances
y = np.cumsum(height_diff)
#determining smoothing factor according to the docs: (m - sqrt(2*m)) * std**2 <= s <= (m + sqrt(2*m)) * std**2 but this gives an horrible over smoothing so I am choosing my own
tck = interpolate.splrep(x, y, s=10) #used to be 40 for the profile with loads of data

xnew = np.arange(0, cum_distances[-1], deltax)
ynew = interpolate.splev(xnew, tck, der=0)
dery =  interpolate.splev(xnew, tck, der=1)
dery_1km_avg = [dery[x*slope_index:x*slope_index+slope_index].mean() for x in range(len(xnew)/slope_index+1)]

fig, ax1 = plt.subplots()
ax1.plot(xnew, ynew + heights[0], color='black')
ax1.plot(cum_distances, heights[1:], 'x')

ax2 = ax1.twinx()
ax2.plot(xnew, dery, color='red')
ax2.bar([xnew[x*slope_index] for x in range(len(xnew)/slope_index+1)], dery_1km_avg, color='green', width=slope_index*deltax, alpha=0.3)

plt.show()

#---------------------------------------------------------------------------

