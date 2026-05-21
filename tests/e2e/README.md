# tests/e2e — 端到端测试（占位）

> **状态**: 占位，V1.1 启动

本目录将存放跨 app 的端到端测试，覆盖：

- 数据导入 → 转换 → 训练 → 评估完整流程
- Web 前端 → 后端 API → platform 引擎的集成链路
- 多端协同场景

## 与各 app 内 `tests/` 的关系

| 层级 | 位置 | 职责 |
|------|------|------|
| 单元测试 | `apps/*/tests/` | 单个模块内部逻辑 |
| 集成测试 | `apps/*/tests/` | app 内部模块协作 |
| E2E 测试 | `tests/e2e/` | 跨 app 的完整链路 |

参考: `docs/architecture/ADR-001-monorepo.md`
