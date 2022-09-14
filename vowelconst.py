ch = input("Please Enter Your Own Character : ")

if(ord(ch) == 65 or ord(ch) == 69 or ord(ch) == 73
       or ord(ch) == 79 or ord(ch) == 85
       or ord(ch) == 97 or ord(ch) == 101 or ord(ch) == 105
       or ord(ch) == 111 or ord(ch) == 117):
    print("The Given Character ", ch, "is a Vowel")
elif((ord(ch) >= 97 and ord(ch) <= 122) or (ord(ch) >= 65 and ord(ch) <= 90)):
