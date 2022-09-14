num = int(input("Please Enter the Number you wish: "))

if(num%4 == 0):
    if(num%100 == 0):
        if(num%400 == 0):
            print("%d is a Leap Year" %num)
        else:
            print("%d is Not" %num)
    else:
        print("%d is a Leap Year" %num)
else:
    print("%d is Not" %num)