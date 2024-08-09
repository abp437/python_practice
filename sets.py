# Sets are just a list of unique elements. But it's unordered.
# Like Lists we can run a for loop on Sets

sample_set = {12, 3, 4, 5, 656, 6, 7, 89}
print("Sample Set:", sample_set)

my_list = [10, 20, 30, 20, 23, 40, 10, 15]

# Lists can be converted to sets like below
list_to_set = set(my_list)

print("List:", my_list)

# Observe that although the values in a Set are unique they aren't ordered like Lists.
print("List to Set:", list_to_set)
