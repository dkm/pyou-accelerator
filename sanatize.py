import sys
import math
import datetime

f = open(sys.argv[1], "r")

for l in f.xreadlines():
    d = l.split()
    dt = datetime.datetime.strptime(d[0], "%Y-%m-%dT%H:%M:%S.%f")
    ms = dt.minute*60*1000*1000 + dt.second * 1000 * 1000 + dt.microsecond
    norm = math.sqrt(float(d[2])**2 + float(d[3])**2 + float(d[4])**2)
    r = [d[0]] + [str(ms)] + d[1:4] + [str(norm)]
    print " ".join(r)
