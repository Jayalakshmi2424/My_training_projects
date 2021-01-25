
'''    3. Write a program that computes the value of a+aa+aaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
3
Then, the output should be:
369'''
a = int(input("Input an integer : "))
n1 =int("%d" % a )
n2 = int( "%d%d" % (a,a) )
n3 = int( "%d%d%d" % (a,a,a) )
print (n1+n2+n3)
