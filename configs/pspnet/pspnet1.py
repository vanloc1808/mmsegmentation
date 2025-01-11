_base_ = "../pspnet/pspnet_r50-d8_4xb4-40k_cityscpaes-512x1024.py"
norm_cfg = dict(type="BN", requires_grad=True)
model = dict(
    backbone=dict(norm_cfg=norm_cfg),
    decode_head=dict(norm_cfg=norm_cfg),
    auxiliary_head=dict(norm_cfg=norm_cfg),
) 