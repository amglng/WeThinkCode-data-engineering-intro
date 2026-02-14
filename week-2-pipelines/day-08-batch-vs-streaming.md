# Batch vs Streaming Processing

---

## 1️⃣ Batch Processing (Review from Day 4 & 7)

### Definition
Process data in chunks at scheduled intervals.

### How it works
Collect data over time → process it all at once → save results.

### Example from your pipeline

```python
batch_size = 3
for i in range(0, len(cleaned_rows), batch_size):
    batch = cleaned_rows[i:i + batch_size]
    # process each batch
```

### Characteristics

- ✅ Runs on a schedule (daily, hourly, weekly)
- ✅ Handles large volumes efficiently
- ❌ Not real-time — there's a delay before results are available
- ✅ Easier to implement and debug

### Use Cases

- Payroll systems
- Daily sales reports
- Monthly financial statements

---

## 2️⃣ Streaming Processing

### Definition
Process data continuously, as it arrives.

### How it works
Each record is processed immediately rather than waiting for a batch.

### Characteristics

- ✅ Low latency (results appear instantly or within seconds)
- ✅ Continuous input and output
- ❌ Requires robust error handling and monitoring
- ❌ Harder to implement and maintain than batch

### Use Cases

- Real-time fraud detection
- Stock market updates
- Social media monitoring
- Ride-hailing location tracking

---

## 3️⃣ Key Differences

| Feature | Batch | Streaming |
|---------|-------|-----------|
| **Processing** | Chunks | Continuous |
| **Latency** | Minutes to hours | Milliseconds to seconds |
| **Complexity** | Lower | Higher |
| **Use Case** | Reports, analytics | Real-time alerts, dashboards |
| **Reliability** | Easier to retry failed batches | Needs robust error handling |

---

## 4️⃣ Real-World Analogy

### Batch
Think of **washing clothes** — you wait until the laundry basket is full, then wash a whole batch at once.

### Streaming
Think of a **dishwasher that washes each plate immediately** as it is used.

---

## 5️⃣ Connection to Your Pipelines

### So far, your Day 5–7 pipelines are batch pipelines:

1. You read a CSV (extract)
2. Clean and transform it
3. Process it in batches
4. Save the cleaned results

### A streaming pipeline would instead:

Read each record in real time (e.g., from an API or live feed) and process it immediately.

---

## Visual Comparison

```
BATCH PROCESSING:
┌─────────────────────────────────────┐
│  Data Collection Period             │
│  [record1, record2, record3, ...]   │
└─────────────────┬───────────────────┘
                  │
                  ▼
          ┌───────────────┐
          │  Process All  │
          └───────┬───────┘
                  │
                  ▼
          ┌───────────────┐
          │ Save Results  │
          └───────────────┘


STREAMING PROCESSING:
record1 → Process → Save → Output
record2 → Process → Save → Output
record3 → Process → Save → Output
   ...       ...      ...     ...
```

---

## Summary

- **Batch**: Collect, wait, process all at once — great for scheduled reports
- **Streaming**: Process each record immediately — great for real-time systems

Your current pipelines are batch-based, which is perfect for learning the fundamentals before moving to more complex streaming architectures.
