# EchoMind：30 个学习日，逐步搬到自己的仓库

适用情况：会一些 Python，希望边搬运、边理解、边验证，最终能够修改项目并参加面试。

每天约 1.5～2 小时，按“学习日”推进，不要求连续 30 个自然日。验收没有完成就延长一天。第 25 天部署和第 29 天个人改进可以各用两天。

本方案根据本地文件和导入依赖制定，已核对 33 个计划搬运的源文件存在。后续执行状态以 `learning-notes/` 下的每日记录为准，未执行的后续命令和业务效果仍待验证。

## 先确定三个位置

| 用途 | 绝对路径 |
|---|---|
| 原始资料 | `C:/Users/Babe/Desktop/myProject/EchoMind所有代码+详细文档+简历/` |
| 原始 Python 后端 | `C:/Users/Babe/Desktop/myProject/EchoMind所有代码+详细文档+简历/EchoMind/` |
| 原始 Vue 前端 | `C:/Users/Babe/Desktop/myProject/EchoMind所有代码+详细文档+简历/EchoMindFrontend/` |
| 你自己的仓库 | `C:/Users/Babe/Desktop/EchoMind_twin/` |

后文的“后端源文件”均相对于上表的原始 Python 后端；目标相对于你的仓库根目录。前端统一放到你的 `frontend/` 目录。完整源文件和目标文件的绝对路径另列于同目录的 `migration-manifest.json`。

最终结构采用后端在根目录、前端在子目录的方式：

```text
C:/Users/Babe/Desktop/EchoMind_twin/
├─ README.md                     自己写
├─ .gitignore                    第 1 天搬入并补充
├─ .env.example                  第 1 天自己写，只有占位符
├─ .env                          本机配置，不进入 Git
├─ requirements.txt
├─ requirements-dev.txt          自己写，放 pytest 等开发依赖
├─ core/
├─ agents/
├─ mcp/
├─ memory/
├─ skills/
├─ monitor/
├─ evaluation/
├─ api/
├─ tests/
├─ exercises/                    自己写的小练习
├─ docs/
│  ├─ learning-plan.md
│  └─ learning-notes/            每天自己的笔记
├─ evaluation_cases/             自建评测样例
├─ evaluation_results/           脱敏后的验证结果
├─ config/
├─ Dockerfile
├─ .dockerignore
├─ docker-compose.yml
└─ frontend/
```

保留 Python 源码的目录层级，例如 `core/llm_utils.py` 对应你仓库中的同名路径。不要把所有 Python 文件摊平到根目录。给 Python 模块目录和 `exercises/` 创建空的 `__init__.py`，便于导入并减少同名第三方包冲突。

## 每天用同一个学习流程

1. **读 20～30 分钟**：只读当天指定函数，写出输入、输出、依赖和失败处理。
2. **搬运或修改 20～30 分钟**：只处理当天清单里的文件。
3. **练习 30～45 分钟**：用固定输入预测结果，然后实际验证。
4. **整理 10～15 分钟**：保存自己写的笔记和结果，检查差异后再提交。

搬运后必须有解释、运行记录或练习。单纯看到文件出现在仓库里，不能算完成学习。

有几个文件比较大，尤其是编排器。为保证导入完整，先搬入整个文件，再分几天学习和验证其中不同部分。前期不强行拆原文件，也不把缺少依赖的半个类当作可运行版本。

## 按天总表

“无新搬运”表示当天继续学习、验证或修改已经搬入的代码，不是休息日。

