# Day 10 — Monitoring & Reliability

## 🛠 What Happens When Pipelines Fail

Even a well-built pipeline can run into issues:

- Missing files or corrupted data
- Unexpected data types or formats
- Network or database errors
- Bugs in code logic

Without monitoring:

- Errors may go unnoticed
- Reports can be wrong
- Decisions based on data may be flawed
- Trust in the system decreases

---

## 📊 Importance of Monitoring

Monitoring helps detect issues early:

- Logs track pipeline execution
- Alerts notify engineers when something goes wrong
- Metrics show pipeline performance and reliability
- Automatic retries can handle temporary failures

Key monitoring techniques:

1. **Logging**
   - Record steps of pipeline execution
   - Include timestamps, processed records, and errors

2. **Error Handling**
   - Catch exceptions
   - Prevent one failure from stopping the entire pipeline

3. **Alerts**
   - Notify engineers immediately for critical failures
   - Can be email, Slack, or monitoring dashboard

4. **Retries**
   - Automatically attempt to process failed steps
   - Useful for temporary issues like network failures

---

## 🔎 Ensuring Reliability

A reliable pipeline should:

- Validate input data before processing
- Clean or skip invalid data gracefully
- Keep track of processed vs unprocessed data
- Be modular and testable for easier debugging
- Maintain consistent outputs

---

## 🧩 Example: Adding Simple Logging to Our ETL Pipeline

```python
import logging

logging.basicConfig(level=logging.INFO)

def extract():
    logging.info("Starting data extraction")
    # extraction logic here
    logging.info("Extraction completed")
    return data

def transform(data):
    logging.info("Starting transformation")
    # cleaning and transforming logic
    logging.info("Transformation completed")
    return cleaned_data

def load(cleaned_data):
    logging.info("Starting data load")
    # write data to CSV or database
    logging.info("Data load completed")

