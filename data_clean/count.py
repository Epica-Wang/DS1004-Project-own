from function_sets import *

from pyspark import SparkContext
from csv import reader

def save_result(cells, i):
    with open("result.txt", "a") as f:
        f.write("------------------\nColumn %s contains: \n" % i)
        for (cell, count) in cells:
            f.write("%s: %i\n" % (cell, count))


# column 11
def law_cat_cd(col):
    sc = SparkContext()
    lines = sc.textFile(file_name, 1)
    cells = lines.mapPartitions(lambda x: reader(x)).map(lambda x: (check_law_cat_cd(x[col]), 1)).reduceByKey(lambda x, y: x + y).collect()
    save_result(cells, col)
    sc.stop()


# column 13
def boro_nm(col):
    sc = SparkContext()
    lines = sc.textFile(file_name, 1)
    cells = lines.mapPartitions(lambda x: reader(x)). \
        map(lambda x: (check_boro_nm(x[col]), 1)).reduceByKey(lambda x, y: x + y).collect()
    save_result(cells, col)
    sc.stop()


if __name__ == "__main__":
    file_name = "ten_thousand_lines_data.csv"
    with open("result.txt", "w") as f:
        f.write("Type Information: \n")
    for i in range(4):
        sc = SparkContext()
        lines = sc.textFile(file_name, 1)
        cells = lines.mapPartitions(lambda x: reader(x)). \
            map(lambda x: (name_of_type(x[i]), 1)).reduceByKey(lambda x, y: x + y).collect()
        with open("result.txt", "a") as f:
            f.write("------------------\nColumn %s contains: \n" % i)
            for (cell, count) in cells:
                f.write("%s, %i\n" % (cell, count))
        sc.stop()
    with open("result.txt", "a") as f:
        f.write("\n\nValue Information: \n")

    law_cat_cd(11)
    boro_nm(13)
