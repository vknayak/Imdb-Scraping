import json,pprint
with open("movies_with_all_details.json","r+") as naik:
	all_movies_list=json.load(naik)

def analyse_language_and_directors(all_movies_list):
	language_and_directors_dic={}
	for director in all_movies_list:
		for each_director in director['director']:
			if each_director=="1 more credit":
				pass
			else:
				languages_list=[]
				languages_dict={}
				for find_director in all_movies_list:

					if each_director in find_director['director']:

						for each_language in find_director['language']:
							if each_language not in languages_list:
								languages_list.append(each_language)
						
						

						for lang in languages_list:
							if lang not in languages_dict:
						 		languages_dict[lang]=0
							for each_lang in find_director['language']:
								if lang==each_lang:
									languages_dict[lang]+=1
				language_and_directors_dic[each_director]=languages_dict
		
	return language_and_directors_dic
pprint.pprint(analyse_language_and_directors(all_movies_list))
