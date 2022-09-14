# using While Loop

number = int(input("Please Enter any Value: "))

reverse = 0
temp = number

while(temp > 0):
    Reminder = temp % 10
    reverse = (reverse * 10) + Reminder
    temp = temp //101
 
print("Reverse of it is = %d" %reverse)

if(number == reverse):
    print("%d is a Palindrome" %number)
else:
    print("%d is Not" %number)