#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt

# The slices will be ordered and plotted counter-clockwise.

fig = plt.figure(figsize=[10, 10])
ax = fig.add_subplot(111)

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0)  # explode a slice if required

#plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        #autopct='%1.1f%%', shadow=True)
#draw a circle at the center of pie to make it look like a donut
centre_circle = plt.Circle((0,0),0.5,color='white', fc='white',linewidth=1.00)
plt.text(0,0,"yoyoyo"+"\n"+"yyy",fontsize=12,color ='black',ha='center')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)       
pie_wedge_collection = ax.pie(sizes, colors=colors, labels=labels, labeldistance=1.05);

for pie_wedge in pie_wedge_collection[0]:
    pie_wedge.set_edgecolor('white')
        
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')
plt.show()