import csv

# Step 1: Read CSV into a list
rows = []
with open("sample.csv", "r") as f:
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
    batch = cleaned_rows

# TODO: Split cleaned_rows into batches of size batch_size

# Step 4: Batch Calculations
for idx, batch in enumerate(batches):
    # TODO:
    # - Calculate average age
    # - Count people older than 30
    # - Print batch info
    pass