| 学习日 | 当天搬入的后端源文件，或注明前端来源 | 当天目标 |
|---|---|---|
| 01 | `.gitignore`、`requirements.txt` | 建目录、环境、自己的 README 和配置模板 |
| 02 | `core/llm_utils.py` | 模型响应文本如何提取 |
| 03 | 无新搬运 | 学异步、并发和异常 |
| 04 | `core/skill_loader.py`、`skills/general_customer_service/SKILL.md` | 加载和匹配一个 Skill |
| 05 | `skills/technical_support/SKILL.md`、`skills/billing_support/SKILL.md`、`skills/README.md` | 验证角色与关键词过滤 |
| 06 | `core/intent_recognizer.py` | 意图、规则、实体、紧急度 |
| 07 | 无新搬运 | 向量分支、投票、阈值、缓存 |
| 08 | `agents/tools.py` | 确定性工具和输入 schema |
| 09 | `agents/agent_orchestrator.py` | 请求数据结构和四类角色 |
| 10 | `tests/test_agent_orchestrator.py` | 用 FakeClient 理解测试 |
| 11 | 无新搬运 | `tool_use` 到 `tool_result` 的循环 |
| 12 | 无新搬运 | 单 Agent 路由、澄清和降级 |
| 13 | 无新搬运 | 主辅 Agent 并发及结果合并 |
| 14 | 无新搬运 | 做最小命令行演示和阶段复盘 |
| 15 | `mcp/tool_manager.py` | 工具注册、缓存、超时 |
| 16 | 无新搬运 | 熔断、fallback、查询改写与重排 |
| 17 | `mcp/knowledge_base.py` | 文档切片、入库、检索 |
| 18 | 无新搬运 | 接通 Agent 的共享 RAG 工具 |
| 19 | `memory/conversation_memory.py` | 会话记忆写入和读取 |
| 20 | 无新搬运 | 摘要压缩、历史检索、画像 |
| 21 | `monitor/performance_monitor.py` | 成功率、延迟、告警和降权 |
| 22 | `evaluation/evaluator.py` | 意图评测、Judge 和回归检测 |
| 23 | `api/main.py` | 接通完整 FastAPI 入口 |
| 24 | 无新搬运 | API、多轮、工具轨迹的集成验证 |
| 25 | `Dockerfile`、`.dockerignore`、`docker-compose.yml`、`config/prometheus.yml`、`config/nginx/nginx.conf` | 容器运行与主机运行的区别 |
| 26 | 前端 10 个文件，见下方清单 | 运行 Vue 调试页面 |
| 27 | 无新搬运 | 跟踪页面请求、响应映射和错误显示 |
| 28 | 无新搬运 | 建立自己的评测基线 |
| 29 | 无新搬运 | 完成一个个人改进并复测 |
| 30 | 无新搬运 | 完成 README、架构图和面试介绍 |

## 第 1～7 天：从小模块开始

### 第 01 天：建好自己的学习工作区

**搬运**：后端 `.gitignore`、`requirements.txt` → 仓库根目录。保留你仓库已有的 README，自行扩写，不覆盖成原项目 README。

**自己创建**：上述目录、空的 `__init__.py`、`.env.example`、`requirements-dev.txt`，以及 `docs/learning-notes/day01.md`。

**学习**：虚拟环境是什么，依赖文件是什么，源码目录和运行数据目录有什么区别。

当前机器默认 Python 是 3.14，另有 3.10 和 3.9；原项目 Dockerfile 使用 3.12。可以先用已安装的 3.10 做本地学习，并在 README 记录环境差异。先不要把这批旧版依赖直接装进默认 3.14 环境。如果后续有版本问题，用实际错误定位；需要与原 Docker 完全一致时再准备 Python 3.12 环境。

从自己的仓库根目录执行：

```powershell
Set-Location -LiteralPath 'C:\Users\Babe\Desktop\EchoMind_twin'
py -3.10 -m venv .venv
.\.venv\Scripts\python.exe -X utf8 -m pip install --upgrade pip
.\.venv\Scripts\python.exe -X utf8 -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install pytest
```

将 `pytest` 写入自己新建的开发依赖文件，运行环境安装成功后记录版本。后面的命令都从仓库根目录运行，使用 `.venv` 内的 Python，避免混用解释器。依赖安装出错就先处理这一项，不把未成功的环境当作可用环境。

配置模板只有占位符：

```dotenv
ANTHROPIC_API_KEY=
ANTHROPIC_BASE_URL=
ANTHROPIC_MODEL=
REDIS_PASSWORD=replace_me
REDIS_URL=redis://:replace_me@localhost:6379/0
CHROMA_HOST=localhost
CHROMA_PORT=8001
CHROMA_PERSIST_DIRECTORY=./data/chroma
EVAL_BASELINE_PATH=./data/eval/baseline.json
ECHOMIND_SKILLS_DIR=./skills
PROMETHEUS_PORT=0
```

原始 `.env` 不搬运；根据自己使用的模型服务填写本机配置。模型名和地址以你实际可用的服务为准，不照抄文档里的示例值。

补充 `.gitignore`：忽略 `.pytest_cache/`、`.env.*`，但用 `!.env.example` 保留占位模板；前端阶段再补 `node_modules/` 和前端构建目录。原有的 `.env`、`.venv`、`data`、`logs` 忽略规则保留。

**验收**：[ ] 能说清源码和运行环境的区别；[ ] Git 中没有密钥、原仓库 `.git`、虚拟环境或数据库；[ ] README 写了项目学习目的、来源和自己的计划。

