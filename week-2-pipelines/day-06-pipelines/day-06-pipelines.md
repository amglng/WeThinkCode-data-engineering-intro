 Day 6 — Understanding Data Pipelines

---

## 🧠 What Is a Data Pipeline?

A **data pipeline** is a structured process that moves data from one place to another while transforming it along the way.

In simple terms:

> A data pipeline takes raw data and turns it into clean, usable data.

It answers four main questions:

1. Where does the data come from?
2. How is the data cleaned or changed?
3. Where does the cleaned data go?
4. How does this process run reliably?

```mermaid
graph LR
    A[Raw Data Source] --> B[Data Pipeline]
    B --> C[Clean Usable Data]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#95e1d3
```

---

## 🔁 What Is ETL?

Most pipelines follow a pattern called **ETL**:

- **E** → Extract  
- **T** → Transform  
- **L** → Load  

Let's connect this directly to the code we wrote in Week 1.

```mermaid
graph TD
    A[ETL Pipeline] --> B[Extract]
    A --> C[Transform]
    A --> D[Load]
    
    B --> B1[Read from Source]
    C --> C1[Clean Data]
    C --> C2[Validate Data]
    C --> C3[Remove Duplicates]
    D --> D1[Write to Destination]
    
    style A fill:#f9ca24
    style B fill:#6c5ce7
    style C fill:#fd79a8
    style D fill:#00b894
```

---

## 1️⃣ Extract — Getting the Data

Extraction means reading data from a source.

In our previous code, we extracted data from a CSV file:

```python
with open("raw_data.csv") as f:
    lines = f.readlines()
```

**This is the Extract step.**

We are simply collecting raw data.

```mermaid
flowchart LR
    A[(CSV Fileraw_data.csv)] -->|Read| B[Extract Function]
    B --> C[Raw Lines in Memory]
    
    style A fill:#e74c3c
    style B fill:#3498db
    style C fill:#f39c12
```

---

## 2️⃣ Transform — Cleaning the Data

Transformation is where the real work happens.

In Week 1, we did things like:

- Removing whitespace
- Capitalizing names
- Converting age to integers
- Skipping invalid values
- Removing duplicates

Example transformation logic:

```python
cleaned_rows = []
seen = set()

for line in lines:
    name, age = line.strip().split(",")

    if age == "not_available":
        continue

    name = name.strip().capitalize()
    age = int(age)

    identifier = (name, age)

    if identifier not in seen:
        seen.add(identifier)
        cleaned_rows.append({"name": name, "age": age})
```

**This is the Transform step.**

We:
- Validated data
- Cleaned formatting
- Removed bad records
- Removed duplicates

Transformation turns raw data into usable data.

```mermaid
flowchart TD
    A[Raw Lines] --> B{For Each Line}
    B --> C[Strip Whitespace]
    C --> D[Split by Comma]
    D --> E{Age Valid?}
    E -->|No| F[Skip Record]
    E -->|Yes| G[Capitalize Name]
    G --> H[Convert Age to Int]
    H --> I{Duplicate?}
    I -->|Yes| F
    I -->|No| J[Add to Cleaned Data]
    J --> K[Cleaned Rows]
    
    style A fill:#e74c3c
    style E fill:#f39c12
    style I fill:#f39c12
    style K fill:#27ae60
```

---

## 3️⃣ Load — Saving the Clean Data

Loading means saving the cleaned data somewhere.

In our previous work, we wrote the cleaned data into a new file:

```python
with open("clean_data.csv", "w") as f:
    for row in cleaned_rows:
        f.write(f"{row['name']},{row['age']}\n")
```

**This is the Load step.**

Now the cleaned data is ready for:
- Reports
- Analysis
- Dashboards
- Further processing

```mermaid
flowchart LR
    A[Cleaned Rows] --> B[Load Function]
    B -->|Write| C[(clean_data.csv)]
    C --> D[Ready for Use]
    D --> E[Reports]
    D --> F[Analysis]
    D --> G[Dashboards]
    
    style A fill:#27ae60
    style B fill:#3498db
    style C fill:#2ecc71
    style D fill:#95a5a6
```

---

## 🏗 Turning Our Script into a Proper Pipeline

Originally, everything was in one long script.

Now we structure it properly:

