from __future__ import print_function
from csv import reader
from pyspark import SparkContext


def name_of_type(x):
    # x = x.strip()
    if not x:
        return "null"
    try:
        int(x)
        return "int"
    except ValueError:
        pass
    try:
        float(x)
        return "decimal"
    except ValueError:
        pass

    return "string"

if __name__ == "__main__":
    result = []
    # 测试某一列，修改i的值
    # i = 1
    # for j in range(1):
    #测试所有列，修改range范围
    for i in range(24):
        sc = SparkContext()
        lines = sc.textFile("/Users/dai/Documents/DS1004/md3797/src/step1/ten_lines_data.csv", 1)
        words = lines.mapPartitions(lambda x: reader(x)).\
            map(lambda x : (name_of_type(x[i]), 1)).\
            reduceByKey(lambda x, y: x + y).collect()
        result.append(('This is type information of column ', i))
        for (word, count) in words:
            result.append((word, count))
            print("%s: %i" % (word, count))
        sc.stop()
    # 用一个list存结果，避免存24个文件的尴尬
    # To do, 把list存到一个txt里。
    print(result)
