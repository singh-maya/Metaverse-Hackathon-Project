import pandas as pd

# Load the dataset
df = pd.read_csv('MSFT.csv')

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for 2021-2022
df = df[(df['Date'] >= '2021-01-01') & (df['Date'] <= '2022-12-31')]

# Set 'Date' as index
df.set_index('Date', inplace=True)

# Format date index to YY-MM-DD
df.index = df.index.strftime('%y-%m-%d')

# Drop unused columns
df.drop(columns=['Open', 'High', 'Low', 'Adj Close', 'Volume'], inplace=True)

# Save cleaned dataset
df.to_csv('cleaned_MSFT_dataset.csv')

# Verify changes
print(df.head())

