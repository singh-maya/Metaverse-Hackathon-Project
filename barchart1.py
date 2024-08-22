import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# Load the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\sammy\OneDrive\Desktop\AllStocks.csv')

# Group the data by age group and calculate the average risk
age_group_vs_risk = df.groupby('age_group')['risk_score'].mean().reset_index()

# Create a Streamlit app
st.title('Age Group vs. Risk')

# Plot the data
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust the size of the figure
colors = plt.cm.coolwarm(range(len(age_group_vs_risk)))  # Use a colormap for better aesthetics

bars = ax.bar(age_group_vs_risk['age_group'], age_group_vs_risk['risk_score'], color=colors)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',  # Format the label to 2 decimal places
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

# Set the title and labels
ax.set_title('Age Group vs. Risk', fontsize=16, fontweight='bold')
ax.set_xlabel('Age Group', fontsize=14)
ax.set_ylabel('Average Risk Score', fontsize=14)

# Customize x-axis and y-axis
ax.set_xticks(age_group_vs_risk['age_group'])
ax.set_xticklabels(age_group_vs_risk['age_group'], rotation=45, ha='right')  # Rotate labels for readability
ax.yaxis.grid(True)  # Add grid lines for y-axis

# Show plot in Streamlit
st.pyplot(fig)

st.bar_chart (age_group_vs_risk)