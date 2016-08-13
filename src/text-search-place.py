import urllib
import json
from bs4 import BeautifulSoup

#AIzaSyCOKld43fXFPYRDEISiqKGrKwzrqUdmNxU

key = 'AIzaSyCOKld43fXFPYRDEISiqKGrKwzrqUdmNxU'

def get_stuff(text):	
	link = 'https://maps.googleapis.com/maps/api/place/textsearch/json?query='+text+'&key='+key
	html_gunk = urllib.urlopen(link).read()
	soup = BeautifulSoup(html_gunk, "html.parser")
	print soup.prettify().encode('utf-8')

def get_city(lat, lng):
	link = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(lng)
	up_json = urllib.urlopen(link).read()
	p_json = json.loads(up_json)
	flag = ''
	address = ''
	for i in range (len(p_json.get('results')[0].get('address_components'))-1, 0, -1):
		flag =  p_json.get('results')[0].get('address_components')[i].get('types')[0]
		if (flag == 'administrative_area_level_2'):
			city = p_json.get('results')[0].get('address_components')[i].get('short_name')
			return city


lat = '23.187181499999998'
lng = '72.6269575'
city = get_city(lat, lng)
text = 'swimming in ' + city
print get_stuff(text)
