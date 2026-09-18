"""Generate messy BrightCart raw exports for a given date. Usage: python make_raw_data.py YYYY-MM-DD"""
import csv, os, random, sys
from datetime import datetime, timedelta

date = sys.argv[1] if len(sys.argv) > 1 else "2026-09-15"
random.seed(date)  # same date → same data, so reruns are reproducible
os.makedirs("raw", exist_ok=True)

PRODUCTS = [  # (name, category, price)
    ("Wireless Mouse", "Electronics", 24.99), ("USB-C Hub", "Electronics", 39.50),
    ("Desk Lamp", "Home", 31.00), ("Ceramic Mug", "Home", 12.75),
    ("Running Shoes", "Apparel", 89.00), ("Rain Jacket", "Apparel", 74.25),
    ("Yoga Mat", "Fitness", 28.00), ("Resistance Bands", "Fitness", 15.99),
]
HUBS = ["NY", "CHI", "LA"]
messy = lambda s: random.choice([s, s.upper(), s.lower(), f"  {s} ", s.replace(" ", "_")])

with open(os.path.join("raw", "products.txt"), "w") as f:
    for name, cat, price in PRODUCTS:
        f.write(f"{messy(name)}|{messy(cat)}|{random.choice([f'${price}', str(price)])}\n")

order_id = 10000
for hub in HUBS:
    rows = []
    for _ in range(random.randint(25, 40)):
        name, cat, price = random.choice(PRODUCTS)
        ordered = datetime.strptime(date, "%Y-%m-%d") + timedelta(
            hours=random.randint(8, 20), minutes=random.randint(0, 59))
        promised = ordered + timedelta(hours=48)
        delivered = ordered + timedelta(hours=random.choice([30, 40, 47, 50, 55, 70]))
        delivered_str = "" if random.random() < 0.15 else delivered.strftime("%Y-%m-%d %H:%M")
        rows.append([order_id, f"user{random.randint(1, 60)}@example.com", messy(name),
                     messy(cat), random.randint(1, 4), random.choice([f"${price}", str(price)]),
                     ordered.strftime("%Y-%m-%d %H:%M"), promised.strftime("%Y-%m-%d %H:%M"),
                     delivered_str, hub])
        order_id += 1
    with open(os.path.join("raw", f"orders_{hub}_{date}.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["order_id", "customer_email", "product", "category", "qty",
                    "unit_price", "ordered_at_local", "promised_by_local",
                    "delivered_at_local", "hub"])
        w.writerows(rows)
    print(f"wrote raw/orders_{hub}_{date}.csv ({len(rows)} rows)")