import csv
import json

YEAR = 2014

def ReadCsvData(filename, year):
    return_dict = dict()
    return_dict['Countries'] = []
    year_row = year + 4 - 1960
    print(year_row)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            if len(row) < 5 or row[0] == "Country Name":
                pass
            else:
                print(row[0] + "\t\t" + row[1] + "\t" + row[year_row])
                return_dict['Countries'].append({"Name": row[0], "Emissions": row[year_row]})
                line_count += 1
    return return_dict

def AddToJSON(filename, year, data_dict):
    with open("countries.js") as json_file:
        new_json_file = open("CountryData/countries - " + str(year) + ".js", "w")
        geo_data = json.load(json_file)
        for i in range(len(data_dict['Countries'])):
            for j in range(len(geo_data['features'])):
                if geo_data['features'][j]['properties']['CountryName'] == data_dict['Countries'][i]['Name']:
                    #print(True)
                    #print(data_dict['Countries'][i])
                    #print(geo_data['features'][j]['properties']['CountryName'])
                    geo_data['features'][j]['properties']['Emissions'] = data_dict['Countries'][i]['Emissions']
        new_json_file.write("var CountriesOutline = " + json.dumps(geo_data))
        new_json_file.close()

csv_data = ReadCsvData("CO2EmissionData.csv", YEAR)
AddToJSON("countries.js", YEAR, csv_data)