# Get input and convert to list of intergers
numbers = input("Enter integers separated by spaces: ")
int_list = list(map(int, numbers.split()))

# Get the total
total = sum(int_list)

print("Sum of the integers:", total)
