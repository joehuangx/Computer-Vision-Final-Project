# put this file in 'mmdetection/mmdet/models/backbones/'
import warnings

import torch
import torch.nn as nn

from mmcv.runner import BaseModule
from ..builder import BACKBONES

@BACKBONES.register_module()
class SSDLOAD_(BaseModule):
    def __init__(self, model_file):
        super(SSDLOAD_, self).__init__()
        self.model = torch.load(model_file)
    def forward(self, x):
        out = self.model.backbone.forward(x)
        return tuple([out['0'],out['1'],out['2'],out['3'],out['4'],out['5']])

