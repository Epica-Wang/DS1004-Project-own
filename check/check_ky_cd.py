from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_ky_cd(line):
	field = line[6].strip()
	if field:
		return field
	else:
		return "NULL"


if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_ky_cd).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x: x[1],False)
    line.saveAsTextFile("check_ky_cd.out")

    sc.stop()