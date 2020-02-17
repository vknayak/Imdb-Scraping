import pprint,os,json,requests,string,time,random
from bs4 import BeautifulSoup
from copy_of_task12 import scrape_movie_cast
with open("position_wise_movies.json","r+") as naik:
	python_data=json.load(naik)
# with open("movies_with_cast_details.json","r+") as f:
# 	cast_data=json.load(f)

def scrape_movie_details(movie_name):
	value=random.randint(1,3)
	movie_details={"name":"","director":[],"country":"","language":[],"poster_image_url":"","bio":"","runtime":"","genre":[]}
	for movie_url in python_data:
		if movie_url['name']==movie_name:
			url=movie_url['url']
			break
	response=requests.get(url)
	time.sleep(value)
	soup=BeautifulSoup(response.text,"html.parser")
	movie_name=soup.find('div',class_="title_wrapper").h1.text
	name=""
	for char in movie_name:
		if char!="(":
			name+=char
		else:
			exact_movie_name=name.strip()
			movie_details['name']=name.strip()
			break
	directors=soup.find('div',class_="credit_summary_item")
	directors_list=[]
	direct=directors.findAll('a')
	languages_list=[]
	for j in direct:
		directors_list.append(j.text)
	movie_details['director']=directors_list
	for_country=soup.findAll("div",class_="txt-block")
	for i in for_country:
		if "Country" in i .text:
			country=i.find('a').text
		elif "Language" in i.text:
			languages=i.findAll('a')
			for lang in languages:
				languages_list.append(lang.text)

	movie_details['country']=country
	movie_details['language']=languages_list
	poster=soup.find("div",class_="poster").a["href"]
	link="https://www.imdb.com"+poster
	movie_details['poster_image_url']=link
	bio=soup.find('div',class_="summary_text").text
	movie_details['bio']=bio.strip()
	runtime=soup.find("time").text
	runtime_list=(runtime.strip())
	exact_runtime=int(runtime_list[0])*60
	run=runtime_list.split()
	if len(run)>=2:
		if (runtime_list[3] in string.digits) and (runtime_list[4] in string.digits):
			exact_runtime+=int(runtime_list[3:5])

		elif (runtime_list[3] in string.digits):
			exact_runtime+=int(runtime_list[3])
	movie_details['runtime']=exact_runtime
	genre_list=soup.findAll("div",class_="see-more inline canwrap")
	exact_genre_list=[]
	for i in genre_list:
		if "Genres" in i.text:
			genre=i.findAll('a')
			for each_genre in genre:
				exact_genre_list.append(each_genre.text)
	movie_details['genre']=exact_genre_list
	cast_div=soup.find("div",class_="plot_summary ")
	list_of_divs=cast_div.findAll("div",class_="credit_summary_item")
	for each_div in list_of_divs:
		list_of_a=each_div.findAll("a")
		for each_a in list_of_a:
			pass
		pass

	movie_details['cast']=url+each_a["href"]
	# for each_cast in cast_data:
	# 	if exact_movie_name==each_cast['name']:
	# 		cast_url=each_cast['cast']
	# 		exact_cast_data=scrape_movie_cast(cast_url)
	# 		break
	# movie_details['cast']=exact_cast_data

	

	
	return movie_details

# movie_name=input("enter movie name")
# pprint.pprint(scrape_movie_details(movie_name))