name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
count=dict()
lst=list()
handle = open(name)
for line in handle:
    if line.startswith("From"):
        if line.startswith("From:"):
            continue
        l=line.split()
        time=l[5].split(":")
        lst.append(time[0])
      
for name in lst:
    count[name]=count.get(name,0)+1
    
temp=list()
for k,v in count.items():
    temp.append((k,v))
temp.sort()

for k,v in temp:
    print k,v
