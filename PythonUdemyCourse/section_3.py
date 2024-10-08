# Assignment-1
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""
def merge_lists(list_a,list_b):
    return list_a + list_b
print(merge_lists([1,2,3,4], ['a','b','c','d']))

# output:- [1, 2, 3, 4, 'a', 'b', 'c', 'd']

# Assignment-2
"""
    create a function called separate() that accepts a string as an argument
    and returns a list containing each of the characters of
    the string separated as individual items in the list.

    Make sure to test the function.
"""

def separate(str):
    return list(str)

print(separate("hello there"))

# output:- ['h', 'e', 'l', 'l', 'o', ' ', 't', 'h', 'e', 'r', 'e']

# Assignment-3
"""
Create a function called multi_merge that takes a list and a string
as arguments.

The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.

"""

def multi_merge(list_a, str):
    return list_a + str.split() + list(str)

print(multi_merge([1,2,3,4], "hello my name is imtiaz"))

# output:- [1, 2, 3, 4, 'hello', 'my', 'name', 'is', 'imtiaz', 'h', 'e', 'l', 'l', 'o', ' ', 'm', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'i', 'm', 't', 'i', 'a', 'z']

# Assignment-4
"""
Define a function called last_list that can accept an unlimited number
of lists but returns only the last list.
"""

def last_list(*args):
    return args[-1 :len(args)]
print(last_list([1,2,3,4,5],['a','b','c'],['mike', 'john']))

# output:- (['mike', 'john'],)

# Assignment-5
"""
Define a function called key_list_items that can accept an unlimited number
of lists along with another argument. The function should return
the second_folder to last item in the specific list specified by the user of the function.
"""

def key_list_items(key, **kwargs):
    value_list = kwargs[key]
    return value_list[-2]
result = key_list_items("things", things=['book','tv','shoes'],people=['mike','pete','jan'],ages = [20,30,40])
print(result)

# output:- tv

# creating function
def greet_person():
    print("hello there, this is a greeting")

def remainder(num1,num2):
    result =num1 % num2
    return result

remainder_value = remainder(10,3)
print(remainder_value)
greet_person()

# *args and **kwargs

def mysum(*args):
    return sum(args)

def key_value_func(**kwargs):
    print(kwargs.get("weight"))

key_value_func(name="mike",weight=200,age=27)

# variable scope

age = 27
print(age)

def increase_age():
    age =30

increase_age()
print(age)

# scope and nested function

age = 27
print(age)

def increase_age():
    age =30
    def add_4_to_age(age):
        age = age + 4
        print("nested method: " + str(age))

    add_4_to_age(22)
    print(age)
increase_age()
print(age)
