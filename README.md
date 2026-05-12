# Retail Sales Data Analysis

## Project Overview
This project analyzes retail sales transaction data using Python.  
The analysis includes data preprocessing, customer behavior analysis, sales trend visualization, outlier detection, and RFM customer segmentation.

---

## Features
- Data cleaning and preprocessing
- Missing value handling
- Datetime conversion
- Outlier detection using Z-score
- Monthly sales analysis
- Customer frequency analysis
- Top customer identification
- Customer churn/response analysis
- RFM (Recency, Frequency, Monetary) segmentation
- Data visualization using Seaborn and Matplotlib

---

## Technologies Used
- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn

---

## Dataset Files
- `Retail_Data_Transactions.csv`
- `Retail_Data_Response.csv`

---

## Project Structure

```text
RetailSalesProject/
│
├── Retail_Data_Transactions.csv
├── Retail_Data_Response.csv
├── project.py
├── Maindata.csv
├── AddAnlys.csv
└── README.md
```

---

## Installation

Install required libraries:

```bash
pip install pandas numpy scipy matplotlib seaborn
```

---

## Run the Project

```bash
python project.py
```

---

## Analysis Performed

### 1. Data Preprocessing
- Merged transaction and response datasets
- Removed missing values
- Converted transaction dates into datetime format

### 2. Outlier Detection
Used Z-score method to detect outliers in customer response data.

### 3. Sales Analysis
- Monthly sales trends
- Highest sales months
- Top spending customers

### 4. Customer Analysis
- Customer transaction frequency
- Top 5 customers by purchases
- Churn/response distribution

### 5. RFM Analysis
RFM stands for:
- Recency
- Frequency
- Monetary

Customers are segmented into:
- P0
- P1
- P2

based on purchase behavior.

---

## Output Files
- `Maindata.csv` → Processed transaction dataset
- `AddAnlys.csv` → RFM analysis dataset

---

## Visualizations
The project generates:
- Boxplots
- Bar charts
- Line graphs
- Monthly sales trend analysis

---

## Author
Karthik S
