# Qgis python console only.
# Through the mine frame ID (.shp) select corresponding mine image.
# Set Qgis Project Properties Coordinate Reference Systems (CRS).
# Import image map(raster type).
# Set raster coordinate.
# Production map tiles.
# Created on: 2021-09-13 09:34:47
# -----------------------------------------------------------------------------------------------------------------------

# Import modules
import os
import processing

# Set input and output file path
frame_path = "D:/ArcMap test/Qgis code test/Mine frame shp/MineArea_test.shp"
image_path = "D:/ArcMap test/Qgis code test/Image test/"
export = "D:/ArcMap test/Qgis code test/map tile/"

# Set Qgis Project Properties CRS
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem('EPSG:3857'))

# List of image file path
image = os.listdir(image_path)

# Select the mine frame ID
Mine_frame = QgsVectorLayer(frame_path, '','ogr')
frame_layer = Mine_frame.getFeatures()
for data in frame_layer:
    frame_ID = data.attributes()
    select_ID = frame_ID[0]
    
    # Select ".jpg" image if the name same to frame ID
    # Build output file
    for name in image:
        if select_ID in name:
            if name.endswith(".jpg"):
                path_layer = image_path + name
                out_layer = export + name[:-4]

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
                print(name + " mapCanvas: " + Correct_extent)

                # Generate XYZ tiles (Directory)
                processing.run("qgis:tilesxyzdirectory", {'EXTENT':Correct_extent,'ZOOM_MIN':0,'ZOOM_MAX':19,'DPI':96,\
                'TILE_FORMAT':0,'QUALITY':75,'METATILESIZE':4,'TILE_WIDTH':256,'TILE_HEIGHT':256,'TMS_CONVENTION':False,\
                'OUTPUT_DIRECTORY':out_layer,'OUTPUT_HTML':'TEMPORARY_OUTPUT'})

                print(name + " has turned to map tiles.")

                # Remove frame and raster
                QgsProject.instance().removeMapLayer(rlayer)

print("Finish!")
