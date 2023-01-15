import os
from turtle import width
import cv2

path = "Images/"
Images = []

os.listdir(path)
os.splitext("111.jpg","112.jpg","113.jpg","114.jpg","115.jpg","116.jpg","117.jpg","118.jpg","119.jpg","120.jpg")

if ext in ['.gif', '.png', '.jpg', '.jpeg', 'jfif']:
    file_name = path+"/"+"111.jpg","112.jpg","113.jpg","114.jpg","115.jpg","116.jpg","117.jpg","118.jpg","119.jpg","120.jpg"
print(file_name)
Images.append()
count = len(images)
frame = cv2.imread(images[0])
frame.shape()
w = width
h = height
size = (w,h)
print(size)
out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    cv2.imread(out)
    out.write()