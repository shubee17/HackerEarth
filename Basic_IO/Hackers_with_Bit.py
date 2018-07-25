"""
Hackers love bits, so does Alex. Alex has just started his career as hacker and found a special binary array A (containing and 0's and 1's).

In one operation, he can choose any two positions in the array, and can swap their values. He has to perform exactly one operation and maximize the length of the subarray containing only 1s.

Note: The positions can be different or same.

As Alex is a newbie in his field, help him for the same, and output the required length of the sub array containing only

.

Input Format:

First line consists of one integer N, denoting the number of elements in the array.

Second line consists of N space-separated integers, denoting the elements of the array.

Output Format:

Print the required length of the sub array containing only 1s.

Input Constraints:
1 <= N <=100
0 <= A[i] <= 1

SAMPLE INPUT

5
1 1 1 0 1

SAMPLE OUTPUT

4

Explanation

Here N = 5.

And if we choose positions 4th and 5th(1 based indexing in array), we can swap their values and the length of the sub-array (from index 1 to 4) containing only 1's, will be 4.
"""
def Bits(Array):
    maxi = 0
    n = Array.count(1)
    for i in range(len(Array)):
        for j in range(i+1,len(Array)+1):
            x = Array[i:j]
            if (0 in x) and (x.count(0) == 1):
                if len(x) != len(Array) and (n != x.count(1)):
                    if len(x) > maxi:
                        arr = x
                        maxi = len(x)
                    else:
                        pass
            elif(x.count(0) == 0):
                if len(x) > maxi:
                    arr = x
                    maxi = len(x)
                else:
                    pass
            elif(x.count(0) == len(Array)):
                maxi = 0

    print maxi
                
No = int(raw_input())
Array = map(int, raw_input().split())
Array = map(int, Array)
if Array.count(0) == len(Array):
    print 0
else:
    Bits(Array)
