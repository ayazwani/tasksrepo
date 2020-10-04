import csv,json
import glob

jsonFilePath = 'all.json'


data={}

data_folder="csvs"
for filename in glob.iglob(data_folder+"/*.csv"):
	with open(filename) as csvf:
		csv_reader = csv.DictReader(csvf)
		for index ,row in enumerate(csv_reader):
			condition = row['condition']
			condition_cui=row['condition_cui']
			if index == 0:
				data[condition]={}
				data[condition]['cui']=condition_cui
				data[condition]['have_had']={}
				data[condition]['looking_for']={}  

			if row['label_bucket']=='have_had':
				data[condition]['have_had'][row['label']]={}
				data[condition]['have_had'][row['label']]['cui']=row['label_cui']
				data[condition]['have_had'][row['label']]['score']=row['label_score']
				data[condition]['have_had'][row['label']]['label_semantic_types']=row['label_semantic_types']
				data[condition]['have_had'][row['label']]['label_ncts_counts']=row['label_ncts_count']
				data[condition]['have_had'][row['label']]['ncts']=row['label_ncts']

			else:
				data[condition]['looking_for'][row['label']]={}
				data[condition]['looking_for'][row['label']]['cui']=row['label_cui']
				data[condition]['looking_for'][row['label']]['score']=row['label_score']
				data[condition]['looking_for'][row['label']]['label_semantic_types']=row['label_semantic_types']
				data[condition]['looking_for'][row['label']]['label_ncts_counts']=row['label_ncts_count']
				data[condition]['looking_for'][row['label']]['ncts']=row['label_ncts']

				
with open(jsonFilePath,'w',encoding='utf-8') as jsf:
	jsf.write(json.dumps(data,sort_keys=True,indent=4))
