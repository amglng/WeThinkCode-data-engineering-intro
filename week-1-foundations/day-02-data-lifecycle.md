# Day 2 – Data Lifecycle

## Goal of the Day
Understand the journey of data from its source to where it is used, and why managing this flow is critical in data engineering.

---

## What is the Data Lifecycle?

The data lifecycle describes the stages that data passes through in an organization, from creation or ingestion to consumption and archiving.  

Typical stages:
1. **Data Generation** – Data is created or collected from sources such as applications, sensors, or external databases.
2. **Data Ingestion** – Moving the raw data into a system where it can be processed.
3. **Data Storage** – Storing data in databases, data lakes, or warehouses.
4. **Data Processing / Transformation** – Cleaning, structuring, and transforming data to make it usable.
5. **Data Consumption** – Using data in dashboards, reports, analytics, or applications.
6. **Data Archiving / Deletion** – Storing old data or deleting it according to retention policies.

---

## Why Understanding the Data Lifecycle Matters

- Helps identify **where errors may occur**
- Ensures **data is reliable and consistent**
- Guides decisions about **how to store and process data**
- Helps design **efficient pipelines** for moving and transforming data

---

## Types of Data

Data comes in many forms:
- **Structured**: Organized in rows and columns (e.g., CSV, SQL databases)
- **Semi-structured**: Has structure but not rigidly (e.g., JSON, XML)
- **Unstructured**: Raw data without a predefined model (e.g., text files, images, logs)

Understanding the type helps determine:
- How to store it
- How to process it
- How to move it efficiently

---

## Data Engineering Perspective

Data engineers focus on:
- Building **pipelines** that move data through the lifecycle reliably
- Ensuring data is **clean and accurate**
- Automating processes to **reduce manual work**
- Maintaining **consistency** across systems

---

## Real-World Example

Example: A sales system

1. **Data Generation**: Point-of-sale systems collect sales transactions.
2. **Data Ingestion**: Transactions are sent to a central server or cloud database.
3. **Data Storage**: Data is stored in a database or data warehouse.
4. **Data Processing**: Invalid transactions are removed, and totals are calculated.
5. **Data Consumption**: Managers view sales dashboards; analysts create reports.
6. **Data Archiving**: Monthly data older than 2 years is archived for compliance.

---

## Reflection

Answer these questions in your own words:
- What are the key stages of the data lifecycle?
- Why is it important to handle data properly at each stage?
- Can you think of a real system you interact with that has a data lifecycle?

---


