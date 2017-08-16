const bbox = require('boundingbox-split');

const boxParameters = {
	centerLat : 40.758896,
	centerLng : -73.985130,
	maxLat : 40.882214,
	minLat : 40.680396,
	maxLng : -74.047285,
	minLng : -73.907000
}
var fs = require('fs');

bbox.boundingBoxCutting(boxParameters, 2).then(function(result) {
	var stream = fs.createWriteStream('boxes.txt', {flags: 'w'});

	var lines;
	stream.write('north_latitude,south_latitude,west_longitud,east_longitude,center_lat,center_long\n');
	for (var i = 0; i < result.length; i++) {
        	stream.write(`${result[i].maxLat},${result[i].minLat},${result[i].maxLng},${result[i].minLng},${result[i].centerLat},${result[i].centerLng}\n`); //<-- the place to test
    }
})
.catch(error => console.log(error))


//var BoundingBox = require('boundingbox')
//var b = new BoundingBox({ minlat: 48.123, minlon: 16.23, maxlat: 49.012, maxlon: 16.367 })
//console.log(b.getEast()) 
