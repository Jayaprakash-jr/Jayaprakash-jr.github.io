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

