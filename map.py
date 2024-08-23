import streamlit as st
import pandas as pd
import pydeck as pdk

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