### 第 02 天：先掌握一个几十行的小函数

**搬运**：`core/llm_utils.py`。

**看**：`extract_text_content()`。比较字符串、字典、对象形式的响应块；观察它如何忽略工具块。

**自己写**：`exercises/day02.py`。构造字符串、`{"type": "text", "text": "hello"}`、带 `type/text` 属性的对象、`tool_use` 和空列表，预测后再打印结果。

```powershell
.\.venv\Scripts\python.exe -m exercises.day02
```

**验收**：[ ] 不联网也能运行；[ ] 能解释为什么模型响应不能直接当字符串；[ ] 能解释工具块和文本块为什么要分开处理。

### 第 03 天：异步基础练习

**搬运**：无。

**自己写**：`exercises/day03.py`，用两个 `asyncio.sleep()` 模拟外部请求。分别顺序等待、用 `gather()` 并发执行、模拟一个任务抛异常。

**看**：协程、任务、`await`、`create_task()`、`gather()`、`return_exceptions=True`。

**验收**：[ ] 测量两种执行方式耗时；[ ] 能说明并发适合等待外部服务；[ ] 知道创建任务后还要处理完成、异常与生命周期。

### 第 04 天：让 Skill 加载器先独立跑起来

**搬运**：`core/skill_loader.py`、`skills/general_customer_service/SKILL.md`。

**看**：`Skill`、`matches()`、`load()`、`prompt_for()` 和元数据解析。项目中的 SKILL.md 是供 EchoMind 读取的业务规则资料。

**自己写**：`exercises/day04.py`，加载自己的 `skills` 目录，打印 `summary()`，对“你好”和一个不含关键词的输入调用 `prompt_for()`。

**验收**：[ ] 能解释 `agents` 与 `keywords`；[ ] 知道 Skill 是提示词规则，不是执行函数；[ ] 知道不命中时为什么返回空文本。

### 第 05 天：三类 Skill 的匹配与热加载

**搬运**：`skills/technical_support/SKILL.md`、`skills/billing_support/SKILL.md`、`skills/README.md`。

**练习**：在 `exercises/day05.py` 对比“登录报错/technical”“退款/billing”“退款/technical”的匹配结果。修改自己仓库中的一句规则后调用 `reload()`，确认新的提示词文本。

**看**：`to_prompt_block()`、长度上限、解析错误记录。此时只调用 Python 加载器；API 的 `/skills/reload` 到第 23 天才接入。

**验收**：[ ] 三个 Skill 都可加载；[ ] 能解释角色隔离；[ ] 能记录修改前后实际文本，而非凭最终回答猜测是否生效。

### 第 06 天：规则识别、实体和紧急度

**搬运**：`core/intent_recognizer.py` 整个文件。

**看**：`IntentCategory`、`UrgencyLevel`、`IntentResult`、`_pattern_recognize()`、`_extract_entities()`、`_urgency()`。

**练习**：新建 `exercises/day06.py`，只调用本地规则方法，输入订单号、金额、401 错误码、退款、发票和转人工样例；暂时不调用完整的 `recognize()`。

构造 SDK 客户端不等于发出网络请求；离线练习可以使用测试占位 key。若客户端构造就失败，记录 SDK/httpx 版本和错误，先排查依赖兼容问题。

**验收**：[ ] 每个输出字段都有实际例子；[ ] 能列出规则识别的两个误判场景；[ ] 不把模型生成的置信度当作经过校准的正确概率。

### 第 07 天：三路融合和缓存

**搬运**：无。

**看**：`recognize()`、`_llm_recognize()`、`_embedding_recognize()`、`_embed_text()`、`_local_embedding()`、`_vote()`、`_cache_key()`。

**练习**：在 `exercises/day07.py` 给 `_vote()` 输入三组手工结果：三路一致、三路冲突、LLM 失败。再比较本地向量相似度，以及带不同历史的缓存键。

**验收**：[ ] 手算一次加权结果并与代码对照；[ ] 解释低于阈值后发生什么；[ ] 说明当前意图向量分支在缺少远端 embedding 接口时是字符 n-gram 哈希向量；[ ] 能说清它与训练好的语义向量模型的区别。

## 第 8～14 天：掌握 Agent 的工作方式

### 第 08 天：先学工具，再学模型怎样调用工具

**搬运**：`agents/tools.py`。

**看**：`AgentToolSpec`、`make_tool()`、各角色工具和 `build_shared_rag_tools()`。

