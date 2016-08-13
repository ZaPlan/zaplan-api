import random
import gapi_places_search
import text_search_place

def lets_do_this(lat, lng, budget, radius, start_time, end_time):
	m = [9, 10, 11]
	a = [11, 12, 13, 14, 15]
	e = [15, 16, 17, 18, 19]
	n = [19, 20, 21, 22, 23]

	all_act = ['restaurant', 'shopping_mall', 'zoo', 'amusement_park', 'cafe', 'book_store', 'park', 'bowling_alley', 'museum', 'campground', 'night_club']
	curr_act = []

	#add on text search queries
	morn = ['zoo', 'museum', 'movie']
	aft = ['restaurant', 'book_store']
	eve = ['shopping', 'bowling_alley', 'park', 'cafe']
	nite = ['movie', 'night_club']

	max_time = ['movie', 'restaurant', 'night_club', 'shopping']

	act = ''
	prev_act = ''
	flag = False

	if start_time in m:
		flag = True
		morn_act = []
		if budget < 700:
			morn.remove('movie')
		act = random.choice(morn)
		data = text_search_place.get_stuff(lat, lng, radius, act)
		data.update({'time', '9000 - 1100'})
		if act == 'movie':
			data.update({'time', '9300 - 1200'})
		curr_act.update({act : data})

	if flag or start_time in aft:
		prev_act = act
		if prev_act == 'movie':
			aft.remove ('book_store')
		act = random.choice(aft)
		if (act == 'restaurant'):
			data = text_search_place.get_stuff(lat, lng, radius, act)










	if start_time == m[0] or start_time == m[1]:




