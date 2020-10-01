# The function calculate_age in script.py creates a variable called age that is the difference between the current year, and a birth year, both of which are inputs of the function. Add a line to return age.
# Outside of the function, call calculate_age with values 2049 (current_year) and 2003 (birth_year) and save the value to a variable called my_age.
# Call calculate_age with values 2049 (current_year) and 1953(birth_year) and save the value to a variable called dads_age.

# Print the string "I am X years old and my dad is Y years old" to the console, with my_age where the X is and dads_age where the Y is.

def calculate_age(current_year, birth_year):
    age = current_year - birth_year 
    return age 

my_age = calculate_age(2049, 2003)

dads_age = calculate_age(2049, 1953)



print(my_age, dads_age)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old.")





    
    

