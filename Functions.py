# def greet_cutomer(special, sale_percent):
#     print("Hello!")
#     print("Our special today is " + special)
#     print("Everything is " + sale_percent + " off today.")
#     print("Have a great time shopping")

# greet_cutomer("Wonton Soup", "70%")

# def first_impression():
#     print("Hi! How was your day?!")
#     print("Ok. Today we have many new things in stock")
#     print("Have a great day!")

# first_impression()

# def add_one(num):
#     if num % 2 != 0:
#         return num + 1
#     else:
#         return num


# x = add_one(1)
# # num == 1

# print(x)

# def add_one_if_odd(num):
#     if num % 2 != 0:
#         return num + 1
#     else:
#         return num


# x = add_one_if_odd(1)
# # num == 1

# print(x)

# def greet_cutomer(special):
#     return "Our special today is " + special

# print(greet_cutomer("banna yogurt"))

z = 10

def sqaure_point_plus_ten(x, y):
    x_2 = x*x + z
    y_2 = y*y + z
    return x_2, y_2 

x_squared, y_sqaured = sqaure_point_plus_ten(2, 4)

print(str(x_squared) + " " + str(y_sqaured))

