import json,pprint
with open("movies_with_all_details.json","r+") as naik:
	python_data=json.load(naik)

def language_wise_movies(python_data):
	directorss_list=[]
	all_directors_list=[]
	director_wise_movies={}
	for dicts in python_data:
		directors=dicts['director']
		for director in directors:
			if director not in directorss_list:
				directorss_list.append(director)
			else:
				all_directors_list.append(director)
	for i in directorss_list:
		director_wise_movies[i]=1
		for dire in all_directors_list:
			if i==dire:
				director_wise_movies[i]+=1

	return(director_wise_movies)

print(language_wise_movies(python_data))

