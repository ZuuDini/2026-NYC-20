'''
Name: Zuberi Daley
# Assignment: SBA 386 - Data Analysis and Visualization with Python
# Overview: In this SBA you are expected to analyze and visualize the given data using Python, Pandas, Matplotlib, and other supporting libraries. 

''' 

import pandas as pd 
import matplotlib.pyplot as plt
# Section 1 
# Question 1 Read the csv
df_woocommerce = pd.read_csv('woocommerce-product-export.csv')

# Question 2 The make a concise summary 
print("\nSummary of WooCommerce")
print(df_woocommerce.info())

# Question 3 Show a summary of statistics pertaining to the columns
print("\nSummary statistics:")
print(df_woocommerce.describe())

#Question 4 Print the First 5 rows 
print("\nThe First 5 Rows")
print(df_woocommerce.head())


# Question 5 Print the Last 5 rows
print("\nThe Last 5 Rows")
print(df_woocommerce.tail())

# Question 6 print the total profit and month number Columns only
print("\nTotal Profit Columns Only")
print(df_woocommerce[['total_profit', 'month_number']])
'''
# Question 7 Read the total of all month and show it using a Bar chart
plt.bar(df_woocommerce['month_number'], df_woocommerce['total_profit'])
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Total Revenue by Month')
plt.show()


# Question 8 Read the total profit of all of the months in a line plot
plt.plot(df_woocommerce['month_number'], df_woocommerce['total_profit'],
         linestyle='dotted',
         color='red',
         linewidth=3,
         marker='o',
         markerfacecolor='black',
         label='Company Profit Per Month',)
plt.xlabel('Month Number')
plt.ylabel('Total Profit')
plt.title('Company Profit Per Month')
plt.legend(loc='lower right')
plt.show()


# Question 9 Print all of the product sales data and show it using a multi-line plot

plt.plot(df_woocommerce['month_number'], df_woocommerce['facecream'], marker='o', label='Facecream Sales Data')
plt.plot(df_woocommerce['month_number'], df_woocommerce['facewash'], marker='o', label='Facewash Sales Data')
plt.plot(df_woocommerce['month_number'], df_woocommerce['toothpaste'], marker='o', label='Toothpaste Sales Data')
plt.plot(df_woocommerce['month_number'], df_woocommerce['bathingsoap'], marker='o', label='BathingSoap Sales Data')
plt.plot(df_woocommerce['month_number'], df_woocommerce['shampoo'], marker='o', label='Shampoo Sales Data')
plt.plot(df_woocommerce['month_number'], df_woocommerce['moisturizer'], marker='o', label='Moisturizer Sales Data')
plt.xlabel('Month')
plt.xticks(df_woocommerce['month_number'])
plt.ylabel('Sales Units in number')
plt.title('Sales Data')
plt.legend(loc='upper left')
plt.show()

# Question 10 Read "bathingsoap" sales data for each month and show it using a scatter plot
plt.scatter(df_woocommerce['month_number'], df_woocommerce['bathingsoap'], label='Bathing soap Sales Data')
plt.xlabel('Month')
plt.xticks(df_woocommerce['month_number'])
plt.ylabel('Number of Units Sold')
plt.title('Bathingsoap Sales Data')
plt.legend(loc='upper left')
plt.grid(linestyle='--')       
plt.show()
'''


# Section Two 
# 1 Create a line chart of data
'''
Date = ['25/12', '26/12', '227/12']
Temp = [8.5, 10.5, 6.8]

plt.plot(Date, Temp)
plt.xlabel('Date')      
plt.ylabel('Temperature')
plt.title('Date-wise Temperature')
plt.show()
'''

# 2 Show the average weight against the average height
height = [121.9, 124.5, 129.5, 134.6, 139.7, 147.3, 152.4, 157.5, 162.6]
weight = [19.7, 21.3, 23.5, 25.9, 28.5, 32.1, 35.7, 39.6, 43.2]

plt.plot(weight, height,
         linestyle="-.",
         color="green",
         marker="o",
         markersize=10,
         markerfacecolor="green",
         label="Weight vs Height")

plt.xlabel("Weight in kg")
plt.ylabel("Height in cm")
plt.title("Average weight with respect to average height")
plt.legend(loc="lower right")
plt.show()

