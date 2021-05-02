# Python-CSV-JSON-Converter

I had a CSV file that I needed to convert to JSON. It was probably enough data to keep me copying/pasting for at least 10 hours so I wrote a python script to do the work. The values were hardcoded, but then I decided to make it a more generic CLI that anyone could use to convert their CSV to JSON. 

Got a CSV that needs to be a JSON file? Try it out!

## Requirements:
- Python 3.x

## To Run:
- Clone Repo
- `python3 main.py`
- Follow Prompt. You'll be asked to enter a file path of the CSV file and then a primary key. The Primary key is required. 

This comes with a sample CSV file in the root directory, `python-csv-test.csv` to try it out. The Primary Key for this file is `"ID"` (although `"name"` would work too ironically enough).