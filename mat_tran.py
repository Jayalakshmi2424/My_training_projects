print ("Enter dimensions of  matrix")

m1=int(input("Enter row value "))

n1=int(input("Enter column value  "))

print ("Enter matrix values rowwise")
A = [[int(input()) for x in range (n1)] for y in range(m1)]
print (A)
C=[]
for x in range(n1):
  a = []
  for y in range(m1):
      a.append(A[y][x])
  C.append(a)
print ("Transpose of a matrix is",C)