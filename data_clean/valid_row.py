from __future__ import print_function
from datetime import datetime
from dic_record import *


def name_of_type(x):
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
    try:
        datetime.strptime(x, '%m/%d/%Y')
        return "date"
    except ValueError:
        pass
    try:
        datetime.strptime(x, '%H:%M:%S')
        return "time"
    except ValueError:
        pass
    return "string"


def check_type(x):
    return (name_of_type(x[0]) == "int" and name_of_type(x[1]) == "date" or "null" and
            name_of_type(x[2]) == "time" and name_of_type(x[3]) == ("date" or "null") and
            name_of_type(x[4]) == ('time' or 'null') and name_of_type(x[5]) == "date" and
            name_of_type(x[6]) == "int" and name_of_type(x[7]) != "null" and
            name_of_type(x[8]) == "int" and name_of_type(x[9]) != "null" and
            name_of_type(x[10]) != "null" and name_of_type(x[11]) != "null" and
            name_of_type(x[12]) != "null" and name_of_type(x[13]) != "null" and
            name_of_type(x[14]) == "int" and name_of_type(x[19]) == "int" and
            name_of_type(x[20]) == "int" and name_of_type(x[21]) == ("int" or "decimal") and
            name_of_type(x[22]) == ("int"or "decimal") and name_of_type(x[23]) != "null")
# 15, 16, 17, 18 can be string or null, thus no need to check
# the way of judging string is not null. a int is also string here.


def check_1_year(x):
    if not x[1]:
        return "null"
    mm_dd_yyyy = x[1].split("/")
    try:
        year = int(mm_dd_yyyy[2])
        if year >= 2006:
            return "valid"
        else:
            return "invalid"
    except:
        return "error"


def check_1_2_3_4_is_time_valid(x):
    if (not x[1]) or (not x[2]):
        return "null"
    if (not x[3]) and (not x[4]):
        return "valid"
    if x[3] and x[4]:
        from_time = datetime.strptime(x[1] + x[2], '%m/%d/%Y%H:%M:%S')
        to_time = datetime.strptime(x[3] + x[4], '%m/%d/%Y%H:%M:%S')
        if from_time <= to_time:
            return "valid"


def check_6_7_ky_code(x):
    if (not x[6]) or (not x[7]):
        return "null"
    if dic_6_7[x[6]] == x[7]:
        return "valid"


def check_8_9_pd_code(x):
    if (not x[8]) or (not x[9]):
        return "valid"
    if dic_8_9[x[8]] == x[9]:
        return "valid"


def check_validation(x):
    return check_1_year(x) == "valid" and check_1_2_3_4_is_time_valid(x) == "valid" and \
           check_6_7_ky_code(x) == "valid" and check_8_9_pd_code(x) == "valid"


def is_valid(x):
    return check_type(x) and check_validation(x)



