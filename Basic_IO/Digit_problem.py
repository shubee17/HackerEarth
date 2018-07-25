"""
This time your task is simple.

Given two integers X and K, find the largest number that can be formed by changing digits at atmost K places in the number X.

Input:

First line of the input contains two integers X and K separated by a single space.

Output:

Print the largest number formed in a single line.

Constraints:
-> 1 <= X <= 10^18
-> 0 <= K <= 9

SAMPLE INPUT

4483 2

SAMPLE OUTPUT

9983

Explanation

First two digits of the number are changed to get the required number.
"""
T = map(str, raw_input().split())
Array = list(T[0])
cnt = 0
for i in range(len(Array)):
    if cnt == int(T[1]):
        print "".join(Array)
        break
    elif Array[i] != '9':
        Array[i] = '9'
        cnt += 1

