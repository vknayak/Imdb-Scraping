import requests,json,pprint,os
with open("original_movies_with_cast_details.json","r+") as naik:
	all_movies_with_cast_details=json.load(naik)
exact_dict={}
movies_listtt=[]
def analyse_co_actors(movies_list):

	for cast_list in movies_list:
		inner_dicts={}
		three_actors_list=[]
		single_actor_list=[]

		three_actors_list.append(cast_list['cast'][1:3]) 
		single_actor_list.append(cast_list['cast'][:1])

		for single in single_actor_list:
			for i in single:
				inner_dicts[i['imdb_id']]={"name":i['name'],"frequent_co_actors":[]}
				
				for checking_cast_list in all_movies_with_cast_details:
					check_list=[]
					check_list.append(checking_cast_list['cast'][:3])

					for each_actor in three_actors_list:
						for each in each_actor:
							if each not in movies_listtt:
								movies_listtt.append(each)
								each['num_of_movies']=1
							else:
								pass

								
							for check in check_list:

								if  (each in check) and (i in check):
									if each in inner_dicts[i['imdb_id']]['frequent_co_actors']:
										each['num_of_movies']+=1
									elif each not in inner_dicts[i['imdb_id']]['frequent_co_actors']:
										# each['num_of_movies']=1
										inner_dicts[i['imdb_id']]['frequent_co_actors'].append(each)

		print(inner_dicts)

	# print(movies_listtt)


analyse_co_actors(all_movies_with_cast_details[:250])
# pprint.pprint(analyse_co_actors(all_movies_with_cast_details[:5]))