"""
code by Xinan Zhang
for interview questions--Deep learning on traffic sign detection using public data.
"""
"""
This file is used for generating anchor boxes with K-means++ and K-means
Input: ground truth
Output: anchor boxes
ref: https://github.com/PaulChongPeng/darknet/blob/master/tools/k_means_yolo.py
"""
from PIL import Image
import numpy as np
from pathlib import Path
import os
import seaborn as sns
import matplotlib.pyplot as plt

root = os.getcwd()
train = root+'/train'
test = root+'/test'
gt_file = root+'/gt.txt'
raw_dataset = root

class Box():
	def __init__(self, element):
		w = int(element[3]) - int(element[1])
		h = -int(element[2]) + int(element[4])
		self.x = 0
		self.y = 0
		self.w = int(w/1360*1280)
		self.h = int(h/800*736)

def overlap(x1, len1, x2, len2):

    return min(len1, len2)

def box_intersection(a, b):
    w = overlap(a.x, a.w, b.x, b.w)
    h = overlap(a.y, a.h, b.y, b.h)
    if w < 0 or h < 0:
        return 0

    area = w * h
    return area

def box_union(a, b):
    i = box_intersection(a, b)
    u = a.w * a.h + b.w * b.h - i
    return u

def box_iou(a, b):
    return box_intersection(a, b) / box_union(a, b)

def init_centroids(boxes,n_anchors):
    centroids = []
    boxes_num = len(boxes)

    centroid_index = np.random.choice(boxes_num, 1)[0]
    centroids.append(boxes[centroid_index])

    print(centroids[0].w,centroids[0].h)

    for centroid_index in range(0,n_anchors-1):

        sum_distance = 0
        distance_thresh = 0
        distance_list = []
        cur_sum = 0

        for box in boxes:
            min_distance = 1
            for centroid_i, centroid in enumerate(centroids):
                distance = (1 - box_iou(box, centroid))
                if distance < min_distance:
                    min_distance = distance
            sum_distance += min_distance
            distance_list.append(min_distance)

        distance_thresh = sum_distance*np.random.random()

        for i in range(0,boxes_num):
            cur_sum += distance_list[i]
            if cur_sum > distance_thresh:
                centroids.append(boxes[i])
                print(boxes[i].w, boxes[i].h)
                break

    return centroids

def get_wh(filename):

	root = os.getcwd()
	with open(root+'/'+filename,'r') as f:
		gt_lines = f.readlines()

	global all_wh
	for line in gt_lines:
		element = line.split(';')
		box = Box(element)
		all_wh.append(box)
	# print(len(gt_lines))

def do_kmeans(n_anchors, boxes, centroids):
    loss = 0
    groups = []
    new_centroids = []
    for i in range(n_anchors):
        groups.append([])
        new_centroids.append(Box([0,0,0,0,0]))

    for box in boxes:
        min_distance = 1
        group_index = 0
        for centroid_index, centroid in enumerate(centroids):
            distance = (1 - box_iou(box, centroid))
            if distance < min_distance:
                min_distance = distance
                group_index = centroid_index
        groups[group_index].append(box)
        loss += min_distance
        new_centroids[group_index].w += box.w
        new_centroids[group_index].h += box.h

    for i in range(n_anchors):
        new_centroids[i].w /= len(groups[i])
        new_centroids[i].h /= len(groups[i])

    return new_centroids, groups, loss


all_wh = list()
get_wh('gt.txt')
# sns_data = dict()
# sns_data['b_w'] = [x.w for x in all_wh]
# sns_data['b_h'] = [x.h for x in all_wh]
# sns.jointplot(x="b_w", y="b_h", data=sns_data)
# plt.show()
centroids = init_centroids(all_wh, 9)
"""
init values:
    21 20
    47 46
    37 36
    100 95
    21 21
    29 28
    111 117
    58 57
    16 16
"""
loss = 0

for _ in range(200):
	centroids, groups, loss = do_kmeans(9, all_wh, centroids)

print("k-means result")
for centroid in centroids:
        print(centroid.w, centroid.h)
        print('')
"""
     20.64748201438849 20.820143884892087

     46.76878612716763 45.092485549132945

     37.973544973544975 36.44444444444444

     76.40506329113924 72.55696202531645

     25.65193370165746 24.425414364640883

     31.22897196261682 30.299065420560748

    104.61702127659575 99.04255319148936

     59.713178294573645 56.86821705426357

     17.193548387096776 17.06451612903226
"""
#17,17,  20,20,  25,24,  31,30,  37,36,  46,45,  59,56,  76,72,  104,99
print('loss:', loss)
"""
loss: 130.15001959543366
"""
x = [x.w for x in centroids]
y = [x.h for x in centroids]
# scatter = {'b_w':x, 'b_h':y}
# sns.jointplot(x="b_w", y="b_h", data=sns_data)
# plt.scatter(x, y, color = "red", marker = "*")
# sns.scatterplot( x="b_w", y="b_h",data=scatter)
#plt.show()