```python
def extract():
    with open("raw_data.csv") as f:
        return f.readlines()

def transform(lines):
    cleaned_rows = []
    seen = set()

    for line in lines:
        name, age = line.strip().split(",")

        if age == "not_available":
            continue

        name = name.strip().capitalize()
        age = int(age)

        identifier = (name, age)

        if identifier not in seen:
            seen.add(identifier)
            cleaned_rows.append({"name": name, "age": age})

    return cleaned_rows

def load(cleaned_rows):
    with open("clean_data.csv", "w") as f:
        for row in cleaned_rows:
            f.write(f"{row['name']},{row['age']}\n")

def main():
    data = extract()
    cleaned = transform(data)
    load(cleaned)

if __name__ == "__main__":
    main()
```

Now we have a proper pipeline structure:

**Extract → Transform → Load**

Each stage has a clear responsibility.

```mermaid
sequenceDiagram
    participant M as main()
    participant E as extract()
    participant T as transform()
    participant L as load()
    participant F as File System
    
    M->>E: Call extract()
    E->>F: Read raw_data.csv
    F-->>E: Return raw lines
    E-->>M: Return data
    
    M->>T: Call transform(data)
    T->>T: Clean & validate
    T->>T: Remove duplicates
    T-->>M: Return cleaned_rows
    
    M->>L: Call load(cleaned_rows)
    L->>F: Write clean_data.csv
    F-->>L: Success
    L-->>M: Complete
```

---

## 🎯 Why This Structure Matters

Separating the stages makes the system:

- ✅ **Easier to read**
- ✅ **Easier to debug**
- ✅ **Easier to extend**
- ✅ **More professional**
- ✅ **Closer to real-world data engineering systems**

Instead of writing scripts…

**We are now designing systems.**

```mermaid
graph TD
    A[Monolithic Script] -->|Refactor| B[Modular Pipeline]
    
    A --> A1[Hard to Debug]
    A --> A2[Hard to Test]
    A --> A3[Hard to Maintain]
    
    B --> B1[Easy to Debug]
    B --> B2[Easy to Test]
    B --> B3[Easy to Maintain]
    B --> B4[Easy to Extend]
    
    style A fill:#e74c3c
    style B fill:#27ae60
```

---

## 🛡 What Makes a Good Pipeline?

A good pipeline is:

1. **Modular** (separate stages)
2. **Reliable** (handles bad data)
3. **Clear** (easy to understand)
4. **Consistent** (predictable output)
5. **Maintainable** (easy to improve later)

```mermaid
mindmap
  root((Good Pipeline))
    Modular
      Separate Stages
      Clear Responsibilities
      Independent Functions
    Reliable
      Error Handling
      Data Validation
      Graceful Failures
    Clear
      Good Documentation
      Readable Code
      Logical Flow
    Consistent
      Predictable Output
      Standard Format
      Reproducible Results
    Maintainable
      Easy to Update
      Simple to Debug
      Well Structured
```

---

## 🧩 The Bigger Picture

This simple CSV cleaning exercise is actually the foundation of:

- Production data systems
- Data warehouses
- Analytics platforms
- Machine learning pipelines

Even large companies follow the same idea:

**Extract → Transform → Load**

The only difference is scale and infrastructure.

```mermaid
graph TB
    A[Simple CSV Pipeline] --> B[Same Principles]
    B --> C[Enterprise Data Warehouse]
    B --> D[Analytics Platform]
    B --> E[ML Pipeline]
    B --> F[Real-time Streaming]
    
    A --> A1[Small Scale]
    C --> C1[Large Scale]
    D --> D1[Large Scale]
    E --> E1[Large Scale]
    F --> F1[Large Scale]
    
    style A fill:#3498db
    style B fill:#f39c12
    style C fill:#9b59b6
    style D fill:#9b59b6
    style E fill:#9b59b6
    style F fill:#9b59b6
```

---

## 📝 Summary

### A data pipeline:
- Moves data from source to destination
- Cleans and validates data
- Structures processing into clear stages

### ETL stands for:
- **Extract** (read data)
- **Transform** (clean data)
- **Load** (save data)

### Key Takeaway:
Our Week 1 cleaning script was already a small pipeline.

Day 6 is about recognizing that structure and implementing it properly.

```mermaid
graph LR
    A[Week 1 Script] -->|Recognition| B[ETL Pattern]
    B -->|Refactoring| C[Proper Pipeline]
    C -->|Foundation| D[Production Systems]
    
    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
    style D fill:#3498db