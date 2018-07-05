"""
Given a List of N number a1,a2,a3........an, You have to find smallest number from the List that is repeated in the List exactly K number of times.

Input Format

First Line of Input Contain Single Value N, Size of List
Second Line of Input Contain N Space Separated Integers
Third Line of Input Contain Single Value K

Output Format

Smallest Integer Value That is Repeated Exactly K Number of Time

Constraints

    0 < N < 100001
    0 <= K < 100001
    0 <= ai < 100001

NOTE
There Will Be Atleast One Variable Which Is Repeated K Times

Sample Input:       Output:

5			1
2 2 1 3 1
2
"""

def Rep_k(array,N,K):
	table = {}

	for element in array:
    		if element in table:
        	table[element] += 1
    	elif element != "":
        	table[element] = 1
    	else:
        	table[element] = 0
	for i in table:
    		if table[i] == int(K):
        		print i
        		break

N = raw_input()
array = raw_input().split()
array = map(int, array)
K = raw_input()
Rep_k(array,N,K)
