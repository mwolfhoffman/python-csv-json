import csv
import json
import os
 
def remove_file_extension(csvFilePath, ext):
    startIndex = csvFilePath.index(ext)
    base=os.path.basename(csvFilePath)
    os.path.splitext(base)
    fileName = os.path.splitext(base)[0]
    return fileName


def make_json(csvFilePath):
    jsonFileName = remove_file_extension(csvFilePath, ".csv")
    jsonFilePath = "/Users/wolfhoffman/Downloads/" +  jsonFileName  +".json" # For now, this just works on my mac.

    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        for rows in csvReader:
             
            # Property should be the primary key.
            key = rows['ID']
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         

def start():
    filePath = input("Please enter the file path you'd like to convert form CSV to JSON")
    make_json(filePath)

# testFilePath = "/Users/wolfhoffman/Github/projects/python-csv-json/python-csv-test.csv"

start()
