import matplotlib
import pylab
import csv


def csvToList(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
    return [float(x) for x in l[0]]

#plot random dataset
"""
x = csvToList('./data/randomdata_x.csv')
y = csvToList('./data/randomdata_y.csv')

matplotlib.pyplot.scatter(x,y,color='blue',s=55,edgecolor='none')
"""

x0 = csvToList('./data/test1_cluster_0_x.csv')
y0 = csvToList('./data/test1_cluster_0_y.csv')
matplotlib.pyplot.scatter(x0,y0,color='blue',s=55,edgecolor='none')

x1 = csvToList('./data/test1_cluster_1_x.csv')
y1 = csvToList('./data/test1_cluster_1_y.csv')
matplotlib.pyplot.scatter(x1,y1,color='black',s=55,edgecolor='none')

x2 = csvToList('./data/test1_cluster_2_x.csv')
y2 = csvToList('./data/test1_cluster_2_y.csv')
matplotlib.pyplot.scatter(x2,y2,color='yellow',s=55,edgecolor='none')

x3 = csvToList('./data/test1_cluster_3_x.csv')
y3 = csvToList('./data/test1_cluster_3_y.csv')
matplotlib.pyplot.scatter(x3,y3,color='green',s=55,edgecolor='none')

x4 = csvToList('./data/test1_cluster_4_x.csv')
y4 = csvToList('./data/test1_cluster_4_y.csv')
matplotlib.pyplot.scatter(x4,y4,color='coral',s=55,edgecolor='none')




x_center = csvToList('./data/test1_result_x.csv')
y_center = csvToList('./data/test1_result_y.csv')
matplotlib.pyplot.scatter(x_center,y_center,marker = '^', color='Red',s=80,edgecolor='none')
matplotlib.pyplot.show()