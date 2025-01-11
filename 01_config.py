from mmengine.config import Config

# cfg = Config.fromfile(
#     "configs/pspnet/pspnet_r50-d8_4xb2-40k_cityscapes-512x1024.py",
# )
cfg = Config.fromfile("configs/pspnet/pspnet.py")
print(cfg.__dict__)
# print("Config train data loader")
# print(cfg.train_dataloader)
# print("Config test data loader")
# print(cfg.test_dataloader)
print("Config model")
print(cfg.model)

cfg = Config.fromfile("configs/pspnet/hrnet.py")
print(cfg.__dict__)
print("Config model")
print(cfg.model)
