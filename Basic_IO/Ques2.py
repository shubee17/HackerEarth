"""

    You are given n inputs and two numbers x and y. check whether all the given numbers lies in range of x and y. (x <= y). If the condition is true print YES else print NO.

input Format:
First line contains N, X, Y seperated by space.
Next Line contains n integers.


SAMPLE INPUT

5 1 5
1 2 3 4 5

SAMPLE OUTPUT

YES

"""
T = map(int, raw_input().split())
Array = map(int, raw_input().split())
if (max(Array) == T[2] or max(Array) < T[2]):
    if (min(Array) == T[1] or min(Array) > T[1]):
        print 'YES'
    else:
        print 'NO'
else:
    print 'NO'

