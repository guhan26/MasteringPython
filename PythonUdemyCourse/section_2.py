# Assignment-1
"""
Print Bill's salary from the my_list object shown below.
"""
my_list = [{'tom': 20000,'bill': 12000},['car','laptop','tv']]
print(my_list[0].get('bill'))

# output:- 12000

# Assignment-2

"""
Using some of the collection data types we learned about
in the course so such as a list and dictionary, create a
data structure that best represents the following scenario:

Tom has a salary of 20000 and is 22 years old. He owns a few items such as
a jacket, a car, and TV. Mike is another person who makes 24000 and is 27 years old
who owns a bike, a laptop and boat.
"""
my_value =[{'tom': {'salary': 20000, 'age': 22,'owns':['car','tv']}},
           {'bill': {'salary': 20000, 'age': 23,'owns':['bike','laptop']}}]
print(my_value)

# output:- [{'tom': {'salary': 20000, 'age': 22, 'owns': ['car', 'tv']}}, {'bill': {'salary': 20000, 'age': 23, 'owns': ['bike', 'laptop']}}]

# Assignment-3

"""
There is a list shown below titled original_list.

Using only what you've learned so far in the course,
write code to create a new list that contains the tuple sorted.

IMPORTANT: you must do this programmatically! Don't just
      hard code a new list with the values rearranged.
"""
original_list = ['cup', 'cereal' , 'milk', (8,4,3)]
num1= original_list[3][0]
num2= original_list[3][1]
num3= original_list[3][2]

new_list = [num1,num2,num3]
new_list.sort()
new_tuple = (new_list[0],new_list[1],new_list[2])
original_list.pop()
original_list.append(new_tuple)
print(original_list)

# output:- ['cup', 'cereal', 'milk', (3, 4, 8)]

# Assignment-4
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""
my_list5 = [(1,2),(3,4),(['c','d','a','m'],[3,9,4,12],4),'tv',42]
my_list5[2][0][3] ='x'
my_list5[3]='television'
print(my_list5)

# output:- [(1, 2), (3, 4), (['c', 'd', 'a', 'x'], [3, 9, 4, 12], 4), 'television', 42]

# List - []

my_list = [1,6,5,4,3,2]

my_list.sort()
appended = my_list.append("this is a sentence")

my_value = my_list.pop()

print(my_list)

print(my_value)

print(appended)

my_list1= ['e','r','s','e',1,4,2,6,7,['apple','orange'],'r']

print(my_list1)

my_value1 = ['a','b','c','d','c','c']
c_count = my_value1.count('c')
print(c_count)


# Tuples - ()

my_tuple = (1,2,3,"some data", [1,2,3])
count = my_tuple.count("some data")

print(count)

# Distionaries - {}

dist = {'k1' : 'some data',7: 'other data'}

dist['7'] = "new value"
print(dist)

# comparison operators
print(10 == 9)
print('hello' == 'hello')
print(5 <= 10 or 5 == 6 and True)

