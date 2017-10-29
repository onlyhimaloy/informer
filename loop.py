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
    elif largest > num :
        print("MAX is ", largest)
    if smallest is None :
         smallest = num
    elif smallest <num  :
        print("MIN is ", smallest)

