# apps/desktop — 桌面客户端（占位）

> **状态**: 占位，V2.0 启动开发

本子项目将提供 ODPlatform 的桌面客户端，面向：

- 本地一键部署，无需配置 Python 环境
- 离线推理场景
- 非技术用户的使用体验

## 为什么现在是空的？

桌面端在 V2.0 启动。提前预留此目录是为了：

- 从第一天就考虑跨端架构（CLI / Web / Desktop 共享核心）
- platform 引擎保持无 UI 依赖，桌面端与 Web 端平等调用

参考: `docs/architecture/ADR-001-monorepo.md`
