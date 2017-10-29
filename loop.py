#Python loop test script

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    #print(num)
    try:
        val = int(num)
    except:
        print('invalid input')
        continue

    if largest is None :
        largest = num
    elif num > largest :
        print("Minimum is ", smallest)
    if smallest is None :
         smallest = num
    elif num < smallest :
        print("Maximum is ", largest)

