from __future__ import annotations
KEY_COLUMNS_TABLE = """
## **Role**
You are a **Data Analysis expert** skilled in selecting the most relevant columns from tabular data.

## **Task**
Analyze the given data table and **identify the minimal set of columns** needed to answer the following question:

### **Question**
{question}

## **Instructions**
1. **Select only the essential column names** that directly contribute to answering the question.
2. **Ensure accuracy** by using the exact column names as provided in the schema.
3. **Avoid including unnecessary columns**—return only the minimal set required.
4. **Do not provide explanations or summaries**—only return the list of column names.

## **Data Table Information**

### **Schema**
{schema_info}

### **Data Table**
{table}

## **Expected Output Format**
A Python list containing the exact column names, e.g.:
```python
["column_name_1", "column_name_2"]

"""
