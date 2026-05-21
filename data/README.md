# data — 数据集目录

数据目录结构：

```
data/
├── raw/            # 原始数据集（不修改，只读）
│   └── <数据集名>/
│       ├── images/
│       └── annotations/
├── train/          # 训练集（转换后）
│   ├── images/
│   └── labels/
├── val/            # 验证集
│   ├── images/
│   └── labels/
└── test/           # 测试集
    ├── images/
    └── labels/
```

## 使用方式

1. 将原始数据集放入 `raw/` 目录
2. 运行数据转换脚本：`odp-convert <数据集名>`
3. 转换后的数据自动进入 `train/`、`val/`、`test/`

原始数据集不会被动到，保证可复现。
