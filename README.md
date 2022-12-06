# Armstrong-number
for i in range(1000,9999):
    arm=0
    num=i
    while i>0:
        rem=i%10
        i=i//10
        arm+=rem**4
    if arm==num:
        print(arm)
