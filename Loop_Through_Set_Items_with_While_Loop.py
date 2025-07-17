# Defining a set with multiple elements
my_set = {1, 2, 3, 4, 5}

# Converting the set to an iterator
set_iterator = iter(my_set)

# Looping through each item in the set using a while loop
while True:
   try:
      # Getting the next item from the iterator
      item = next(set_iterator)
      # Performing operations on each element
      print("Item:", item)
   except StopIteration:
      # If StopIteration is raised, break from the loop
      break