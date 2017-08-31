setwd("/home/joelerll/espol-2017/analisis_datos/proyecto")
library(ggmap)
boxes<-data.frame(maxlat = 40.6910569858,minlat = 40.680396,maxlong = -73.9176609858,minlong = -73.907, id="1")
boxes<-transform(boxes, laby=(maxlat +minlat )/2, labx=(maxlong+minlong )/2)
datos <- read.csv('data/enero3.csv')
datos = datos[datos$pickups_place == '7,6',]
map <- get_map(location = 'Manhattan', zoom = 12)
mapPoints <- ggmap(map) + geom_point(data = datos, aes(x = pickup_longitude, y = pickup_latitude), color = "black", size = 0.001)  
#+ geom_polygon( data=datos, aes(x=pickup_longitude, y=pickup_latitude,group=group),colour="black", fill="white" )
#+  geom_rect(data=boxes, aes(xmin=minlong , xmax=maxlong, ymin=minlat, ymax=maxlat ), color="red", fill="transparent") 
#geom_point(data = datos, aes(x = dropoff_longitude, y = dropoff_latitude), color = "red", size = 0.001) +
mapPoints

,p <- ggplot(mtcars, aes(wt, mpg))
p + geom_point()
