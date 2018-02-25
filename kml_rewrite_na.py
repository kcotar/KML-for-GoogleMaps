old_file = 'SI.GURS.RPE.PUB.NA.kml'
final_str = '</Folder>\n  <Style id="PolyStyle00">\n    <LabelStyle>\n      <color>00000000</color>\n      <scale>0.000000</scale>\n    </LabelStyle>\n    <LineStyle>\n      <color>ff0099ff</color>\n      <width>0.500000</width>\n    </LineStyle>\n    <PolyStyle>\n      <color>00f0f0f0</color>\n      <outline>1</outline>\n    </PolyStyle>\n  </Style>\n</Document></kml>'

i_poly = 0
i_out = 1
new_file = 'naseljamulti'+str(i_out)+'.txt'

txt_r = open(old_file, 'r')
txt_w = open(new_file, 'w')

for line in txt_r:
	if 'SimpleData' in line or 'ExtendedData' in line or 'Schema' in line or 'SimpleField' in line:
		if 'name="NA_UIME">' in line:
			# found a name of naselje
			obcina = line[line.index('">')+2 : line.index('</')]
			out_line = '      <description><![CDATA['
			# out_line += '<html><body>'
			out_line += '<font size="10"><strong>Naselje: </strong>'+obcina+'</font>'
			# out_line += '</html></body>'
			out_line += ']]></description>\n'
			txt_w.write(out_line)
		else:
			continue
	elif '<Style><LineStyle><color>ff0000ff' in line:
		txt_w.write('      <styleUrl>#PolyStyle00</styleUrl>\n')
	elif 'Polygon' in line:
		beg_str = '<coordinates>'
		end_str = '</coordinates>'
		i_beg = line.index(beg_str)+len(beg_str)
		i_end = line.index(end_str)
		line_beg = line[:i_beg]
		line_coord = line[i_beg:i_end]
		line_end = line[i_end:]
		# define new begining and end of the polgon line description
		line_beg = '      <Polygon><extrude>0</extrude><altitudeMode>clampToGround</altitudeMode><outerBoundaryIs><LinearRing><coordinates>'
		line_end = '</coordinates></LinearRing></outerBoundaryIs></Polygon>\n'
		#print line_coord
		line_coord_new = ''
		coords = line_coord.split(' ')
		i_p = 0
		every_nth = 2
		# use every n-th point in boundary description
		for coord in coords:
			i_p += 1
			if i_p % every_nth != 0:
				continue
			lat_lon = coord.split(',')
			# remove decimal points
			line_coord_new += lat_lon[0][:9]+','+lat_lon[1][:9]+' '
		txt_w.write(line_beg+line_coord_new+line_end)
	#elif 'LineStyle' in line:
	#	txt_w.write('      <styleUrl>#PolyStyle00</styleUrl>\n')
	elif '</Folder>' in line:
		txt_w.write(final_str)
		break
	else:
		txt_w.write(line)
	if '</Placemark>' in line:
		i_poly += 1
	if i_poly > 950:
		txt_w.write(final_str)
		txt_w.close()
		i_out += 1
		new_file = 'naseljamulti'+str(i_out)+'.txt'
		txt_w = open(new_file, 'w')
		i_poly = 0
		txt_w.write('<?xml version="1.0" encoding="utf-8" ?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document id="root_doc">\n<Folder><name>SI.GURS.RPE.PUB.NA</name>\n')
	
		
txt_r.close()
txt_w.close()
