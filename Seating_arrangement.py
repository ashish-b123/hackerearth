import math
# Write your code here
testcase=int(input())
for i in range(testcase):
    seat=int(input())
    if(seat<109):
        compartment=math.floor(((seat-1)/12))
        firstseat=(compartment*12)+1
        lastseat=firstseat+12
        distance=lastseat-seat
        oppositeseat=firstseat+distance
        position=seat%6
        if(position==0 or position==1):
            print(oppositeseat-1, "WS")
        if(position==2 or position==5):
            print(oppositeseat-1, "MS")
        if(position==3 or position==4):
            print(oppositeseat-1, "AS")
 
