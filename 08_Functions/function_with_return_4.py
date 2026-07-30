print("\n-------Simple Function with Return--------")

def add_number(a,b):
    return a + b

result = add_number(10,20)
print(result)

print(add_number(50,40))

print("\n-------Return with If-Else--------")

def check_even_odd(number):
    if number %2 ==0:
        return "Even"
    else:
        return "odd"


result1 = check_even_odd(51)
result2 = check_even_odd(30)  
print(check_even_odd(10))

print(result1)
print(result2)

if check_even_odd(15) == "odd":
    print("15 is confirmed odd")
    
print("\n-------Return a List--------")

def get_even_numbers(limit):            # parameter: upper limit to check up to
    even_list = []                        # revising: empty list (basket pattern)

    for num in range(1, limit + 1):          # revising: for loop with range()
        if num % 2 == 0:                       # revising: modulus check
            even_list.append(num)                # revising: .append()

    return even_list                          # returning the ENTIRE list, not just printing it

evens_upto_20 = get_even_numbers(20)          # storing the returned list in a variable
print("Even numbers up to 20:", evens_upto_20)

evens_upto_10 = get_even_numbers(10)           # reusing function, different limit
print("Even numbers up to 10:", evens_upto_10)

print("Total evens found (up to 20):", len(evens_upto_20))   # using the returned list further
    
print("\n-------Return Multiple Values--------")

def get_min_max_avg(numbers):            # parameter: a list of numbers
    smallest = float('inf')                 # revising: starting point for finding minimum
    largest = float('-inf')                  # revising: starting point for finding maximum
    total = 0

    for num in numbers:                       # revising: for loop with comparisons
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
        total += num

    average = total / len(numbers)             # revising: average calculation

    return smallest, largest, average             # returning THREE values as a tuple

scores = [45, 78, 92, 60, 88, 30]

low, high, avg = get_min_max_avg(scores)          # revising: tuple unpacking

print("Lowest score:", low)
print("Highest score:", high)
print(f"Average score: {avg:.2f}")

print("\n-------Return a Dictionary with Full Analysis--------")

def analyze_text(text):                  # parameter: a sentence/string to analyze
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    space_count = 0

    for ch in text:                          # revising: for loop over a string
        if ch == " ":                          # revising: if-elif-else
            space_count += 1
        elif ch.lower() in vowels:               # revising: .lower() + 'in' operator
            vowel_count += 1
        elif ch.isalpha():                        # revising: isalpha()
            consonant_count += 1

    result = {                                  # revising: building a dictionary
        "vowels": vowel_count,
        "consonants": consonant_count,
        "spaces": space_count,
        "total_length": len(text)
    }

    return result                                 # returning the entire dictionary

analysis = analyze_text("hello world from python")

print("Vowels:", analysis["vowels"])
print("Consonants:", analysis["consonants"])
print("Spaces:", analysis["spaces"])
print("Total length:", analysis["total_length"])
