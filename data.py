# Import pandas library for data analysis
import pandas as pd

# Import numpy library for numerical operations
import numpy as np

# Import statistical functions
from scipy import stats

# Import seaborn library for visualization
import seaborn as sns

# Import matplotlib for plotting graphs
import matplotlib.pyplot as plt

# Import date formatting tools
import matplotlib.dates as mdates

# Read transaction dataset
trxn = pd.read_csv('Retail_Data_Transactions.csv')

# Read response dataset
response = pd.read_csv('Retail_Data_Response.csv')

# Merge transaction and response datasets
df = trxn.merge(response, on='customer_id', how='left')

# Check missing values
miss = df.isnull().sum()

# Remove rows with missing values
df = df.dropna()

# Convert transaction date into datetime format
df['trans_date'] = pd.to_datetime(df['trans_date'])

# Convert response column into integer datatype
df['response'] = df['response'].astype('int64')

# Calculate z-score for outlier detection
z_scores = np.abs(stats.zscore(df['response']))

# Set threshold value for outliers
threshold = 3

# Detect outliers
outliers = z_scores > threshold

# Print outliers
print(outliers)

# Create boxplot for transaction amount
sns.boxplot(x=df['tran_amount'])

# Display graph
plt.show()

# Extract month from transaction date
df['month']=df['trans_date'].dt.month

# Print dataframe
print(df)

# Calculate total monthly sales
monthly_sales=df.groupby('month')['tran_amount'].sum()

# Sort monthly sales in descending order
monthly_sales=monthly_sales.sort_values(ascending=False).reset_index().head(3)

# Print top 3 monthly sales
print(monthly_sales)

# Count customer transactions
customer_counts=df['customer_id'].value_counts().reset_index()

# Rename columns
customer_counts.coloums=['customer_id','count']

# Print customer transaction counts
print(customer_counts)

# Get top 5 customers
top_5=customer_counts.sort_values(by='count',ascending=False).head(5)

# Print top 5 customers
print(top_5)

# Create barplot for top customers
sns.barplot(x='customer_id',y='count',data=top_5)

# Display graph
plt.show()

# Calculate customer sales
customer_sales=df.groupby('customer_id')['tran_amount'].sum().reset_index()

# Print customer sales
print(customer_sales)

# Get top 5 customers by sales
top_5_sal=customer_sales.sort_values(by='tran_amount',ascending=False).head(5)

# Print top 5 sales customers
print(top_5_sal)

# Create barplot for top customer sales
sns.barplot(x='customer_id',y='tran_amount',data=top_5_sal)

# Display graph
plt.show()

# Create month-year column
df['month_year'] = df['trans_date'].dt.to_period('M')

# Calculate monthly sales
monthly_sales = df.groupby('month_year')['tran_amount'].sum()

# Convert period index into timestamp
monthly_sales.index = monthly_sales.index.to_timestamp()

# Set figure size
plt.figure(figsize=(12,6))

# Plot monthly sales trend
plt.plot(monthly_sales.index, monthly_sales.values)

# Format x-axis dates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Set x-axis interval
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))

# Set x-axis label
plt.xlabel('Month-Year')

# Set y-axis label
plt.ylabel('Sales')

# Set graph title
plt.title('Monthly Sales')

# Rotate x-axis labels
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Display graph
plt.show()

# Calculate recency
recency = df.groupby('customer_id')['trans_date'].max()

# Calculate frequency
frequency = df.groupby('customer_id')['trans_date'].count()

# Calculate monetary value
monetary = df.groupby('customer_id')['tran_amount'].sum()

# Create RFM dataframe
rfm = pd.DataFrame({
    'recency': recency,
    'frequency': frequency,
    'monetary': monetary
})

# Print RFM dataframe
print(rfm)

# Create customer segmentation function
def segment_customer(row):

    # Premium customer condition
    if row['recency'].year >= 2012 and row['frequency'] >= 15 and row['monetary'] > 1000:
        return 'P0'

    # Medium customer condition
    elif (2011 <= row['recency'].year < 2012) and (10 < row['frequency'] < 15) and (500 <= row['monetary'] <= 1000):
        return 'P1'

    # Low customer condition
    else:
        return 'P2'

# Apply segmentation to RFM dataframe
rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# Print segmented RFM data
print(rfm)

# Count churn responses
churn_counts=df['response'].value_counts()

# Plot churn graph
churn_counts.plot(kind='bar')

# Display graph
plt.show()

# Get top 5 customers based on monetary value
top_5_cus = monetary.sort_values(ascending=False).head(5).index

# Filter top customers dataframe
top_customers_df = df[df['customer_id'].isin(top_5_cus)]

# Calculate monthly sales for top customers
top_customer_sales = top_customers_df.groupby(
    ['customer_id', 'month_year']
)['tran_amount'].sum().unstack(level=0)

# Plot top customer sales trend
top_customer_sales.plot(kind='line')

# Display graph
plt.show()

# Print final dataframe
print(df)

# Save cleaned dataset
df.to_csv('Maindata.csv')

# Save RFM analysis dataset
rfm.to_csv('AddAnlys.csv')