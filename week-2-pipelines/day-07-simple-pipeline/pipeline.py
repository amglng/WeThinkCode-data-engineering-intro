import csv

RAW_FILE = "raw_data.csv"
CLEAN_FILE = "clean_data.csv"
BATCH_SIZE = 3

# ---------- EXTRACT ----------
def extract(file_path):
    """Read raw CSV into a list of dicts."""
    rows = []
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

# ---------- TRANSFORM ----------
def transform(rows):
    """Clean names, convert ages, remove duplicates."""
    cleaned_rows = []

    for row in rows:
        name = row["name"].strip()
        age = row["age"].strip()

        if name and age.isdigit():
            row["name"] = name.capitalize()
            row["age"] = int(age)
            cleaned_rows.append(row)

    # Remove duplicates based on ID
    unique_rows = []
    seen = set()
    for row in cleaned_rows:
        row_id = row["id"]
        if row_id not in seen:
            unique_rows.append(row)
            seen.add(row_id)

    return unique_rows

# ---------- BATCH PROCESS ----------
def batch_data(data, batch_size=BATCH_SIZE):
    """Split data into batches."""
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]

# ---------- LOAD ----------
def load(data, file_path=CLEAN_FILE):
    """Write cleaned data to a CSV file."""
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "age"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Cleaned data saved to {file_path}")

# ---------- PIPELINE ----------
def main():
    raw = extract(RAW_FILE)
    print(f"Extracted {len(raw)} rows")

    cleaned = transform(raw)
    print(f"Transformed {len(cleaned)} rows (cleaned & deduplicated)")

    # Optional: process in batches
    batches = batch_data(cleaned)
    for idx, batch in enumerate(batches):
        print(f"\nProcessing Batch {idx + 1}")
        ages = [row["age"] for row in batch]
        avg_age = sum(ages)/len(ages)
        over_30 = sum(1 for age in ages if age > 30)
        print(f"Average age: {avg_age}")
        print(f"People older than 30: {over_30}")

    load(cleaned)

if __name__ == "__main__":
    main()

