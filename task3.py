import pprint,json,os
with open("position_wise_movies.json","r+") as naik:
	python_data=json.load(naik)

list1=
decade_wise_movies={1950:[],1960:[],1970:[],1980:[],1990:[],2000:[],2010:[],2020:[]}
def group_by_decade(python_data):
	movies_of_1950=[]
	movies_of_1960=[]
	movies_of_1970=[]
	movies_of_1980=[]
	movies_of_1990=[]
	movies_of_2000=[]
	movies_of_2010=[]
	movies_of_2020=[]
	for detail in python_data:
		if (detail['year']>1950) and (detail['year']<=1960):
			movies_of_1950.append(detail)
		elif (detail['year']>1960) and (detail['year']<=1970):
			movies_of_1970.append(detail)
		elif (detail['year']>1970) and (detail['year']<=1990):
			movies_of_1980.append(detail)
		elif (detail['year']>1980) and (detail['year']<=1990):
			movies_of_1990.append(detail)
		elif (detail['year']>1990) and (detail['year']<=2000):
			movies_of_2000.append(detail)
		elif (detail['year']>2000) and (detail['year']<=2010):
			movies_of_2010.append(detail)
		elif (detail['year']>2010) and (detail['year']<=2020):
			movies_of_2020.append(detail)
	decade_wise_movies[1950]=movies_of_1950
	decade_wise_movies[1960]=movies_of_1960
	decade_wise_movies[1970]=movies_of_1970
	decade_wise_movies[1980]=movies_of_1980
	decade_wise_movies[1990]=movies_of_1990
	decade_wise_movies[2000]=movies_of_2000
	decade_wise_movies[2010]=movies_of_2010
	decade_wise_movies[2020]=movies_of_2020
	return decade_wise_movies


python_string=group_by_decade(python_data)

if os.path.exists("group_by_decade.json"):
	pass
else:
	with open("group_by_decade.json","w+") as naik:
		json_data=json.dump(python_string,naik,indent=2)
pprint.pprint(group_by_decade(python_data))