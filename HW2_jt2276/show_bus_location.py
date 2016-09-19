##########################################################################################
# Code adapted from APIreadingJson.py.ipynb found at
# https://github.com/fedhere/PUI2016_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb
#
# Input is of the form 'python show_bus_location.py <MTA_KEY> <BUS_LINE>'
# where <MTA_KEY> is a valid MTA API key
# and <BUS_LINE> is a valid line # (B54, etc.)
#
# Output: The current bus line
#         The number of buses on the line
#         The GPS coordinates of each bus
##########################################################################################
from __future__ import print_function
import pylab as pl
import sys
import json
import urllib.request as ulr

myKey = sys.argv[1]
myLine = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + myKey + "&VehicleMonitoringDetailLevel=normal&LineRef=" + myLine

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

print("Bus Line : " + myLine)
print("Number of Active Buses :" + str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))
for i,it in enumerate(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']):
    lon = it['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat = it['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("Bus #" + str(i) + " is currently at longitude " + str(lon) + " and latitude " + str(lat))
