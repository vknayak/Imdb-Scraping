import requests,json,pprint,os
with open("original_movies_with_cast_details.json","r+") as naik:
	all_movies_with_cast_details=json.load(naik)
actors_list=[]
def analyse_actors(movies_list):
	inner_dicts={}
	for each_movie in movies_list:
		
		for all_cast_of_each_movie in each_movie['cast']:
			if all_cast_of_each_movie not in actors_list:
				actors_list.append(all_cast_of_each_movie)
				inner_dicts[all_cast_of_each_movie['imdb_id']]={"name":all_cast_of_each_movie['name'],'num_of_movies':0}
			else:
				continue
			for check_movie in all_movies_with_cast_details:
				if all_cast_of_each_movie in check_movie['cast']:
					inner_dicts[all_cast_of_each_movie['imdb_id']]['num_of_movies']+=1

	pprint.pprint(inner_dicts)






pprint.pprint(analyse_actors(all_movies_with_cast_details[:250]))