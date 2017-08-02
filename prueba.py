import neighborhoodize

hood_map = neighborhoodize.NeighborhoodMap(neighborhoodize.zillow.NEW_YORK)

a =  hood_map.get_neighborhoods(40.73470, -73.99037)
print(a)
