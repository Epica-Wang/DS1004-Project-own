from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_time(line):   # XX:XX:XX
	time_pattern = re.compile("(0[0-9]|1[0-9]|2[0-3])[:](0[0-9]|[1-5][0-9])[:](0[0-9]|[1-9][0-9])")

	field = line[2].strip()
	if time_pattern.match(field) is not None:
		return "VALID"
	elif field:
		return ("INVALID", field)
	else:
		return "NULL"


if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_time).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    line.saveAsTextFile("check_time.out")

    sc.stop()
