from bs4 import BeautifulSoup
import requests,json,pprint,os
# movie_link="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
with open("movies_with_cast_details.json","r+") as naik:
	python_data=json.load(naik)
def for_moving_link(python_data):
	for each_movie_link in python_data:
		movie_link=each_movie_link['cast']
		scrape_movie_cast(movie_link)
		


def scrape_movie_cast(movie_caste_url):
	naming_for_json=""
	for char in movie_caste_url:
		if char.isnumeric():
			naming_for_json+=char
	naming_for_json="tt"+naming_for_json

	response=requests.get(movie_caste_url)
	soup=BeautifulSoup(response.text,"html.parser")
	cast_list=soup.find("table",class_="cast_list")
	tr=cast_list.findAll("tr")
	exact_dict=[]
	for each_tr in tr:
		for_tds=each_tr.findAll("td")
		count=0
		id_and_name_dict={}
		for each_td in for_tds:
			for_anchor_data=each_td.findAll("a")
			for each_anchor in for_anchor_data:
			
				id=each_anchor["href"]
				imdb_id=""
				for i in id:
					if i.isnumeric():
						imdb_id+=i
				imdb_id="nm"+imdb_id
				id_and_name_dict["imdb_id"]=imdb_id
				id_and_name_dict["name"]=each_anchor.text
			if count==2:
				break
			count+=1
		if len(id_and_name_dict)>1:
			exact_dict.append(id_and_name_dict)


	if os.path.exists(f"{naming_for_json}_cast.json"):
		pass
	else:
		with open(f"{naming_for_json}_cast.json","w+") as naik:
			json_data=json.dump(exact_dict,naik)

	return exact_dict

print(for_moving_link(python_data))