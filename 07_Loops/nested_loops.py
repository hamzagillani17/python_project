print("\n=========Nested Loops: Multiplication Table=========")
'''Nested loops are loops inside another loop.
The inner loop completes all its iterations for each iteration of the outer loop.
'''
print("\n=============Nested for Loop Example============")


print("----------Basic Nested Loop Example----------")

months = ["jan", "feb", "mar"]
days = ["sun", "mon", "tue"]

for x in months:
  for y in days:
    print(x, y)

print("Good bye!")

print("\n-------Multiplication Table--------")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()   # move to next line after each row of multiplication table

print("-------Mid: Star Pyramid--------")

rows = 5

for i in range(1, rows + 1):           # outer loop: controls row number
    for space in range(rows - i):        # inner loop 1: print leading spaces
        print(" ", end="")
    for star in range(2 * i - 1):         # inner loop 2: print stars (odd count each row)
        print("*", end="")
    print()                                # move to next line after row is done    

print("-------Advanced: Find Pairs with Target Sum--------")

numbers = [2, 4, 6, 8, 10, 3, 7]
target_sum = 10
pairs_found = []

for i in range(len(numbers)):                      # outer loop: pick first number
    for j in range(i + 1, len(numbers)):              # inner loop: pick second number (AFTER i, avoid repeats)
        if numbers[i] + numbers[j] == target_sum:
            pairs_found.append((numbers[i], numbers[j]))   # store as a tuple

print("Pairs with sum", target_sum, ":", pairs_found)


print("\n-------Advanced: Find Pairs with Target Sum (Unique)--------")

numbers = [2, 4, 6, 8, 10, 3, 7]
target_sum = 10
pairs_found = []

for i in range(len(numbers)):                      # outer loop: pick first number
    for j in range(i + 1, len(numbers)):              # inner loop: pick second number (AFTER i, avoid repeats)
        if numbers[i] + numbers[j] == target_sum:
            pairs_found.append((numbers[i], numbers[j]))   # store as a tuple

# Remove duplicate pairs (if any)
unique_pairs = list(set(pairs_found))

print("Unique pairs with sum", target_sum, ":", unique_pairs)


print("\n-------Advanced: Find Pairs with Target Sum (Unique) using Set--------")
numbers = [2, 4, 6, 8, 10, 3, 7]
target_sum = 10
unique_pairs = set()

for i in range(len(numbers)):                      # outer loop: pick first number
    for j in range(i + 1, len(numbers)):              # inner loop: pick second number (AFTER i, avoid repeats)
        if numbers[i] + numbers[j] == target_sum:
            unique_pairs.add((numbers[i], numbers[j]))   # store as a tuple

print("Unique pairs with sum", target_sum, ":", unique_pairs)


print("\n=========while Loop with Nested Loops=========")

print("\n-------Nested while Loop Example--------")
i = 0
while i < 5:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1

print("\n-------Basic: Grid Print using While--------")

i = 1
while i <= 3:                    # outer while loop: rows
    j = 1
    while j <= 3:                  # inner while loop: columns — needs its OWN counter
        print(f"({i},{j})", end=" ")
        j += 1
    print()                         # new line after each row
    i += 1

print("\n-------Mid: Number Triangle using While--------")

rows = 5
i = 1

while i <= rows:                  # outer loop: row number
    j = 1
    while j <= i:                   # inner loop: goes up to current row number
        print(j, end=" ")
        j += 1
    print()
    i += 1

print("\n-------Advanced: Find Prime Numbers using Nested While--------")

start = 2
end = 20
prime_numbers = []

num = start
while num <= end:                        # outer loop: check each number from start to end
    is_prime = True
    divisor = 2

    while divisor < num:                    # inner loop: check if 'num' is divisible by anything
        if num % divisor == 0:
            is_prime = False
            break                             # no need to check further, already proven not prime
        divisor += 1

    if is_prime:
        prime_numbers.append(num)

    num += 1

print("Prime numbers between", start, "and", end, ":", prime_numbers)


print("\n-------Advanced: Find Pairs with Target Sum using Nested While--------")
numbers = [2, 4, 6, 8, 10, 3, 7]
target_sum = 10
pairs_found = []

i = 0
while i < len(numbers):                      # outer loop: pick first number
    j = i + 1
    while j < len(numbers):              # inner loop: pick second number (AFTER i, avoid repeats)
        if numbers[i] + numbers[j] == target_sum:
            pairs_found.append((numbers[i], numbers[j]))   # store as a tuple
        j += 1
    i += 1

print("Pairs with sum", target_sum, ":", pairs_found)

print("\n-------Advanced: Find Unique Pairs with Target Sum using Nested While--------")
numbers = [2, 4, 6, 8, 10, 3, 7]
target_sum = 10
pairs_found = set()  # use a set to automatically handle uniqueness

i = 0
while i < len(numbers):                      # outer loop: pick first number
    j = i + 1
    while j < len(numbers):              # inner loop: pick second number (AFTER i, avoid repeats)
        if numbers[i] + numbers[j] == target_sum:
            pairs_found.add((numbers[i], numbers[j]))   # store as a tuple in set
        j += 1
    i += 1