#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import cnames
#colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)

fig, ax = plt.subplots(1, 1, figsize=(12, 14))
ax.xaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))
ax.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}%'.format))

N = 10
daytime = (2,3,4,4,5,6,5,4,3,2)
night = (5,6,2,3,4,1,3,2,7,1)
midnight = (4,4,8,8,9,9,12,12,6,2)

ind = np.arange(N)
width = 0.35
p1 = plt.bar(ind,daytime,width,color ='#CCCC99',edgecolor = "none",align="center")
p2 = plt.bar(ind,night,width, bottom =daytime,color ='#CC9900',edgecolor = "none",align="center")
p3 = plt.bar(ind,midnight,width,bottom = np.array(daytime)+np.array(night),color = '#660000',edgecolor = "none",align="center")

plt.ylabel("Percentage")
plt.title("TEST")
plt.xticks(ind, ('D1','D2','D3','D4','D5','D6','D7','D8','D9','D10'))
plt.yticks(np.arange(0,20,2))
plt.legend((p1[0],p2[0],p3[0]),("daytime","night","midnight"))

plt.show()