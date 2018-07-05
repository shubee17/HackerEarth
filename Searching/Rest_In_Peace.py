"""
The grandest stage of all, Wrestlemania XXX recently happened. And with it, happened one of the biggest heartbreaks for the WWE fans around the world. The Undertaker's undefeated streak was finally over.

Now as an Undertaker fan, you're disappointed, disheartened and shattered to pieces. And Little Jhool doesn't want to upset you in any way possible. (After all you are his only friend, true friend!) Little Jhool knows that you're still sensitive to the loss, so he decides to help you out.

Every time you come across a number, Little Jhool carefully manipulates it. He doesn't want you to face numbers which have "21" as a part of them. Or, in the worst case possible, are divisible by 21.

If you end up facing such a number you feel sad... and no one wants that - because you start chanting "The streak is broken!" , if the number doesn't make you feel sad, you say, "The streak lives still in our heart!"

Help Little Jhool so that he can help you!

Input Format:
The first line contains a number, t, denoting the number of test cases.
After that, for t lines there is one number in every line.

Output Format:
Print the required string, depending on how the number will make you feel.

Constraints:
1 ≤ t ≤ 100
1 ≤ n ≤ 1000000 

Sample Input:		Output:

3			The streak lives still in our heart!
120			The streak is broken!
121			The streak is broken!
231"""

T = raw_input()
for i in range(int(T)):
    N = raw_input()
    list1 = []
    if int(N)%21 == 0:
        print 'The streak is broken!'
    else:
        N = map(int, N)
        for k in range(len(N)):
            for k1 in range(k+1,len(N)+1):
                x = "".join(map(str, N[k:k1]))
                list1.append(x)
        if '21' in list1:
            print 'The streak is broken!'
        else:
            print 'The streak lives still in our heart!'
