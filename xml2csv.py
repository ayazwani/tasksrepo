import xml.etree.ElementTree as ET
import csv

tree = ET.parse("food.xml")
root = tree.getroot()

# open a file for writing

data = open('food.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(data)
food_head = []

count = 0
for food in root.findall('food'):
	food_list = []
	food2=[]
	if count == 0:
		name = food.find('name').tag
		food_head.append(name)
		price = food.find('price').tag
		food_head.append(price)
		descriptions = food.find('description').tag
		food_head.append(descriptions)
		calories = food.find('calories').tag
		food_head.append(calories)
		csvwriter.writerow(food_head)
		count = count + 1

	name = food.find('name').text
	food2.append(name)
	price = food.find('price').text
	food2.append(price)
	descriptions = food.find('description').text
	food2.append(descriptions)
	calories = food.find('calories').text
	food2.append(calories)
	
	csvwriter.writerow(food2)
data.close()
