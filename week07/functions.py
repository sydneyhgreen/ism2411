# 1. The first bug I spotted in Exercise 5 was the missing colon on the second for loop, which I found from the traceback's SyntaxError, so my current debugging instincts are to read the error message first and then use print() statements to check my logic.
# 2. apply_discount(price, tier) takes a price and a tier string ("gold", "silver", "bronze", or anything else) and returns the price after a 15%, 10%, 5%, or 0% discount, so a colleague could use it without reading the body.
# 3. AI disclosure: I used Google to help understand some certain parts and what to do because I had a little trouble, so the AI tool inside of Google built my understanding. I'm guessing that probably counts, and if it's an issue, please let me know so I can improve someway!

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

print(f"Tax on $100 at 7%: ${calculate_tax(100, 0.07):.2f}")
print(f"Tax on $250 at 8%: ${calculate_tax(250, 0.08):.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * (1 - 0.15)
    elif tier == "silver":
        return price * (1 - 0.10)
    elif tier == "bronze":
        return price * (1 - 0.05)
    else:
        return price

print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---
discounted = apply_discount(200, "gold")
with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${with_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    return discounted_price + calculate_tax(discounted_price, tax_rate)

print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
# Bug 1 (syntax): the second for loop was missing a colon after "in sales".
# Fix: add the colon so Python can parse the loop.
# Bug 2 (logic): "total = sale" replaced the total each time instead of adding to it, so it only kept the last sale.
# Fix: use "total += sale" so each sale is added to the running total.
# Bug 3 (off-by-one): "while i <= len(sales)" ran one time too many, and sales[5] doesn't exist, which causes an IndexError.
# Fix: use "i < len(sales)" so the last index used is 4.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---
# Scope: a variable created inside a function is local and only exists while that function runs, so the x = 999 inside double_it() is a different variable from the global x = 100 and never changes it.

x = 100  # global variable

def double_it():
    x = 999  # local variable, different from global x
    return x * 2

print(x)            # prints 100
print(double_it())  # prints 1998
print(x)            # prints 100, global x did not change