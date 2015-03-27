name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
list=list()
for line in handle:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        l=line.split()
        list.append(l[1])

dicts = dict()
#Following method checks the entry in the dictonary and if found will retrieve the value and will add 1 to it, else will return 0  and then will add 1 to the count.
for name in list:
    dicts[name] = dicts.get(name,0)+1

bigcount=None
bigname=None
#dicts.items() : This method returns a list of tuple pairs.
#Example : dict = {'Name': 'Zara', 'Age': 7}
#print "Value : %s" %  dict.items()
#Value : [('Age', 7), ('Name', 'Zara')]
#
for na,key in dicts.items():
    if key is None or key>bigcount:
        bigname=na
        bigcount=key
print bigname,bigcount