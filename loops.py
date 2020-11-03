# names = ["alex", "john", "ryan", "ramiro", "andrew", "jordan"]
# for name in names:
#     print(name)

# rng = list(range(6))
# print(rng)

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in lst:
#     print(num)

# for index in range(len(lst)):
#     lst[index] = 2 * lst[index]
#     print(lst[index])

# lst = [1, 2, 3, 4, 5, 6, 7]
# for num in lst:
#     print(num2)
# print(lst)
# for index in range(len(lst)):
#     lst[index] = lst[index]
#     print(lst[index])
# print(lst)

# names = ["alex", "allistair", "andrew", "angelo", "elijah", "george", "jonathan"]
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])
# names = ["alex", "allistair", "andrew", "angelo", "elijah", "george", "jonathan"]
# for person in names:
#     print(person)
# person = "alex"
# print(person)
# person = "allistair"
# print(person)
# person = "andrew"
# print(person)
# rng = list(range(6))
# print(rng)
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for num in lst:
#     print(num*2)
# print("unmodified list: ", lst)
#range(6) -> [0, 1, 2, 3, 4, 5]
#range(8) -> [0, 1, 2, 3, 4, 5, 6, 7]
#range(len(lst)) -> [0, 1, 2, 3, 4, 5, ... len(lst) - 1]
# list_length = len(lst)
# for index in range(list_length):
#     lst[index] = 2 * lst[index]
#     print(lst[index])
# print("modified list: ", lst)

# * Infinte Loop 
# my_favorite_numbers = [4, 8, 15, 16, 42]

# for num in my_favorite_numbers:
#     my_favorite_numbers.append(1)
# print my_favorite_numbers

# items_on_sale = ["blue_shirt", "striped_socks", "knit_dress", "red_headband"]

# for item in items_on_sale:
#     if item == "knit_dress":
#         print("knitdress is on sale!")
#         break 

# print("end of search!")

# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
# for i in big_number_list:
#     if i < 0:
#         continue
#     print(i)

# nums = [1, 2, 3, 4, 5, 6, 7]
# for num in nums:
#     if num%2 == 0:
#         continue 
#     print(num)

# dog_breeds = ['bulldog', 'dalmation', 'shihtzu', 'poodle', 'collie']

# index = 0
# while index < len(dog_breeds):


# project_teams = [["ava", "samantha", "james"], ["ryan", "jacky"], ["JT", "andrew"]]
# for team in project_teams:
#     for student in team:
#         print(student)

names_and_heights = [["jenny", 67],["alexus", 70]]

for student in names_and_heights:
    for attrribute in student:
        print(attrribute)