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

    arr = ['Afghani', 'African', 'American', 'Andhra', 'Arabian', 'Armenian', 'Asian', 'Assamese', 'Awadhi', 'Bakery', 'Bangladeshi', 'Bar Food', 'Belgian', 'Bengali', 'Beverages', 'Bihari', 'Biryani', 'Breakfast', 'British', 'Burger', 'Burmese', 'Cafe', 'Chettinad', 'Chili', 'Chinese', 'Continental', 'Cuisine Varies', 'Desserts', 'Drinks Only', 'European', 'Fast Food', 'Finger Food', 'French', 'German', 'Goan', 'Greek', 'Gujarati', 'Healthy Food', 'Home-made', 'Hyderabadi', 'Ice Cream', 'Indian', 'Indonesian', 'Iranian', 'Italian', 'Japanese', 'Juices', 'Kashmiri', 'Kerala', 'Korean', 'Lebanese', 'Lucknowi', 'Maharashtrian', 'Malaysian', 'Mangalorean', 'Mediterranean', 'Mexican', 'Middle Eastern', 'Mithai', 'Moroccan', 'Mughlai', 'Naga', 'Nepalese', 'North Eastern', 'North Indian', 'Oriya', 'Pakistani', 'Parsi', 'Persian', 'Pizza', 'Portuguese', 'Rajasthani', 'Raw Meats', 'Russian', 'Salad', 'Sandwich', 'Seafood', 'Shanghai', 'Sindhi', 'Singaporean', 'South American', 'South Indian', 'Spanish', 'Sri Lankan', 'Steakhouse', 'Street Food', 'Sushi', 'Tea', 'Tex-Mex', 'Thai', 'Tibetan', 'Turkish', 'Vegetarian', 'Vietnamese', 'Coffee and Tea', 'Kebab', 'Kebabs', 'Mongolian', 'Patisserie', 'Tibetian', 'BBQ', 'Charcoal Chicken', 'Charcoal Grill', 'Fish and Chips', 'Fusion', 'Grill', 'Khaleeji', 'Konkan', 'Malwani', 'Oriental', 'Roast Chicken', 'Sichuan', 'Australian', 'Contemporary', 'Falafel', 'Salgados', 'Syrian', 'Irish', 'Pastry', 'Southwestern', 'Deli', 'Pan Asian', 'Multi Cuisine', 'Others', 'West Indian', 'Israeli', 'Hakka Chinese', 'Cajun', 'Argentine', 'Brazilian', 'Bubble Tea', 'Cuban', 'Eastern European', 'Egyptian', 'Emirati', 'Ethiopian', 'Filipino', 'International', 'Latin American', 'Mandi', 'Peruvian', 'Pub Food', 'Tapas', 'Tunisian', 'Uzbek', 'Cantonese', 'Frozen Yogurt', 'Hainanese', 'Hokkien', 'Ramen', 'Taiwanese', 'Western', 'Cafeteria', 'Aegean', 'Balkans', 'Black Sea', 'Central Anatolia', 'Eastern Anatolia', 'Fresh Fish', 'Giblets', 'Izgara', 'Kumpir', 'Old Turkish Bars', 'Ottoman', 'Pilav', 'Restaurant Cafe', 'South East', 'Turkish Pizza', 'World Cuisine', 'Algerian', 'Austrian', 'Balti', 'Brasserie', 'Canadian', 'Caribbean', 'Central Asian', 'Colombian', 'Crepes', 'Curry', 'Cypriot', 'Dim Sum', 'Georgian', 'Hawaiian', 'Jamaican', 'Jewish', 'Kazakh', 'Kiwi', 'Kyrgyz', 'Lithuanian', 'Mauritian', 'Modern European', 'Nigerian', 'Polish', 'Raclette', 'Romanian', 'Scandinavian', 'Scottish', 'Sicilian', 'Somali', 'South African', 'Swedish', 'Ukrainian', 'Venezualan', 'Zambian', 'Kapampangan', 'Puerto Rican', 'Swiss', 'Yugoslavian', 'Cape Malay', 'Dumplings', 'Durban', 'Tea House', 'Teppanyaki', 'Baiana', 'Fujian', 'Mineira', 'Author', 'Caipira', 'Capixaba', 'Chilean', 'Fondue', 'Gourmet Fast Food', 'Hungarian', 'Diner', 'Asian Fusion', 'Cambodian', 'Fijian', 'Pacific', 'Lounge', 'Aceh', 'Bakmi', 'Bakso', 'Balinese', 'Bangka', 'Batak', 'Belanda', 'Betawi', 'Dimsum', 'Jawa', 'Kalimantan', 'Lombok', 'Makassar', 'Manado', 'Medan', 'Padang', 'Palembang', 'Peranakan', 'Satay', 'Soto', 'Sulawesi', 'Sumatera', 'Sunda', 'Yogyakarta', 'Mozambican', 'Alentejana', 'Angolan', 'Cape Verdean', 'Madeiran', 'Minhota', 'Moroccon', 'Petiscos', 'Pub Grub', 'Santomean', 'Snack Bar', 'Snacks', 'Transmontana', 'Chifa', 'Creole', 'Ecuadorian', 'Empanadas', 'Nikkei', 'Bulgarian', 'Czech', 'Slovak', 'Venison', 'Gulf Food', 'Iraqi', 'Shawarma', 'Chinese Muslim', 'Ikan Bakar', 'Malay', 'Nyonya', 'Steamboat', 'Teochew', 'Bagels', 'California', 'First Nations', 'Guyanese', 'Hong Kong Style', 'Moldovan', 'New Mexican', 'Northern Chinese', 'Pacific Northwest', 'Quebecois', 'Salvadorean', 'Soul Food', 'Southern', 'Tanzanian', 'Trinbagonian', 'Xinjiang', 'Yunnan', 'Carvery', 'Donuts', 'Welsh', 'Old Bohemian', 'Moravian', 'New Zealand', 'Abruzzese', 'Altoatesine', 'Apulian', 'Calabrian', 'Cucina Campana', 'Danish', 'Dutch', 'Emilian', 'Friulan', 'Haute Cuisine', 'Ligurian', 'Lucanian', 'Neapolitan', 'Panini', 'Piadineria', 'Piedmont', 'Roman', 'Sardinian', 'Tavola Calda', 'Tavola Fredda', 'Tuscan', 'Venetian', 'Catalan', 'Lombard', 'Senegalese', 'Basque', 'Croatian', 'Meat Pie', 'Modern Australian', 'Parma', 'Teriyaki', 'Uruguayan', 'Yum Cha', 'Floribbean', 'Laotian', 'New American', 'Taco', 'Dominican', 'Nicaraguan', 'Amish', 'Southern American', 'Grill House', 'Native Australian']
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
                information.update({'rest_id': int(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['id'])})
                information.update({'distance': distance})
                information.update({'rating': float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['user_rating']['aggregate_rating'])})
                information.update({'cuisines': str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['cuisines']).split(',')})
                information.update({'price_range': float(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['price_range'])})
                information.update({'image_url': str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['thumb'])})
                information.update({'zomato_url': str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['url'])})
                information.update({'address': str(restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['location']['address'])})
                test_arr = []
                for item in information['cuisines']:
                    for cuisine in arr:
                        if item == cuisine or item == ' '+cuisine:
                            test_arr.append(1)
                        else:
                            test_arr.append(0)
                information.update({'cuisinesML': test_arr})
                name = restaurants['nearby_restaurants'][str(restaurant)]['restaurant']['name']
                filtered.update({str(name): information})
        
        json.dumps(filtered)
        return filtered
