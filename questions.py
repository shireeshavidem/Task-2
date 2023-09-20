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
