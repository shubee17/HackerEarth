"""
Given an array of integers . Check if all the numbers between minimum and maximum number in array exist's within the array .

Print 'YES' if numbers exist otherwise print 'NO'(without quotes).

Input:

Integer N denoting size of array

Next line contains N space separated integers denoting elements in array

Output:

Output your answer

Constraints:

1<= N <= 1000

1<= a[i] <= 100
SAMPLE INPUT

6
4 2 1 3 5 6

SAMPLE OUTPUT

YES

"""
T = raw_input()
Array = map(int, raw_input().split())
Array = sorted(Array)
Array = list(set(Array))
flag = 0
if len(Array) == 1:
    print 'YES'
else:
    for i in range(len(Array)-1):
        if Array[i] == Array[i+1] - 1:
            flag = 1
        else:
            print 'NO'
            break
    if flag == 1:
        print 'YES'
    else:
        pass
