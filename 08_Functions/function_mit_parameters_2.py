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



