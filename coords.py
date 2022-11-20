import pandas as pd
from math import sqrt

data = pd.read_csv("Dataset/Dataset.csv", sep=";", encoding = 'ISO-8859-1')

xp1 = (min(list(data['X'])), 0)
xp2 = (max(list(data['X'])), 1)

mx = (xp2[1] - xp1[1]) / (xp2[0] - xp1[0])
normalize_x = lambda x: mx * (x - xp1[0]) + xp1[1]

yp1 = (min(list(data['Y'])), 0)
yp2 = (max(list(data['Y'])), 1)

my = (yp2[1] - yp1[1]) / (yp2[0] - yp1[0])
normalize_y = lambda x: my * (x - yp1[0]) + yp1[1]


total_w = xp2[0] - xp1[0]
total_h = yp2[0] - yp1[0]

data['X'] = data['X'].map(normalize_x)
data['Y'] = data['Y'].map(normalize_y)

x = list(data['X'])
y = list(data['Y'])

