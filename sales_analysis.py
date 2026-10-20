import pandas as pd
import matplotlib.pyplot as plt

# 1. Create sample sales data
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard"],
    "Units_Sold": [10, 25, 15, 30, 20],
    "Price": [50000, 20000, 15000, 2000, 1500],
    "Cost_Per_Unit": [35000, 14000, 10000, 1200, 800]
}

df = pd.DataFrame(data)


# 2. Validate the data
def validate_data(df):
    if df.empty:
        raise ValueError("Sales data cannot be empty.")

    if df["Product"].isna().any():
        raise ValueError("Product names cannot be empty.")

    numeric_columns = [
        "Units_Sold", "Price", "Cost_Per_Unit"
    ]

    if df[numeric_columns].isna().any().any():
        raise ValueError("Numeric values cannot be empty.")

    if (df["Units_Sold"] < 0).any():
        raise ValueError("Units sold cannot be negative.")

    if (df[["Price", "Cost_Per_Unit"]] < 0).any().any():
        raise ValueError("Prices and costs cannot be negative.")

    print("Data validation successful!")


# 3. Calculate revenue, profit, and profit margin
def analyze_sales(df):
    df = df.copy()

    df["Revenue"] = df["Units_Sold"] * df["Price"]

    df["Profit"] = (
        df["Units_Sold"] *
        (df["Price"] - df["Cost_Per_Unit"])
    )

    df["Profit_Margin_%"] = 0.0

    nonzero_revenue = df["Revenue"] != 0

    df.loc[nonzero_revenue, "Profit_Margin_%"] = (
        df.loc[nonzero_revenue, "Profit"]
        / df.loc[nonzero_revenue, "Revenue"] * 100
    )

    return df


# 4. Classify product performance
def classify_profit(profit):
    if profit >= 100000:
        return "High Profit"
    elif profit >= 50000:
        return "Medium Profit"
    else:
        return "Low Profit"


# 5. Run the analysis
validate_data(df)
df = analyze_sales(df)

df["Profit_Category"] = df["Profit"].apply(classify_profit)

print("\nSALES DATA")
print(df)

total_units = df["Units_Sold"].sum()
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()
average_margin = df["Profit_Margin_%"].mean()

best_selling = df.loc[
    df["Units_Sold"].idxmax(), "Product"
]

highest_revenue = df.loc[
    df["Revenue"].idxmax(), "Product"
]

highest_profit = df.loc[
    df["Profit"].idxmax(), "Product"
]

print("\nPRODUCT PERFORMANCE")
print(df[["Product", "Profit", "Profit_Category"]])

print("\nSALES SUMMARY REPORT")
print("Total Products:", len(df))
print("Total Units Sold:", total_units)
print("Total Revenue: Rs.", total_revenue)
print("Total Profit: Rs.", total_profit)
print("Average Profit Margin:", round(average_margin, 2), "%")
print("Best-Selling Product:", best_selling)
print("Highest Revenue Product:", highest_revenue)
print("Highest Profit Product:", highest_profit)


# 6. Save analysis results
df.to_csv("sales_analysis_results.csv", index=False)

with open("sales_summary.txt", "w") as file:
    file.write("SALES SUMMARY REPORT\n")
    file.write("====================\n")
    file.write(f"Total Products: {len(df)}\n")
    file.write(f"Total Units Sold: {total_units}\n")
    file.write(f"Total Revenue: Rs. {total_revenue}\n")
    file.write(f"Total Profit: Rs. {total_profit}\n")
    file.write(f"Average Profit Margin: {average_margin:.2f}%\n")
    file.write(f"Best-Selling Product: {best_selling}\n")
    file.write(f"Highest Revenue Product: {highest_revenue}\n")
    file.write(f"Highest Profit Product: {highest_profit}\n")

print("\nAnalysis results saved successfully!")


# 7. Create and save the revenue chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()


# 8. Create and save the profit chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Profit"])
plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit (Rs.)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("profit_by_product.png")
plt.show()
