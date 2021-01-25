'''    5. Please write a program which count and print the numbers of each character in a string input by console.
Ex:aabc
o/p -> a:2,b:1,c:1'''
str = input("Enter a string: ").casefold()

str=str.replace(" ","")
print(str)
tempStr = ''
for char in str:
    if char not in tempStr:
        print(char, ', ', str.count(char))
        tempStr = tempStr+char