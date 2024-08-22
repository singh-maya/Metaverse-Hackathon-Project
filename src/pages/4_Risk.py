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

# Load the CSV file into a DataFrame
df = pd.read_csv("../Parsed Datasets/AllStocks.csv")

# Group the data by age group and calculate the average risk
age_group_vs_risk = df.groupby('age_group')['risk_score'].mean()
age_group_vs_risk_df = age_group_vs_risk.reset_index()
age_group_vs_risk_df.columns = ['Age Group', 'Risk']


col1, col2 = st.columns(2)
with col1:
    st.dataframe(age_group_vs_risk_df, hide_index=True )
with col2:
    st.bar_chart(age_group_vs_risk, y_label= "Age Group", x_label="Average Risk Score", horizontal=True)

# # Create a Streamlit app
# st.title('Age Group vs. Risk')

# # Plot the data
# fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the size of the figure
# colors = plt.cm.coolwarm(range(len(age_group_vs_risk)))  # Use a colormap for better aesthetics

# bars = ax.bar(age_group_vs_risk['age_group'], age_group_vs_risk['risk_score'], color=colors)

# # Add data labels
# for bar in bars:
#     height = bar.get_height()
#     ax.annotate(f'{height:.2f}',  # Format the label to 2 decimal places
#                 xy=(bar.get_x() + bar.get_width() / 2, height),
#                 xytext=(0, 3),  # 3 points vertical offset
#                 textcoords="offset points",
#                 ha='center', va='bottom')

# # Set the title and labels
# ax.set_title('Age Group vs. Risk', fontsize=16, fontweight='bold')
# ax.set_xlabel('Age Group', fontsize=14)
# ax.set_ylabel('Average Risk Score', fontsize=14)

# # Customize x-axis and y-axis
# ax.set_xticks(age_group_vs_risk['age_group'])
# ax.set_xticklabels(age_group_vs_risk['age_group'], rotation=45, ha='right')  # Rotate labels for readability
# ax.yaxis.grid(True)  # Add grid lines for y-axis

# # Show plot in Streamlit
# st.pyplot(fig)

