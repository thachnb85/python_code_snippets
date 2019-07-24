import gmplot 


lat = [ LIST_OF_LATS ]
lon = [ LIST_OF_LONGS ]

# Init with Toronto location:
gmap3 = gmplot.GoogleMapPlotter(43.6965327, 
                                -79.4064928, 17.54) 

gmap3.apikey = '___YOUR_KEY_HERE____'

# scatter method of map object  
# scatter points on the google map 
gmap3.scatter( lat, lon, '#FF0000', size = 5, marker = False ) 

# Plot method Draw a line in 
# between given coordinates 
gmap3.plot(lat, lon, 'cornflowerblue', edge_width = 1.5) 
gmap3.draw( "./map_with_trace.html" )
