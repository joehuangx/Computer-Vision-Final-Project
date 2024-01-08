# -*- coding:utf-8 -*-
# config file 
mmdetection_configs_root = "D:\FinalCV\mmdetection\configs"
_base_ = [
    f'{mmdetection_configs_root}/ssd/ssd300_coco.py'
]

custom_imports = dict(
    imports=['mmdet.models.backbones.ssd_load_',
            'mmdet.models.necks.direct_'],
    allow_failed_imports=False
)

# model settings
model = dict(
    backbone=dict(
        _delete_=True,
        type='SSDLOAD_',
        model_file= r'./ssd_0.0.pth'
        # model_file= r'./sss_mm0.pth'
        ),
    neck=dict(
        _delete_=True,
        type='DIRECT_',
        ),
    bbox_head=dict(
        in_channels=(512, 1024, 512, 256, 256, 256),
        #in_channels=(409, 1024, 512, 256, 256, 256),
        num_classes=90,
        anchor_generator=dict(
            _delete_=True,
            type='PreciseAnchorGenerator',
            strides=[8, 16, 32, 64, 100, 300],
            scale_ratios=(((0.07, 1.0), (0.1025, 1.0), (0.07, 0.5), (0.07, 2.0)),
                  ((0.15, 1.0),
                   (0.2225, 1.0),
                   (0.15, 0.5),
                   (0.15, 2.0),
                   (0.15, 0.3333),
                   (0.15, 3.0)),
                  ((0.33, 1.0),
                   (0.4102, 1.0),
                   (0.33, 0.5),
                   (0.33, 2.0),
                   (0.33, 0.3333),
                   (0.33, 3.0)),
                  ((0.51, 1.0),
                   (0.5932, 1.0),
                   (0.51, 0.5),
                   (0.51, 2.0),
                   (0.51, 0.3333),
                   (0.51, 3.0)),
                  ((0.69, 1.0), (0.7748, 1.0), (0.69, 0.5), (0.69, 2.0)),
                  ((0.87, 1.0), (0.9558, 1.0), (0.87, 0.5), (0.87, 2.0))),
            anchor_base_size=300,
            centers=((4, 4), (8, 8), (16, 16), (32, 32), (50, 50), (150, 150))
            )
        ),

)


COCO_80_CLASSES = ('person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
               'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
               'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog',
               'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe',
               'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
               'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat',
               'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
               'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
               'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot',
               'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
               'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
               'mouse', 'remote', 'keyboard', 'cell phone', 'microwave',
               'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock',
               'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush')


COCO_91_CLASSES=('person','bicycle','car','motorbike','aeroplane',
'bus','train','truck','boat','trafficlight','firehydrant','streetsign','stopsign',
'parkingmeter','bench','bird','cat','dog','horse','sheep','cow','elephant',
'bear','zebra','giraffe','hat','backpack','umbrella','shoe',
'eyeglasses','handbag','tie','suitcase','frisbee','skis','snowboard',
'sportsball','kite','baseballbat','baseballglove','skateboard',
'surfboard','tennisracket','bottle','plate','wineglass','cup',
'fork','knife','spoon','bowl','banana','apple','sandwich','orange',
'broccoli','carrot','hotdog','pizza','donut','cake','chair',
'sofa','pottedplant','bed','mirror','diningtable','window',
'desk','toilet','door','tvmonitor','laptop','mouse','remote',
'keyboard','cellphone','microwave','oven','toaster','sink',
'refrigerator','blender','book','clock','vase','scissors',
'teddybear','hairdrier','toothbrush','hairbrush')