from __future__ import print_function
from datetime import datetime


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


def check_ky_cd(line):
    field = line[6].strip()
    if field:
        return field
    else:
        return "NULL"


def check_law_cat_cd(x):
    if x:
        if x == "FELONY" or x == "MISDEMEANOR" or x == "VIOLATION":
            return x
        else:
            return ("INVALID",x)
    else:
        return "NULL"


def check_boro_nm(x):
    if x:
        if x == "MANHATTAN" or x == "BROOKLYN" or x == "QUEENS" or x == "BRONX" or x == "STATEN ISLAND":
            return x
        else:
            return ("INVALID",x)
    else:
        return "NULL"