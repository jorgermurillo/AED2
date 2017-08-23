import time
import io
import math
def anadir_grid(north_lat, south_lat, weast_lon, east_lon):
	grids.append({'north_lat': north_lat, 'south_lat': south_lat, 'weast_lon': -weast_lon, 'east_lon': -east_lon})
	print({'north_lat': north_lat, 'south_lat': south_lat, 'weast_lon': -weast_lon, 'east_lon': -east_lon})
	archivo.write(u'{},{},{},{}\n'.format(north_lat, south_lat, -weast_lon, -east_lon))

archivo = io.open('boxes2.txt','w')
archivo.write(u'north_latitude,south_latitude,west_longitud,east_longitude\n')
""""
centerLat : 40.758896,
	centerLng : -73.985130,
	maxLat : 40.882214,
	minLat : 40.680396,
	maxLng : -74.047285,
	minLng : -73.907000
"""

"""
# cellSize es el tam de celda en mts
R = 6378137 #radius of earth, meters
stepLatitude =   cellSize *1.1* 180/(pi * R)
stepLongitude =  cellSize *0.9*180 /( self.R* cos(pi*lat1/180) * pi )
el southWest es lat1,lon1
i = int(math.trunc((lat - lat1) / stepLatitude))
j = int(math.trunc((lon - lon1) / stepLongitude))
"""

"""
north_lat = 53 
south_lat = 41
weast_lon = -63 * (-1)
east_lon = -44 * (-1)
"""

north_lat = 40.882214 
south_lat = 40.680396
weast_lon = -74.047285 * (-1)
east_lon = -73.907000 * (-1)

dif_vertical = north_lat - south_lat
dif_horizontal = weast_lon - east_lon

divisor = (north_lat - south_lat)/20

cellSize = 1000
R = 6378137 
stepLatitude =   cellSize *1.1* 180/(math.pi * R)
print("Step Lat: %f"%(stepLatitude))
stepLongitude =  cellSize *0.9*180 /( R* math.cos(math.pi*south_lat/180) * math.pi )
print("Step Lon: %f"%(stepLongitude))

formato_grid = {
	"lim_sup": -1,
	"lim_inf": -1,
	"lim_der": -1,
	"lim_izq": -1
}

grids = []
north_lat_tmp = south_lat + stepLongitude
south_lat_tmp = south_lat
east_lon_tmp = east_lon
weast_lon_tmp = east_lon + stepLongitude
bandera = False
anadir_grid(north_lat_tmp, south_lat_tmp, weast_lon_tmp, east_lon_tmp)
print(grids)
iteraciones = 0
cnt = 0
cnt_y = 0
while(1):
	if (weast_lon_tmp >= weast_lon):
		print('cambio')
		cnt = 0
		cnt_y +=1
		east_lon_tmp = east_lon
		weast_lon_tmp = east_lon + stepLongitude
		south_lat_tmp = north_lat_tmp
		north_lat_tmp = north_lat_tmp + stepLatitude
	else:
		cnt+=1
		east_lon_tmp = weast_lon_tmp
		weast_lon_tmp = weast_lon_tmp + stepLongitude
		anadir_grid(north_lat_tmp, south_lat_tmp, weast_lon_tmp, east_lon_tmp)	
	if (south_lat_tmp >= north_lat):
		break
	stepLongitude =  cellSize *0.9*180 /( R* math.cos(math.pi*south_lat_tmp/180) * math.pi )
	time.sleep(0.1)
	iteraciones = iteraciones + 1
	print(cnt)
print(cnt_y)
