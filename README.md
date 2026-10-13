# EchoMind_twin

通过逐步迁移和练习学习 EchoMind 的个人仓库，目标是掌握 Python/FastAPI、Agent 编排、工具调用、RAG、分层记忆、监控与评测。

## 当前进度

第 1 天：建立目录、Python 虚拟环境、依赖清单、环境配置模板和学习笔记。业务模块将按计划逐日迁移；目前还没有可启动的客服 API。

已验证：11 个运行/开发依赖成功导入，同步和异步模型客户端离线初始化成功，`pip check` 通过。详细结果见第 1 天笔记。

- [30 个学习日的任务与文件清单](docs/learning-plan.md)
- [源文件与目标路径的搬运清单](docs/migration-manifest.json)
- [第 1 天笔记与环境验证记录](docs/learning-notes/day01.md)

## 本地环境

本地学习使用 Python 3.10，原始项目的 Dockerfile 使用 Python 3.12。虚拟环境放在 `.venv`，依赖与全局 Python 隔离。

在 Windows PowerShell 中，从仓库根目录执行：

```powershell
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -X utf8 -m pip install --upgrade pip
.\.venv\Scripts\python.exe -X utf8 -m pip install -r requirements-dev.txt
Copy-Item -LiteralPath .env.example -Destination .env
.\.venv\Scripts\python.exe scripts/check_environment.py
.\.venv\Scripts\python.exe -m pip check
```

已有 `.env` 时不要重复复制覆盖，直接编辑本地文件。第 1 天的环境检查不使用真实密钥，不请求模型，也不连接 Redis 或 ChromaDB。

## 配置与数据

- `.env.example`：可提交的占位配置，说明需要哪些变量。
- `.env`：本机配置，不进入 Git；接入真实模型时再填写密钥、地址和模型名。
- `requirements.txt`：从原项目迁入的运行依赖版本。
- `requirements-dev.txt`：运行依赖和测试工具。
- `data/`、`logs/`：运行数据，不进入 Git。

主机上的服务通常使用 `localhost` 与主机端口；容器内连接依赖服务时，需要改用 Compose 服务名与容器端口。后续部署阶段再配置。

## 目录

```text
core/                 文本响应解析、意图识别、Skill 加载
agents/               角色工具和 Agent 编排
mcp/                  本地工具管理、缓存、熔断与知识库
memory/               会话、摘要和用户画像
skills/               按角色匹配的业务处理规则
monitor/              指标、告警与路由惩罚
evaluation/           意图与对话质量评测
api/                  FastAPI 入口
tests/                模块与回归测试
exercises/            自己编写的每日练习
scripts/              环境检查等辅助命令
evaluation_cases/     自建评测输入
evaluation_results/   脱敏后的评测记录
docs/                 学习路线、笔记、架构说明
config/               后续部署配置
frontend/             后期迁入 Vue 调试页面
```

第 2 天将迁入 `core/llm_utils.py`，编写响应文本提取练习。

## 项目来源与学习成果

参考提供的 EchoMind Python 源码及配套文档，逐步迁移、阅读、验证和改进。原项目功能与个人新增练习、修改、评测结果会在记录中注明。效果指标以自己保存的样例和运行结果为准。
