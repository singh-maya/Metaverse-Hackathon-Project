import streamlit as st
import pandas as pd
import altair as alt

# Load CSV files
dfMETA = pd.read_csv("../Parsed Datasets/meta.csv", parse_dates=['Date'])
dfRBLX = pd.read_csv("../Parsed Datasets/rblx.csv", parse_dates=['Date'])
dfMSFT = pd.read_csv("../Parsed Datasets/MSFT_parsed.csv", parse_dates=['Date'])
dfNVDA = pd.read_csv("../Parsed Datasets/cleaned_NVDA_data.csv", parse_dates=['Date'])
dfGOGL = pd.read_csv("../Parsed Datasets/GoogleParsed.csv", parse_dates=['Date'])

# Merge the data on the Date column and rename columns as needed
merged_df = dfMETA[['Date', 'Close']].merge(dfRBLX[['Date', 'Close']], on='Date', suffixes=('', '_RBLX'))
merged_df.rename(columns={"Close": "META", "Close_RBLX": "RBLX"}, inplace=True)

merged_df = merged_df.merge(dfMSFT[['Date', 'Close']], on='Date').rename(columns={"Close": "MSFT"})
merged_df = merged_df.merge(dfNVDA[['Date', 'Close']], on='Date').rename(columns={"Close": "NVDA"})
merged_df = merged_df.merge(dfGOGL[['Date', 'Close']], on='Date').rename(columns={"Close": "GOGL"})

# Handle NaN values
merged_df.fillna(method='ffill', inplace=True)

# Melt the DataFrame for Altair
melted_df = merged_df.melt(id_vars='Date', value_vars=['META', 'RBLX', 'MSFT', 'NVDA', 'GOGL'],
                           var_name='Company', value_name='Close')


# Dynamic filters setup
st.sidebar.header('Filters')

# Multi-select for companies
selected_companies = st.sidebar.multiselect(
    'Select Companies',
    options=melted_df['Company'].unique(),
    default=melted_df['Company'].unique()  # Default to all companies selected
)

# Date range filter
start_date, end_date = st.sidebar.date_input(
    'Select Date Range',
    value=[melted_df['Date'].min(), melted_df['Date'].max()],
    min_value=melted_df['Date'].min(),
    max_value=melted_df['Date'].max()
)

# Filter data based on selections
filtered_df = melted_df[
    (melted_df['Company'].isin(selected_companies)) &
    (melted_df['Date'] >= pd.Timestamp(start_date)) &
    (melted_df['Date'] <= pd.Timestamp(end_date))
]

# Check if filtered DataFrame is empty
if filtered_df.empty:
    st.write("No data available for the selected filters.")
else:
    # Create an Altair chart with tooltips and mark_point() for better interactivity
    line_chart = alt.Chart(filtered_df).mark_line().encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(format='%B, %Y')),
        y=alt.Y('Close:Q', title='Close Price (USD)'),
        color='Company:N',
        tooltip=['Date:T', 'Company:N', 'Close:Q']
    ).properties(
        title='Close Prices Amongst Top Tech Companies Over Time',
        width=700,
        height=400
    )

    # Add points on the line to improve tooltip visibility
    points = alt.Chart(filtered_df).mark_point(filled=True, size=60).encode(
        x=alt.X('Date:T', title='Date', axis=alt.Axis(format='%B, %Y')),
        y=alt.Y('Close:Q', title='Close Price (USD)'),
        color='Company:N',
        tooltip=['Date:T', 'Company:N', 'Close:Q']
    )

    # Combine line and points charts
    final_chart = line_chart + points

    # Display the chart in Streamlit
    st.altair_chart(final_chart, use_container_width=True)
