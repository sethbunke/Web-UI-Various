import torch
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I
import numpy as np


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 64 output channels/feature maps, 3x3 square convolution kernel
        #(W-F)/S +1 = (224-5)/1 +1 =220 
        self.conv1 = nn.Conv2d(1, 32, 5)
        #torch.nn.init.xavier_normal_( self.conv1.weight)
        #110X110X32
        self.pool1= nn.MaxPool2d(2,2)
        #(W-F)/S +1 = (110-4)/1 +1 = 108
        self.conv2 = nn.Conv2d(32,  64, 3)
     
        #54X54X64
        self.pool2= nn.MaxPool2d(2,2)
        #(W-F)/S +1 = (54-3)/1 +1 = 52
        self.conv3 = nn.Conv2d(64,  128, 3)
        #torch.nn.init.xavier_normal_( self.conv3.weight)
        #26X26X128
        self.pool3 = nn.MaxPool2d(2,2)
        #(W-F)/S +1 = (26-1)/1 +1 = 26
        self.conv4 = nn.Conv2d(128,  256, 1)
        #13X13X256
        self.pool4 = nn.MaxPool2d(2,2)
        
        self.fc1= nn.Linear(13*13*256,1024)
        self.fc2= nn.Linear(1024,136)
        
        self.dropout = nn.Dropout(p=0.2)
     
        
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## Define the feedforward behavior of this model
       
        x= self.pool1(F.selu(self.conv1(x)))
        x= self.dropout(x)
        x= self.pool2(F.selu(self.conv2(x)))
        x= self.dropout(x)
        x= self.pool3(F.selu(self.conv3(x)))
        x= self.dropout(x)
        x =self.pool4(F.selu(self.conv4(x)))
        x= self.dropout(x)
        x = x.view(x.size(0), -1)
        x= F.selu(self.fc1(x))
        x= self.dropout(x)
        x= self.fc2(x)

       
        # a modified x, having gone through all the layers of your model, should be returned
        return x