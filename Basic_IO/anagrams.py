"""
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

    test cases,t
    two strings a and b, for each test case

Output:

Desired O/p

Constraints :

string lengths<=10000

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.
SAMPLE INPUT

1
cde
abc

SAMPLE OUTPUT

4

"""

N = raw_input()
for i in range(int(N)):
    str1 = raw_input()
    str2 = raw_input()
    table,table1 = {},{}
    for element in str1:
        if element in table:
            table[element] += 1
        elif element not in table:
            table[element] = 1
        else:
            table[element] = 0
            
    for element in str2:
        if element in table1:
            table1[element] += 1
        elif element not in table1:
            table1[element] = 1
        else:
            table1[element] = 0
     
    cnt = 0        
    for ele in table:
        if ele in table1:
            if table[ele] < table1[ele]:
                cnt = cnt + table[ele]*2
            else:
                cnt = cnt + table1[ele]*2
        else:
            pass
    print (len(str1) + len(str2)) - cnt
