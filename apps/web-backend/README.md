# apps/web-backend — Web 后端服务（占位）

> **状态**: 占位，V1.1 启动开发

本子项目将提供 ODPlatform 的 Web 后端服务，基于：

- FastAPI（REST API）
- 复用 `apps/platform/` 的核心引擎（数据转换、推理）
- 共享 `packages/shared-schemas/` 的 Pydantic 数据模型

## 为什么现在是空的？

这一目录的存在是 **架构层面的预约**——
我们今天就给它留好位置，这样 V1.1 启动时：

- backend 团队知道往哪建
- platform 一行代码不用动
- 共享数据（`/data`、`/models`）直接复用

参考: `docs/architecture/ADR-001-monorepo.md`
