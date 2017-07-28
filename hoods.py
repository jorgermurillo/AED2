import neighborhoodize
import sys
import unicodedata
import time


file = open(sys.argv[1], "r")

outputfile = open(sys.argv[2],"w")

hood_map = neighborhoodize.NeighborhoodMap(neighborhoodize.zillow.NEW_YORK)

cnt=0

start = time.time()
for line in file: 
	if cnt==0:
		data =line.split(",")
		data.append("pickup_neighborhood,dropoff_neighborhood")
		output_line = ",".join(data) 
		outputfile.write(output_line)
		cnt+=1
	else:
		data = line.split(',')
		#GEt pickup neighborhood
		pick = hood_map.get_neighborhoods(float(data[1]),float(data[2]))
		#print(pick)
		if len(pick)!=0:
			pick = unicodedata.normalize('NFKD', pick[0]).encode('ascii','ignore')
		else:
			pick="NA"
		#Get dropoff neighborhood
		drop = hood_map.get_neighborhoods(float(data[6]),float(data[7]))
		#print(drop)
		if len(drop)!=0:
			drop = unicodedata.normalize('NFKD', drop[0]).encode('ascii','ignore')
		else:
			drop="NA"

		data.append(pick)
		data.append(drop)
		output_line =  ",".join(data)

		outputfile.write(output_line)
end = time.time()
duration = end - start

print(duration)

file.close()
outputfile.close()
