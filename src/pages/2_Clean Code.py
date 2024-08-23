import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.header("Jupyter Notebook")
st.write("We compiled our datasets from Kaggle and then imported them into Jupyter Notebook to clean")
st.write("For the datasets with the stock information we mainly needed the Dates and the Closing Price")
st.write("1. Import the CSV file")
st.code('''df = pd.read_csv("../Datasets/META.csv", index_col='Date', parse_dates=True)''', language="python")

st.write("2. Drop any unused columns, converted the Dates to Datetime objects, and limited the dataset to 2021-2022")
st.code('''
        df = df.drop(columns=["Unnamed: 0", "Open", "High", "Low", "Volume"])
        start = datetime(2021, 1, 1)
        stop = datetime(2022, 12, 31)
        df = df[start:stop])''', language="python")

st.write("3. Check to see if the constraints work")
st.code('''
        df.head())
        df.tail()
        ''',language="python")

st.write("4. Check for null values")
st.code('''
        df.isnull().sum()
        ''', language="python")

st.write("5. Convert back to CSV to be used in visualizations")
st.code('''df.to_csv('../Parsed Datasets/meta.csv')''',language="python")

st.write("The primary dataset we used was the Metaverse Transactions Data thus, we joined the Stock Datasets with it by Date")
st.code('''join_meta_metaverse = pd.merge(mv,meta, how ='inner', on='Date')''',language="python")
st.write("")

st.divider()
st.header("Streamlit")
st.markdown("**What is streamlit?**  Streamlit is a Python library that allows for easy dataframe visualizations in the form of a web app. It easily takes pandas dataframes and converts them into interactive visualizations")
st.write("Creating a bar chart: Streamlit vs Matplotlib")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Streamlit")
    st.code('''st.bar_chart(top_10_dates, y_label="Amount of Transactions")''', language="python")
    df = pd.read_csv("../Parsed Datasets/AllStocks.csv")

        # Ensure 'date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

        # Group the data by 'date' and sum the 'amount'
    daily_amount = df.groupby('Date')['amount'].sum()

        # Sort the data to find the top 10 dates with highest amounts
    top_10_dates = daily_amount.nlargest(10)
    st.bar_chart(top_10_dates, y_label="Amount of Transactions")
with col2:
    st.subheader("Matplotlib")
    st.code('''
        fig, ax = plt.subplots()
        top_10_dates.plot(kind='bar', color='green', ax=ax)
        ax.set_title('Top 10 Transaction Dates by Amount')
        ax.set_xlabel('Date')
        ax.set_ylabel('Amount of Transactions')
        ax.set_xticklabels(top_10_dates.index.strftime('%Y-%m-%d'), rotation=45, ha='right')
        plt.tight_layout()  # Adjust layout to make room for x-axis labels


        st.pyplot(fig))
            ''',language="python")
    df = pd.read_csv("../Parsed Datasets/AllStocks.csv")

        # Ensure 'date' column is in datetime format
    df['Date'] = pd.to_datetime(df['Date'])

        # Group the data by 'date' and sum the 'amount'
    daily_amount = df.groupby('Date')['amount'].sum()

        # Sort the data to find the top 10 dates with highest amounts
    top_10_dates = daily_amount.nlargest(10)
    fig, ax = plt.subplots()
    top_10_dates.plot(kind='bar', color='green', ax=ax)
    ax.set_title('Top 10 Transaction Dates by Amount')        
    ax.set_xlabel('Date')
    ax.set_ylabel('Amount of Transactions')
    ax.set_xticklabels(top_10_dates.index.strftime('%Y-%m-%d'), rotation=45, ha='right')
    plt.tight_layout()  # Adjust layout to make room for x-axis labels


    st.pyplot(fig)