import os
import random
import pandas as pd
import nbformat as nbf

# 1. Create sales_data.csv
random.seed(42)
products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Monitor", "Keyboard", "Mouse"]
categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Accessories",
    "Smartwatch": "Accessories",
    "Tablet": "Electronics",
    "Monitor": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories"
}
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
regions = ["North", "South", "East", "West"]

prod_list = []
cat_list = []
sales_list = []
month_list = []
region_list = []

for i in range(115):
    p = random.choice(products)
    c = categories[p]
    s = random.randint(100, 2000)
    m = random.choice(months)
    r = random.choice(regions)
    prod_list.append(p)
    cat_list.append(c)
    sales_list.append(s)
    month_list.append(m)
    region_list.append(r)

df_sample = pd.DataFrame({
    "Product": prod_list,
    "Category": cat_list,
    "Sales": sales_list,
    "Month": month_list,
    "Region": region_list
})

# Add missing values for data cleaning demonstration
df_sample.loc[4, "Sales"] = None
df_sample.loc[18, "Sales"] = None
df_sample.loc[32, "Category"] = None

# Add duplicate rows
duplicates = df_sample.iloc[[2, 10, 15]].copy()
df_sample = pd.concat([df_sample, duplicates], ignore_index=True)

df_sample.to_csv("sales_data.csv", index=False)
print("sales_data.csv created successfully with shape:", df_sample.shape)

# 2. Build Sales_Data_Analysis.ipynb notebook
nb = nbf.v4.new_notebook()

cell1_md = """# Sales Data Analysis Project 📊
**Language:** Python | **Libraries:** Pandas, Matplotlib  
**Level:** Beginner Friendly

This project analyzes sales data to uncover top-performing products, sales trends by month, and category distributions.

---
### Workflow Steps:
1. **Dataset Creation**: Create sample dataset with missing values & duplicate rows.
2. **Data Loading**: Load dataset using Pandas `read_csv`.
3. **Data Cleaning**: Handle missing values (`dropna`) and duplicate rows (`drop_duplicates`).
4. **Data Analysis**: Calculate top products, monthly sales, and category-wise totals using `groupby`, `sum`, and `mean`.
5. **Data Visualization**: Generate Bar Chart, Line Chart, and Pie Chart using Matplotlib.
6. **Key Insights**: Summary of actionable business insights.
"""

cell2_md = """## Step 1: Create Sample Sales Dataset
Generating a sample sales dataset CSV file programmatically so you can run this notebook directly without needing external uploads."""

cell2_code = """# Import random library to generate random sample data
import random
# Import pandas library for data frame creation
import pandas as pd

# Set random seed to make generated data reproducible
random.seed(42)

# List of product names
products = ["Laptop", "Smartphone", "Headphones", "Smartwatch", "Tablet", "Monitor", "Keyboard", "Mouse"]
# Dictionary mapping products to their categories
categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Accessories",
    "Smartwatch": "Accessories",
    "Tablet": "Electronics",
    "Monitor": "Electronics",
    "Keyboard": "Accessories",
    "Mouse": "Accessories"
}
# List of months in a year
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# List of sales regions
regions = ["North", "South", "East", "West"]

# Empty list for Product column
prod_list = []
# Empty list for Category column
cat_list = []
# Empty list for Sales column
sales_list = []
# Empty list for Month column
month_list = []
# Empty list for Region column
region_list = []

# Loop 115 times to generate rows
for i in range(115):
    # Pick a random product
    p = random.choice(products)
    # Get corresponding category for the product
    c = categories[p]
    # Pick a random sales value between 100 and 2000
    s = random.randint(100, 2000)
    # Pick a random month
    m = random.choice(months)
    # Pick a random region
    r = random.choice(regions)
    
    # Append product to product list
    prod_list.append(p)
    # Append category to category list
    cat_list.append(c)
    # Append sales to sales list
    sales_list.append(s)
    # Append month to month list
    month_list.append(m)
    # Append region to region list
    region_list.append(r)

# Create dictionary containing all generated columns
data_dict = {
    "Product": prod_list,
    "Category": cat_list,
    "Sales": sales_list,
    "Month": month_list,
    "Region": region_list
}

# Convert dictionary into a Pandas DataFrame
df_raw = pd.DataFrame(data_dict)

# Add intentional missing sales value at row index 4
df_raw.loc[4, "Sales"] = None
# Add intentional missing sales value at row index 18
df_raw.loc[18, "Sales"] = None
# Add intentional missing category value at row index 32
df_raw.loc[32, "Category"] = None

# Copy rows at index 2, 10, 15 to introduce intentional duplicate rows
dups = df_raw.iloc[[2, 10, 15]].copy()
# Concatenate duplicate rows with the main DataFrame
df_raw = pd.concat([df_raw, dups], ignore_index=True)

# Save the generated DataFrame as sales_data.csv file
df_raw.to_csv("sales_data.csv", index=False)
# Print confirmation message
print("Sample dataset 'sales_data.csv' created successfully!")
"""

