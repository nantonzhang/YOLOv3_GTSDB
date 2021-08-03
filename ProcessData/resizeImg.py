"""
code by Xinan Zhang
for interview questions--Deep learning on traffic sign detection using public data.
"""
"""
This file is used for resizing the raw images for training and test
Input: raw images
Output: new dataset
"""
from PIL import Image
import numpy as np
from pathlib import Path
import os

root = os.getcwd()
train = root+'/train'
test = root+'/test'
gt_file = root+'/gt.txt'
raw_dataset = root

if os.path.exists(train):
	print(train)
else:
	os.makedirs(train)

if os.path.exists(test):
	print(test)
else:
	os.makedirs(test)

for i in range(900):
	img_name = '{:05d}'.format(i) + '.ppm'

	img = Image.open(root+'/'+img_name)
	out = img.resize((1280, 736),Image.ANTIALIAS)
	# (1280, 763) is the new size for YOLO training

	if i < 600:
		img_path = 'train/'+img_name[:-3]+'jpg'
		with open('train.txt', 'a+') as f:
			f.write('train/'+img_name[:-3]+'jpg\n')
	else:
		img_path = 'test/'+img_name[:-3]+'jpg'
		with open('test.txt', 'a+') as f:
			f.write('test/'+img_name[:-3]+'jpg\n')
	# According to the data intro, 600 pics are for training
	# The rest is for test

	out.save(img_path)
