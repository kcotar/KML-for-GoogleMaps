Python skripti sta namenjeni predelavi kml datotek, ki jih ogr2gor izdela iz originalnih
shp fajlov za naselja in obcine.

Ogr2ogr postopek
export SHAPE_ENCODING="WINDOWS-1250"
ogr2ogr -f kml -s_srs EPSG:3912 -t_srs EPSG:4326 -lco ENCODING=UTF-8  SI.GURS.RPE.PUB.NA.kml SI.GURS.RPE.PUB.NA.shp

Skripta vsebuje: zmanjšanje natančnosti (število decimalk) točk in izpuščanje števila točk na poligonih.
Za naselja se izvede še tajlanje na več faljov saj ima google omejitve: 3MB, 1000 poligonov na kml fajl.
