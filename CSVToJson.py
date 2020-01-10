import csv

FILENAME = "FullGreenhouseData.csv"

with open(FILENAME) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[6] == "2017":
                print(f'\tCountry: {row[1]} \t\tEmmisionType: {row[3]} \tYear: {row[6]} \tAmount: {row[14]}')
                line_count += 1
    print(f'Processed {line_count} lines.')