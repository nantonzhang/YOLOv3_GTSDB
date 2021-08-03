#!/bin/bash
echo "----Scripts start----"

pip3 install -r requirements.txt
python3 resizeImg.py
python3 label.py
python3 anchorBox.py

zip -r train.zip train
zip -r test.zip test

echo "----Scripts finished----"
