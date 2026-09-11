# Zuberi Daley 
# Practice Activity 385.2.3 Dictionary Exercises Basic

'''
Problem 1 

Use the following states and capitals to create dictionary objects:
- Los angeles california
- albany, new york 
- Honolulu, Hawaii
- Juneau, Alaska
- Austin, Taxas
Task 
- Create a dictionary object using curly brace {} notation, where the states are the keys and the capitals are the values. 
- Create a **dictionary object** using the built-in dict() function**, where the **states are the keys** and the **capitals are the values**.
- Use the **`type()`** function to check the **data type** of each dictionary.
- Print each dictionary to display all **key-value pairs**.
'''
'''
# Problem 1 - Creating dictionaries of states and capitals

# Dictionary created with curly brace {} notation
capitals = {
    'California': 'Los Angeles',
    'New York': 'Albany',
    'Hawaii': 'Honolulu',
    'Alaska': 'Juneau',
    'Texas': 'Austin'
}

# Same dictionary created with the built-in dict() function and a list of tuples
capitals_dict = dict([
    ('California', 'Los Angeles'),
    ('New York', 'Albany'),
    ('Hawaii', 'Honolulu'),
    ('Alaska', 'Juneau'),
    ('Texas', 'Austin')
])

# Check the data type of each dictionary
print(type(capitals))
print(type(capitals_dict))

# Print each dictionary to display all key-value pairs
print(capitals)
print(capitals_dict)
'''
'''
Use one of the **dictionary objects** created in **Problem 1** to complete the following tasks:

---

### **Tasks**

- Retrieve the **value** associated with the key **"California"**.
- Add a new **key-value pair** for **Florida** and its capital to the dictionary.
- Update the value for **"California"** to **"Sacramento"**.
- Remove the key-value pair for **"Alaska"** from the dictionary.
'''
'''
# Problem 2

print(f'The capital of California is {capitals['California']}')

# add a new key-value pair for Florida and its capital
capitals['Florida'] = 'Tallahassee'
print("After adding Florida:")
print(capitals)

# Updae the value for "California" to "Sacramento"
capitals['California'] = 'Sacramento'
print("After updating California:")
print(capitals)

del capitals['Alaska']
print("After removing Alaska:")
print(capitals) 
'''

'''
# Problem 3
#  **Tasks**

- Create a dictionary object called **`playlist`** with **at least 6 key-value pairs**:
  - Each **key** should be an **artist name**.
  - Each **value** should be a **song by that artist**.

- Use a **for loop** to print all the **artist names** in the playlist.

- Use a **for loop** to print all the **song titles** in the playlist.

- Use a **for loop** to print the following statement for each entry:  
  **"(Song Name) by (Artist) is in the current playlist."**

- Remove the **last key-value pair** from the dictionary.

- Add the song **"Anti-Hero" by Taylor Swift** to the playlist.

- Update one of the songs so that the title begins with **"REMIX"**.

- Define and call a **function** that accepts a dictionary as a parameter and prints all **artists and songs** from it.
'''
playlist = {
    "lil Durk": "Hats Off (Feat. Travis Scott)",
    "Meek Mill": "Dreams and Nightmares",
    "Kanye West": "Stronger",
    "Jay-Z": "Empire State Of Mind",
    "King Von": "Crazy Story, Pt.3",
    "Bad Bunny": "DtMF"
}
for playlist in playlist:
    print(playlist)

