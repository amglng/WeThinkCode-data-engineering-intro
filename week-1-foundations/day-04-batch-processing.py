import csv
# from random import sample

csv_file = r"c:\Users\AMGLNG\OneDrive\Documents\GitHub\WeThinkCode-data-engineering-intro\week-1-foundations\day-03-data-formats\sample.csv"

# Step 1: Read CSV into a list
rows = []
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        rows.append(row)

# Step 2: Data Cleaning
# TODO: Remove rows where 'age' is missing or empty
# Hint: use an if-statement inside a loop

cleaned_rows = []
for row in rows:
    if row["age"]:
        cleaned_rows.append(row)

# Step 3: Batch Processing
batch_size = 2
batches = []

for i in range(0, len(cleaned_rows), batch_size):
    batch = cleaned_rows[i:i + batch_size]
    batches.append(batch) 

# TODO: Split cleaned_rows into batches of size batch_size

# Step 4: Batch Calculations
for idx, batch in enumerate(batches):
    # TODO:
    # - Calculate average age
    # - Count people older than 30
    # - Print batch info
    print(f"Processing Batch {idx + 1}")

    ages = []
    for row in batch:
        ages.append(int(row["age"]))

    average_age = sum(ages) / len(ages)
    count_over_30 = sum(1 for age in ages
                         if age > 30)

    print("Average age:", average_age)
    print("People older than 30:", count_over_30)
    print("-" * 40)

