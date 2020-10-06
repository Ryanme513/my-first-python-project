#-----------------------------------------------------
# Challenge 5 - Not Equal
#-----------------------------------------------------

# Create a function named not_sum_to_ten() that has two parameters named num1 and num2. Return True if num1 and num2 do not sum to 10. Return False otherwise.

# Write your not_sum_to_ten function here:
  
# Uncomment these function calls to test your not_sum_to_ten function:
#print(not_sum_to_ten(9, -1))
# should print True
#print(not_sum_to_ten(9, 1))
# should print False
#print(not_sum_to_ten(5,5))
# should print False

def not_sum_to_ten(num1, num2):
    if(num1 + num2 == 10):
        return False
    else:
        return True

print(not_sum_to_ten(1,1))