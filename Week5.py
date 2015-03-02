smallest = None
largest = None
#print 'Before:', smallest
while True:
    num1 = raw_input("Enter the number")
    try:
            num = int(num1)
            if largest is None or num > largest :
                largest = num
            if smallest is None or num < smallest :
               	smallest = num
    except:
         if num1 == "done":
            break
         else:
            print "Invalid input"
   # print 'Minimum is ',smallest
print 'Maximum is', largest
print 'Minimum is', smallest