# 1. What surprised me most was that slicing stops before the end index, so inventory[:3] gave me indices 0, 1, and 2 instead of 1 through 3. I also didn’t expect list methods like .append(), .remove(), and .sort() to change the original list directly instead of returning a new one.
# 2. If a small business wanted to know which sales were over $300 and their average, Excel would mean filtering, copying the results, and writing a separate formula every time new sales came in. In Exercise 8, a loop with an if amount > 300 check built a high_sales list, and len() and sum() gave the count and average instantly for 10 sales or 10,000.

print("--- Exercise 1: Build a List ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: Index Practice ---")
print(inventory[0]) # always grabs the first item in a list
print(inventory[-1]) # always grabs the last item in a list

middle = len(inventory) // 2
print(inventory[middle])

print("--- Exercise 3: List Slicing ---")

print(inventory[:3]) # grabs the first three items (indices 0, 1, and 2)
print(inventory[-2:]) # grabs the last two items
print(inventory[::2]) # grabs every other item in the list

print("--- Exercise 4: List Methods ---")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")

print(coords)

print("--- Exercise 6: List Average Sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print (f"Total sales:{total}")
print (f"Number of sales: {count}")
print (f"Average sale: {average}")
print (f"Best sale:{max(sales)}")
print (f"Worst sale:{min(sales)}")

best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print (f"Best sale (loop):{best}")
print (f"Worst sale (loop):{worst}")

print("--- Exercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"Count: {len(high_sales)}")
print (f"Average: {sum(high_sales)/len(high_sales):.2f}")