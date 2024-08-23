import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Parsed Datasets/AllStocks.csv")

# Set the title of the Streamlit app
st.title("Number Transactions from 2022 - 2023")

    # Ensure 'date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

    # Group the data by 'date' and sum the 'amount'
daily_amount = df.groupby('Date')['amount'].sum()

    # Sort the data to find the top 10 dates with highest amounts
top_10_dates = daily_amount.nlargest(10)

    # Plot the bar graph using Matplotlib
fig, ax = plt.subplots()
top_10_dates.plot(kind='bar', color='green', ax=ax)
ax.set_title('Top 10 Transaction Dates by Amount')
ax.set_xlabel('Date')
ax.set_ylabel('Amount of Transactions')
ax.set_xticklabels(top_10_dates.index.strftime('%Y-%m-%d'), rotation=45, ha='right')
plt.tight_layout()  # Adjust layout to make room for x-axis labels

# Display the bar chart in the Streamlit app
# st.pyplot(fig)

st.line_chart(top_10_dates, y_label="Number of Transactions")

st.divider()

url = "https://raw.githubusercontent.com/singh-maya/Metaverse-Hackathon-Project/main/Parsed%20Datasets/AllStocks.csv"
df = pd.read_csv(url)
print(df.head())


# st.title("Risk Score")
st.title( "Number of Transactions by Hour of Day" )

# Group the data by 'hour_of_day' and count the number of transactions
hourly_transactions = df.groupby('hour_of_day').size()

#     # Plot the bar graph using Matplotlib
# plt.figure(figsize=(10, 6))
# hourly_transactions.plot(kind='bar', color='skyblue')
# plt.title('Number of Transactions by Hour of Day')
# plt.xlabel('Hour of Day')
# plt.ylabel('Number of Transactions')
# plt.xticks(rotation=0)  # Keep the hour labels horizontal
# plt.grid(axis='y', linestyle='--', alpha=0.7)

#     # Display the plot in the Streamlit app
# st.pyplot(plt)

st.line_chart(hourly_transactions, x_label="Hour of Day", y_label="Number of Transactions")