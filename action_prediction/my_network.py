import math
import numpy as np

import torch
from torch import nn
import torch.nn.functional as F
from torch import distributions as torchd

# Define an Action Prediction Model with FC layers
class ActionPredictor(nn.Module):
    def __init__(self, input_dim, output_dim, hidden_dim=128):
        super().__init__()
        self.fc1 = nn.Linear(input_dim*2, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim)
        self.fc3 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, previous_state, current_state):
        x = torch.cat([previous_state, current_state], dim=1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x