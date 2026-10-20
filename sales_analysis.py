import pandas as pd
import matplotlib.pyplot as plt

# Create sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500]
}

df = pd.DataFrame(data)

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Price"]

# Calculate cost per unit
df["Cost_Per_Unit"] = [35000, 14000, 10000, 1200, 800]

# Calculate profit
df["Profit"] = df["Units_Sold"] * (
    df["Price"] - df["Cost_Per_Unit"]
)

# Display sales data
print("SALES DATA")
print(df)

# Display profit by product
print("\nProfit by Product:")
print(df[["Product", "Revenue", "Profit"]])

# Calculate total revenue
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Calculate total profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Find the best-selling product
best_selling = df.loc[df["Units_Sold"].idxmax(), "Product"]
print("Best-Selling Product:", best_selling)

# Find the product with the highest revenue
top_revenue = df.loc[df["Revenue"].idxmax(), "Product"]
print("Highest Revenue Product:", top_revenue)

# Create a revenue chart
plt.figure()
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# Create a profit chart
plt.figure()
plt.bar(df["Product"], df["Profit"])
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit (₹)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("profit_by_product.png")
plt.show()

# Calculate profit margin percentage
df["Profit_Margin_%"] = (
    df["Profit"] / df["Revenue"]
) * 100

print("\nProfit Margin by Product:")
print(df[["Product", "Profit_Margin_%"]].round(2))

# Find the product with the highest profit margin
top_margin = df.loc[
    df["Profit_Margin_%"].idxmax(), "Product"
]
print("\nHighest Profit Margin Product:", top_margin)

# Classify products based on profit
def classify_profit(profit):
    if profit >= 100000:
        return "High Profit"
    elif profit >= 50000:
        return "Medium Profit"
    else:
        return "Low Profit"

df["Profit_Category"] = df["Profit"].apply(classify_profit)

print("\nProduct Performance Summary:")
print(df[["Product", "Profit", "Profit_Category"]])

# Calculate summary values
total_units = df["Units_Sold"].sum()
average_profit_margin = df["Profit_Margin_%"].mean()

# Find the product with the highest profit
highest_profit = df.loc[df["Profit"].idxmax(), "Product"]

# Save analysis results to a CSV file
df.to_csv("sales_analysis_results.csv", index=False)

print("\nAnalysis results saved successfully!")
print("File: sales_analysis_results.csv")

# Save the sales summary as a text file
with open("sales_summary.txt", "w") as file:
    file.write("SALES SUMMARY REPORT\n")
    file.write("====================\n")
    file.write(f"Total Products: {len(df)}\n")
    file.write(f"Total Units Sold: {total_units}\n")
    file.write(f"Total Revenue: Rs. {total_revenue}\n")
    file.write(f"Total Profit: Rs. {total_profit}\n")
    file.write(
        f"Average Profit Margin: "
        f"{average_profit_margin:.2f}%\n"
    )
    file.write(f"Best-Selling Product: {best_selling}\n")
    file.write(f"Highest Revenue Product: {top_revenue}\n")
    file.write(f"Highest Profit Product: {highest_profit}\n")
    file.write(f"Highest Profit Margin Product: {top_margin}\n")

print("\nSales summary saved to sales_summary.txt")
print("\nAll sales analysis tasks completed successfully!")
