import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Load data
data = pd.read_csv(filepath_or_buffer='Parsed Datasets/Metaverse.csv')
df = pd.DataFrame(data, columns=["login_frequency", "session_duration", "anomaly"])

st.title("Analysis of Risk Scores")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.write("Sample of related data", data[['amount','risk_score',"anomaly"]].iloc[200:205])
    st.write("Avg risk_score:", data['risk_score'].mean())
    st.write("Min risk_score:", data['risk_score'].min())

# Define color map
color_map = {
    'low_risk': '#a8d9ff',
    'moderate_risk': '#4c4cff',
    'high_risk': '#ff6a6a'
}

# First multiselect filter for anomaly
selected_anomalies = st.multiselect(
    'Select anomaly',
    options=['low_risk', 'moderate_risk', 'high_risk'],
    default=['low_risk', 'moderate_risk', 'high_risk'],
    key='anomly_filter'
)
filtered_df = df[df['anomaly'].isin(selected_anomalies)]

# Scatter plot for login_frequency vs session_duration
chart = alt.Chart(filtered_df).mark_circle(size=100).encode(
    x=alt.X('login_frequency', title='Login Frequency'),
    y=alt.Y('session_duration', title='Session Duration (min)'),
    color=alt.Color('anomaly', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))),
    tooltip=['login_frequency', 'session_duration', 'anomaly']
).properties(
    title='Scatter Plot of Risk correlated to Frequency and Duration',
    width=800,
    height=600
).interactive()

# Display the chart in Streamlit
st.altair_chart(chart)




# Second multiselect filter for anomaly
# selected_a = st.multiselect(
#     'Select anomaly types to display in Amount vs Duration:',
#     options=['low_risk', 'moderate_risk', 'high_risk'],
#     default=['low_risk', 'moderate_risk', 'high_risk'],
#     key='amount_duration_filter'
# )
amount_df = pd.DataFrame(data, columns=["amount", "session_duration", "risk_score", "anomaly"])
amount_df_filtered = amount_df[amount_df['anomaly'].isin(selected_anomalies)]
amount_df_filtered['anomaly'] = pd.Categorical(amount_df_filtered['anomaly'], categories=['low_risk', 'moderate_risk', 'high_risk'], ordered=True)


# Scatter plot for amount vs session_duration
chart = alt.Chart(amount_df_filtered).mark_circle().encode(
    x=alt.X('amount', title='Amount'),
    y=alt.Y('session_duration', title='Session Duration(min)'),
    size='risk_score',
    color=alt.Color('anomaly', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))),
    tooltip=['amount', 'session_duration', 'risk_score', 'anomaly']
).properties(
    title='Scatter Plot of Amount, Session Duration, and Risk Score by Anomaly',
    width=600,
    height=400
).interactive()

st.altair_chart(chart)


histogram = alt.Chart(amount_df_filtered).mark_bar(opacity=0.5).encode(
    x=alt.X('amount:Q', bin=alt.Bin(maxbins=50), title='Transaction Amount'),
    y=alt.Y('count()', stack='zero',title='Frequency'),
    color=alt.Color('anomaly:N', scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values()))),
    order=alt.Order('anomaly', sort='ascending'),  # This ensures the layering order
    tooltip=['anomaly:N', 'count()']
).properties(
    width=650,
    height=450,
    title='Distribution of Transaction Amount by Anomaly'
)

st.altair_chart(histogram)


