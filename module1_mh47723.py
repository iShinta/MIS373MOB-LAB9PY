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
            res += str(fib(i+1)) + ", "
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



def main():
    print("Start Program")
    # print("\n--beesnees--")
    # beesnees()
    # print("\n--factorial--")
    # factorial()
    # print("\n--fibonacci--")
    # fibonacci()
    # print("\n--pyramid--")
    # pyramid()
    # print("\n--towercash--")
    # towercash()
    # print("\n--wordcount--")
    # wordcount()
    print("\n--cipher--")
    cipher()
    print("End Program")

main()
