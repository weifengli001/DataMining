import matplotlib
import pylab
import csv


def csvToList(filepath):
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
    return [float(x) for x in l[0]]

#plot random dataset

x = csvToList('./data/Gaussian_x.csv')
y = csvToList('./data/Gaussian_y.csv')

matplotlib.pyplot.scatter(x,y,color='blue',s=55,edgecolor='none')


centroid_x = csvToList('./data/Gaussian_centroids_x.csv')
centroid_y = csvToList('./data/Gaussian_centroids_y.csv')

matplotlib.pyplot.scatter(centroid_x,centroid_y,color='red',s=80,edgecolor='none')



pre_centroid_x = csvToList('./data/test2_result_x.csv')
pre_centroid_y = csvToList('./data/test2_result_y.csv')

matplotlib.pyplot.scatter(pre_centroid_x,pre_centroid_y, marker='^',color='cyan',s=80,edgecolor='none')


matplotlib.pyplot.show()

