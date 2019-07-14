def div42by(divideBy):
    try:
        return 42 / divideBy
    # Can be ran without specific error, in this case, it will catch all errors
    except ZeroDivisionError: # name of error when ran without try and except clause
        print("Error: Cannot divide by 0")

def cats(num):
    try:
        if int(num) >= 4:
            print("That is a lot of cats!")
        else:
            print("That is not a lot of cats.")
    except ValueError:
        print("You did not enter a number.")

print(div42by(2))
print(div42by(42))
print(div42by(7))
print(div42by(0))
print()
print()
print("How many cats do you have?")
cats(input())
