import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import cv2
from keras.models import Sequential,load_model,Model
from keras.layers import Conv2D,MaxPool2D,Dense,Dropout,BatchNormalization,Flatten,Input
from sklearn.model_selection import train_test_split
from cvzone.FaceDetectionModule import FaceDetector

# Create a path variable to the path of your dataset
path = "Pneumothorax-New-Dataset"

# Create empty images list and categories list
infected = []
uninfected = []

# Loop throught each img in path
for img in os.listdir(path):
    # Add try block
    try:
        # Print the img
        print(img)
    
        # Split the img address from "_" and get the first character and store in type variable
        type = img.split("_")[0]
        # Load the image
        img = cv2.imread(str(path)+"/"+str(img))
        # Change image from BGR to RGB
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # Resize the image to 200,200
        resizeImg = [cv2.resize(crop, (200, 200))]
        # Append the image to images list
        img.append(img)
        # Append the type to categories list
        type.append(categoriesList)
    # Add except block  
    except:
        print("error in reading")
# Print count of all image i.e len(images)
print("Count of infected images", len(infected))
print("Count of uninfected images", len(uninfected))

