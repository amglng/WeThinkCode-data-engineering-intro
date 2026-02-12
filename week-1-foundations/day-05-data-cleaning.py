import csv

sample_csv = "/home/wethinkcode_/Desktop/GitHub Projects/WeThinkCode-data-engineering-intro/week-1-foundations/day-03-data-formats/sample.csv"

rows= []
with open(sample_csv) as f :
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

print("Original Rows:")
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
print(len(unique_rows))
#Batching from day 4:
batch_size = 3
batches = []

# start = 0 → start at the first index
# stop = len(unique_rows) → stop at the end of your dataset
# step = batch_size → jump by 3 each time

for i in range(0, len(unique_rows), batch_size):
    batch = unique_rows[i:i + batch_size]
    batches.append(batch)

print(batches)


for idx, batch in enumerate(batches):
    print(f"Processing Batch {idx + 1}")

    ages = [row["age"] for row in batch]

    avg = sum(ages)/len(ages)
    
    count_over_30 = sum(1 for age in ages if age > 30)
    
    print("Average Age:", average_age)
    print("People older than 30:", count_over_30)
    print("-" * 40)
