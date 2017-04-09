from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_law_cat_cd(line):
	field = line[11].strip()
	if field:
		if field == "FELONY" or field == "MISDEMEANOR" or field == "VIOLATION":
			return field
		else:
			return ("INVALID",field)
	else:
		return "NULL"


if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_law_cat_cd).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    line.saveAsTextFile("check_law_cat_cd.out")

    sc.stop()
 