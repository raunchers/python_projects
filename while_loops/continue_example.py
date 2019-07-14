spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue # continue skips this part of the loop
    print("Spam: " + str(spam))
