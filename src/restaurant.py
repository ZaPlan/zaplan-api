import requests
import math
from pprint import pprint
import json

def filterRestaurants(UserLatitude, UserLongitude, radius, key):
    baseUrl = "https://developers.zomato.com/api/v2.1/"
    locationUrl = baseUrl + "cities?lat="+str(UserLatitude)+"&lon="+str(UserLongitude)
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": key}
   
    response = requests.get(locationUrl, headers=header)
    cityId = response.json()

    test_arr = open('assets/cuisines.txt','r').read().split(,)
    if len(cityId['location_suggestions']) == 0:
        return 0
    
    cityId = cityId['location_suggestions'][0]['id']
    
    geocodeUrl = baseUrl + "geocode?lat="+str(UserLatitude)+"&lon="+str(UserLongitude)
    
    response = requests.get(geocodeUrl, headers=header)
    restaurants = response.json()
    filtered = dict()

    if not(response.status_code == 200):
        return 0
    else:
        
        for restaurant in range(1, len(restaurants['nearby_restaurants'])+1):
            restaurantLatitude = float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['location']['latitude'])
            restaurantLongitude = float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['location']['longitude'])
            latDiff = math.radians(restaurantLatitude - UserLatitude)
            lonDiff = math.radians(restaurantLongitude - UserLongitude)
            distance = math.sin(latDiff/2)**2 + math.cos(restaurantLatitude) * math.cos(UserLatitude) * math.sin(lonDiff)**2
            distance = 2 * math.asin(math.sqrt(distance))
            distance = 6367 * distance
            if distance < radius:
                information = dict()
                information.update({'distance': distance})
                information.update({'rating': float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['user_rating']['aggregate_rating'])})
                information.update({'cuisines':str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['cuisines']).split(',')})
                information.update({'price_range': float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['price_range'])})
                information.update({'image_url':str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['thumb'])})
                information.update({'zomato_url':str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['url'])})
                information.update({'address':str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['location']['address'])})
                arr = []
                for item in information['cuisines']:
                    for cuisine in test_arr:
                        if item == cuisine:
                            arr.append(1)
                        else:
                            arr.append(0)
                information.update({'cuisinesML': arr})
                name = restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['name']
                filtered.update({str(name): information})
        
        json.dumps(filtered)
        return filtered