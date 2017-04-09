from __future__ import print_function

import sys
import string
from operator import add
from pyspark import SparkContext
from csv import reader

def check_null(line):
	field = line[0].strip()
	if field:
		return "Not null"      #field is not null
	else:
		return "Null"		#field is null



if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_null).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    line.saveAsTextFile("check_null_1.out")