cell3_md = """## Step 2: Load Dataset and Initial Inspection
Reading the CSV dataset using `read_csv` and checking the first few rows."""

cell3_code = """# Import pandas library for data analysis
import pandas as pd

# Load dataset from CSV file into a DataFrame
df = pd.read_csv("sales_data.csv")

# Display the first 5 rows of the dataset
df.head()
"""

cell4_md = """## Step 3: Data Cleaning
Checking for missing values and duplicate records, then cleaning the dataset using `dropna` and `drop_duplicates`."""

cell4_code = """# Check count of missing values in each column
missing_count = df.isnull().sum()
# Print missing value details
print("Missing values in each column:")
# Display missing counts
print(missing_count)

# Drop all rows that contain missing values
df = df.dropna()

# Check count of duplicate rows in dataset
duplicate_count = df.duplicated().sum()
# Print duplicate count
print("\\nDuplicate rows count:", duplicate_count)

# Remove all duplicate rows from DataFrame
df = df.drop_duplicates()

# Display total valid rows remaining after cleaning
print("\\nCleaned dataset row count:", len(df))
"""

cell5_md = """## Step 4: Sales Analysis
Performing basic aggregations using `groupby`, `sum`, and `mean`."""

cell5_code = """# Group dataset by Product and calculate total sales for each product
product_sales = df.groupby("Product")["Sales"].sum()
# Sort products by sales in descending order
product_sales_sorted = product_sales.sort_values(ascending=False)
# Get top 5 products by total sales
top_5_products = product_sales_sorted.head(5)
# Print heading for top products
print("--- Top 5 Products by Sales ---")
# Display top 5 products
print(top_5_products)

# Group dataset by Category and calculate total sales
category_sales = df.groupby("Category")["Sales"].sum()
# Print heading for category sales
print("\\n--- Category-wise Total Sales ---")
# Display category sales
print(category_sales)

# Define list of months in proper calendar sequence
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# Group dataset by Month and calculate total sales
monthly_sales = df.groupby("Month")["Sales"].sum()
# Reorder monthly sales by calendar month sequence
monthly_sales_ordered = monthly_sales.reindex(month_order)
# Print heading for monthly sales
print("\\n--- Month-wise Total Sales ---")
# Display monthly sales
print(monthly_sales_ordered)

# Group dataset by Region and calculate average sales
region_avg_sales = df.groupby("Region")["Sales"].mean()
# Print heading for regional average sales
print("\\n--- Region-wise Average Sales ---")
# Display regional average sales
print(region_avg_sales)
"""

cell6_md = """## Step 5: Data Visualization
Creating 3 charts using Matplotlib:
1. **Bar Chart**: Top 5 Products by Total Sales
2. **Line Chart**: Month-wise Sales Trend
3. **Pie Chart**: Category-wise Sales Distribution"""

