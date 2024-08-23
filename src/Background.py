import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("../Parsed Datasets/Metaverse.csv", usecols = ['location_region'])

value_counts = df["location_region"].value_counts()
value_counts_df = value_counts.reset_index()
value_counts_df.columns = ['Continent', 'Number of Transactions']


st.header("What is the Metaverse?")
st.markdown("The Metaverse is \" :blue-background[a set of digital spaces to socialize, learn, play and more] \"")
st.markdown("The Metaverse primarily uses **cryptocurrency** for its transactions within each world and each world utilizes its own cryptocurrency")


col1, col2 = st.columns(2)

with col1:
    st.write("")
    st.write("")
    st.dataframe(value_counts_df, hide_index=True)
    st.write("Total Number of Transactions: " + str(value_counts_df["Number of Transactions"].sum()))


with col2:
    fig = px.pie(value_counts_df, 
                 values='Number of Transactions', 
                 names='Continent', 
                 title="Number of Transactions Per Continent")
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

