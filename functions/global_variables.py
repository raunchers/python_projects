def spam():
    global eggs # sets the variable as global, allowing use outside of function
    eggs = "Hello"
    print(eggs)

eggs = 42
spam()
print(eggs)
