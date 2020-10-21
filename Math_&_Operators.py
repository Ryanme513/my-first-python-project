# x = 1
# y = 2
# z = 3

# print(x*y) Multiplying 
# print(x/y) Divion
# print(x**y) Exponent

# x = 5
# x += 2
# print(x)

# if(5 > 7):
#     print("hello")
# else:
#     print("goodbye")

# expression= "hello" if 6 >=6 else "goodbye"
# orint(expression)

# sale= True
# store_message = "Hello, we have a sale today!" if sale else "We don't have a sale today"

# print(store_message)

# if(sale):
#     store_message = "Hello, we don't have sale today"
# else:
#     store_message = "We don't have a sale today"
# print(store_message)

# if((2**3 == 8) and (4**2 == 8)):
#     print("true")
# else:
#     print("false")

# if((2**3 == 8) or (4**2 == 8)):
#     print("true")
# else:
#     print("false")

# if(not (2**3 == 8) or (4**2 == 8)):
#     print("true")
# else:
#     print("false")

# def addTwoIfEven(num):
#     if(num % 2 == 0):
#         return num + 2
#     else:
#         return num 

# try:
#     a = 1
#     b = 0
#     print(a/b)
# except ZeroDivisionError
# print("Computer's can't divied by zero")

try:
    a = int(input("a: "))
    b = int(input("b: "))
    print(a/b)
except ZeroDivisionError:
    print("Computer's can't divied by zero")
    b = int(input("b: "))
    print(a/b)