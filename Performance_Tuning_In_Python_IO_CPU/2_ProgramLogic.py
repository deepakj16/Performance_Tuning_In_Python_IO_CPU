from Python_Classics import Pandas as pd
import time
data = pd.read_csv("D:\Python\DE_Path\Data\ecommerce5000.csv", encoding="Latin-1")
query=data.loc[0:4999,"query"]
print(query.size)
#print(query)

iz_operations = 0
# Initialize a list to store our duplicates
duplicates = []

start = time.time()
# Loop through each item in the query column.
for i, item in enumerate(query):
    duplicate = False
    # Loop through each item in the query column.
    for z, item2 in enumerate(query):
        # If the outer and inner loops are on the same value, keep going.
        # Without this, we'll falsely detect rows as duplicates.
        iz_operations += 1
        if i == z:
            continue
        # Mark as duplicate if we find a match.
        if item == item2:
            duplicate = True
    # Add to the duplicates list.
    if duplicate:
        duplicates.append(item)
print(iz_operations)
elapsed = time.time() - start
print(elapsed)

counts_increments = 0
value_checks = 0
start = time.time()
counts = {}
for item in query:
    if item not in counts:
        counts[item] = 0
    counts_increments += 1
    counts[item] += 1

duplicates = []
for key, val in counts.items():
    value_checks += 1
    if val > 1:
        duplicates.append(key)

print(counts_increments)
print(value_checks)
elapsed = time.time() - start
print(elapsed)

start = time.time()
duplicate_series = query.duplicated()
#duplicate_values_series = query[duplicate_series]
pandas_elapsed = time.time() - start
print(pandas_elapsed)