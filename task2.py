import pprint,json,os
with open("position_wise_movies.json","r+") as naik:
	python_data=json.load(naik)

def group_by_year(python_data):
	year_wise_movies={}
	for detail in python_data:
		year=detail['year']
		new_list=[]
		for check_year in python_data:
			if year==check_year['year']:
				new_list.append(check_year)
		year_wise_movies[int(year)]=new_list
	return year_wise_movies

python_string=group_by_year(python_data)
if os.path.exists("group_by_year.json"):
	pass
else:
	with open("group_by_year.json","w+") as naik:
		json_data=json.dump(python_string,naik,indent=2)

pprint.pprint(group_by_year(python_data))



