
sfrom bs4 import BeautifulSoup
import requests,pprint,json,os
from task4 import scrape_movie_details
with open("position_wise_movies.json","r+") as naik:
	python_data=json.load(naik)

for i in python_data:
	link=i['url']
	name=i['name']
	id=link[-10:-1]
	with open(f"{id}.json","w+") as naik:
		with open("movies_with_all_details.json",'r+') as check:
			movies_data=json.load(check)
		for movie in movies_data:
			if movie['name']==name:
				json_data=json.dump(movie,naik)

	1
2
3
4
