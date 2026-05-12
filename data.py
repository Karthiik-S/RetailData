import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

trxn = pd.read_csv('Retail_Data_Transactions.csv')

response = pd.read_csv('Retail_Data_Response.csv')

df = trxn.merge(response, on='customer_id', how='left')

miss = df.isnull().sum()

df = df.dropna()

df['trans_date'] = pd.to_datetime(df['trans_date'])

df['response'] = df['response'].astype('int64')

z_scores = np.abs(stats.zscore(df['response']))

threshold = 3

outliers = z_scores > threshold

print(outliers)

sns.boxplot(x=df['tran_amount'])

#plt.show()

df['month']=df['trans_date'].dt.month
#print(df)

monthly_sales=df.groupby('month')['tran_amount'].sum()
monthly_sales=monthly_sales.sort_values(ascending=False).reset_index().head(3)
#print(monthly_sales)

customer_counts=df['customer_id'].value_counts().reset_index()
customer_counts.coloums=['customer_id','count']
#print(customer_counts)

top_5=customer_counts.sort_values(by='count',ascending=False).head(5)
#print(top_5)

sns.barplot(x='customer_id',y='count',data=top_5)
#plt.show()

customer_sales=df.groupby('customer_id')['tran_amount'].sum().reset_index()
#print(customer_sales)

top_5_sal=customer_sales.sort_values(by='tran_amount',ascending=False).head(5)
#print(top_5_sal)

sns.barplot(x='customer_id',y='tran_amount',data=top_5_sal)
#plt.show()


df['month_year'] = df['trans_date'].dt.to_period('M')

monthly_sales = df.groupby('month_year')['tran_amount'].sum()

monthly_sales.index = monthly_sales.index.to_timestamp()

plt.figure(figsize=(12,6))

plt.plot(monthly_sales.index, monthly_sales.values)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))

plt.xlabel('Month-Year')

plt.ylabel('Sales')

plt.title('Monthly Sales')

plt.xticks(rotation=45)

plt.tight_layout()

#plt.show()

# Recency
recency = df.groupby('customer_id')['trans_date'].max()

# Frequency
frequency = df.groupby('customer_id')['trans_date'].count()

# Monetary
monetary = df.groupby('customer_id')['tran_amount'].sum()

# Combine
rfm = pd.DataFrame({
    'recency': recency,
    'frequency': frequency,
    'monetary': monetary
})

#print(rfm)

def segment_customer(row):

    if row['recency'].year >= 2012 and row['frequency'] >= 15 and row['monetary'] > 1000:
        return 'P0'

    elif (2011 <= row['recency'].year < 2012) and (10 < row['frequency'] < 15) and (500 <= row['monetary'] <= 1000):
        return 'P1'

    else:
        return 'P2'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

#print(rfm)

churn_counts=df['response'].value_counts()
churn_counts.plot(kind='bar')
#plt.show()

top_5_cus = monetary.sort_values(ascending=False).head(5).index

top_customers_df = df[df['customer_id'].isin(top_5_cus)]

top_customer_sales = top_customers_df.groupby(
    ['customer_id', 'month_year']
)['tran_amount'].sum().unstack(level=0)

top_customer_sales.plot(kind='line')

#plt.show()

#print(df)

df.to_csv('Maindata.csv')
rfm.to_csv('AddAnlys.csv')

