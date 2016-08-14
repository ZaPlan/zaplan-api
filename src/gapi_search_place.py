import urllib
import json
from bs4 import BeautifulSoup

#to query: 

key = 'AIzaSyCOKld43fXFPYRDEISiqKGrKwzrqUdmNxU'

def get_stuff(latitude, longitude, radius, place_type):	
	link = 'https://maps.googleapis.com/maps/api/place/search/json?location='+str(latitude)+','+str(longitude)+'&radius='+str(radius)+'&types='+place_type+'&key='+key
	json_gunk = urllib.urlopen(link).read()
	data = json.loads(json_gunk).get('results')
	places_result = dict()
	rating = 0
	for results in data:
		place_name = results['name'].encode('utf-8')
		place_details = dict()
		if 'photos' in results:
			place_image_link = 'https://maps.googleapis.com/maps/api/place/photo?photoreference='+results['photos'][0].get('photo_reference')+'&key='+key
			place_details.update({'image':place_image_link})
		if 'rating' in results:
			rating = results['rating']
			place_details.update({'rating':rating})
		place_lat = results['geometry'].get('location').get('lat')
		place_lng = results['geometry'].get('location').get('lng')
		place_details.update({'location' : str(place_lat)+','+str(place_lng)})
		places_result.update({place_name : place_details})
		
	final_dic = ({place_type : places_result})
	return final_dic

# latitude = '12.844413099999999'
# longitude = '80.1524191' 
# place_type = 'museum'
# radius = 100000 #km
# print get_stuff(latitude, longitude, radius, place_type)

