import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Data reading, cleaning and primary preparation
pd.read_excel('Sales Data.xlsx')
df= pd.read_excel("Sales Data.xlsx")
print(df)
#Task solving
products = df["Product"].unique()
product_quantities = df[["Product", "Quantity Ordered"]].groupby("Product").sum()
product_quantities.head()
print(product_quantities)
#sort in ascending order
product_quantities = product_quantities["Quantity Ordered"].sort_values(ascending=False)
product_quantities.head()
print(product_quantities)
#lets see five most sold products.
my_Idea = { product : product_quantities[product]/df[df["Product"]==product]["Price Each"].mean() for product in products }
my_Idea = pd.Series(my_Idea).sort_values(ascending=False)
my_Idea.head()
print(my_Idea)
#lets see what item was sold the most in each city
cities = df["City"].unique()
print(cities)
product_sells_per_sity = {
    city : df[df["City"] == city][["Product", "Quantity Ordered"]].groupby("Product").sum()["Quantity Ordered"].sort_values(ascending=False) for city in cities
}
for city, products in product_sells_per_sity.items():
    print(city)
    print(products.head(), end="\n\n")
#graph showing which city sold the most product  
keys = list(df['City'].unique())

plt.bar(keys, df.groupby('City')['Sales'].sum())
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()

#What product sold the most? Why do you think it sold the most?
product_group = df.groupby('Product')
quantity_ordered = product_group['Quantity Ordered'].sum()
keys = list(product_group.groups.keys())
plt.bar(keys, quantity_ordered)
plt.xticks(keys, rotation='vertical', size=8)
plt.show()
#which month sold best?
results = df.groupby('Month').sum()
months=range(1,13)
plt.bar(months,results['Sales'])
plt.xticks(months)
plt.xlabel("Month number")
plt.ylabel("Sales in USD ($)")
plt.show()
#show the most sold hour
# Step 1: 
results = df.groupby('Hour')['Sales'].sum()

# Step 2: Create separate lists for 'Hour' and 'Sales' data
hours = results.index.tolist()
sales_data = results.tolist()

# Step 3: Plot the bar chart using the lists and make the bars red
plt.bar(hours, sales_data, color='red')
plt.xlabel("Hour")
plt.ylabel("Sales in USD ($)")
plt.title("Total Sales for Each Hour")
plt.show()
#This shows that the sales are high between 8 am to 11 pm and would the appropriate time to play ads
#Peak Hours 
popular_hour=df.groupby(["Month","Hour"])
popular_hour = pd.DataFrame(popular_hour["Sales"].sum(), columns=["Sales"])
popular_hour = popular_hour.reset_index()
print(popular_hour)

popular_hour_month = popular_hour.loc[popular_hour["Month"] == 10]

# Create the bar chart using plt.bar()
plt.bar(popular_hour_month['Hour'], popular_hour_month['Sales'])

# Set labels and title
plt.xlabel('Hour')
plt.ylabel('Sales')
plt.title('Peak Hours for Sales in October')

# Show the chart
plt.show()
# Create the scatter plot using plt.scatter()
plt.scatter(popular_hour_month["Hour"], popular_hour_month["Sales"])

# Set labels and title
plt.xlabel('Hour')
plt.ylabel('Sales')
plt.title('Peak Hours for Sales in October')

# Display the chart
plt.show()
#total sales in each city
Area_value=df.groupby(["City"])
Area_value = Area_value["Sales"].sum().reset_index()
print(Area_value)
# Create the scatter plot using plt.scatter()
plt.scatter(Area_value['City'], Area_value['Sales'])

# Set labels and title
plt.xlabel('City')
plt.ylabel('Sales')
plt.title('Cities and Sales')

# Display the plot
plt.show()
#ordderdate to datetime
df['Year'] = pd.to_datetime(df['Order Date']).dt.year
df['Order Date'] = pd.to_datetime(df['Order Date'])
#print(df.head)
#Monthly sales - weekly and AOV
month_df = df.groupby(["Year","Month"])
monthly_sales=pd.DataFrame(month_df["Sales"].sum(), columns=["Sales"])
avg_order_month = month_df["Sales"].mean()
avg_order_month = avg_order_month.reset_index()
monthly_sales = monthly_sales.reset_index()
monthly_sales = monthly_sales.loc[monthly_sales["Year"]==2019]
monthly_sales["AOV"] = avg_order_month["Sales"]
print(monthly_sales)


# Create the bar chart using plt.bar()
plt.bar(monthly_sales['Month'], monthly_sales['Sales'])
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Bar Chart with Month and Sales')

# Create the scatter plot using plt.plot()
plt.plot(monthly_sales['Month'], monthly_sales['AOV'], label='Average Order Value')
plt.xlabel('Month')
plt.ylabel('Average Order Value')

# Display the plot
plt.legend()
plt.show()