from qgis.core import *

qgs = QgsApplication([], False)
qgs.setPrefixPath("C:\\OSGeo4W\\apps\\qgis", True)
qgs.initQgis()

# Set coordinate
QgsProject.instance().setCrs(QgsCoordinateReferenceSystem('EPSG:3857'))

import processing
from processing.core.Processing import Processing

Processing.initialize()

# set image path
path = "D:\\ArcMap test\\Qgis code test\\"

# image without coordinate
image_path = path + "Image test\\GA9-5.jpg"
# image with coordinate
CRS_image_path = path + "map tile\\GA9-5.jpg"

# set coordinate: EPSG:3826
processing.run("gdal:warpreproject", {
    'INPUT': image_path,
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
    'OUTPUT': CRS_image_path
})

from PyQt5.QtCore import *

# add image (with coordinate)
def StringToRaster(raster):
    fileInfo = QFileInfo(raster)
    path = fileInfo.filePath()
    baseName = fileInfo.baseName()
    layer = QgsRasterLayer(path, baseName)
    QgsProject.instance().addMapLayer(layer)

fn = CRS_image_path

StringToRaster(fn)

# map tile
processing.run("qgis:tilesxyzdirectory", {
    'EXTENT': '13522390.9099, 13528797.2088, 2906026.6409, 2911227.5521',
    'ZOOM_MIN': 0,
    'ZOOM_MAX': 12,
    'DPI': 96,
    'TILE_FORMAT': 0,
    'QUALITY': 75,
    'METATILESIZE': 4,
    'TILE_WIDTH': 256,
    'TILE_HEIGHT': 256,
    'TMS_CONVENTION': False,
    'OUTPUT_DIRECTORY': path + "Tile\\qgistilb\\", 'OUTPUT_HTML': 'TEMPORARY_OUTPUT'
})
