''' There are two arrays
       A = (1,2,3,4,5) the result should be
       B = (120,60,40,30,24)
        120 = 2*3*4*5
          60 = 1*3*4*5
          40 = 1*2*4*5
          30 = 1*2*3*5
          24 = 1*2*3*4
'''
num=int(input("Enter list length    "))
a=[]
print("Enter elements")
for i in range(0, num):
    ele = int(input())
    a.append(ele)
print("List is  ", a)
b=[]
c=[]
for i in range(0,num) :
    b= a.copy()
    b[i]=1
    res=1
    for i in range(0,num):
        res=res*b[i]
    c.append(res)
print (c)
