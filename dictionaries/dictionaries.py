# Key valued pairs
# unordered
# can use numbers for keys
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur')

# Checking if key exist in dictionary
print()
print()
print('Checking if keys exist using in keyword')
print('size' in myCat)
print('cat' in myCat)
print()
print()

# not in examples
print('Checking if keys do not exist using not in keyword')
print('size' not in myCat)
print('cat' not in myCat)
print()
print()

# Listing all keys
print('Listing all keys in dictionary')
print(list(myCat.keys()))
print()
print()

# Listing all items
print('Listing all items in dictionary')
print(list(myCat.items()))
print()
print()

# using loops
print('Using for loop to print keys')
for k in myCat.keys():
    print(k)
print()
print()

print('Using for loop to print values')
for v in myCat.values():
    print(v)
print()
print()

print('Using for loop to print keys and values')
for k, v in myCat.items():
    print(k, v)
print()
print()

# Get method
# Checks for key, if no key, have default value to fall back on
print(myCat.get('color', 0))
print(myCat.get('monster', 0))
print()
print()

# Set default
print("Using an if statement with not in keyword to check for a key valued pair, if not found, creates it.")
print(myCat)
if 'monster' not in myCat:
    myCat['monster'] = 'yes'
print(myCat)
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print('Resetting myCat dictionary')
print(myCat)
print()
print()
print("Using setdefault to add a key valued pair to dictionary if it is not found")
myCat.setdefault('monster', 'yes')
print(myCat)
