import csv
import json

csv_file = "/home/wethinkcode_/Desktop/GitHub Projects/WeThinkCode-data-engineering-intro/week-1-foundations/day-03-data-formats/sample.csv"
# TODO: Open the CSV file and read it as dictionaries
# Hint: use csv.DictReader
sample = []
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        sample.append(row)
    
print(sample)


json_file = "/home/wethinkcode_/Desktop/GitHub Projects/WeThinkCode-data-engineering-intro/week-1-foundations/day-03-data-formats/sample.json"

# TODO: Open the JSON file and load the data

dample = []
with open(json_file, "r") as f:
    reader = json.load(f)
    for row in reader:
        dample.append(row)
        

print(dample)
    # pass


# ===== Challenge =====
# After reading both files, try:
# 1. Print the name of the oldest person
ages = []

for row in dample:
    ages.append(int(row["age"]))

print(ages)


# 2. Print the average age
print(sum(ages)/ len(ages))
# 3. Add a new entry to the CSV data
new_person = {"id": "9", "name": "Lee", "age": 22}

with open(csv_file, "a", newline="") as f:
    fieldnames = ["id","name","age"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writerow(new_person)