# Zuberi Daley
# PRACTICE ACTIVITY 385.2.1 - List Excercises- Basic

# Initial Guest List

guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
print("Initial list:", guests) 

# 1. Add Frank to the end
guests.append("Frank")
print("Q1: " + str(guests))

# 2. Add Grace to the front 
guests.insert(0,"Grace")
print("Q2: " + str(guests))

# 3. Replace Charlie With Chuck
guests[3] = "Chuck"
print("Q3: " + str(guests))

# 4 Remove the person at index 3 (Check the list after previous steps!)
guests.remove("Chuck")
print("Q4: " + str(guests))

# 5. Print final results
print ("Q5: " + str(guests))