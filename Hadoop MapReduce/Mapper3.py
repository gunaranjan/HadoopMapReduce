import sys
import re

#fname = "C:\\Users\\hp rdrl4\\Desktop\\sample.txt"
#with open(fname) as f:
     #print f.readlines()
#with open(fname, "r") as ins:
array = []
regex = '([\d.]+) [a-z]*-[[a-z]* .+\[.+] \"[A-Z]+ (.*) [A-Z]+.+" (\d+)(.*)';
for line in sys.stdin:
    array.append(line)
    data = re.match(regex, line).groups();
    ip, addpath, stat, sizeb= data;
    print "{0}\t{1}".format(ip,addpath);
    #print dat
