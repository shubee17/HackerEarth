"""
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like Diagram

So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows :

    Window Seat : WS
    Middle Seat : MS
    Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS

    1<=T<=105
    1<=N<=108

SAMPLE INPUT

2
18
40

SAMPLE OUTPUT

19 WS
45 AS

"""
seat,left_seat,right_seat,array = [],[],[],[]

for i in range(1,109):
    array.append(i)

n1,n2 = 0,6
seating = ['WS','MS','AS','AS','MS','WS']
for i in range(0,18):
	if i%2 == 0:
		left_seat = left_seat + array[n1:n2]
		n1 += 6
		n2 += 6
	else:
		right_seat = right_seat + array[n1:n2][::-1]
		n1 += 6
		n2 += 6
	seat = seat + seating

T = raw_input()
for j in range(int(T)):
    No = raw_input()
    for i in range(len(left_seat)):
	    if left_seat[i] == int(No):
		    print right_seat[i],seat[i] 
	    elif right_seat[i] == int(No):
		    print left_seat[i],seat[i]
	    else:
		    pass


