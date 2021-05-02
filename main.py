import csv
import json
import os


def remove_file_extension(csvFilePath, ext):
    startIndex = csvFilePath.index(ext)
    base = os.path.basename(csvFilePath)
    os.path.splitext(base)
    fileName = os.path.splitext(base)[0]
    return fileName


def make_json(csvFilePath, pk):
    print(pk)
    if pk is None:
        raise TypeError
    jsonFileName = remove_file_extension(csvFilePath, ".csv")
    downloadPath = os.path.expanduser("~")+"/Downloads/"
    print(downloadPath)
    # For now, this just works on my mac.
    jsonFilePath = downloadPath + jsonFileName + ".json"
    print(jsonFilePath)

    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:

            # Property should be the primary key.
            key = rows[pk]
            data[key] = rows

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def start():
    filePath = input(
        "Please enter the file path you'd like to convert form CSV to JSON")
    primaryKey = input("Please enter the primary key, this is required.")
    make_json(filePath, primaryKey)

start()
