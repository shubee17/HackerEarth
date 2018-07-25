"""
After doing a lot of hardwork, Monk has finally reached to the second checkpoint. He became such an awesome programmer that he found a way to enter into the Digital World.
While observing the beauty of the new world, he saw two strings A and B of same length N, fighting with each other. String A has the power to take any two characters of its own and swap them, and can perform this swap operation any number of times. Monk being curious, wants to know whether String A can convert itself into String B using swap operations.

INPUT:
First line of input will consists of integer N. Next line will consists of N lowercase English alphabets('a'-'z') denoting string A. Next line will consists of N lowercase English alphabets('a'-'z') denoting string B.

OUTPUT:
Print "YES" (without quotes), if String A can convert itself to string B using this swap operation any number of times, else print "NO" (without quotes).

CONSTRAINTS:
1 ≤ N ≤ 1000
SAMPLE INPUT

4
abcd
bcda

SAMPLE OUTPUT

YES

Explanation

String A ("abcd") can convert itself to String B ("bcda") using sequence of swap operations.
"""
T = raw_input()
string = raw_input()
string1 = raw_input()
string = list(string)
string1 = list(string1)
string = sorted(string)
string1 = sorted(string1)
if string == string1:
    print 'YES'
else:
    print 'NO'
