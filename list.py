#names = ["jenny", "alexus", "sam", "grace"]
# names = ["jenny", "alexus"]
#print(names[0,0])

# names_and_heights = [["jenny", 67], ["alexus", 70]]

# print(names_and_heights[0][1]) #prints only the name 
# # print(names_and_heights[0][0]) + " is " + str(names_and_heights[0][1] + " inches tall") #prints name and height

# names = ["jenny", "alexus"]
# heights = [67, 70]

# names_and_heights = list(zip(names, heights))

# tuples: (x, y) and cannot be changed
# list: [x, y]
# zip() does not include items from the longer list if list legnths are not the same 

# print(list(names_and_heights))

# print(names_and_heights[0][0])

# names = ["jenny", "alexus"]
# print("before adding \"sam\": ", str(names))
# names.append("sam")
# print("After adding \"sam\": ", str(names))

# names = ["jenny", "alexus"]
#name.insert(1, "ryan")
#names = ["jenny", "ryan", "alexus"]


#range(x)
#start: 0
#stop: x-1
#step 1
# new_range = list(range(10))
# print(new_range)

#range(x, y, z)
#start: x
#stop: y-1 
#step: z
# even_range = list(range(0, 21, 2))
# print(even_range)

#range(x, y)
#start: 
#stop
#step: 1

# zero_to_five = list(range(0, 6))
# print(zero_to_five)

# *Slicing List*

# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# sublist = letters[1:6]

# print(sublist)

# Mississippi = ['m', 'i', 's', 's', 'i', 's', 's', 'i', 'p', 'p', 'i']

# Mis = Mississippi.count('i')

# print(Mis)

#nums.sort() is the command that sorts the numbers in your list from smallest(at the left) to greatest(at the right) and does the same with letters as well

# nums = [1,2,5,2,2,5,7,8,3,2,1,5,7,8,5,22,1,55]
# num_46s = nums.count(1)
# print(num_46s)
# sorted_nums = sorted(nums)
# print(nums)
# print(sorted_nums)
#sorted doesnt sort the orginal list it creates a new list 
#mean while .sort does change the orginal list
names = ["tyler", "jacky", "ryan", "ramiro", "kingsley"]

# names.sort()
# name = names[-1]
# print(name)

sorted_names = sorted(names)
name = names[-1]
first_sorted_name = sorted_names[0]
print(name)
print(sorted_names)