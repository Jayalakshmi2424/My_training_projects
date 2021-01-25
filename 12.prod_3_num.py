'''12. Given an array A, of N integers A.

Return the highest product possible by multiplying 3 numbers from the array.
Input 1:
A = [1, 2, 3, 4]
Output 1:
24
Explanation 1:
2 * 3 * 4 = 24'''
n = int(input("Enter number of elements : "))
a=[]
print("Enter elements")
for i in range(0, n):
    ele = int(input())
    a.append(ele)
print("List is  ", a)
a.sort(reverse=True)
print("Highest product possible from the list is",a[0]*a[1]*a[2])