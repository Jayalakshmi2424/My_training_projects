print ("Enter dimensions of first matrix")

m1=int(input("Enter row value "))

n1=int(input("Enter column value  "))

print ("Enter dimensions of second matrix")

m2=int(input("Enter row value "))

n2=int(input("Enter column value  "))


if( n2==m1 ) :
    print ("Enter first matrix values rowwise")
    A = [[int(input()) for x in range (n1)] for y in range(m1)]
    print ("Enter second matrix values rowwise")
    B = [[int(input()) for x in range (n2)] for y in range(m2)]

    #multiplication
    C = []
    for i in range(m1):
      a = []
      for j in range(m1):
        summ = 0
        for k in range(n1):
          summ = summ+(A[i][k]*B[k][j])
        a.append(summ)
      C.append(a)
    print ("Multiplication of 2 Matrices1 is",C)
else:
    print("Incompatible Matrices First matrix's column value should be equal to Second matrix's row value")

