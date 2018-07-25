"""
You are given T test cases. For each test case you are given an integer n. For every test case you need to print a pyramid made up of symbol '*' of height n in new line.
SAMPLE INPUT

2
1
3

SAMPLE OUTPUT

*
  *
 ***
*****

"""
T = raw_input()
for i in range(int(T)):
    N = raw_input()
    space = " "
    n,n1 = 1,1
    for j in range(int(N)):
        print (int(N)-n)*space + n1*'*'
        n += 1
        n1 += 2
