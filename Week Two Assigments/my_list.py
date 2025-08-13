#1 Create an empty list
my_list = []

# 2 add using append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# 3 insert 15 at the second position (index 1)
my_list.insert(1, 15)

# 4 extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# 5 remove the last element
my_list.pop()

# 6 sort the list in ascending order
my_list.sort()

# lastly find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# print out the final state of the list
print("Final my_list:", my_list)
