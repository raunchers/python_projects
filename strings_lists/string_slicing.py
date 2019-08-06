# Strings are immutable
# Create new string and use slicing to change a string
import copy

name = "Zophie a cat"
newName  = name[0:7] + "the" + name[8:12]
print(newName)


# appending
def eggs(parm):
    parm.append("Hello")

spam = [1,2,3]
eggs(spam)
print(spam)

# Copying list, not just the reference
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese.append('E')
print(spam)
print(cheese)
