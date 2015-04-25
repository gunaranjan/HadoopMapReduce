#!/usr/bin/python

import sys

largesales = 0.0;
oldKey = None
count = 0;

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale = float(thisSale);
    largesales = largesales + thisSale;
    count = count + 1;

if oldKey == None:
    print count, "\t", largesales