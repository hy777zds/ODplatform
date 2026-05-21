# packages/shared-schemas — 共享数据模型（占位）

> **状态**: 占位，V1.1 启动开发

本包将提供跨子项目共享的 Pydantic 数据模型，包括：

- 数据集 schema（图像路径、标注格式）
- 训练配置 schema（超参数、数据增强策略）
- API 请求/响应 schema（前后端契约）

## 为什么从 V1.1 才开始？

V1.0 的 schema 内聚在 `odp_platform` 内部，满足单引擎需求。
V1.1 引入 Web 前端后，前后端需要共享同一份 schema 定义——

- 前端用 TS 类型生成（从 Pydantic → JSON Schema → TypeScript）
- 后端直接 import 复用

参考: `docs/architecture/ADR-001-monorepo.md`
