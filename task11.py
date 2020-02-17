import json,pprint
with open("movies_with_all_details.json","r+") as naik:
	all_movies_list=json.load(naik)

def analyse_movies_genre(all_movies_list):
	genres_list=[]
	all_geners_dict={}
	for genres in all_movies_list:
		for each_genre in genres['genre']:
			if each_genre not in genres_list:
				genres_list.append(each_genre)
	for gen in genres_list:
		all_geners_dict[gen]=0
		for checking_genre in all_movies_list:
			for each_checking_genre in checking_genre['genre']:
				if gen==each_checking_genre:
					all_geners_dict[gen]+=1
	return all_geners_dict
print(analyse_movies_genre(all_movies_list))
