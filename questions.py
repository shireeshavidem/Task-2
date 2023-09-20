#1.Write a python program to remove a given  character from string.
#using replace() 
str = "I want to go shopping today"
print(str.replace("p",""))

#using translate()
s = "My favourite food is biryani!"
print(s.translate({ord("o"): None}))

#2.Write a program to check String is Palindrome or not.
s = "madam"
def ispalindrome(s):
    return s == s[::-1]
if ispalindrome(s):
    print("yes")
else :
    print("no")

#3.Write a python program to check given character is vowel or consonant.
# char = input("Enter a character : ") 
# vowels = ["a","e","i","o","u","A","E","I","O","U"]
# if char in vowels:
#     print(f"'{char}' is a vowel")
# else:
#     print(f"'{char}' is a consonant")

#4.Write a python program to replace string space with given character in Python.
# name = "my name is videm shireesha"
# charecter = input("Enter a character: ")
# print(name.replace(" ",charecter))

#5.Write a python program to count alphabets, digits, and special characters in the string.
s1 = "siri@123"
alphabets=digits=special=0
for i in range(len(s1)):
     if (s1[i].isalpha()):
         alphabets = alphabets + 1
     elif (s1[i].isdigit()):
         digits = digits + 1
     else:
         special = special + 1
print(alphabets)
print(digits)
print(special)

#6.Write a python program to remove all the blank spaces in a given string.
name = "my name is videm shireesha"
print(name.translate({ord(" "): None}))

#7.Write a python program to find sum of integers in the string.
str1 = "12345siri"
def sum_digits_string(str1):
    sum_digit = 0
    for i in str1:
        if i.isdigit():
            x = int(i)
            sum_digit = sum_digit + x
    return sum_digit
print(sum_digits_string(str1))

#8.Write a python program to Remove Repeated Character from String.
str2 = "shireesha"
s = ""
for i in str2:
    if i not in s:
        s = s + i
print(s)        

#9.Write a python program to count occurrence of given character in string. 
str3 = "today is working day!"
print(str3.count("i"))

#10.Write a python program to check string is anagrams or not in Python.
s3 = "night"
s4 = "thing"
a = sorted(s3.lower())
b = sorted(s4.lower())
def isanagram():
    if a == b:
        print("Given strings are anagrams")
    else:
        print("Given strings are not anagrams")
print(isanagram())

