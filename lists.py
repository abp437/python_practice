# Just like Ruby the elements in a list doesn't need to be of the same type.
# All the other scenarios are similar to Arrays like Ruby
# Here the terminology just changes to `List` instead of arrays
my_list = [1, 3, 4, 55, 6, 78, "August"]
my_list.append(32)

print(my_list)

# CORNER CASE:
# Unlike Ruby though, This line will produce an `IndexError: list index out of range`
# Because the size of the list is smaller than the one given below
# Ruby will return `nil` but in Python it produces `IndexError`
# print(my_list[20])
