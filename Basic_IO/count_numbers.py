"""
Your task is pretty simple , given a string S , find the total count of numbers present in the digit.

Input

The first line contains T , the number of test cases. The first line of each and every testc ase will contain a integer N , the length of the string . The second line of each and every test case will contain a string S of length N.

Output

For each and every testcase , output the total count of numbers present in the string.

Constraints

    0<T<200

    0<N<10000

SAMPLE INPUT

1
26
sadw96aeafae4awdw2wd100awd

SAMPLE OUTPUT

4

Explanation

For the first test case , the string given is "sadw96aeafae4awdw2wd100awd". There are total of 4 numbers in the string - [96,4,2,100]. So , we output 4.
"""
T = raw_input()
Digits = ['0','1','2','3','4','5','6','7','8','9']
for i in range(int(T)):
    N = raw_input()
    Array = map(str, raw_input())
    arr = []
    cnt = 0
    Array = list(Array)
    for j in range(len(Array)):
        if Array[j] in Digits:
            arr.append(j)
        else:
            pass
    for k in range(len(arr)-1):
        if arr[k] == arr[k+1]-1:
            pass
        else:
            cnt += 1
    print cnt+1
