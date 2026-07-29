print("-------Function with One Parameter--------")

def greet(name):
    print("Hello,",name, "Welcom!")

greet("Mughal")
greet("Ahmad")    

print("\n-------Function with Two Parameters + If-Else--------")

def check_pass_fail(name,marks):
    if marks >= 50:
        print(name, "passed with", marks, "marks")
    else:
        print(f"{name} Failed with {marks}, marks")

check_pass_fail("Ahmad",79)
check_pass_fail("Faizan",49)


print("\n-------Function with a List Parameter + For Loop--------")

def show_all_items(items):
    for i in items:
        print("Items: ",i)
    print("Total items: ", len(items))  

fruits = ["apple", "banana", "cherry"]
show_all_items(fruits)  
fruits1 = ("Banana", "Orange", "Charry","Mango")
show_all_items(fruits1)
vegetables = ["potato", "onion"]
show_all_items(vegetables) 

print("\n-------Function with Parameter + While Loop--------")

def count_digit(number):
    temp = number
    count = 0

    while temp > 0:
        temp = temp // 10
        count +=1
    print(f"{number} has {count} Digits")   
count_digit(23456789)
count_digit(234576897654356789087654356789765467865436786455678964535678)
count_digit(0)
     
print("\n==========Multiple Parameters + Dictionary + Nested Logic (bigger revision)==========")

print("-------Function with Multiple Parameters + Dictionary--------")

def analyze_student(name, subjects, marks_list):     # three parameters
    marks_dict = {}                                     # revising: empty dictionary

    for i in range(len(subjects)):                        # revising: range() + indexing
        marks_dict[subjects[i]] = marks_list[i]             # revising: building a dictionary

    total = 0
    for subject, marks in marks_dict.items():               # revising: dictionary .items()
        total += marks
        if marks >= 80:                                       # revising: if-else
            print(f"{subject}: {marks} -> Excellent")
        elif marks >= 50:
            print(f"{subject}: {marks} -> Average")
        else:
            print(f"{subject}: {marks} -> Needs Improvement")

    average = total / len(subjects)                          # revising: average calculation
    print(f"{name}'s average: {average:.1f}\n")

analyze_student("Ali", ["Math", "Science", "English"], [85, 60, 45])
analyze_student("Sara", ["Math", "Science", "English"], [95, 88, 92])
