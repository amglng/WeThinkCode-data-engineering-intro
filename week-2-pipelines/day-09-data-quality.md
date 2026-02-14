# Day 09 — Data Quality & Integrity

## 🧠 What Is Data Quality?

Data quality refers to how **accurate, complete, consistent, and reliable** data is. High-quality data is essential for correct insights, decisions, and automated processes.

Key dimensions of data quality:

1. **Accuracy**  
   - Data correctly represents the real-world entities or events.  
   - Example: A person's age should match their birthdate.

2. **Completeness**  
   - All required fields or records are present.  
   - Example: No missing names or transaction amounts.

3. **Consistency**  
   - Data values are standardized and follow defined formats.  
   - Example: Dates follow `YYYY-MM-DD` across all tables.

4. **Validity**  
   - Data follows defined rules or constraints.  
   - Example: Age should be a positive integer, email addresses must contain `@`.

5. **Timeliness**  
   - Data is up-to-date and available when needed.  
   - Example: Sales data is recorded daily, not weekly, for daily dashboards.

---

## 🔍 Why Data Quality Matters

- Bad data → Incorrect analysis → Wrong decisions.
- Pipelines amplify errors: small mistakes in raw data can propagate downstream.
- Reliable reporting, business intelligence, and machine learning models all depend on **clean, trustworthy data**.

---

## 🛠 How to Ensure Data Quality

Data engineers use multiple strategies to maintain high-quality data:

1. **Validation during ETL**  
   - Example: Check `age` is an integer before loading.
   - Remove or flag invalid records.

2. **Deduplication**  
   - Ensure no duplicate records exist.
   - We did this in Day 5 using sets.

3. **Standardization**  
   - Normalize text, dates, numbers.
   - Example: Capitalize names, convert ages to integers.

4. **Automated Tests / Assertions**  
   - Add checks in pipelines.
   - Example: Assert that a CSV has all required columns.

5. **Logging & Monitoring**  
   - Track anomalies.
   - Alert engineers when data doesn’t meet quality standards.

---

## 📌 Examples Using Our Previous Work

Using the cleaned CSV from Day 6:

```python
import csv

with open("cleaned_data.csv") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Check for missing or invalid ages
invalid_rows = [row for row in rows if not isinstance(row["age"], int)]
print("Invalid rows:", invalid_rows)

# Check for duplicates
seen = set()
duplicates = []
for row in rows:
    key = (row["name"], row["age"])
    if key in seen:
        duplicates.append(row)
    else:
        seen.add(key)

print("Duplicates found:", duplicates)
