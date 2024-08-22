import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(filepath_or_buffer='../Parsed Datasets/Metaverse.csv')
df = pd.DataFrame(data)

color_map = {    'low_risk': 'green',    'moderate_risk': 'orange',    'high_risk': 'red'}#
#Plotting the scatter plot
plt.figure(figsize=(10, 6))
for anomaly_type,color in color_map.items():
    subset =  df[df['anomaly'] == anomaly_type]   
    plt.scatter(subset['login_frequency'], subset['session_duration'], c=color, label=anomaly_type, s=100)

plt.title('Scatter Plot of Risk correlated to Frequency and Duration')
plt.xlabel('Login Frequency')
plt.ylabel('Session Duration (minutes)')
plt.legend(title='Anomaly')
plt.grid(True)
# Show the scatter plot in Streamlitstequency with Anomaly")st.pyplot(ation vs Login Frequency with Anomaly")
st.pyplot(plt)
# Plotting the scatter plot

