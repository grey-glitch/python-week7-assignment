import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('week 7 assignment\sales_data.csv') 

# Step 2: Display the first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# Step 3: Explore the structure
print("\n📐 Data types of each column:")
print(df.dtypes)

print("\n🕳️ Missing values in each column:")
print(df.isnull().sum())

# Step 4: Clean the dataset
# Option A: Drop rows with missing values
df_cleaned = df.dropna()

# Option B: Fill missing values (example: fill with mean for numeric columns)
df_cleaned = df.fillna(df.mean(numeric_only=True))

print("\n✅ Cleaned dataset preview:")
print(df_cleaned.head())

df = pd.read_csv('week 7 assignment\sales_data.csv')  # Replace with your actual path

# Step 1: Basic statistics
print("📈 Basic statistics:")
print(df[['Quantity Sold', 'Revenue ($)']].describe())

# Step 2: Grouping by Product
product_group = df.groupby('Product')[['Quantity Sold', 'Revenue ($)']].mean()

print("\n📊 Average Quantity Sold and Revenue by Product:")
print(product_group.sort_values(by='Revenue ($)', ascending=False))

# Step 3: Identify patterns

top_product = product_group['Revenue ($)'].idxmax()
top_revenue = product_group['Revenue ($)'].max()

print(f"\n🔥 Highest earning product on average: {top_product} (${top_revenue:.2f})")

# Load and clean dataset
df = pd.read_csv('week 7 assignment\sales_data.csv')  
df.dropna(inplace=True)

# Convert date column to datetime format
df['Date (YYYY-MM-DD)'] = pd.to_datetime(df['Date (YYYY-MM-DD)'])

# Set plot style
sns.set(style="whitegrid")

# 1️⃣ Line Chart: Revenue over Time
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x='Date (YYYY-MM-DD)', y='Revenue ($)', marker='o')
plt.title('📈 Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2️⃣ Bar Chart: Average Revenue per Product
avg_revenue = df.groupby('Product')['Revenue ($)'].mean().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
sns.barplot(x=avg_revenue.index, y=avg_revenue.values, palette='viridis')
plt.title('📊 Average Revenue by Product')
plt.xlabel('Product')
plt.ylabel('Average Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3️⃣ Histogram: Distribution of Quantity Sold
plt.figure(figsize=(8, 5))
sns.histplot(df['Quantity Sold'], bins=10, kde=True, color='skyblue')
plt.title('📦 Distribution of Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 4️⃣ Scatter Plot: Quantity Sold vs Revenue
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Quantity Sold', y='Revenue ($)', hue='Product', palette='deep')
plt.title('🔍 Quantity Sold vs Revenue by Product')
plt.xlabel('Quantity Sold')
plt.ylabel('Revenue ($)')
plt.legend(title='Product')
plt.tight_layout()
plt.show()
