"""num=int(input("Enter the number:-"))
x=num
y=str(num)
z=len(y)
rem=0
arm=0
while num>0:
    w=int(num)
    rem=num%10
    num=num//10
    arm+=rem**z
if arm==x:
    print('armstrong')
else:
    print('not_armstrong')




for i in range(1000,9999):
    arm=0
    num=i
    while i>0:
        rem=i%10
        i=i//10
        arm+=rem**4
    if arm==num:
        print(arm)"""

def find_length_str(string):
	counter=0
    if type(string)!=str:
        print("Please enter a string...")
    else:
        for s in string:
        	counter += 1
            string += s
        return counter
        
find_length_string('ABCDEFG')

find_length_str("saksham gupta")


    
    
    
    
    
