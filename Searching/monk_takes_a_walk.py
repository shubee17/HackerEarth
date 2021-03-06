"""

Today, Monk went for a walk in a garden. There are many trees in the garden and each tree has an English alphabet on it. While Monk was walking, he noticed that all trees with vowels on it are not in good state. He decided to take care of them. So, he asked you to tell him the count of such trees in the garden.
Note : The following letters are vowels: 'A', 'E', 'I', 'O', 'U' ,'a','e','i','o' and 'u'.

Input:
The first line consists of an integer T denoting the number of test cases.
Each test case consists of only one string, each character of string denoting the alphabet (may be lowercase or uppercase) on a tree in the garden.

Output:
For each test case, print the count in a new line.

Constraints:

SAMPLE INPUT		Sample Output:

2			2
nBBZLaosnm		1
JHkIsnZtTL

 Explanation

In test case 1, a and o are the only vowels. So, count=2
"""

N = raw_input()
vowel = ['a','e','i','o','u']
cnt = 0
for i in range(int(N)):
    name = raw_input().lower()
    for j in range(len(name)):
        if name[j] in vowel:
            cnt += 1
    print cnt
    cnt = 0

