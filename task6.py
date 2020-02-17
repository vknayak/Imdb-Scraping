import json,pprint
with open("movies_with_all_details.json","r+") as naik:
	python_data=json.load(naik)

def language_wise_movies(python_data):
	languages_list=[]
	all_languages_list=[]
	language_wise_movies={}
	for dicts in python_data:
		languages=dicts['language']
		for lang in languages:
			if lang not in languages_list:
				languages_list.append(lang)
			else:
				all_languages_list.append(lang)
	for i in languages_list:
		language_wise_movies[i]=1
		for lang in all_languages_list:
			if i==lang:
				language_wise_movies[i]+=1

	return(language_wise_movies)

print(language_wise_movies(python_data[:10]))

