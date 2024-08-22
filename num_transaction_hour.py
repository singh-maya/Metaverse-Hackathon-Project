import streamlit as st
import matplotlib.pyplot as plt
st.title("Risk Score")
st.write(
    ""
)
import pandas as pd
url = "https://raw.githubusercontent.com/singh-maya/Metaverse-Hackathon-Project/main/Parsed%20Datasets/AllStocks.csv"
df = pd.read_csv(url)
print(df.head())
# Group the data by 'hour_of_day' and count the number of transactions
hourly_transactions = df.groupby('hour_of_day').size()

    # Plot the bar graph using Matplotlib
plt.figure(figsize=(10, 6))
hourly_transactions.plot(kind='bar', color='skyblue')
plt.title('Number of Transactions by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=0)  # Keep the hour labels horizontal
plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot in the Streamlit app
st.pyplot(plt)


