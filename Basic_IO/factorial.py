"""
You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

Input Format:
The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

Output Format
Output a single line denoting the factorial of the number N.

Constraints
1 <= N <= 10

SAMPLE INPUT

2

SAMPLE OUTPUT

2

"""

N = raw_input()
fact = 1
for i in range(1,int(N)+1):
    fact = fact*i
print fact

