# YOLOv3_GTSDB

In this project, a traffic-sign detector will be trained on **GTSDB**, which is a public dataset containing 900 German road images(https://benchmark.ini.rub.de/gtsdb_dataset.html). The detetor will be trained on **YOLOv3** network(https://github.com/AlexeyAB/darknet).  

This project is divided into two parts. In the first part, **GTSDB** is pre-processed to form the dataset of **YOLOv3** network training. The second part will deal with training details. The first part is recommended to be done in pc and the second part will be conducted in **Colab** <a href="https://colab.research.google.com/drive/1hGvWJCLaSg6j4KQLbXoQrWwKnhv0FgZE?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>.

Here's a demo output image: 

```<label> : <confidence of detector>```

<img src="https://github.com/NantonZZZ/YOLOv3_GTSDB/blob/master/00051.jpg" width="65%"/>

## Part 1: Data Preparation

In this part, data is processed to form the dataset for further network training. The whole raw dataset(a zip file), including training set, test set and ground truth file could be downloaded from this url: https://benchmark.ini.rub.de/gtsdb_dataset.html. The whole file could be around 1.2G in total so it is recommended to process the data in PC rather than uploading it to online VMs before processing it.  

A few steps are included in this part:

1. Download the full raw data from https://benchmark.ini.rub.de/gtsdb_dataset.html and unzip it in your PC. You will get a folder named as 'FullIJCNN2013'
2. Download this repo/ProcessData on https://github.com/NantonZZZ/YOLOv3_GTSDB/tree/master/ProcessData and drag all the files to the above folder 'FullIJCNN2013'
3. Go to folder 'FullIJCNN2013'. Since we will use python scripts to process data, install the required libriries: ```pip3 install -r requirements.txt```
4. Run ```python3 resizeImg.py``` and ```python3 label.py```. There will be two new folders 'train' and 'test' in 'FullIJCNN2013', each of which contains resized jpg images and their corresponding ground-truth labels for training and test. Details will be found in comments in these python files.
5. Finally, we can zip 'train' and 'test' folders to get two zip files. Other required files are ready in this repo. Explanation and requirements could be found here: https://github.com/AlexeyAB/darknet

Now, we are ready for training!

## Part 2: Detector Training

In this part, training will be done in **Colab** which provides online GPU resources. Before we go there, we have to upload the two zip files obtained in **Part 1** to our own google drive, which our Colab could get easy access to. Now, let's go--><a href="https://colab.research.google.com/drive/1hGvWJCLaSg6j4KQLbXoQrWwKnhv0FgZE?usp=sharing"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
