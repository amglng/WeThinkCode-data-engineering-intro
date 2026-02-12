import csv

sample_csv = "/home/wethinkcode_/Desktop/GitHub Projects/WeThinkCode-data-engineering-intro/week-1-foundations/day-03-data-formats/sample.csv"

rows= []
with open(sample_csv) as f :
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)


print("/nOriginal Rows:")
print(rows)
print("-" * 200)

cleaned_rows = []

for row in rows:
    name = row["name"].strip()# .strip removes all the extra spaces " bob " → "bob"
    age = row["age"].strip()


    if name and age.isdigit():
        row["name"] = name.capitalize() #.capitalize() → makes first letter uppercase → "Bob"
        row["age"] = int(age) 
        cleaned_rows.append(row)

unique_rows = []
seen = set()

#Romoval of all duplicates, based mainly on "id" or other fields
for row in cleaned_rows:
    row_id = row["id"]
    if row_id not in seen:
        unique_rows.append(row)
        seen.add(row_id)

print("After Removing Duplicates, Coverting age to Int and Capitalizing name:")
print(unique_rows)
print("-" * 200)

# for row in unique_rows: #changing age into integers
#     row["age"] = int(row["age"])

#Converting names into uppercase
# row["name"] → gets the string
# .strip() → removes extra spaces like " bob " → "bob"
# .capitalize() → makes first letter uppercase → "Bob"
# ***for row in unique_rows:
#     row["name"] = row["name"].strip().capitalize()

# print("After Converting Ages to Integers:")
# print(unique_rows)
# print("-" * 40)