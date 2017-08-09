import sys

boroughs = {}

bronx_file = open('Boroughs/bronx','r')

for line in bronx_file:
    neighborhoods = line.split(',')
    for e in neighborhoods:
        e = e.strip(" ").strip("\n")
        boroughs[e] = 'Bronx'

manhattan_file = open('Boroughs/manhattan','r')

for line in manhattan_file:
    neighborhoods = line.split(',')
    for e in neighborhoods:
        e = e.strip(" ").strip("\n")
        boroughs[e] = 'Manhattan'

queens_file = open('Boroughs/queens','r')

for line in queens_file:
    neighborhoods = line.split(',')
    for e in neighborhoods:
        e = e.strip(" ").strip("\n")
        boroughs[e] = 'Queens'

brooklyn_file = open('Boroughs/brooklyn','r')

for line in brooklyn_file:
    neighborhoods = line.split(',')
    for e in neighborhoods:
        e = e.strip(" ").strip("\n")
        boroughs[e] = 'Brooklyn'


statenIsland_file = open('Boroughs/staten_island','r')

for line in statenIsland_file:
    neighborhoods = line.split(',')
    for e in neighborhoods:
        e = e.strip(" ").strip("\n")
        boroughs[e] = 'Staten Island'

print(boroughs)

bronx_file.close()
manhattan_file.close()
queens_file.close()
statenIsland_file.close()
brooklyn_file.close()

month_file = open(sys.argv[1],"r")

output_file = open(sys.argv[2],"w")


cnt = 0

for line in month_file:
	if cnt ==0:
		line = line.strip("\n") + "pickup_burough,dropoff_burough\n"
		output_file.write(line)
		cnt+=1
	else:
		line = line.strip("\n")
		data = line.split(',')
		if data[14] == "NA":
			pick= "NA"
		else:
			pick = boroughs[ data[14] ]

		if data[15] == "NA":
			drop= "NA"
		else:
			drop = boroughs[ data[15] ]
		data.append(pick)
		data.append(drop)	

		output_line = ",".join(data)

		output_file.write(output_line)
        cnt +=1
        if cnt == 5:
            break