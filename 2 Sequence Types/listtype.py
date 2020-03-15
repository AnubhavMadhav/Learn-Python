
"""Create a List"""
# Declaring a List
l1 = [1,2, 'Anubhav', 10.5, -30]


# Print a List
print(l1)

# Print element of a List at given Index
print(l1[3])

# Slicing a List
print(l1[3:5])

# Repitition in a List
print(l1*4)

# Length of a List
print(len(l1))



"""Adding and Removing List Elements"""
# Append an element
l1.append(40)           # will add the element at the end of List

# Remove an element 
l1.remove("Anubhav")    # removes "Anubhav" from l1

# delete an element through it's index by passing the list "del" function
del(l1[1])              # it is not a function for list, it is an inbuilt function in python in which we can pass a list or anything else

print(l1)