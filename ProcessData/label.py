"""
code by Xinan Zhang
for interview questions--Deep learning on traffic sign detection using public data.
"""
"""
This file is used for resizing the raw images for training and test
Input: raw gt.txt
Output: new gt for each image
"""
import os

root = os.getcwd()
dataset = root
train = dataset + '/train/'
test = dataset + '/test/'

def get_gt(filename):
	
	with open(root+'/'+filename,'r') as f:
		gt_lines = f.readlines()

	return gt_lines

def process_gt(filename):
	# <object-class> <x_center> <y_center> <width> <height>
	gt_lines = get_gt(filename)
	for gt_line in gt_lines:
		line = gt_line.strip()
		element = line.split(';')
		x = (int(element[1])+int(element[3]))/2 /1360
		y = (int(element[2])+int(element[4]))/2 /800
		w = (int(element[3])-int(element[1]))/1360
		h = (int(element[4])-int(element[2]))/800
		txt_name = element[0].split('.')[0] + '.txt'
		cla = element[-1]
		string = f'0 {x} {y} {w} {h}\n'
		# print(string)
		create_txt(txt_name, string)
		# break

def create_txt(txt_name, string):
	image_index = int(txt_name.split('.')[0])
	if image_index<600:
		with open(train+txt_name, 'a+') as f:
			f.write(string)
	else:
		with open(test+txt_name, 'a+') as f:
			f.write(string)
for i in range(900):
    file_name = '{:05d}'.format(i) + '.txt'
    if i < 600:
        with open(train+file_name, 'a+') as f:
            pass
    else:
        with open(test+file_name, 'a+') as f:
            pass
process_gt('gt.txt')
