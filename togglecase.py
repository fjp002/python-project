# Python Program to Toggle Characters Case in a String
 
string = input("Please Enter your Own String : ")

string1 = ''

for i in string:
    if(i >= 'a' and i <= 'z'): 
        string1 = string1 + chr((ord(i) - 32)) 
    elif(i >= 'A' and i <= 'Z'):
        string1 = string1 + chr((ord(i) + 32))
    else:
        string1 = string1 + i
 
print("\nOriginal String                      =  ", string)
print("The Given String After Toggling Case =  ", string1)
