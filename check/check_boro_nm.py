from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_boro_nm(line):
	field = line[13].strip()
	if field:
		if field == "MANHATTAN" or field == "BROOKLYN" or field == "QUEENS" or field == "BRONX" or field == "STATEN ISLAND":
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
    line = line.map(check_boro_nm).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    line.saveAsTextFile("check_boro_nm.out")

    sc.stop()