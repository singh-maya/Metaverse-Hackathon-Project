import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Parsed Datasets/AllStocks.csv")

# Set the title of the Streamlit app
st.title("Top 10 Transaction Dates by Amount")

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
ax.set_ylabel('Amount')
ax.set_xticklabels(top_10_dates.index.strftime('%Y-%m-%d'), rotation=45, ha='right')
plt.tight_layout()  # Adjust layout to make room for x-axis labels

    # Display the bar chart in the Streamlit app
st.pyplot(fig)