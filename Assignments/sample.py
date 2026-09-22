
# 1. Raw product descriptions needing cleanup
raw_descriptions = [
    "  PERFECT_PYTHON_GUIDE  ",
    "DATA_ANALYTICS_HANDBOOK ",
    "  MYSQL_DATABASE_MASTERY"
]

# 2. Cleaning raw strings using string methods (.strip(), .replace(), .title())
cleaned_product_names = []
for desc in raw_descriptions:
    # Remove leading/trailing whitespace and format as title case
    clean_name = desc.strip().replace("_", " ").title()
    cleaned_product_names.append(clean_name)

# 3. Using a dictionary with nested attributes (price, stock, category)
product_catalog = {
    "Perfect Python Guide": {
        "price": 29.99,
        "stock": 150,
        "category": "Books"
    },
    "Data Analytics Handbook": {
        "price": 45.00,
        "stock": 85,
        "category": "Books"
    },
    "Mysql Database Mastery": {
        "price": 39.95,
        "stock": 0,
        "category": "Books"
    }
}

# 4. Iterating through the ordered list of product names and retrieving details safely
print("=== E-COMMERCE PRODUCT CATALOG ===")
for name in cleaned_product_names:
    # Use .get() to retrieve details safely without raising a KeyError
    details = product_catalog.get(name, {})
    
    price = details.get("price", 0.00)
    stock = details.get("stock", 0)
    category = details.get("category", "Uncategorized")
    
    # Neatly formatted catalog display in the console
    print(f"Product:  {name}")
    print(f"Category: {category}")
    print(f"Price:    ${price:.2f}")
    print(f"Stock:    {stock} units available")
    print("-" * 35)
