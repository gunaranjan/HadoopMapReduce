Reducer
#################################
#!/usr/bin/python

import sys

largesales = 0.0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale);

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", largesales
        oldKey = thisKey;
        largesales = 0

    oldKey = thisKey
    if thisSale > largesales:
    largesales = thisSale;

if oldKey != None:
    print oldKey, "\t", largesales