def add_all(*args):        # *args collects ANY number of values into a tuple
    print(args)

add_all(1, 2)                # args = (1, 2)
add_all(1, 2, 3, 4, 5)         # args = (1, 2, 3, 4, 5)
add_all()                     # args = () — empty tuple, bhi chalega

print("-------Basic *args--------")

def show_all_values(*args):        # accepts ANY number of arguments
    print("Values received:", args)
    print("Type of args:", type(args))       # confirming it's a tuple

show_all_values(1, 2, 3)
show_all_values("apple", "banana")
show_all_values(10)
show_all_values()                    # even zero arguments work fine


print("-------Sum Using *args--------")

def add_all(*args):                  # can accept 2, 5, 10, or any number of values
    total = 0
    for num in args:                    # revising: for loop over a tuple
        total += num
    return total                          # revising: return statement

print("Sum of 2 numbers:", add_all(5, 10))
print("Sum of 4 numbers:", add_all(1, 2, 3, 4))
print("Sum of 6 numbers:", add_all(10, 20, 30, 40, 50, 60))

print("-------Find Max and Min using *args--------")

def find_max_min(*args):
    if len(args) == 0:                        # revising: if-else, len() check
        print("No numbers provided")
        return

    largest = args[0]                            # revising: tuple indexing
    smallest = args[0]

    for num in args:                                # revising: for loop, comparison
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    print(f"Numbers: {args} -> Max: {largest}, Min: {smallest}")

find_max_min(5, 12, 3, 45, 8)
find_max_min(100)
find_max_min()


print("-------Find Largest using *args with Return--------")

def find_largest(*args):
    largest = args[0]                # start with the first value

    for num in args:                    # loop through all values
        if num > largest:
            largest = num

    return largest                        # return the largest number found

biggest1 = find_largest(4, 19, 7, 25, 3)
biggest2 = find_largest(100, 50)

print("Largest 1:", biggest1)
print("Largest 2:", biggest2)






