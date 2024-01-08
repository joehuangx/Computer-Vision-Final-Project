# put this file in 'mmdetection/mmdet/models/necks/'
from ..builder import NECKS
import torch.nn as nn

@NECKS.register_module()
class DIRECT_(nn.Module):
    def __init__(self):
        super(DIRECT_, self).__init__()
    def forward(self, x):
        outs = [feat for feat in x]
        return tuple(outs)