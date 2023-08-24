# Question 1
# Write a function to print “hello_USERNAME!” 
# USERNAME is the input of the function. The 
# first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello, " + user_name.title() + "!")

hello_name("mary")
    

# Question 2
# Write a python function, first_odds that prints 
# the odd numbers from 1-100 and returns nothing

def first_odds():
    for num in range(1, 101):
        if num % 2 == 1:
            print(num)

first_odds()


# Question 3
# Please write a Python function, max_num_in_list 
# to return the max number of a given list. The 
# first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num

a_list = [1, 4, 6, 7, 2, 9, 7]
print(max_num_in_list(a_list))
        

# Question 4
# Write a function to return if the given year is 
# a leap year. A leap year is divisible by 4, but 
# not divisible by 100, unless it is also divisible 
# by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        leap_year = True
    else:
        return False

    return leap_year
  
print(is_leap_year(1900)) # False
print(is_leap_year(1992)) # True
print(is_leap_year(2000)) # True

print(is_leap_year(2010)) # False
print(is_leap_year(2011)) # False
print(is_leap_year(2012)) # True
print(is_leap_year(2013)) # False
print(is_leap_year(2014)) # False
print(is_leap_year(2015)) # False
print(is_leap_year(2016)) # True
print(is_leap_year(2017)) # False
print(is_leap_year(2018)) # False
print(is_leap_year(2019)) # False
print(is_leap_year(2020)) # True
print(is_leap_year(2021)) # False
print(is_leap_year(2022)) # False
print(is_leap_year(2023)) # False
print(is_leap_year(2024)) # True
print(is_leap_year(2025)) # False
print(is_leap_year(2026)) # False
print(is_leap_year(2027)) # False
print(is_leap_year(2028)) # True

        
# Question 5
# Write a function to check to see if all numbers 
# in list are consecutive numbers. For example, 
# [2,3,4,5,6,7] are consecutive numbers, but 
# [1,2,4,5] are not consecutive numbers. The 
# return should be boolean Type.

def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    for num in range(len(sorted_list)-1):
        if sorted_list[num] + 1 != sorted_list[num+1]:
            return False
    else:
        return True
    
print(is_consecutive([1, 2, 3, 4])) # True
print(is_consecutive([1, 3, 2, 5])) # False
print(is_consecutive([4, 5, 6, 7])) # True
print(is_consecutive([8, 9, 10, 12])) # False
