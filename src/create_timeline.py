import random
import gapi_search_place
import text_search_place
import restaurant
import movies

def lets_do_this(lat, lng, budget, radius, start_time, end_time):
	lat = str(lat)
	lng = str(lng)
	budget = int(budget)
	radius = int(radius)
	start_time = int(start_time)
	end_time = int(end_time)
	m = [9, 10, 11]
	a = [12, 13, 14, 15]
	e = [16, 17, 18, 19]
	n = [20, 21, 22, 23]

	all_act = ['restaurant', 'shopping_mall', 'zoo', 'amusement_park', 'cafe', 'book_store', 'park', 'bowling_alley', 'museum', 'campground', 'night_club']
	act_cost = {'restaurant' : 300, 'shopping_mall': 800, 'amusement_park': 1000, 'cafe' : 300, 'book_store': 50, 'park' : 50, 'bowling_alley' : 400, 'museum' : 100, 'night_club': 700}
	act_msg = {
	'restaurant': 'Head out into the city for a sumptuous meal',
	'shopping_mall': 'How about some (window) shopping and checking out what\'s new?',
	'zoo' : 'Man zoos are awesome',
	'cafe' : 'Hang out with some friends and meet up at a cafe!',
	'book_store' : 'When\'s the last time you read a book? How about heading out to a good \'ol bookstore? '
	}
	curr_act = []

	#add on text search queries
	morn = ['zoo', 'museum', 'movie']
	aft = ['restaurant', 'book_store']
	eve = ['shopping', 'bowling_alley', 'park', 'cafe']
	nite = ['restaurant', 'movie', 'night_club']

	act = ''
	imte = ''
	data = dict()
	flag = False

	if start_time in m:
		flag = True
		morn_act = []
		if budget < 700:
			morn.remove('movie')
		act = random.choice(morn)
		if act == 'movie':
			data = movies.get_movies_by_city(lat, lng)
			time = '0930 - 1200'
			nite.remove('movie')
		else:
			data = gapi_search_place.get_stuff(lat, lng, radius, act)
			time = '0900 - 1100'
		curr_act.append({time : data})

	if end_time <= a[0]:
		flag = False

	if flag or start_time in aft:
		prev_act = act
		if prev_act == 'movie':
			aft.remove ('book_store')
		act = random.choice(aft)

		if (act == 'restaurant'):
			data = restaurant.filterRestaurants(lat, lng, radius)
			time = '1300 - 1500'
			curr_act.append({time : data})
		else:
			data = gapi_search_place.get_stuff(lat, lng, radius, act) 
			time = '1200 - 1300'
			curr_act.append({time : data})

			data = restaurant.filterRestaurants(lat, lng, radius)
			time = '1300 - 1500'
			curr_act.append({time : data})

		nite.remove('restaurant')
		if 'movie' not in nite:
			nite.append('movie')

	if end_time <= e[0]:
		flag = False

	if flag or start_time in eve:
		act = random.choice(eve)
		data = gapi_search_place.get_stuff(lat, lng, radius, act)
		if act == 'shopping_mall':
			time = '1600 - 1800'
		else:
			time = '1500 - 1600'
			curr_act.append({time : data})
			data = gapi_search_place.get_stuff(lat, lng, radius, act)
			time = '1630 - 1830'
		curr_act.append({time : data})

	if end_time <= n[0]:
		flag = False

	if flag or end_time in nite:
		if budget < 1000:
			nite.remove('night-club')
		act = random.choice(nite)
		if act == 'restaurant' and 'restaurant' in curr_act and 'cafe' not in curr_act:
			act = 'cafe'
			data = gapi_search_place.get_stuff(lat, lng, radius, act)
			time = '2030 - 2300'
			curr_act.append({time : data})
		else:
			data = gapi_search_place.get_stuff(lat, lng, radius, act)
			time = '2030 - 2300'
			curr_act.append({time : data})

	return curr_act

# latitude='12.844413099999999'
# longitude='80.1524191'
# budget=1500
# radius=10000
# start_time=9
# end_time=22 
# print lets_do_this(latitude, longitude, budget, radius, start_time, end_time)