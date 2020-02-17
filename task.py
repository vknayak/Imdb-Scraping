from bs4 import BeautifulSoup
import requests,pprint,json,os
response=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
soup=BeautifulSoup(response.text,'html.parser')


def Scrap_all_movies():
	details_list=[]
	table_data=soup.find("div",class_="lister")
	tbody_data=table_data.find('tbody',class_="lister-list")
	all_trs=tbody_data.findAll('tr')

	for tr in all_trs:
		details_dict={"name":"","year":"","position":"","rating":"","url":""}

		position=tr.find('td',class_="titleColumn").text
		rank=""
		for exact_position in position:
			if "."!=exact_position:
				rank+=exact_position
			else:
				break
		
		movie_name=tr.find('td',class_="titleColumn").a.text
		exact_year=tr.find('td',class_="titleColumn").span.text
		rating=tr.find('td',class_="ratingColumn").strong.text
		url=tr.find('td',class_="titleColumn").a["href"]
		exact_url="https://www.imdb.com/"+url


		details_dict["position"]=int(rank.strip())
		details_dict['name']=movie_name
		details_dict['year']=int(exact_year[1:5])
		details_dict['rating']=float(rating)
		details_dict['url']=exact_url


		details_list.append(details_dict.copy())
		

	return details_list

# python_data=Scrap_all_movies()

# if os.path.exists("position_wise_movies.json"):
# 	pass
# else:
# 	with open("position_wise_movies.json","w+") as naik:
# 		json_data=json.dump(python_data,naik,indent=2)


# pprint.pprint(Scrap_all_movies())
