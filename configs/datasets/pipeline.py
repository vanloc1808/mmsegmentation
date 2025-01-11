_base_ = "../pspnet/pspnet_r50-d8_4xb4-40k_cityscpaes-512x1024.py"
crop_size = (512, 1024)
dataset_type = "CityscapesDataset"  # Dataset type, this will be used to define the dataset.
data_root = 'data/cityscapes/'  # Root path of data.

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53],
    std=[58.395, 57.12, 57.375],
    to_rgb=True,
)

train_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(type="LoadAnnotations"),
    dict(
        type="RandomResize",
        img_scale=(2048, 1024),
        ratio_range=(1.00, 2.00),
        keep_ration=True,
    ),
    dict(
        type="RandomCrop",
        crop_size=crop_size,
        cat_max_ratio=0.75,
    ),
    dict(type="RandomFlip", flip_ratio=0.5),
    dict(type="PhotoMetricDistortion"),
    dict(type="PackSegInputs"),
]

test_pipeline = [
    dict(type="LoadImageFromFile"),
    dict(
        type="Resize",
        scale=(2048, 1024),
        keep_ratio=True,
    ),
    dict(type="LoadAnnotations"),
    dict(type="PackSegInputs"),
]

train_dataset = dict(
    type=dataset_type,
    data_root=data_root,
    data_prefix=dict(
        img_path="leftImg8bit/train",
        seg_map_path="gtFine/train",
        pipeline=train_pipeline,
    ),
)

test_dataset = dict(
    type=dataset_type,
    data_root=data_root,
    data_prefix=dict(
        img_path="leftImg8bit/val",
        seg_map_path="gtFine/val",
        pipeline=test_pipeline,
    ),
)

train_dataloader = dict(dataset=train_dataset)
val_dataloader = dict(dataset=test_dataset)
test_dataloader = val_dataloader
