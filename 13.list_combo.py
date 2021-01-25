'''13. Write a function that takes a list L and returns a sublist of size N of that list. Assume that the index is in a decreasing order.you cannot go frontwards
Ex: [1,2,3,4]
N = 3

Ans:
[4,3,2]
[4,3,1]
[3,2,1]
[4,2,1]'''

def list_combo(lst, k, ans):
    if len(lst) == k:
        if lst not in ans:
            ans.append(lst)
        return ans
    if len(lst) < k or k == 0:
        return [[]]
    for i in range(4,0,-1):
        a = lst.copy()
        a.remove(i)
        list_combo(a, k, ans)
    print (ans)
list_combo([1,2,3,4], 3,[])