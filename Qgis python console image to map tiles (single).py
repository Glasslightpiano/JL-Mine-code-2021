# Qgis python console only.
# Import image map(raster type).
# Set correct coordinate.
# Production map tiles.
# Created on: 2021-08-31 10:27:43
# -------------------------------------------------------------------------------------------------------------

# Import model
import os
import processing

path_layer = "D:/ArcMap test/Mine image/GB8-13.jpg"
out_layer = 'D:/ArcMap test/Mine wmts test/GB8-13' 

# Add raster
iface.addRasterLayer(path_layer, "test")

# Set raster CRS
rlayer = QgsProject.instance().mapLayersByName("test")[0]
rlayer.setCrs(QgsCoordinateReferenceSystem('EPSG:3826'))

# Zoom to layer
qgis.utils.iface.setActiveLayer(rlayer)
qgis.utils.iface.zoomToActiveLayer()

# Get mapCanvas extent
extent = iface.mapCanvas().extent()

xLL = extent.xMinimum()
yLL = extent.yMinimum()
xUR = extent.xMaximum()
yUR = extent.yMaximum()

Correct_extent = str(xLL) + ',' + str(xUR) + ',' + str(yLL) + ',' + str(yUR)

print('mapCanvas LL, UR: ' + Correct_extent)

# Generate XYZ tiles (Directory)
processing.run("qgis:tilesxyzdirectory", {'EXTENT':Correct_extent,'ZOOM_MIN':0,'ZOOM_MAX':19,'DPI':96,\
'TILE_FORMAT':0,'QUALITY':75,'METATILESIZE':4,'TILE_WIDTH':256,'TILE_HEIGHT':256,'TMS_CONVENTION':False,\
'OUTPUT_DIRECTORY':out_layer,'OUTPUT_HTML':'TEMPORARY_OUTPUT'})

print("Finish!")

# Remove raster
QgsProject.instance().removeMapLayer(rlayer)