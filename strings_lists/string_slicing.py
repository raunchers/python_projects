# Strings are immutable
# Create new string and use slicing to change a string
name = "Zophie a cat"
newName  = name[0:7] + "the" + name[8:12]
print(newName)


# appending
def eggs(parm):
    parm.append("Hello")

spam = [1,2,3]
eggs(spam)
print(spam)
