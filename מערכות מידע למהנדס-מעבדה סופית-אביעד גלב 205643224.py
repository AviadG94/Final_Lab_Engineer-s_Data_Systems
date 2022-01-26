import os
from qgis.PyQt.QtCore import QVariant

# .3
vl = QgsVectorLayer("LineString?crs=EPSG:26910", 'Line Layer', "memory")
pr = vl.dataProvider()
pr.addAttributes([QgsField("layer", QVariant.String),
                  QgsField("count",  QVariant.Int)])
vl.updateFields()

uri = "C://Users/Aviad Glav/Desktop/BLD_PERMIT.dxf|layername=entities|geometrytype=line"
vlayer = QgsVectorLayer(uri, "layer_name_like", "ogr")
QgsProject.instance().addMapLayer(vlayer)

i=0
for feature in vlayer.getFeatures():
        if (feature['Layer'])=="M2404":
            print (feature['Layer'])
            print(type (feature['Layer']))
            i=i+1
            print(i)

            geom = feature.geometry()
            feat = QgsFeature()
            feat.setGeometry(geom)
            feat.setAttributes([feature['Layer'], i])
            pr.addFeature(feat)
            vl.updateExtents()
QgsProject.instance().addMapLayer(vl)

# .4
vectorLyr =  QgsVectorLayer('/qgis_dat/paths.shp', 'Paths' , "ogr")
vectorLyr.isValid()
vpr = vectorLyr.dataProvider()

points = []
points.append(QgsPoint(178328.0,659032.0))
points.append(QgsPoint(178316.0,659030.0))
points.append(QgsPoint(178328.0,659030.0))
points.append(QgsPoint(178316.0,659028.0))

line = QgsGeometry.fromPolyline(points)

f = QgsFeature()
f.setGeometry(line)
vpr.addFeatures([f])
vectorLyr.updateExtents()
QgsProject.instance().addMapLayer(vectorLyr)

# .5

path_input = r"C://Users/Aviad Glav/Desktop/Final_Lab/Gush100150.shp"

out_put1    = r"C://Users/Aviad Glav/Desktop/Final_Lab/Gush100150_out.shp"

processing.run("native:simplifygeometries",
                {'INPUT':path_input,
                'METHOD':0,
                'TOLERANCE':100,
                'OUTPUT':out_put1})


