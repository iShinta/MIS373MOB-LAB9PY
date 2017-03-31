from random import randint

def beesnees():
    res = ""
    for i in range(100):
        j = i + 1

        if j%3==0 and j%5==0:
            res += " BEESNEES"
        elif j%3==0:
            res += " Bees"
        elif j%5==0:
            res += " Nees"
        else: res += " " + str(j)
    print res

def factorial():
    n = input("Factorial: Enter a positive integer : ")
    if(isinstance(n, int) and n > 0):
        print(str(n) + "! is " + str(fact(n)))

def fact(n):
    if n == 1: return 1
    else: return n * fact(n-1)

def fibonacci():
    n = input("Fibonacci: Enter a positive integer : ")
    if(isinstance(n, int) and n > 0):
        res = ""
        for i in range(n):
            res += str(fib(i+1)) + "\t"
        print(res)

def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)

def pyramid():
    n = input("Pyramid: Enter a positive integer : ")
    if(isinstance(n, int) and n > 0):
        for i in range(n):
            res = ""
            j = i+1
            for l in range(n-i):
                res += " "
            for k in range(j):
                res += "* "
            print(res)

def towercash():
    h = 0.00011
    day = 1
    pile = h
    tower = 94
    print("DAY\tHEIGHT (In meters)")
    while(pile <= tower):
        print(str(day) + "\t" + str(pile))
        day += 1
        pile *= 2
    print(str(day) + "\t" + str(pile))

def wordcount():
    list1 = ['the', 'cat', 'sat', 'on','the','wall','and','the','cat','sat','on','the','mat', 'where','the','rat','usually','sat','and','the','cat','sat','on','the','rat']
    dict1 = {}
    for i in list1:
        if(i in dict1):
            dict1[i] += 1
        else:
            dict1[i] = 1
    for key, value in sorted(dict1.iteritems(), key=lambda (k, v): (v, k), reverse=True):
        print("%s: %s" % (key, value))

def cipher():
    st = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # print st
    st2 = 'GnWkmEJIRQsHLzPSdqVoxfrZbTyOBXhNiwCDcupUYMKgAjlavtFe'
    # print st2

    user = raw_input("Enter a string : ")
    if(user == 'x' or user == 'X'): return
    elif(user[0] == str(1)):
        res = ""
        for i in range(len(user)):
            if(i != 0):
                res += (st[st2.find(user[i])])
        print res
    else:
        res = ""
        for i in range(len(user)):
            res += (st2[st.find(user[i])])
        print res

def indexer():
    list1 = ['the', 'cat', 'sat', 'on','the','wall','and','the','cat','sat','on','the','mat', 'where','the','rat','usually','sat','and','the','cat','sat','on','the','rat']
    print list1

    word = raw_input("Enter a word from the list : ")
    res = []
    # print(list1.index(word.lower())+1)
    for i in range(len(list1)):
        if(list1[i] == word.lower()):
            res.append(str(i+1))
    print(res)

def hangman():
    origin = ['purchasing', 'snake', 'venom', 'makes', 'savagery', 'attainable']
    list1 = origin[:]
    again = "yes"

    #Initialization
    while(again == "yes"):
        win  = False

        # print list1
        if(len(list1) > 0):
            ran = randint(0, len(list1)-1)
            word = list1[ran]
            del list1[ran]
        else:
            list1 = origin[:]

        nbGuess = len(word) + 3
        countdown = len(word)
        list2 = []
        for i in range(len(word)):
            list2.append('-')

        while(nbGuess > 0):
            exist = False
            display = hangmanListToString(list2)
            print(display)
            print("You have " + str(nbGuess) + " guesses left!")
            guess = raw_input("Enter a letter : ")
            for i in range(len(list2)):
                if(word[i] == guess):
                    exist = True
                    list2[i] = guess
                    countdown -= 1
            if(countdown == 0):
                win = True
                break
            nbGuess -= 1
            if(not exist): print("The letter doesn't exist")

        if(win): print "You won!"
        else: print "You lost!"
        again = raw_input("Play again? [yes/no]: ")

def hangmanListToString(word):
    res = ""
    for i in word:
        res += i + " "
    return res

def palindrome():
    win = True
    user = raw_input("Palindrome: Enter a string : ")
    for i in range(len(user)):
        # print(user[i] + "" + user[-i-1])
        if(user[i].lower() != user[-i-1].lower()):
            win = False
    if(win): print("It's a palindrome")
    else: print("It's not a palindrome")

def odometer():
    list1 = [0, 0, 0, 0, 0, 0]

    for i in range(10):
        list1[0] = i
        for j in range(10):
            list1[1] = j
            for k in range(10):
                list1[2] = k
                for l in range(10):
                    list1[3] = l
                    for m in range(10):
                        list1[4] = m
                        for n in range(10):
                            list1[5] = n
                            list2 = list1[:]
                            # print list1

                            # the last 4 digits were palindromic
                            #[0,1,2,3,4,5]
                            if(list2[2] == list2[5] and list2[3] == list2[4]):
                                # print(list1)
                                # print(list2)

                                #One mile later, the last 5 numbers were palindromic
                                #[0,1,2,3,4,5]
                                list2[5] += 1
                                if(list2[1] == list2[5] and list2[2] == list2[4]):
                                    # print(list1)

                                    #One mile after that, the middle 4 out of 6 numbers were palindromic.
                                    #[0,1,2,3,4,5]
                                    list2[5] += 1
                                    if(list2[1] == list2[4] and list2[2] == list2[3]):
                                        # print(list1)

                                        # One mile later, all 6 were palindromic!
                                        #[0,1,2,3,4,5]
                                        list2[5] += 1
                                        if(list2[0] == list2[5] and list2[1] == list2[4] and list2[2] == list2[3]):
                                            print(list1)
                                            # print("")

def main():
    print("Start Program")
    print("\n--beesnees--")
    beesnees()
    print("\n--factorial--")
    factorial()
    print("\n--fibonacci--")
    fibonacci()
    print("\n--pyramid--")
    pyramid()
    print("\n--towercash--")
    towercash()
    print("\n--wordcount--")
    wordcount()
    print("\n--cipher--")
    cipher()
    print("\n--indexer--")
    indexer()
    print("\n--hangman--")
    hangman()
    print("\n--palindrome--")
    palindrome()
    print("\n--odometer--")
    odometer()
    print("End Program")

main()
