#names = ["jenny", "alexus", "sam", "grace"]
# names = ["jenny", "alexus"]
#print(names[0,0])

# names_and_heights = [["jenny", 67], ["alexus", 70]]

# print(names_and_heights[0][1]) #prints only the name 
# # print(names_and_heights[0][0]) + " is " + str(names_and_heights[0][1] + " inches tall") #prints name and height

names = ["jenny", "alexus"]
heights = [67, 70]

names_and_heights = list(zip(names, heights))

# tuples: (x, y) and cannot be changed
# list: [x, y]
# zip() does not include items from the longer list if list legnths are not the same 

# print(list(names_and_heights))

# print(names_and_heights[0][0])

names = ["jenny", "alexus"]
print("before adding \"sam\": ", str(names))
names.append("sam")
print("After adding \"sam\": ", str(names))

#name.insert(0, "ryan")

#range(x)
#start: 0
#stop: x-1
#step 1
new_range = list(range(10))
print(new_range)

#range(x, y, z)
#start: x
#stop: y-1 
#step: z
even_range = list(range(0, 21, 2))
print(even_range)

#range(x, y)
#start: 
#stop
#step: 1

zero_to_five = list(range(0, 6))
print(zero_to_five)