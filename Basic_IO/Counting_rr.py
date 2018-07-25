"""
Given a string consisting of lower-case letters . Count the total number of substring 'rr' present in the given string.No substring should be counted twice.

Input
Given a string s consisting of lower-case letters.
Output
Print the total number of substring 'rr' present in the given string.
Constraints
1 ≤ strlen(s) ≤ 10^5

SAMPLE INPUT

rrrabc

SAMPLE OUTPUT

2

Explanation

"rr" substring is present two times in given string.
"""

string = list(raw_input())
arr = []
for i in range(len(string)):
    if string[i] == 'r':
        arr.append(i)

cnt = 0
for j in range(len(arr)-1):
    if arr[j] == arr[j+1]-1:
        cnt += 1
print cnt
