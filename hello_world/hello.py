# This program says hello and asks for my name

print('Hello World!')
print('What is your name?')

# Ask for name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))

# Ask for their age
print('What is your age?')
myAge = input()

print('You will be ' + str(int(myAge) + 1) + ' in a year')
