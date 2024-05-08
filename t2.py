import subprocess as sub
import geopy.distance
import math
import time
#sudo tcpdump -A -i any dst port 5055
#('sudo', 'tcpdump' ,'-A' ,'-i' ,'any' , 'dst' ,'port', '5055')



def calcBearing (lat1, long1, lat2, long2):
    dLon = (long2 - long1)
    x = math.cos(math.radians(lat2)) * math.sin(math.radians(dLon))
    y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(dLon))
    bearing = math.atan2(x,y)   # use atan2 to determine the quadrant
    bearing = math.degrees(bearing)
    return bearing

def calcNEWS(lat1, long1, lat2, long2):
    points = ["north", "north east", "east", "south east", "south", "south west", "west", "north west"]
    bearing = calcBearing(lat1, long1, lat2, long2)
    bearing += 22.5
    bearing = bearing % 360
    bearing = int(bearing / 45) # values 0 to 7
    NEWS = points [bearing]
    return NEWS





p = sub.Popen("sudo tcpdump -A -i any dst port 5055", shell=True ,stdout=sub.PIPE)
while 1:
  #while 1:      
        p = sub.Popen("sudo tcpdump -A -i any dst port 5055", shell=True ,stdout=sub.PIPE)
        for row in iter(p.stdout.readline, b''):
            dt=row.rstrip()
            dt=dt.decode()
            dt=str(dt)

            if "id" in str(dt):
                print(dt[dt.find("id="):])
                dt=dt[dt.find("id="):]
                dt=dt.split('&')
                print(dt)
              
                if (dt[0] =="id=RECEIVER"):
                    Rlat=dt[1][dt.find("=")+1:]
                    Rlon=dt[2][dt.find("=")+1:]
                    Rcoords=(Rlat,Rlon)
                    Tcoords=(lat,lon)
                    Distance=("%.2f"%(geopy.distance.geodesic(Rcoords, Tcoords).km))
                    
                #coords_1 = (38.898556, -77.037852)
               # coords_2 = (38.897147, -77.043934)

                print("%.2f"%(geopy.distance.geodesic(coords_1, coords_2).km))
                break
        p = sub.Popen("sudo tcpdump -A -i any dst port 5055", shell=True ,stdout=sub.PIPE)
        time.sleep(10)
        print("DORA")        





# White house 38.8977° N, 77.0365° W
lat1 = 38.8976763
long1 = -77.0365298
# Lincoln memorial 38.8893° N, 77.0506° W
lat2 = 38.8893
long2 = 77.0506

points = calcNSEW(lat1, long1, lat2, long2)
print ("The Lincoln memorial is " + points + " of the White House")
print ("Actually bearing of 231.88 degrees")











https://www.openandromaps.org/en/downloads/general-maps
Manual installation, unzip if needed, move map file to a folder which can be handled by the resp. app.

import os

from flask import Flask, flash, redirect, render_template, request, url_for, send_file

app = Flask(__name__)
LLData= 'Init'

@app.route('/postLLdata', methods = ['POST'])  
def success():
    global LLData
    LLData=request.data
    return "OK"

@app.route('/getLLdata', methods = ['GET'])
def download_file():
    global  LLData
    return  LLData

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
















import requests
import json
import time
url='http://localhost:5000/postLLdata'
#url='http://localhost:5055'
import random
import random
data=""
#http://demo.traccar.org:5055/?id=12345&lat=48.8566&lon=2.3522&timestamp=1609459200000
def sendData(url,post_data):
        #url='http://localhost:5055/postLLdata'
        url='http://localhost:5055'
        data1=f'id=123&lat=48.8566&lon=2.3522&timestamp=1609459200000&distance={random.randint(1,500)}&T2=123'
        data2=f'id=12&lat=70.8566&lon=2.3522&timestamp=1609459200000&distance={random.randint(1,5000)}&T2=123&roaming=NorthEast&bearing={random.randint(1,360)}'
        #data1 = f'id=DORA&lat={random.randint(1,3)}&lon=2.3522&timestamp={random.randint(1,500)}'
        print(data2)
        content = requests.post(url,data=data1)
        content = requests.post(url,data=data2)
        return content.status_code

def getRecLLdata():
        content = requests.get("http://localhost:5000/getLLdata")
        if content.status_code == 200 :
           return content.text
        else:
           return None
while 1:
    print(sendData(url,data))
    print(getRecLLdata())
    time.sleep(3)












https://forums.raspberrypi.com/viewtopic.php?t=244827
Re: Pi-4 Activating additional UART ports

Tue Aug 06, 2019 3:16 pm
I suggest you start by running the following to establish whether the configuration has been successful: 
https://forums.raspberrypi.com/viewtopic.php?t=354412


















