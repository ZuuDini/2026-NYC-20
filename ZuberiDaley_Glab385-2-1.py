# Zuberi Daley
# Guided Lab 385.2.1 - Working with Lists and Functions in Python
# Example 1: List Manipulation


# --- 1. Defining a List ---
# Creating a list of tools
thingsAroundMyHouse = ["Keyboard", "Pen", "GamingPC", "Bed", "Laptop", "Monitor", "Tablet"]
print("1.1 - Defining a List: " + str(thingsAroundMyHouse))        # Output: ['Keyboard', 'Pen', 'Ruler', 'Mouse', 'Laptop', 'Monitor', 'Tablet']


# --- 2. Indexing and Slicing ---
# 2a Accessing elements by position (0-based)
print("2a.1 - Indexing and Slicing: " + thingsAroundMyHouse[2])     # Output: Gaming PC
print("2a.2 - Indexing and Slicing: " + thingsAroundMyHouse[-1])    # Output: Tablet (Last item)

# 2b Slicing: [Start : Stop] - Note: Stop index is exclusive
at_home = thingsAroundMyHouse[1:3]
print("2b.1 - Indexing and Slicing: " + str(at_home))     # Output: ['Pen', 'Bed']


# --- 3. Modifying Elements ---
# Changing a value at a specific index
thingsAroundMyHouse[2] = "Webcam"
print("3.1 - Modifying Elements: " + str(thingsAroundMyHouse))        # Output: ["Keyboard", "Pen", "Webcam", "Bed", "Laptop", "Monitor", "Tablet"]


# --- 4. Adding Elements ---
# Use append() to add to the end of the list
thingsAroundMyHouse.append("Black Boots")

# Use insert() to add at a specific index
thingsAroundMyHouse.insert(1, "Headphones")
print("4.1 - Adding Elements: " + str(thingsAroundMyHouse))        # Output: ["Keyboard", "HeadPhones", "Webcam", "Bed", "Laptop", "Monitor", "Tablet"]


# --- 5. Removing Elements ---
# Use remove() to delete a specific value by name
thingsAroundMyHouse.remove("Monitor")
print("5.1 - Removing Elements: " + str(thingsAroundMyHouse))        # Output: ['Keyboard', 'Headphones', 'Pen', 'Webcam', 'Mouse', 'Laptop', 'Tablet', 'Desk']


# --- 6. Checking Length ---
# Using the len() function to see total count
total_items = len(thingsAroundMyHouse)
print("6.1 - Checking Length: " + str(total_items))  # Output: 8

'''
Example 2: Using .reverse() and .extent() methods
Python List Methods Overview: .reverse() and .extend()
'''

def record_profit_years(recent_first, recent_last):
    # Reverse the order of the "recent_first" list so that it is in chronological order.
    recent_first.reverse()

    #Extend the "Recent_last" list by appending the newly reversed "recent_first" list.
    recent_last.extend(recent_first)

    # Return the "recent_last", Which now contains the two lists combined in chronologhical order.
    return recent_last

recent_first = [2022, 2018, 2011, 2006]
recent_last = [1989,1992, 1997, 2001]

#call the record_profit_years() funtion anc pass the two lists as parameters
print(record_profit_years(recent_first, recent_last))
