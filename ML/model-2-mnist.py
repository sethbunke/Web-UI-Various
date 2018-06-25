import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I

#this performs poorly
# Net(
#   (conv1): Conv2d(1, 64, kernel_size=(5, 5), stride=(1, 1))
#   (conv2): Conv2d(64, 128, kernel_size=(5, 5), stride=(1, 1))
#   (conv2_drop): Dropout2d(p=0.5)
#   (conv3): Conv2d(128, 20, kernel_size=(5, 5), stride=(1, 1))
#   (conv3_drop): Dropout2d(p=0.5)
#   (fc1): Linear(in_features=11520, out_features=50, bias=True)
#   (fc2): Linear(in_features=50, out_features=136, bias=True)
# )

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 64, kernel_size=5)
        
        self.conv2 = nn.Conv2d(64, 128, kernel_size=5)        
        self.conv2_drop = nn.Dropout2d()
        
        self.conv3 = nn.Conv2d(128, 20, kernel_size=5)
        self.conv3_drop = nn.Dropout2d()
        
        self.fc1 = nn.Linear(11520, 50)
        self.fc2 = nn.Linear(50, 136)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2_drop(self.conv2(x)), 2))
        x = F.relu(F.max_pool2d(self.conv3_drop(self.conv3(x)), 2))
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return x #F.log_softmax(x)