# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:14:39 2024

@author: dell
"""

import matplotlib.pyplot as pyplot
#plt.plot([1,2,3,4,5],[10,20,30,40,50])
#plt.plot([1,2,3,4,5],[10,20,30,40,50],'ro')
#plt.plot([1,2,3,4,5],[10,20,30,40,50],'r--')
#plt.plot([1,2,3,4,5],[10,20,30,40,50],'bs')
#plt.plot([1,2,3,4,5],[10,20,30,40,50],'g^')
#plt.show()
# Set up the data
x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 2, 6, 14, 30, 43, 75]
# Set the axes headings
pyplot.ylabel('Speed', fontsize=12)
pyplot.xlabel('Time', fontsize=12)
# Set the title
pyplot.title("Speed v Time")
# Plot and display the graph
# Using blue circles for markers ('bo')
# and a solid line ('-')
pyplot.plot(x, y, 'bo-')
pyplot.show()