该文件对 `Request` 的导入在 `TYPE_CHECKING` 中，运行时不要求编排器已搬入；`from __future__ import annotations` 延迟处理类型注解。

**练习**：用 `types.SimpleNamespace` 创建具备必要属性的最小请求对象，放进 `exercises/day08.py`；直接运行错误码查询、金额比较和账单字段检查。

**验收**：[ ] 知道 schema 定义与参数校验执行的区别；[ ] 知道工具返回是本地代码算出的；[ ] 明确字段检查和金额差值不代表已完成退款核验。

### 第 09 天：搬入编排器，先只理解数据结构与角色

**搬运**：`agents/agent_orchestrator.py` 整个文件。前置的 `agents/tools.py`、意图识别器和文本工具已齐。

**看**：`AgentType`、`AgentProfile`、`Request`、`AgentResponse`、`OrchestratorResult`、`RoutingDecision`；比较四个角色的 profile 和 `_build_role_packet()`。

**练习**：用假的客户端实例化不同角色，打印角色输入包和工具列表。今天不要求看完约千行的编排器。

**验收**：[ ] 能指出角色使命、输入输出契约、工具和生成参数的差异；[ ] 知道升级角色可以不调用 LLM；[ ] 能成功导入编排器。

### 第 10 天：用现成测试看懂预期行为

**搬运**：`tests/test_agent_orchestrator.py`。

