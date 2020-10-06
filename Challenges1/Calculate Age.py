# The function calculate_age in script.py creates a variable called age that is the difference between the current year, and a birth year, both of which are inputs of the function. Add a line to return age.
# Outside of the function, call calculate_age with values 2049 (current_year) and 2003 (birth_year) and save the value to a variable called my_age.
# Call calculate_age with values 2049 (current_year) and 1953(birth_year) and save the value to a variable called dads_age.

# Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is and dads_age where the Y is.

# def calculate_age(current_year, birth_year):
#     age = current_year - birth_year 
#     return age 

# my_age = calculate_age(2049, 2003)

# dads_age = calculate_age(2049, 1953)



# print(my_age, dads_age)
# print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old.")

# --------------------------------------------------
# Challenge 1 Advanced - In Range
# --------------------------------------------------

# Create a function named in_range() that has three parameters named num, lower, and upper.

# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

# Write your in_range function here:

# Uncomment these function calls to test your in_range function:
# print(in_range(10, 10, 10))
# should print True
# print(in_range(5, 10, 20))
# should print False

# def in_range(num, lower, upper):
#     if(num >= lower) and (lower <= upper):
#         return True
#     else:
#        return False

# print(in_range(10, 10, 10))

# --------------------------------------------------
# Challenge 2 - Same Name
# --------------------------------------------------

# Create a function named same_name() that has two parameters named your_name and my_name.

# If our names are identical, return True. Otherwise, return False.

# Write your same_name function here:

# Uncomment these function calls to test your same_name function:
#print(same_name("Colby", "Colby"))
# should print True
#print(same_name("Tina", "Amber"))
# should print False

# def same_name(your_name, my_name):
#     if(your_name == my_name):
#         return True
#     else:
#         return False
# print(same_name("Colby", "Colby"))

# --------------------------------------------------
# Challenge 3 - Always False
# --------------------------------------------------

# Create a function named always_false() that has one parameter named num.

# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.

# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

# Write your always_false function here:

# Uncomment these function calls to test your always_false function:
#print(always_false(0))
# should print False
#print(always_false(-1))
# should print False
#print(always_false(1))
# should print False

# def always_false(num):
#     if(num > num):
#         return False 
#     else:
#         return True
# print(always_false(1))

# --------------------------------------------------
# Challenge 4 - Movie Review
# --------------------------------------------------

# Create a function named movie_review() that has one parameter named rating.

# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". If rating is 9 or above, return "Outstanding!"

# Write your movie_review function here:

# Uncomment these function calls to test your movie_review function:
#print(movie_review(9))
# should print "Outstanding!"
#print(movie_review(4))
# should print "Avoid at all costs!"
#print(movie_review(6))
# should print "This one was fun."

# def movie_review(rating):
#     if(rating <= 5):
#         return ("Avoid at all costs!")
#     if(rating > 5) and (rating < 9):
#         return ("This one was fun.")
#     if(rating >= 9):
#         return ("Outstanding!")
# print(movie_review(6))

# --------------------------------------------------
# Challenge 5 - Max Number
# --------------------------------------------------

# Write your max_num function here:

# Uncomment these function calls to test your max_num function:
#print(max_num(-10, 0, 10))
# should print 10
#print(max_num(-10, 5, -30))
# should print 5
#print(max_num(-5, -10, -10))
# should print -5
#print(max_num(2, 3, 3))
# should print "It's a tie!"

def max_num(num1, num2, num3):
    if(num1 > num2) and (num1 > num3):
        return num1
    if(num2 > num1) and (num2 > num3):
        return num2
    if(num3 > num1) and (num3 > num2):
        return num3
    if(num1 == num2) or (num2 == num3) or (num3 == num1):
        return "It's a tie"
print(max_num(2, 3, 3))

    
    

