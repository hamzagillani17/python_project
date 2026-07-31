def show_info(**kwargs):     # kwargs collects name=value pairs into a dictionary
    print(kwargs)

show_info(name="Ali", age=25)    # kwargs = {'name': 'Ali', 'age': 25}


print("-------Basic **kwargs--------")

def show_info(**kwargs):          # collects any name=value pairs into a dictionary
    print(kwargs)

show_info(name="Ali", age=25, city="Karachi")
show_info(fruit="mango", price=100)


print("-------Loop through **kwargs--------")

def show_profile(**kwargs):
    for key, value in kwargs.items():     # revising: dictionary .items()
        print(f"{key}: {value}")

show_profile(name="Sara", age=30, city="Lahore")


print("-------**kwargs with Return--------")

def build_profile(**kwargs):
    return kwargs                # return the dictionary as it is

profile = build_profile(name="Ahmed", age=22, city="Islamabad")

print(profile)
print("Name:", profile["name"])



def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)



def addr(**kwargs):
   for k,v in kwargs.items():
      print ("{}:{}".format(k,v))

print ("pass two keyword args")
addr(Name="John", City="Mumbai")
print ("pass four keyword args")

# pass four keyword args
addr(Name="Raam", City="Mumbai", ph_no="9123134567", PIN="400001")



