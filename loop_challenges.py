#----------------------------------------------------------
# Challenge 1 - Divisible by Ten
#----------------------------------------------------------
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

# def divisible_by_ten(nums):
#     x = 0
#     for num in nums: 
#         if num % 10 == 0: 
#             x += 1
#     return x

#Uncomment the line below when your function is done
# print(divisible_by_ten([20, 25, 30, 35, 40]))

#----------------------------------------------------------
# Challenge 2 - Greetings
#----------------------------------------------------------
# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

# def add_greetings(names):
#     lst = []
#     for b in names:
#         lst.append("Hello, " + b)
#     return lst
#Uncomment the line below when your function is done
# print(add_greetings(["Owen", "Max", "Sophie"]))

#----------------------------------------------------------
# Challenge 3 - Delete Starting Even Numbers
#----------------------------------------------------------

# Write a function called delete_starting_evens() that has a parameter named lst.

# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

# def delete_starting_evens(lst):
#     while len(lst) > 0  and lst[0] % 2 == 0:
#         lst.pop(0)
#     return lst 

#Uncomment the lines below when your function is done
# print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
# print(delete_starting_evens([4, 8, 10]))

#----------------------------------------------------------
# Challenge 4 - Odd Indices
#----------------------------------------------------------

# Create a function named odd_indices() that has one parameter named lst.

# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

# def odd_indices(lst):
#     empty = []
#     x = 0 
#     for num in lst:
#         if x % 2 != 0:
#             empty.append(lst[x])
#         x += 1
#     return empty

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))

#----------------------------------------------------------
# Challenge 5 - Exponents
#----------------------------------------------------------

# Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

# For example, consider the following code.

# exponents([2, 3, 4], [1, 2, 3])

# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

# def exponents(bases, powers):
#     lst = []
#     for num in bases:
#         for power in powers:
#             lst.append(num**power)
#     return lst


#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))


#----------------------------------------------------------
# Challenge 6 - Larger Sum
#----------------------------------------------------------

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1, lst2):
    x = 
    for x in y:
        for nums in lst2:
            if x > y:
                return lst1
            else: 
                return lst2
                if x == y:
                    return lst1
                

    
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

