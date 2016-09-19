##########################################################################################
# Code adapted from APIreadingJson.py.ipynb found at
# https://github.com/fedhere/PUI2016_fb55/blob/master/Lab2_fb55/APIreadingJson.py.ipynb
#
# Input is of the form 'python show_bus_location.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv'
# where <MTA_KEY> is a valid MTA API key
# and <BUS_LINE> is a valid line # (B54, etc.)
#
# Output: A .csv file containing the GPS coordinates of each bus,
#         the next stop location and the distance from the stop
#
##########################################################################################
from __future__ import print_function
import pylab as pl
import sys
import json
import urllib.request as ulr

myKey = sys.argv[1]
myLine = sys.argv[2]
outFile = sys.argv[3]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" \
      + myKey + "&VehicleMonitoringDetailLevel=calls&LineRef=" + myLine

response = ulr.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

fout = open(outFile, "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
for it in data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0] \
    ['VehicleActivity']:
    
    lon = it['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat = it['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    stop_name = it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
    stop_status = it['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    
    fout.write(str(lat) + "," + str(lon) + "," + str(stop_name) + ","
          + str(stop_status) + "\n")
