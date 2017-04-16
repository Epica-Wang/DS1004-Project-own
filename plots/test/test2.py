#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv

x = [2006,2007,2008,2009,2010,2011]
with open('test.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		y = []
		y = row[1:10]
		line = plt.plot(x,y, label=row[0])
plt.xlabel('year')
plt.ylabel('amount')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()