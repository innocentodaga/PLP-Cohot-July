# obtain input of two sets of integers
set1 = set(map(int, input("Enter integers for Set 1 (space-separated): ").split()))
set2 = set(map(int, input("Enter integers for Set 2 (space-separated): ").split()))

# Find common elements
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)