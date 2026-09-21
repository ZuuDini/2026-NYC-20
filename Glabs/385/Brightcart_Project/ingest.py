import os, sys
# what is args?  Its means something related to system/command line arguments 
args = sys.argv[1:] #everything after the script name
date = args[0] if args else input("Date (YYYY-MM-DD): ")

path = os.path.join("raw", f"orders_NY_{date}.csv")
status = "FOUND" if os.path.exists(path) else "MISSING  "

print(f"{'NY':<5}{path:<}{status:>8}") # <5 left-pad to 5, >8 right-pad to 8

