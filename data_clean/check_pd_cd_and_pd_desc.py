from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_pd_cd_and_pd_desc(line):
	pd_cd = line[8].strip()
    pd_desc = line[9].strip()
	if pd_cd and pd_desc:
		return (pd_cd,pd_desc)
	else:
		return "NULL"
 
pdcd_desc={}    # a global dictionary to store valid pdcd and pd_desc pair

def define_valid_pd_cd_and_pd_desc(line):
    global pdcd_desc
    pd_cd = line[0][0].strip()
    pd_desc = line[0][1].strip()
    if pd_cd in pdcd_desc:
        pass
    else:
        pdcd_desc[pd_cd] = pd_desc
        return (pd_cd,pd_desc)    


if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_pd_cd_and_pd_desc).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x: x[0][0], False).map(define_valid_pd_cd_and_pd_desc)
    line.saveAsTextFile("define_valid_pd_cd_and_pd_desc.out")

    sc.stop()