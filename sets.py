# You cannot index into a set and when you print it it will come out in a random order
# You can loop a set
# elements in sets cannot be changed

names = {"alex", "john", "ryan", "ramiro", "andrew", "jordan"}

for name in names:

print("jacky" in names)

names.add("jacky") #Adding one element to the set 

names.update(["jacky", "jt"]) #using a list you can add mulitple elements to the set at once

print(len(names)) #prints the number of how many elements are in a set

names.romve("jordan") #removes an element from the set
names.discard #does the samething as .remove

#.pop will remove the last item from the set
names.clear #will clear the list 
names.del #will delete the whole set

set1 = {1, 2, 3 ,4}
set2 = {1, 5, 6, 7, 8}
set3 = set1.union(set2) #this is how you combine a set if the elements of the 2 sets are the same the new set will not have two of the same elements 
print(set3) 

set4 = set1.intersection(set2) #only makes a new set with elements that exist in both sets
print(set4)
