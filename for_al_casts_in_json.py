import pprint,os,json,requests,string
from bs4 import BeautifulSoup
from for_all_casts import scrape_movie_details

with open("position_wise_movies.json") as naik:
	top_movies=json.load(naik)

movies_list_all_details=[]
def get_movie_list_details(movies_list):
	for movie in movies_list:
		movie_name=movie['name']
		each_movie_details=scrape_movie_details(movie_name)
		movies_list_all_details.append(each_movie_details)
	return movies_list_all_details
 



movies_list=top_movies[:250]


python_data=get_movie_list_details(movies_list)
if os.path.exists("original_movies_with_cast_details.json"):
	pass
else:
	with open("original_movies_with_cast_details.json","w+") as naik:
		json_data=json.dump(python_data,naik,indent=2)