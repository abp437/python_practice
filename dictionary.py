my_dictionary = {
  "hello": "World",
  "world": "Hello",
}

print(my_dictionary)
# Unlike Ruby we can't access values inside a Python dictrionary using the `.` operator
print(my_dictionary["hello"])

# A Python dictionary can have keys as immutable data types only.
# Dictionary with different types of immutable keys
d = {
  'name': 'Alice',
  42: 'The Answer',
  (1, 2): 'Tuple key',
  True: 'Boolean key'
}

# Accessing values
print(d['name'])  # Output: Alice
print(d[42])      # Output: The Answer
print(d[(1, 2)])  # Output: Tuple key
print(d[True])    # Output: Boolean key
