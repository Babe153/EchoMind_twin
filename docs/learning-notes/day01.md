# 第 1 天：工作区、环境与配置

实际执行日期：2026-10-13（Australia/Sydney）。Git 的四个新提交按指定日期分别设置为 2026-10-09、2026-10-11、2026-10-12、2026-10-13；这与本次实际执行日期分开记录。

## 完成内容

- 从原始后端迁入 `.gitignore` 和 `requirements.txt`。
- 建立 `core`、`agents`、`mcp`、`memory`、`monitor`、`evaluation`、`api`、`tests`、`exercises` 等 Python 包，加入空的 `__init__.py`。
- 建立 Skills、评测数据、评测结果、部署配置和前端的目录占位。
- 扩写本仓库 README，注明项目来源、当前进度和运行方式。
- 保留 30 天学习路线和完整源文件/目标文件映射。
- 创建占位 `.env.example` 及本机 `.env`，没有填入真实密钥。
- 创建 Python 3.10 虚拟环境 `.venv`，独立于系统默认 Python 3.14。
- 新建 `requirements-dev.txt`，包含运行依赖及 `pytest==8.3.4`。
- 新建 `scripts/check_environment.py`，检查依赖导入、解释器、目录、配置模板和模型客户端初始化，不发出 API 请求。

## 今天需要理解的概念

### 为什么使用虚拟环境

`.venv` 中的 Python 和包用于这个项目。其他项目或全局 Python 安装的库不会直接成为本项目的依赖。命令中明确使用 `.venv\Scripts\python.exe`，可以避免误用解释器；虚拟环境本身不提交到 Git。

### 源码、配置与运行数据

- 源码和占位配置进入仓库，其他人可以据此重建环境。
- `.env` 放本机设置和未来的密钥，不进入仓库。
- `data/`、`logs/` 保存后续运行产生的数据库和日志，也不进入仓库。
- `.gitkeep` 仅让尚无内容的目录可以进入 Git；实际业务模块按后续学习日迁移。

### 依赖与开发依赖

`requirements.txt` 固定核心运行依赖；`requirements-dev.txt` 引用它并加入测试工具。直接依赖版本固定不代表所有间接依赖都已锁定；安装后还需要 `pip check` 和真实导入验证。

## 本次遇到的问题

Python 3.10 自带的 pip 21.2.3 按 Windows GBK 读取含 UTF-8 中文注释的原始依赖文件，报 `UnicodeDecodeError`。处理方式：只升级本项目虚拟环境的 pip 到 26.2.1，并通过 `-X utf8` 运行安装命令。

```powershell
.\.venv\Scripts\python.exe -X utf8 -m pip install --upgrade pip
.\.venv\Scripts\python.exe -X utf8 -m pip install -r requirements-dev.txt
```

本次使用 Python 3.10.0，原始 Docker 环境是 3.12。后续涉及容器时另行验证，不把本机导入成功视为容器部署成功。

## 验证记录

环境依赖安装成功，原始运行依赖的版本未调整；新增开发依赖 `pytest==8.3.4`。

实际运行：

```powershell
.\.venv\Scripts\python.exe -X utf8 scripts/check_environment.py
.\.venv\Scripts\python.exe -m pip check
```

结果：环境检查退出码 0；`pip check` 输出 `No broken requirements found.`，退出码 0。

| 依赖 | 已安装且成功导入的版本 |
|---|---|
| anthropic | 0.40.0 |
| fastapi | 0.115.5 |
| uvicorn | 0.32.1 |
| pydantic | 2.10.3 |
| python-multipart | 0.0.12 |
| redis | 5.2.1 |
| chromadb | 0.5.23 |
| prometheus-client | 0.21.1 |
| httpx | 0.28.1 |
| python-dotenv | 1.0.1 |
| pytest | 8.3.4 |

同步和异步 Anthropic 客户端都成功构造并关闭，使用的是测试占位 key 和无效示例域名，没有发出模型请求。检查脚本最初误用了 `python_multipart` 模块名，已改为这个版本实际提供的 `multipart`；发行包名与导入模块名不一定相同。

已检查 Git 忽略规则：`.env`、`.env.local`、`.venv`、数据、日志、前端依赖和 pytest 缓存均被忽略；`.env.example` 可以提交。

第 1 天验收：

- [x] 源码目录、配置模板和运行数据位置已区分。
- [x] 虚拟环境已建立，运行依赖和测试工具安装成功。
- [x] 关键依赖可以导入，模型客户端可以离线初始化。
- [x] 本机 `.env`、虚拟环境和运行数据被 Git 忽略。
- [x] README 包含来源、学习目标、当前进度和重建命令。
- [x] 第 2 天的迁移对象和练习已明确。

目前还没有启动业务 API，没有调用真实模型，没有连接 Redis 或 ChromaDB，也没有运行后续 Agent 测试。第 1 天验证范围是基础工作区与 Python 环境。

## 下一步

第 2 天迁入 `core/llm_utils.py`，自己编写五类响应块输入的文本提取练习，理解模型响应为何不能直接当成字符串。

复习自测：

1. `.env.example` 与 `.env` 分别解决什么问题？
2. 为什么不能把 `.venv` 复制进 Git 仓库？
3. 怎样确认当前命令使用的是本项目 Python？
4. `pip check` 通过与“项目可以启动”有什么区别？
