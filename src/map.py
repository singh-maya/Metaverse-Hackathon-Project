import streamlit as st
import pandas as pd
import pydeck as pdk
import altair as alt

# Assume the dataset already includes a 'Continent' column
data = pd.read_csv(filepath_or_buffer='Parsed Datasets/long_lat_metaverse.csv')

# If the continent data is not available, you would need to map each lat/lon to a continent.
# Assuming that step is done and the dataset now includes 'Continent' information.

# Aggregate data to get the sum of risk scores for each continent
agg_data = data.groupby('location_region').agg({
    'risk_score': 'sum',
    'Latitude': 'mean',  # Use the mean latitude for the continent's central point
    'Longitude': 'mean'  # Use the mean longitude for the continent's central point
}).reset_index()

# Create a DataFrame with the relevant columns for pydeck
map_df = pd.DataFrame({
    "lat": agg_data["Latitude"],
    "lon": agg_data["Longitude"],
    "risk_score": agg_data["risk_score"],
    "continent": agg_data["location_region"]
})

def get_color(risk_score):
    if risk_score < map_df['risk_score'].quantile(0.25):
        return [0, 255, 0]  # Green for lower risk scores
    elif risk_score < map_df['risk_score'].quantile(0.5):
        return [255, 255, 0]  # Yellow for medium-low risk scores
    elif risk_score < map_df['risk_score'].quantile(0.75):
        return [255, 165, 0]  # Orange for medium-high risk scores
    else:
        return [255, 0, 0]  # Red for high risk scores

# Apply the color mapping to the DataFrame
risk = agg_data['risk_score'].round(0).astype(int)
map_df['color'] = map_df['risk_score'].apply(get_color)

# Define the layer for pydeck
layer = pdk.Layer(
    'ScatterplotLayer',
    data=map_df,
    get_position='[lon, lat]',
    get_radius='risk_score / 2.5',  # Adjust size scaling; smaller divisor = larger circles
    get_fill_color= 'color',
    pickable=True,
    opacity=0.5,
)

# Set the view state (center of the map)
view_state = pdk.ViewState(
    latitude=map_df['lat'].mean(),
    longitude=map_df['lon'].mean(),
    zoom=1,  # Adjust zoom level
    pitch=0,
)

# Create the pydeck map and display it in Streamlit
r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"text": "{continent}\nRisk Score: {risk_score}"})
st.pydeck_chart(r)

st.markdown("""
### Legend
- <span style="color:rgb(0, 255, 0)">&#11044;</span> Low Risk: Lower 25% of risk scores
- <span style="color:rgb(255, 255, 0)">&#11044;</span> Medium-Low Risk: 25% to 50% of risk scores
- <span style="color:rgb(255, 165, 0)">&#11044;</span> Medium-High Risk: 50% to 75% of risk scores
- <span style="color:rgb(255, 0, 0)">&#11044;</span> High Risk: Top 25% of risk scores
""", unsafe_allow_html=True)


# Display the sum of risk scores by continent in Streamlit
st.write(f"Sum of Risk Scores by Continent:")
st.write(map_df[['continent', 'risk_score']])

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