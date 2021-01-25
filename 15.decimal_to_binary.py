'''15. convert a decimal number to binary using recursion.
    Ex: 3
    Ans : 11
 '''
def dec_to_bin(num):
    if(num>1):
        dec_to_bin(num//2)
    print (num%2,end='')

num = int(input("Enter an integer to convert it to binary  "))
dec_to_bin(num)