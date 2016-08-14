import urllib
import json
from bs4 import BeautifulSoup

def get_movies_by_city(lat, lng):
	link = 'http://maps.googleapis.com/maps/api/geocode/json?latlng='+str(lat)+','+str(lng)
	up_json = urllib.urlopen(link).read()
	p_json = json.loads(up_json)
	flag = ''
	address = ''
	city = ''
	for i in range (len(p_json.get('results')[0].get('address_components'))-1, 0, -1):
		flag =  p_json.get('results')[0].get('address_components')[i].get('types')[0]
		if (flag == 'administrative_area_level_2'):
			city = p_json.get('results')[0].get('address_components')[i].get('short_name')
	link = 'https://google.com/movies?near='+city
	html_gunk = urllib.urlopen(link).read()
	soup = BeautifulSoup(html_gunk, "html.parser")
	movie_data = soup.findAll('div', {'class':'movie'})
	movie_set=dict()
	for i in range(0, len(movie_data)):
		name = movie_data[i].find('div', {'class':'name'}).get_text()
		up_info = movie_data[i].find('span', {'class':'info'}).get_text().split(' - ')
		time = up_info[0]
		genre = up_info[1].split('/')
		lang = up_info[2]
		info = dict()
		info.update({'time':time})
		info.update({'genre':genre})
		info.update({'lang':lang})
		movie_set.update({name : info})
	movie_set = ({'movie' : movie_set})
	return movie_set