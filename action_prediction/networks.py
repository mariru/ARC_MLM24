import math
import numpy as np
import re

import torch
from torch import nn
import torch.nn.functional as F
from torch import distributions as torchd

import tools

class CNN_encoder(nn.Module):
    def __init__(
            self, 
            grid_size,
            input_dim, 
            cnn_output_dim, 
            layer_dims,
            embedding_dim=128,
            kernel_size=4, 
            is_norm = True, 
            activation = "ReLU"
            ):
        super().__init__()

        print(type(grid_size))
        layer_dims = [input_dim] + layer_dims + [cnn_output_dim]
        layers = []
        for i in range(len(layer_dims) - 1):
            layers.append(Conv2dSamePad(layer_dims[i], layer_dims[i + 1], kernel_size))
            if is_norm:
                layers.append(nn.BatchNorm2d(layer_dims[i + 1]))
            layers.append(getattr(nn, activation)())
        self.cnn_layers = nn.Sequential(*layers)
        fc_input_dim = cnn_output_dim * np.prod(grid_size)
        self.fc = nn.Sequential(
            nn.Linear(fc_input_dim, cnn_output_dim),
            nn.ReLU(),
            nn.Linear(cnn_output_dim, embedding_dim)
        )

    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.reshape(x.shape[0], -1)
        x = self.fc(x)
        return x

class Conv2dSamePad(torch.nn.Conv2d):
    def calc_same_pad(self, i, k, s, d):
        return max((math.ceil(i / s) - 1) * s + (k - 1) * d + 1 - i, 0)

    def forward(self, x):
        ih, iw = x.size()[-2:]
        pad_h = self.calc_same_pad(
            i=ih, k=self.kernel_size[0], s=self.stride[0], d=self.dilation[0]
        )
        pad_w = self.calc_same_pad(
            i=iw, k=self.kernel_size[1], s=self.stride[1], d=self.dilation[1]
        )

        if pad_h > 0 or pad_w > 0:
            x = F.pad(
                x, [pad_w // 2, pad_w - pad_w // 2, pad_h // 2, pad_h - pad_h // 2]
            )

        ret = F.conv2d(
            x,
            self.weight,
            self.bias,
            self.stride,
            self.padding,
            self.dilation,
            self.groups,
        )
        return ret


