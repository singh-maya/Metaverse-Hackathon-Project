import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("../Parsed Datasets/Metaverse.csv", usecols = ['location_region'])

value_counts = df["location_region"].value_counts()

st.bar_chart(value_counts, horizontal=True, x_label="Number of Transactions", y_label="Continent")
st.write(value_counts)

fig, ax = plt.subplots()
value_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax, startangle=90, legend=False)

# Customize appearance
ax.set_facecolor('#1e1e1e')  # Set background color of the pie chart
fig.patch.set_facecolor('#1e1e1e')  # Set background color of the figure
ax.texts[0].set_color('white')  # Set text color
ax.texts[2].set_color('white')  # Set text color
ax.texts[4].set_color('white')  # Set text color
ax.texts[6].set_color('white')  # Set text color
ax.texts[8].set_color('white')  # Set text color
ax.set_title('Demographic of Metaverse Users', color='white', fontsize=14, fontweight='bold', fontname='Sans Serif')  # Title customization

# Remove grid lines and spines
ax.grid(False)
for spine in ax.spines.values():
    spine.set_visible(False)

# Display the pie chart in Streamlit
st.pyplot(fig)

df = value_counts.to_frame()
st.write(df)
fig = px.pie(df, values='count', names='location_region')
st.plotly_chart(fig)

# df["location_region"] = df["location_region"].replace({"Africa" : "8.7832,34.5085"})
# df["location_region"] = df["location_region"].replace({"Asia" : "34.0479,100.6197"})
# df["location_region"] = df["location_region"].replace({"Europe" : "54.5260,15.2551"})
# df["location_region"] = df["location_region"].replace({"North America" : "54.5260,-105.2551"})
# df["location_region"] = df["location_region"].replace({"South America" : "-8.7832 ,-55.4915"})

# df[['latitude', 'longitude']] = df['location_region'].str.split(',', expand=True)

# df['latitude'] = pd.to_numeric(df['latitude'])
# df['longitude'] = pd.to_numeric(df['longitude'])

# df["latitude"] = df['latitude'] + np.random.randn(len(df))
# df["longitude"] = df['longitude'] + np.random.randn(len(df))

# st.map(df)

