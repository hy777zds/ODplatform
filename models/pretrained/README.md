# models/pretrained — 预训练模型目录

存放从外部下载的预训练权重文件，如：

- YOLO 系列（yolov8n.pt, yolov8s.pt, ...）
- 其他目标检测模型的预训练权重

## 使用方式

权重文件在训练启动时自动从 Ultralytics 等源下载到此目录，
也可手动放置 `.pt` / `.pth` 文件到此目录后直接引用。
