from __future__ import print_function

import sys
import string
import re
from operator import add
from pyspark import SparkContext
from csv import reader

def check_date(line):   # mm/dd/yyyy
	date_pattern1 = re.compile("(0[13578]|1[02])[/](0[1-9]|[12][0-9]|3[01])[/](19|20)\d\d$")
	date_pattern2 = re.compile("(0[4679]|11)[/](0[1-9]|[12][0-9]|30)[/](19|20)\d\d$")
	date_pattern3 = re.compile("(02)[/](0[1-9]|1[0-9]|2[0-8])[/](19|20)\d\d$")
	date_pattern4 = re.compile("(02)[/](29)[/](19|20)\d\d$")
	field = line[1].strip()
	if date_pattern1.match(field) is not None:
		return "VALID"      #field is valid
	elif date_pattern2.match(field) is not None:
		return "VALID"		#field is valid
	elif date_pattern3.match(field) is not None:
		return "VALID"
	elif date_pattern4.match(field) is not None:
			mm_dd_yyyy = field.split("/")
			try:
				year = int(mm_dd_yyyy[2])
				if year % 4 ==0:
					return "VALID"
				else:
					return ("INVALID", field)	# field is 02/29/yyyy but the year is not the leap year
			except:
				return ("INVALID",field)
	elif field:                  # field is not valid but not null
		return ("INVALID", field)
	else:						# field is null
		return "NULL"




if __name__ == "__main__":
	if len(sys.argv) != 2:
        print("Usage: bigram <file>", file=sys.stderr)
        exit(-1)
    sc = SparkContext()
    line = sc.textFile(sys.argv[1], 1)
    line = line.mapPartitions(lambda x: reader(x))
    line = line.map(check_date).map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    line.saveAsTextFile("check_date.out")

    sc.stop()
