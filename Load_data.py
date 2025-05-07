import pandas as pd
import matplotlib.pyplot as plt

order_products = pd.read_csv('order_products__prior.csv')
products = pd.read_csv('products.csv')

# Merge the order-product pairs with product names
order_details = order_products.merge(products, on='product_id')


# Count how many times each product was ordered
top_products = order_details['product_name'].value_counts().head(10)

print("\nTop 10 most ordered products:")
print(top_products)


# Count how many times each product was ordered
top_products = order_details['product_name'].value_counts().head(10)

print("\nTop 10 most ordered products:")
print(top_products)


# Load the orders data
orders = pd.read_csv('orders.csv')

# Show first 5 rows
print(orders.head())

# Check shape (how many rows and columns)
print("\nData shape:", orders.shape)

# Check data types of each column
print("\nData types:")
print(orders.dtypes)

# Check for missing values in each column
print("\nMissing values:")
print(orders.isnull().sum())

# Summary statistics for numerical columns
print("\nSummary stats:")
print(orders.describe())

# Calculate the average days between orders (ignoring missing values)
average_days = orders['days_since_prior_order'].mean()

print("\nAverage days between orders:", average_days)

# Count orders per day of week
orders_per_day = orders['order_dow'].value_counts().sort_index()

print("\nOrders per day of week:")
print(orders_per_day)

# Create a mapping from numbers to day names
day_names = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

# Rename the index (so 0 becomes 'Sunday', etc.)
orders_per_day.index = orders_per_day.index.map(day_names)

# Define custom colors for each bar
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']

# Count how many orders placed each hour
orders_per_hour = orders['order_hour_of_day'].value_counts().sort_index()


plt.figure(figsize=(8, 5))  # Add this before first chart
orders_per_day.plot(kind='bar', color=colors)
plt.title('Orders per Day of the Week')
plt.xlabel('Day of Week')
plt.ylabel('Number of Orders')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(10, 5))  # New figure for second chart
orders_per_hour.plot(kind='bar', color='skyblue')
plt.title('Orders per Hour of Day')
plt.xlabel('Hour of Day (0 = Midnight)')
plt.ylabel('Number of Orders')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind='barh', color='green')  # Horizontal bar chart
plt.title('Top 10 Most Ordered Products')
plt.xlabel('Number of Orders')
plt.ylabel('Product Name')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

with pd.ExcelWriter("instacart_analysis_report.xlsx") as writer:
    orders_per_day.to_frame(name='orders_count').to_excel(writer, sheet_name='Orders by Day')
    orders_per_hour.to_frame(name='orders_count').to_excel(writer, sheet_name='Orders by Hour')
    top_products.to_frame(name='total_orders').to_excel(writer, sheet_name='Top Products')
    
print("Excel report saved successfully!")


