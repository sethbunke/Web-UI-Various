import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I

#WORKS - BUT NOT WELL - NOT GOOD SCORE

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        # output size = (W-F)/S +1 = (224-5)/1 +1 = 220
        # the output Tensor for one image, will have the dimensions: (32, 220, 220)
        # after one pool layer, this becomes (32, 110, 110)

        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        
        self.conv1 = nn.Conv2d(1, 32, 5)
        
        # pool with kernel_size=2, stride=2
        self.pool = nn.MaxPool2d(2, 2)               
        
        self.conv2 = nn.Conv2d(32, 64, 5)
        
        self.conv2_drop = nn.Dropout2d()
        
        self.conv3 = nn.Conv2d(64, 128, 5)
        
        self.conv3_drop = nn.Dropout2d()
        
        self.conv4 = nn.Conv2d(128, 256, 5)
        
        self.conv4_drop = nn.Dropout2d()
               
        # 20 outputs * the 5*5 filtered/pooled map size
        self.fc1 = nn.Linear(25600, 50)
        
        # dropout with p=0.4
        self.fc1_drop = nn.Dropout(p=0.4)
        
        # finally, create 10 output channels (for the 10 classes)
        self.fc2 = nn.Linear(50, 136)      
        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        log = False
        
        x = self.pool(F.relu(self.conv1(x)))
        if log:
            print('conv1: ' + str(x.shape))
    
        x = self.pool(F.relu(self.conv2(x)))
        #x = self.pool(F.relu(self.conv2(x)))
        if log:
            print('conv2: ' + str(x.shape))
         
        x = self.pool(F.relu(self.conv3(x)))
        #x = self.pool(F.relu(self.conv3(x)))
        if log:
            print('conv3: ' + str(x.shape))
            
        x = self.pool(F.relu(self.conv4(x)))
        #x = self.pool(F.relu(self.conv3(x)))
        if log:
            print('conv4: ' + str(x.shape))
        
        x = x.view(x.size(0), -1)
        if log:
            print('flatten: ' + str(x.shape))
        
        x = F.relu(self.fc1(x))
        if log:
            print('fc1: ' + str(x.shape))
        
        x = self.fc1_drop(x)
        if log:
            print('drop: ' + str(x.shape))
        
        x = self.fc2(x)
        if log:
            print('fc2: ' + str(x.shape))
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x