**看**：`FakeClient`、`make_request()`，以及角色差异、升级节点、工具隔离、合成结果回退的测试。原测试采用假的模型响应，不需要真实 key。

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_agent_orchestrator.py -q
```

**验收**：[ ] 保存实际测试结果，失败则定位而非忽略；[ ] 能解释至少三个断言验证什么；[ ] 区分“本地逻辑测试通过”和“真实模型服务可用”。

### 第 11 天：看懂完整工具调用循环

**搬运**：无。

**看**：`BaseAgent._call_llm()`、`get_tools()`、`_validate_tool_input()`。重点画出：模型返回 `tool_use` → 白名单 → 参数校验 → handler → `tool_result` → 下一次模型请求。

**练习**：跟踪已有 `test_tool_use_round_trip_executes_only_whitelisted_tool()`。在自己的测试里增加不在白名单的工具名，观察返回给模型的错误结果。正常执行与拒绝执行分别记录。

**验收**：[ ] 知道工具调用是代码执行，不是模型“自行操作”；[ ] 知道为什么限制轮数；[ ] 能说明异常怎样回填以及如何避免无限工具循环。

### 第 12 天：单 Agent 路由、澄清和降级

**搬运**：无。

**看**：`run()`、`_needs_clarification()`、`_route_decision()`、`_domain_scores()`、`_best_agent()`、`_execute()`。

**练习**：在 `tests/test_learning_routing.py` 构造已给定意图的 `Request`，验证登录、退款、转人工、低置信度未知意图；用假客户端模拟技术 Agent 失败后的通用 Agent 降级。

**验收**：[ ] 路由用例不依赖模型随机输出；[ ] 解释意图分组、领域信号、实例选择的关系；[ ] 保存一个澄清样例和一个失败降级样例。

### 第 13 天：主辅协作与结果合并

**搬运**：无。

**看**：`RoutingDecision.agent_types`、`multi_agent`、`run_parallel()`、`ResponseComposer.compose()`。

**练习**：沿用“登录 401，同时重复扣款”；固定主辅角色的假回复，模拟一个辅助角色失败，以及合成模型失败。对照 `return_exceptions=True` 和回退文本。

**验收**：[ ] 能解释为何并行后还要统一回复；[ ] 知道多次模型调用可能增加成本；[ ] 知道部分失败与全部失败的结果需要分别验证。

### 第 14 天：第一个自己的命令行演示

**搬运**：无。

**自己写**：`exercises/day14_chat.py`。从本机 `.env` 加载模型配置，创建编排器，构造请求并打印结果。今天先跑不依赖知识库的示例，RAG 在第 18 天再接。

先用 FakeClient 跑通逻辑；有可用模型配置后再做少量真实请求。没有 key 时保留离线成果并标注“真实服务待验证”，不声称完成真实端到端运行。

```powershell
.\.venv\Scripts\python.exe -m exercises.day14_chat
```

**验收**：[ ] 能画出“意图 → 路由 → Agent → 工具 → 回复”的流程；[ ] 能把 FakeClient 演示和真实调用分开记录；[ ] 已有至少一个自己新增的有效用例。

## 第 15～22 天：逐项补齐运行能力

### 第 15 天：工具管理层的缓存和超时

**搬运**：`mcp/tool_manager.py`。

**看**：`Tool`、`ToolResult`、`ToolStats`、`register()`、`call()`、参数校验和缓存键。与前面 `AgentToolSpec` 比较：一个是角色可见的工具描述，一个是底层能力调用管理。

**练习**：在 `exercises/day15.py` 注册一个本地计数 handler；同参数调用两次，查看 handler 执行次数和缓存状态。用短超时加长延迟 handler 验证超时。

**验收**：[ ] 无外部模型调用也能验证 handler 管理；[ ] 能解释缓存命中与源数据更新的关系；[ ] 知道代码里的“mcp”名称不自动证明实现了标准 MCP 通信协议。

### 第 16 天：熔断、fallback 和检索增强

**搬运**：无。

**看**：`CircuitBreaker` 的状态、`record_failure()`、`allow()`、`_fallback_result()`、`rewrite_query()`、`search_with_rewrite()`、`_rerank()`。

**练习**：用短恢复时间的熔断器模拟连续失败、拒绝调用和恢复探测；用假的改写/重排模型响应，验证召回合并去重的结果。缓存和熔断实验分开，避免缓存掩盖失败。

**验收**：[ ] 知道熔断与单次超时的区别；[ ] fallback 明确标注未能查询，而不是编造查询成功；[ ] 说明多次改写和重排会增加模型调用及延迟。

### 第 17 天：知识库独立验证

**搬运**：`mcp/knowledge_base.py`。

**看**：`__init__()`、`_chunk_text()`、`add_documents()`、`search()` 及异步包装。注意构造知识库时就可能连接 ChromaDB、加载默认资料和准备 embedding 模型。

**练习**：在 `exercises/day17_kb.py` 明确使用自己仓库的 `./data/chroma-learning` 持久化路径。先尝试连接服务；没有服务时源码会回退到本地持久化模式。准备三篇自己写的退款、发票和 401 排障资料，先直接检索。

首次准备 embedding 模型可能需要下载；记录实际错误与日志。不要把模型下载失败当成“检索没找到文档”。重复导入注意文档 ID 去重逻辑，先看实现再重跑。

**验收**：[ ] 保存问题、返回片段和相关度；[ ] 区分片段数和原文档数；[ ] 知道向量距离不一定是可直接使用的正确概率。

### 第 18 天：把 RAG 接入 Agent

**搬运**：无。

**练习**：在 `exercises/day18_rag.py` 创建知识库、工具管理器，注册 `knowledge_search`，再通过 `build_shared_rag_tools()` 和 `set_shared_tools()` 暴露给 Agent。初始化方式参考原 API 的 `lifespan()`，今天只阅读，不搬 API。

先用 FakeClient 强制输出一次检索 `tool_use`，验证整条回填流程；再用真实模型观察它是否选择检索。看工具轨迹中的调用与结果，不能只凭回答含有文档词句就断言 RAG 生效。

**验收**：[ ] Agent 工具名 `search_knowledge_base` 与底层 `knowledge_search` 的关系清楚；[ ] 保存实际工具调用记录；[ ] 能解释当前代码是 Agent 调用检索，而非 `/chat` 固定前置检索。

### 第 19 天：工作记忆写入和读取

**搬运**：`memory/conversation_memory.py`。

**看**：`MsgRole`、`Message`、`MemoryContext`、`MemoryManager.__init__()`、`add_message()`、`get_context()`、键生成方法。

**自己创建**：`docker-compose.learning.yml`，仅配置 Redis 学习服务并映射主机 6379 端口；使用自己设置的密码。原 Redis 服务配置可以作为参考，不提前复制完整部署文件。ChromaDB 暂时继续本地模式。

```powershell
docker compose -f docker-compose.learning.yml up -d redis
```

**练习**：`exercises/day19_memory.py`。给同用户同会话写入两条消息，再使用不同 `conv_id` 和不同 `user_id` 读取；检查 Redis TTL 和本次结果。

**验收**：[ ] Redis 可连接；[ ] 不同用户消息隔离；[ ] 区分当前会话近期消息和同用户跨会话情景检索，不误以为所有记忆都严格按会话隔离。

### 第 20 天：压缩摘要、情景记忆和用户画像

**搬运**：无。

**看**：`_compress()`、`_merge_summary()`、`_store_episodic()`、`_search_episodic()`、`update_profile()`、`to_prompt_text()`。

**练习**：在独立学习会话中逐步写入超过压缩阈值的消息，观察 Redis 最近消息、摘要和情景集合的变化。再做“我要退款 → 订单号是 #12345 → 多久能到账”的连续对话。

**验收**：[ ] 记录压缩前后实际条数；[ ] 说明消息条数与对话轮数不同；[ ] 比较是否保留订单号；[ ] 知道摘要和画像也可能产生错误，后台画像任务还需管理生命周期。

### 第 21 天：监控是否真的影响选择

**搬运**：`monitor/performance_monitor.py`。

**看**：`AnomalyDetector`、`start()/stop()`、`_collect()`、`_routing_penalty()`、告警阈值和 `summary()`。回到编排器读 `routing_score()`、`update_routing_penalties()`、`_best_agent()`。

**练习**：用假统计或固定调用结果验证成功率、延迟和惩罚分。比较同角色一个实例与两个实例时的选择结果。

**验收**：[ ] 单实例配置下不夸大降权带来的调度效果；[ ] 停止后台任务后能正常退出；[ ] 知道项目专用 Prometheus 指标的注册受初始化配置影响，默认 `/metrics` 有内容不代表这些业务指标已注册。

### 第 22 天：评测器能证明什么

**搬运**：`evaluation/evaluator.py`。

**看**：`IntentEvaluator.evaluate()`、`LLMJudge.judge()`、`EndToEndEvaluator.run()`、`_evaluate_dialog_case()`、`_detect_regressions()` 和基线保存。

**练习**：自己构造五条意图评测，先用可控预测值验证准确率和每类指标。用假的 Judge 返回值验证通过阈值和回归逻辑；真实模型评分放到第 28 天。

**验收**：[ ] 能解释 Accuracy 和 Macro-F1 关注的差别；[ ] 知道 Judge 失败要单独记录；[ ] 知道对话评测直接调用编排器，并未完整覆盖 `/chat` 的 Redis 读写和画像任务。

## 第 23～30 天：接通、验证、形成自己的成果

### 第 23 天：现在再搬完整 API 入口

**搬运**：`api/main.py`。它需要的本地模块到今天已经齐全。

**看**：`lifespan()`、`ChatRequest`、`ChatResponse`、`chat()`；先忽略装饰性 banner。核对本机 `.env` 中的 localhost、端口和相对数据路径。

先启动第 19 天的 Redis 学习服务，再运行：

```powershell
.\.venv\Scripts\python.exe -m uvicorn api.main:app --host 127.0.0.1 --port 8000
```

打开 `http://localhost:8000/health` 和 `http://localhost:8000/docs`，通过 `/chat` 发送 JSON。

