"""

Coders here is a simple task for you, you have given an array of size N and an integer M.
Your task is to calculate the difference between maximum sum and minimum sum of N-M elements of the given array.

Constraints:
1<=t<=10
1<=n<=1000
1<=a[i]<=1000

Input:
First line contains an integer T denoting the number of testcases.
First line of every testcase contains two integer N and M.
Next line contains N space separated integers denoting the elements of array
Output:
For every test case print your answer in new line


SAMPLE INPUT

1
5 1
1 2 3 4 5

SAMPLE OUTPUT

4

Explanation

M is 1 and N is 5 so you have to calculate maximum and minimum sum using (5-1 =) 4 elements.
Maximum sum using the 4 elements would be (2+3+4+5=)14.
Minimum sum using the 4 elements would be (1+2+3+4=)10.
Difference will be 14-10=4.
"""

def bubble_sort(array):
    for j in range(len(array)):
        for k in range(len(array)-1,j,-1):
            if array[k] < array[k-1]:
                swap(array,k,k-1)
    a = N[0] - N[1]
    b = array[::-1]
    x = b[0:int(a)]           
    y = array[0:int(a)]
    print sum(x) - sum(y)
def swap(array,x,y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

T = raw_input()
for i in range(int(T)):
    N = raw_input().split(" ")
    N = map(int, N)
    array = raw_input().split(" ")
    array = filter(None, array)
    array = map(int, array)
    bubble_sort(array)
