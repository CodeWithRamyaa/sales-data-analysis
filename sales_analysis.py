import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500]
}

df = pd.DataFrame(data)
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500]
}

df = pd.DataFrame(data)

# NEW CODE: Calculate profit
df["Cost_Per_Unit"] = [35000, 14000, 10000, 1200, 800]

df["Profit"] = (
    df["Units_Sold"] *
    (df["Price"] - df["Cost_Per_Unit"])
)

# Original code continues here
print("SALES DATA")
print(df)

print("\nProfit by Product:")
print(df[["Product", "Revenue", "Profit"]])

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Display the dataset
print("SALES DATA")
print(df)

# Calculate total revenue
print("\nTotal Revenue:", df["Revenue"].sum())

# Find the best-selling product
best_selling = df.loc[df["Units_Sold"].idxmax(), "Product"]
print("Best-Selling Product:", best_selling)

# Find the product with the highest revenue
top_revenue = df.loc[df["Revenue"].idxmax(), "Product"]
print("Highest Revenue Product:", top_revenue)

# Create a revenue chart
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