**验收**：[ ] 能解释启动阶段初始化哪些对象；[ ] 区分服务启动失败与请求处理失败；[ ] 返回字段能对应编排器结果；[ ] 服务退出时检查连接和监控任务的关闭行为。

### 第 24 天：用接口检查完整链路

**搬运**：无。

**验证清单**：问候、技术问题、账单问题、复合请求、转人工、低置信度澄清，以及连续三轮退款问题。

查看 `/skills`、`/skills/reload`、`/knowledge/add`、`/knowledge/stats`、`/search`、`/trace/tools` 和 `/trace/tool/{request_id}`。以 `/docs` 中实际请求 schema 为准，注意有的接口用 JSON body，有的用查询参数。

**自己写**：`docs/learning-notes/day24.md`，保存脱敏后的请求和结果，注明模型配置、是否真实调用、工具是否使用、记忆是否影响答案。

**验收**：[ ] 同会话继续请求会沿用 `conv_id`；[ ] 不同用户上下文不串用；[ ] `knowledge_used` 能与工具轨迹对照；[ ] 接口验证和离线测试分别记录。

### 第 25 天：理解完整 Docker 部署

**搬运**：`Dockerfile`、`.dockerignore`、`docker-compose.yml`、`config/prometheus.yml`、`config/nginx/nginx.conf`。

**看**：构建阶段、依赖服务、健康检查、端口映射、数据卷和 `.env`。停止第 19 天的学习 Redis 服务以释放端口，但不删除其数据卷：

```powershell
docker compose -f docker-compose.learning.yml stop
```

本机模式用 `localhost:8001` 连接 ChromaDB；容器内应使用服务名 `chromadb:8000`。迁移后的 `.env` 如果仍写 localhost，需在 Compose 的应用 `environment` 中明确覆盖：

```yaml
CHROMA_HOST: chromadb
CHROMA_PORT: 8000
```