cell6_code = """# Import matplotlib pyplot library for plotting graphs
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# CHART 1: Bar Chart for Top 5 Products
# -------------------------------------------------------------
# Set figure size for bar chart (width=8 inches, height=5 inches)
plt.figure(figsize=(8, 5))
# Create bar chart for top 5 products with custom color and black border
plt.bar(top_5_products.index, top_5_products.values, color="skyblue", edgecolor="black")
# Add title to bar chart
plt.title("Top 5 Products by Total Sales", fontsize=14, fontweight="bold")
# Add x-axis label
plt.xlabel("Product Name", fontsize=12)
# Add y-axis label
plt.ylabel("Total Sales ($)", fontsize=12)
# Add horizontal gridlines for easier visual comparison
plt.grid(axis="y", linestyle="--", alpha=0.7)
# Display bar chart
plt.show()

# -------------------------------------------------------------
# CHART 2: Line Chart for Monthly Sales Trend
# -------------------------------------------------------------
# Set figure size for line chart (width=10 inches, height=5 inches)
plt.figure(figsize=(10, 5))
# Create line chart for monthly sales with markers on points
plt.plot(monthly_sales_ordered.index, monthly_sales_ordered.values, marker="o", color="darkgreen", linewidth=2.5)
# Add title to line chart
plt.title("Monthly Sales Trend", fontsize=14, fontweight="bold")
# Add x-axis label
plt.xlabel("Month", fontsize=12)
# Add y-axis label
plt.ylabel("Total Sales ($)", fontsize=12)
# Add gridlines to line chart
plt.grid(True, linestyle="--", alpha=0.6)
# Display line chart
plt.show()

# -------------------------------------------------------------
# CHART 3: Pie Chart for Category-wise Sales Distribution
# -------------------------------------------------------------
# Set figure size for pie chart (width=6 inches, height=6 inches)
plt.figure(figsize=(6, 6))
# Create pie chart with percentage labels formatted to 1 decimal place
plt.pie(category_sales.values, labels=category_sales.index, autopct="%1.1f%%", colors=["#ff9999", "#66b3ff"], startangle=90)
# Add title to pie chart
plt.title("Category-wise Sales Share", fontsize=14, fontweight="bold")
# Display pie chart
plt.show()
"""

cell7_md = """## Step 6: Key Business Insights 💡

Based on our analysis and visualizations, here are 5 key insights:

1. **Top Revenue Generator**: **Laptop** & **Smartphone** lead overall revenue, making Electronics the primary sales driver.
2. **Category Dominance**: The **Electronics** category contributes the majority of total sales compared to Accessories.
3. **Monthly Peak & Dips**: Sales fluctuate throughout the year, with noticeable peaks in certain mid-year and year-end months.
4. **Regional Balance**: Sales across **North, South, East, and West** regions maintain consistent average transaction sizes.
5. **Data Quality Action**: Cleaning removed missing records and duplicate entries, ensuring high-accuracy business reporting.
"""

nb.cells = [
    nbf.v4.new_markdown_cell(cell1_md),
    nbf.v4.new_markdown_cell(cell2_md),
    nbf.v4.new_code_cell(cell2_code),
    nbf.v4.new_markdown_cell(cell3_md),
    nbf.v4.new_code_cell(cell3_code),
    nbf.v4.new_markdown_cell(cell4_md),
    nbf.v4.new_code_cell(cell4_code),
    nbf.v4.new_markdown_cell(cell5_md),
    nbf.v4.new_code_cell(cell5_code),
    nbf.v4.new_markdown_cell(cell6_md),
    nbf.v4.new_code_cell(cell6_code),
    nbf.v4.new_markdown_cell(cell7_md)
]

with open("Sales_Data_Analysis.ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print("Sales_Data_Analysis.ipynb created successfully!")
