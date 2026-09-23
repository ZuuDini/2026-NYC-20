'''

# Assignment: 
# PA - Practice Activity - 386.6.1 - Analyzing Monthly Expenses

# Overview:
# You have been provided with data regarding your monthly expenses in various categories. 
Your task is to crate a bar chart to visualize the distribution of expenses across different categories. 

Sample Data:
Expense Categories: ['Groceries', 'Utilities', 'Transportation,' 'Dining Out,' and 'Entertainment'].
Amount Spent: [500, 300, 200, 400, and 250].

'''

import matplotlib.pyplot as plt

# Expense categories and the amount spent in each one
Expense_Categories = ['Groceries', 'Utilities', 'Transportation', 'Dining Out', 'Entertainment']
Amount_Spent = [500, 300, 200, 400, 250]
colors = ['Red', 'Blue', 'Green', 'Orange', 'Black']

# Draw a horizontal bar chart, one color per category
plt.barh(Expense_Categories, Amount_Spent, color=colors)

# Label the axes
plt.xlabel('Amount Spent')
plt.ylabel('Categories')

# Display the chart
plt.show()