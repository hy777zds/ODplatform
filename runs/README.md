# runs — 训练运行结果目录

存放每次训练运行的输出，按时间戳子目录组织：

```
runs/
├── 20260519_120000/   # 训练结果
│   ├── weights/       # 最佳权重
│   ├── results.csv    # 指标曲线数据
│   └── args.yaml      # 训练参数快照
└── ...
```

## 与 models/checkpoints 的区别

| 目录 | 用途 |
|------|------|
| `runs/` | 按运行组织的结果（指标、曲线、日志） |
| `models/checkpoints/` | 按模型分类的检查点文件 |

训练完成后的最佳权重建议归档到 `models/checkpoints/`。
