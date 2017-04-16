from __future__ import print_function
from pyspark import SparkContext
from csv import reader

def check_pd_cd_and_pd_desc(x):
	pd_cd = x[8].strip()
	pd_desc = x[9].strip()
	if pd_cd and pd_desc:
		return pd_cd, pd_desc
	else:
		return ("null value", "invalid")

def define_valid_pd_cd_and_pd_desc(x, ky_cd_dict):
	pd_cd = x[0][0]
	pd_desc = x[0][1]
	# if pd_cd in ky_cd_dict:
	# 	pass
	# else:
	# 	ky_cd_dict[pd_cd] = pd_desc
	# 	return pd_cd, pd_desc

	ky_cd_dict[pd_cd] = pd_desc
	return pd_cd, pd_desc


def dic_ky_cd(lines, ky_cd_dict):
	line = lines.mapPartitions(lambda x: reader(x)).map(lambda x: check_pd_cd_and_pd_desc(x)).map(lambda x: (x, 1)). \
		reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[0][0], False). \
		map(lambda x: define_valid_pd_cd_and_pd_desc(x, ky_cd_dict)).sortBy(lambda x: x[0]).collect()
	# for element in line:
	# 	ky_cd_dict[element[0]] = element[1]
	print(ky_cd_dict)
	return ky_cd_dict


if __name__ == "__main__":
	file_name = "ten_thousand_lines_data.csv"
	sc = SparkContext()
	lines = sc.textFile(file_name, 1)
	ky_cd_dict = {}
	ky_cd_dict = dic_ky_cd(lines, ky_cd_dict)
	sc.stop()
	print(ky_cd_dict)