按源文件现有 environment 是映射还是列表的格式加入相同设置。Redis URL 和 `/app/data` 路径也核对容器配置。不要把本机可用的 localhost 原样当作容器依赖地址。

```powershell
docker compose up -d --build
docker compose ps
docker compose logs --tail 100 echomind
```

**验收**：[ ] API、Redis、ChromaDB 的连接关系清楚；[ ] 数据卷能持久化；[ ] 查看真实健康状态；[ ] 如果服务不健康，确认具体原因，例如 embedding 下载、服务配置或健康检查工具缺失，不盲删健康检查。

源码的 Linux shell 部署脚本不列入核心搬运；先用跨平台的 Compose 命令理解部署。

### 第 26 天：搬入可运行的前端最小集合

**来源**：原始前端目录；**目标**：你的 `frontend/` 目录。

| 前端源文件 | 目标路径，相对于你的仓库 |
|---|---|
| `package.json` | `frontend/package.json` |
| `package-lock.json` | `frontend/package-lock.json` |
| `vite.config.js` | `frontend/vite.config.js` |
| `index.html` | `frontend/index.html` |
| `public/runtime-config.js` | `frontend/public/runtime-config.js` |
| `src/main.js` | `frontend/src/main.js` |
| `src/App.vue` | `frontend/src/App.vue` |
| `src/styles.css` | `frontend/src/styles.css` |
| `src/lib/backends.js` | `frontend/src/lib/backends.js` |
| `.gitignore` | `frontend/.gitignore` |

`index.html` 加载运行时配置；`main.js` 导入页面和样式；页面依赖后端适配文件，因此这批文件一并搬运。保留 lock 文件以便重复安装；Node 环境与构建工具要求根据实际依赖和报错核对。

```powershell
Set-Location -LiteralPath 'C:\Users\Babe\Desktop\EchoMind_twin\frontend'
npm ci
npm run dev
```

选择 Python 后端，默认开发代理指向 `http://localhost:8000`。当日在浏览器发送一条消息并查看网络请求。

**验收**：[ ] 页面可加载；[ ] 知道 `/api/python` 被 Vite 如何改写；[ ] 请求确实到自己的 Python 服务；[ ] 本地运行并完成一次 `npm run build` 验证。

原前端 Compose 同时引用了缺失的 Java 项目，并假定特定兄弟目录布局，故不在今天搬运。前端 Dockerfile 和 Nginx 配置是后续可选部署内容，届时针对你的根目录/`frontend` 布局改写。

### 第 27 天：页面交互和后端字段对应

**搬运**：无。

**看**：页面中发送消息、维护 `conv_id`、展示 Agent/路由/工具信息的代码，以及 `src/lib/backends.js` 中的 fetch 和响应映射。

**练习**：在自己的前端中移除 Java 选项或明确只启用 Python；为断开后端时的情况显示一条易懂的错误信息。修改后检查能否继续发消息和正确保留会话标识。

**验收**：[ ] 能把浏览器请求追踪到后端 `chat()`；[ ] 网络或服务失败能显示；[ ] 不把前端按钮存在当作后端能力已实现的证据。

### 第 28 天：自己的数据和基线

**搬运**：无。

**自己写**：`evaluation_cases/intent_cases.json`、`evaluation_cases/dialog_cases.json`，以及脱敏后的 `evaluation_results/baseline.md`。

准备约 50 条意图样例和 10 组对话样例，按业务类型均衡分布。先标注再跑，留下约 20% 的样例用于第 29 天最终验证。标注意图名取自代码枚举；预期回复采用核验要点，不要求逐字一致。

用 `/eval/run` 的自定义请求 body 验证，避免只跑默认样例。若只跑意图评测，显式传 `dialog_cases: []`；若只跑对话评测，显式传 `intent_cases: []`，以免自动补入另一类默认用例。

**记录**：实际模型、样本量、Accuracy、Macro-F1、每类错误、对话 Judge 分数、失败数。HTTP 响应耗时与编排器的 `latency_ms` 分开，后者不包含整个请求链路。Judge 分数不要直接改名为人工标注的“回答准确率”。

**验收**：[ ] 固定数据和模型配置；[ ] 包含失败样例；[ ] 人工核对至少几条高分/低分结果；[ ] 小样本结果限定在本评测集上。

### 第 29 天：完成一个你自己的改进

**搬运**：无。

推荐选择退款、支付异常和发票之间的意图边界改进。先找三个已出现的错误，在自己的规则、模板或 Few-shot 提示中做小修改；给这些情况增加回归用例。不要同时修改路由、RAG 和记忆，避免无法判断提升原因。

