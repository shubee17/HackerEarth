"""
You are given an array of integers A, you need to find the maximum sum that can be obtained by picking some non-empty subset of the array. If there are many such non-empty subsets, choose the one with the maximum number of elements. Print the maximum sum and the number of elements in the chosen subset.

Input:

The first line contains an integer N, denoting the number of elements of the array. Next line contains N space-separated integers, denoting the elements of the array.

Output:

Print 2 space-separated integers, the maximum sum that can be obtained by choosing some subset and the maximum number of elements among all such subsets which have the same maximum sum.


SAMPLE INPUT		Sample Output:

5			6 3
1 2 -4 -2 3

Explanation:

The chosen subset is {1, 2, 3}.
"""

def max_sum(Array):
	maxi = cnt = neg = 0
	for i in range(len(Array)):
		if Array[i] > -1:
			maxi += Array[i]
			cnt += 1
		else:
			neg += 1
			pass
	if neg != len(Array):
		print maxi,cnt
	else:
		maxi = -100000000000
		for i in range(len(Array)):
			if Array[i] > maxi:
				maxi = Array[i]
			else:
				pass
		print maxi,1

N = int(raw_input())
Array = str(raw_input())
Array = map(int, Array.split(" "))
max_sum(Array)
