import pandas as pd
import matplotlib
matplotlib.use('Agg') # Non-gui backend for testing
import matplotlib.pyplot as plt

# Step 2: Load Data
df = pd.read_csv("sales_data.csv")
print("Data head:")
print(df.head())

# Step 3: Data Cleaning
print("Missing values:")
print(df.isnull().sum())

df = df.dropna()
df = df.drop_duplicates()
print("Cleaned rows count:", len(df))

# Step 4: Analysis
top_5_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(5)
print("\nTop 5 products:\n", top_5_products)

category_sales = df.groupby("Category")["Sales"].sum()
print("\nCategory sales:\n", category_sales)

month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
monthly_sales = df.groupby("Month")["Sales"].sum().reindex(month_order)
print("\nMonthly sales:\n", monthly_sales)

region_avg_sales = df.groupby("Region")["Sales"].mean()
print("\nRegion avg sales:\n", region_avg_sales)

# Step 5: Charts test
plt.figure(figsize=(8, 5))
plt.bar(top_5_products.index, top_5_products.values, color="skyblue", edgecolor="black")
plt.title("Top 5 Products by Total Sales")
plt.xlabel("Product Name")
plt.ylabel("Total Sales ($)")
plt.savefig("chart1.png")
plt.close()

plt.figure(figsize=(10, 5))
plt.plot(monthly_sales.index, monthly_sales.values, marker="o", color="darkgreen", linewidth=2.5)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales ($)")
plt.savefig("chart2.png")
plt.close()

plt.figure(figsize=(6, 6))
plt.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%", colors=["#ff9999", "#66b3ff"], startangle=90)
plt.title("Category-wise Sales Share")
plt.savefig("chart3.png")
plt.close()

print("All analysis and chart generation tested successfully!")
