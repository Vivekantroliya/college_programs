# 13.Write a program to make use of map(), filter()
# and reduce() functions with context to lambda functions.

# Use Of 'map()' Fuction

lst=[1,2,3,4,5,6,7]

square = lambda a : pow(a,2)

map_lst = list(map(square,lst))

print("List Using 'map()' Function :",map_lst) 

# Use Of 'filter()' Function

even = lambda a : a%2==0

filter_lst = list(filter(even,lst))

print("List Using 'filter()' Function :",filter_lst)

# Use Of 'reduce()' Function

from functools import reduce

multi = lambda a,b : a*b

reduce_lst = reduce(multi,lst)

print("Variable After Using 'filter()' Function :",reduce_lst)
