"""
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

Input Format
The first and only line of input contains the String S

Output Format
Print the resultant String on a single line.

Constraints
1 <= S <= 100 where S denotes the length of string S.

SAMPLE INPUT

abcdE

SAMPLE OUTPUT

ABCDe

"""
name = raw_input().split()
save = []
for i in range(len(name[0])):
    if name[0][i].isupper():
        save.append(name[0][i].lower())
    else:
        save.append(name[0][i].upper())
print "".join(save)