其他可选方向：跨轮实体传递、知识检索偏题、工具错误回填、前端调试展示。先复现具体问题再决定改哪里。

**自己写**：`evaluation_results/improvement.md`，写清问题、原因、改动、固定样例的前后结果和仍然失败的情况。

**验收**：[ ] 原来的失败可以复现；[ ] 修改后用同一批数据比较；[ ] 检查未参与调整的保留样例；[ ] 没有只挑成功样例汇报。

### 第 30 天：让别人能看懂你的成果

**搬运**：无。原始 Wiki 可以在本地参考，学习成果文档由自己写。

**完成**：自己的 README、`docs/architecture.md`、`docs/interview.md` 和改进记录。README 写安装启动、目录、接口、项目来源、自己的实现/改动、实测范围和已知限制。

三分钟介绍按“业务问题 → 请求链路 → 两个设计取舍 → 我的改进 → 验证结果 → 当前限制”组织。准备回答：为什么多 Agent、为什么分层记忆、什么时候检索、工具由谁执行、失败如何处理、评测覆盖到哪里。

**验收**：[ ] 从自己的仓库可以重建环境；[ ] 能完整讲一条请求；[ ] 能解释一处自己的修改；[ ] 指标能找到对应数据；[ ] 不把学习搬运项目表述成全部独立原创。

## 搬运操作模板：一次只搬当天的文件

例如第 2 天，以下代码仅复制文本工具。此模板供你届时执行，方案编写时没有执行源码复制。

```powershell
$learnSource = 'C:\Users\Babe\Desktop\myProject\EchoMind所有代码+详细文档+简历\EchoMind'
$learnRepo = 'C:\Users\Babe\Desktop\EchoMind_twin'
$learnFiles = @('core\llm_utils.py')

foreach ($learnFile in $learnFiles) {
    $learnFrom = Join-Path $learnSource $learnFile
    $learnTo = Join-Path $learnRepo $learnFile
    if (-not (Test-Path -LiteralPath $learnFrom -PathType Leaf)) {
        throw "源文件不存在: $learnFrom"
    }
    if (Test-Path -LiteralPath $learnTo) {
        throw "目标已有文件，请先比较: $learnTo"
    }
    New-Item -ItemType Directory -Path (Split-Path -Parent $learnTo) -Force | Out-Null
    Copy-Item -LiteralPath $learnFrom -Destination $learnTo
}
```

原项目的 `.git`、`.venv`、`.idea`、`.pytest_cache`、`data`、`logs` 和 `.env` 不在清单里。数据库和运行日志使用自己跑出来的内容。

原始资料里的“简历包装”文案和指标是参考材料。效果数字只有你在明确样本和配置下跑出结果后才能作为你的项目记录；真实支付、退款执行和人工工单接入也按实际实现描述。

## 每日提交模板

每天的源码、练习和笔记放在同一次提交里。先检查差异，逐个加入当天文件，避免一次性加入无关内容。以下仍以第 2 天为例：

```powershell
Set-Location -LiteralPath 'C:\Users\Babe\Desktop\EchoMind_twin'
git status --short
git diff
git add -- core/llm_utils.py exercises/day02.py docs/learning-notes/day02.md
git diff --cached --stat
git diff --cached
git commit -m 'day02: understand LLM text extraction'
```

新建的 `__init__.py`、环境模板等也在对应天逐项加入。提交前确认暂存区没有真实密钥和运行数据。推送是之后按你的实际进度进行的 Git 操作，本方案没有创建源码提交或向远端推送。

笔记模板：

```text
今天学习了什么：
搬入/修改了哪些文件：
关键函数的输入、输出和依赖：
一个具体请求怎样经过这个模块：
我写了什么练习，实际输出是什么：
一个失败案例和可能原因：
我还没理解的点：
今天能用于面试解释的一句话：
```

## 里程碑

- **第 7 天**：能独立说明响应解析、Skills 和意图融合。
- **第 14 天**：能用离线客户端演示角色、工具、路由和协作；具备真实服务配置时再验证模型调用。
- **第 18 天**：能把自己编写的知识文档经工具回填到 Agent。
- **第 24 天**：能验证自己的 API、多轮对话和工具轨迹。
- **第 27 天**：能从自己的页面追踪到自己的后端。
- **第 30 天**：仓库包含可复现的运行说明、自己的练习、改动和验证证据。

下一步从第 1 天开始，完成环境、目录和配置模板；第 2 天才搬第一个 Python 源文件。
