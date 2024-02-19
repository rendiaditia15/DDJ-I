for x in range(1,21):
    if (x % 3 == 0 and x % 5 == 0):
        print("fizzfuzz")
    elif (x %5 == 0):
        print("fuzz")
    elif (x %3 == 0):
        print("fizz")
    else:
        print(x)    