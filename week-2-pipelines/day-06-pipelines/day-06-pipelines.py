import csv

sample_file = r"c:\Users\AMGLNG\OneDrive\Documents\GitHub\WeThinkCode-data-engineering-intro\week-1-foundations\day-03-data-formats\sample.csv"

def extract(file_path):
    rows = []
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

def transform(rows):
    cleaned_rows = []

    for row in rows:
        name = row['name'].strip()
        age = row["age"].strip()
        
        if name and age.isdigit():
            row["name"] = name.capitalize()
            row["age"] = int(age)
            cleaned_rows.append(row)

    unique_rows = []
    seen = set()
    for row in cleaned_rows:
        row_id = row['id']
        if row_id not in seen:
            unique_rows.append(row)
            seen.add(row_id)

    return unique_rows

def load(unique_rows):
    output_file = "cleaned_data.csv"

    with open(output_file, "w", newline="") as f:
        fieldnames = ["id", "name", "age"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_rows)
    print(f"Cleaned data saved to {output_file}")


def main():
    data = extract(sample_file)
    cleaned = transform(data)
    load(cleaned)

if __name__ == "__main__":
    main()
