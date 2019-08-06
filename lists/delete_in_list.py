# deleting from list
spam = ["Stuff", "More stuff", "stuff stuff", "stuffy stuff"]
print (spam)
del spam[2]
print (spam)
# -1 refers to last item, -2 second to last, etc...


print(list(range(0, 100, 2))) # creates list from 0 to 100 while stepping up by two

supplies = ["stuff", "things", "more things", "thing things"]

for i in range(len(supplies)):
    print("Index: " + str(i) + " in supplies is: " + supplies[i])
