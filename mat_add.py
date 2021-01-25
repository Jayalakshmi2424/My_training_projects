print ("Enter dimensions of first matrix")

m1=int(input("Enter row value "))

n1=int(input("Enter column value  "))

print ("Enter dimensions of second matrix")

m2=int(input("Enter row value "))

n2=int(input("Enter column value  "))


if(m1==m2 and n1==n2) :
    print ("Enter first matrix values rowwise")
    A = [[int(input()) for x in range (n1)] for y in range(m1)]
    print ("Enter second matrix values rowwise")
    B = [[int(input()) for x in range (n2)] for y in range(m2)]


    #Addition
    C= []
    for i in range(m1):
      a = []
      for j in range(n1):
        a.append(A[i][j]+B[i][j])
      C.append(a)
    print ("Addition of matrix is",C)

else:
    print ("Incompatible Matrices")