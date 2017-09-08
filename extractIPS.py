print("\n")
print("###############################################")
print("#                 KTIMEZ                      #")
print("#          visit us on ktimez.com             #")
print("#          Author: @BahatiPhill               #")
print("###############################################")
print("\n")
import sys
import re
import os
import operator
from collections import OrderedDict


try:
    if sys.argv[1:]:
        print ("File: %s" % (sys.argv[1]))
        logfile = sys.argv[1]
    else:
        logfile = input("Shyiramo izina rya logfile (e.g: /tmp/logIPs.txt): ")
    try:
        file = open(logfile, "r")
        ips = []
        Ips_with_most_hits = {}
        for text in file.readlines():
           text = text.rstrip()
           found = re.findall(r'(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})',text)
           if found:
               ips.extend(found)

        for ip in ips:
            if not ip in Ips_with_most_hits:
                Ips_with_most_hits[ip] = 1
            if ip in Ips_with_most_hits:
                Ips_with_most_hits[ip] = Ips_with_most_hits[ip] + 1

        Ips_with_most_hits = OrderedDict(sorted(Ips_with_most_hits.items(), key=lambda t: t[1]))
        Save_location = os.getcwd()
        fp = open(Save_location+'/IPs_and_times_TheyHit.txt','w')
     
        for key,value in Ips_with_most_hits.items():
            fp.write(str(key) + '  ==>  ' + str(value) + '\n')

        fp.close()
        print('done')
    finally:
        file.close()
except IOError:
        print ("I/O Error(%s) : %s" % (IOError))