
'''9. Given the array of strings A,
you need to find the longest string S which is the prefix of ALL the strings in the array.

Longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
and S2.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc" :
Ex: ‘ab’,’ac’,’adf’,’abcd’ is ‘a’'''
arr = ["abcdefgh" , "abcefgh","abgs" ]

if not arr:
  print("There's no common prefix for the given array")

elif len(arr) == 1:
  print("Longest common prefix:", arr[0])
else:
  arr.sort()
  result = ""
  for i in range(len(arr[0])):
    if arr[0][i] == arr[-1][i]:
          result += arr[0][i]

    else:
          break
  print("Longest common prefix is", result)