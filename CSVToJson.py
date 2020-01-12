import csv
import json

FILENAME = "FullGreenhouseData.csv"
JSONFILENAME = "countries.js"

NewData = dict()
NewData["type"] = "FeatureCollection"
NewData["features"] = []

with open(JSONFILENAME) as json_file:
    data = json.load(json_file)

csv_data = dict()
csv_data['countries'] = []

f = open("countrydata.txt", "w")

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[6] == "2017" and row[3] == "Greenhouse gases" and row[4] == "TOTAL":
                csv_data['countries'].append({})
                csv_data['countries'][line_count-1]['name'] = row[1]
                csv_data['countries'][line_count-1]['type'] = row[3]
                #csv_data['countries'][line_count-1]['year'] = row[6] ##### Year will be in file name
                csv_data['countries'][line_count-1]['amount'] = row[14]
                print(f'\tCountry: {row[1]} \t\tEmmisionType: {row[3]} \tYear: {row[6]} \tAmount: {row[14]}')
                print("\n\n")
                f.write("Country - " + row[1] + ': "type": "' + row[3] + '", "amount": "' + row[14] + '"\n')
                line_count += 1
    print(f'Processed {line_count} lines.')

f.close()


"""
for c in csv_data:
    for i in range(len(data['features'])):
        NewData['features'].append({})
        NewData['features'][i]['type'] = "feature"
        NewData['features'][i]['properties'] = {}
        NewData['features'][i]['properties']['name'] = data['features'][i]['properties']['name']
        NewData['features'][i]['properties']['geometry'] = data['features'][i]['geometry']
    
print(NewData)
"""