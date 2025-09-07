# Preprocessing Script for Superstore Dataset

import pandas as pd

# 1. Convert date columns to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], errors='coerce')

# 2. Standardize categorical text columns (strip spaces, title case)
for col in ['Ship Mode', 'Segment', 'Country', 'City', 'State', 'Region', 'Category', 'Sub-Category']:
    df[col] = df[col].astype(str).str.strip().str.title()

# 3. Create new calculated columns
df['Profit Margin'] = (df['Profit'] / df['Sales']).round(4)  # profit margin %
df['Revenue Per Item'] = (df['Sales'] / df['Quantity']).round(2)  # revenue per item
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()
df['Quarter'] = df['Order Date'].dt.to_period('Q')

# 4. Remove duplicates based on Row ID + Order ID
df = df.drop_duplicates(subset=['Row ID', 'Order ID'])

# 5. Handle missing values fill postal codes with 0, drop rows with missing salesprofit
df['Postal Code'] = df['Postal Code'].fillna(0).astype(int)
df = df.dropna(subset=['Sales', 'Profit'])

# 6. Reorder columns for clarity
reordered_cols = ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit', 'Profit Margin', 'Revenue Per Item', 'Year', 'Month', 'Quarter']
df = df[reordered_cols]

# Save cleaned version
output_path = "D:\\Project_Main\\P03 Sale_Analysis\\Superstore_Cleaned.csv"
df.to_csv(output_path, index=False)

