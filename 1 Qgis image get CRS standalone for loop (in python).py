from qgis.core import *

qgs = QgsApplication([], False)
qgs.setPrefixPath("C:\\OSGeo4W\\apps\\qgis", True)
qgs.initQgis()

# Set coordinate
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem('EPSG:3857'))

import processing
from processing.core.Processing import Processing

Processing.initialize()

import os

# Set frame path
frame_path = "D:\\ArcMap test\\Qgis code test\\Mine frame shp\\MineArea_test.shp"
# Set image input and output path
input_path = "D:\\ArcMap test\\Qgis code test\\Image test\\"
CRS_output = "D:\\ArcMap test\\Qgis code test\\CRS image\\"

# List of image file path
image = os.listdir(input_path)

# Select the mine frame ID
Mine_frame = QgsVectorLayer(frame_path, '', 'ogr')
frame_layer = Mine_frame.getFeatures()
for data in frame_layer:
    frame_ID = data.attributes()
    select_id = frame_ID[0]

    # Select ".jpg" image if the name same to frame ID
    for name in image:
        if select_id in name:
            if name.endswith(".jpg"):
                input_layer = input_path + name
                out_layer = CRS_output + name

                # set coordinate "EPSG:3826"
                processing.run("gdal:warpreproject",
                               {'INPUT': input_layer,
                                'SOURCE_CRS': None,
                                'TARGET_CRS': 'EPSG:3826',
                                'RESAMPLING': 0,
                                'NODATA': None,
                                'TARGET_RESOLUTION': None,
                                'OPTIONS': '',
                                'DATA_TYPE': 0,
                                'TARGET_EXTENT': None,
                                'TARGET_EXTENT_CRS': None,
                                'MULTITHREADING': False,
                                'EXTRA': '',
                                'OUTPUT': out_layer})

                print(name + " get coordinate!")

print("Finish!")