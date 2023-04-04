import random
while True:
    list1 = []
    list2 = ""
    wordssmall = ("abcdefghijklmnopqrstuvwxyz")
    wordsbig = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    nums = ("1234567890")
    specha = ("_?!+=-#*")
    ask = input("How long is your password? ")
    while int(ask) < 8:
        print("Must be larger than 8")
        ask = input("How long is your password? ")

    print('''Choose character set for password from these :
         1. Small Letters
         2. Big Letters
         3. Digits
         4. Special characters
         5. Exit''')
    while(True):
        choice = int(input("Pick a number: "))
        if(choice == 1):
            list1.append(random.choice(wordssmall))
            list2 += wordssmall
        elif(choice == 2):
            list1.append(random.choice(wordsbig))
            list2 += wordsbig
        elif(choice == 3):
            list1.append(random.choice(nums))
            list2 += nums
        elif(choice == 4):
            list1.append(random.choice(specha))
            list2 += specha
        elif(choice == 5):
            break
        else:
            print("Please pick a valid option!")
    
    total = int(ask) - len(list1)

    for i in range(total):
        gen = random.choice(list2)
        list1.append(gen)
    
    random.shuffle(list1)
    print("".join(list1))

    ask = input("Generate another password? (y/n): ").lower()
    if ask != "y":
        break

