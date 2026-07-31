print("-------Basic Positional Arguments--------")

def show_profile(name, age, city):        # order of parameters: name, age, city
    print(f"Name: {name}, Age: {age}, City: {city}")

show_profile("Ali", 25, "Karachi")          # correct order -> correct result
show_profile("Sara", 30, "Lahore")           # correct order again -> correct result

# now let's see what happens with WRONG order
show_profile(25, "Ali", "Karachi")            # wrong order -> wrong result (no error, just messed up!)

print("-------Positional Arguments in Calculation--------")

def calculate_rectangle_area(length, width):      # position 1: length, position 2: width
    area = length * width                            # revising: multiplication
    print(f"Length={length}, Width={width}, Area={area}")

calculate_rectangle_area(10, 5)          # length=10, width=5 -> area=50
calculate_rectangle_area(5, 10)           # length=5, width=10 -> area=50 (same answer, different meaning!)

print("-------Positional Arguments where Order REALLY Matters--------")

def calculate_discount(original_price, discount_percent):    # position 1: price, position 2: discount%
    discounted = original_price - (original_price * discount_percent / 100)

    if discount_percent > 0:                                    # revising: if-else
        print(f"Price {original_price} with {discount_percent}% off = {discounted:.2f}")
    else:
        print(f"No discount applied, price stays {original_price}")

calculate_discount(1000, 20)     # correct: price=1000, discount=20% -> makes sense
calculate_discount(20, 1000)      # WRONG ORDER: price=20, discount=1000% -> nonsense result!


print("-------Positional Arguments with List Processing--------")

def filter_by_range(numbers, min_value, max_value):       # position 1,2,3 in this exact order
    result = []                                              # revising: empty list (basket)

    for num in numbers:                                        # revising: for loop over list
        if num >= min_value and num <= max_value:                # revising: logical 'and'
            result.append(num)

    print(f"Numbers between {min_value} and {max_value}: {result}")

data = [5, 12, 8, 25, 3, 18, 30, 7]

filter_by_range(data, 5, 20)         # positional: numbers=data, min=5, max=20
filter_by_range(data, 10, 30)         # different range, same order pattern


print("-------Positional Arguments in a Complete Function--------")

def process_order(item_name, quantity, price_per_unit, discount_percent):    # 4 positions, order fixed
    subtotal = quantity * price_per_unit                    # revising: multiplication
    discount_amount = subtotal * discount_percent / 100        # revising: percentage calculation
    final_amount = subtotal - discount_amount

    print(f"Item: {item_name}")
    print(f"Quantity: {quantity} x Price: {price_per_unit} = Subtotal: {subtotal}")
    print(f"Discount ({discount_percent}%): -{discount_amount:.2f}")
    print(f"Final Amount: {final_amount:.2f}\n")

# correct order every time: name, quantity, price, discount
process_order("Laptop", 2, 50000, 10)
process_order("Mouse", 5, 500, 5)
process_order("Keyboard", 1, 2000, 0)


