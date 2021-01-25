'''11. Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d    = target? Find all unique quadruplets in the array which gives the sum of target.

 Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
Example :
Given array S = {1 0 -1 0 -2 2}, and target = 0
A solution set is:
(-2, -1, 1, 2)
(-2,  0, 0, 2)
(-1,  0, 0, 1)
'''
num=int(input("Enter list length    "))
a=[]
print("Enter elements")
for i in range(0, num):
    ele = int(input())
    a.append(ele)
print("List is  ", a)
val=0
d=[]
for i in a:
    val=val+i
for i in a:
    b=a.copy()
    b.remove(i)
    for j in b:
        c=b.copy()
        c.remove(j)
        sum=0
        for k in c:
            sum=sum+k
        if (sum==val) :
            c.sort()
            if c not in d:
                print(c)
                d.append(c)



