def computepay(h,r):
    if(h<=40):
        return h*r
    elif(h>40):
        return 40*r+((h-40)*(1.5*r))



hrs=raw_input("Enter the Hours")
h=float(hrs)
rate=raw_input("Enter the rate")
r=float(rate)

print "Pay :",computepay(h,r)

