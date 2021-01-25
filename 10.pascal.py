'''10.Given numRows = 5,.

Generate
A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
.
-------------------------------------------------------------------------------------------------'''
def printPascal(n):
    for line in range(1, n + 1):
        C = 1
        for i in range(1, line + 1):
            print(C, end=" ")
            C = int((C * (line - i)) / i)
        print("")
n = 5
printPascal(n)
