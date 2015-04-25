#Reducer1.py
import sys
count = 0;
oldkey = None;
    
for li in sys.stdin:
    dat = li.strip().split("\t")
    if len(dat)!=2:
        continue;
        
    thisvalue, thiskey = dat;
        
    if oldkey and oldkey!=thiskey:
        print oldkey, "\t", count;
        oldkey = thiskey;
        count = 0;
    oldkey = thiskey;
    count = count + 1;
if oldkey!= None:
    print oldkey, "\t", count;