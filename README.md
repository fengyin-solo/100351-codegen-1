# 计量器具检定校准平台

面向计量标准器溯源、被检器具检定、校准证书出具、期间核查与不合格处置的一体化计量业务后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 计量标准器 | `stddevice` | 计量标准器 | 标准器编号、标准器名称、准确度等级 |
| 被检器具 | `instrument` | 被检器具 | 器具编号、器具名称、规格型号 |
| 检定规程 | `regulation` | 检定规程 | 规程编号、规程名称、适用器具 |
| 检定任务 | `job` | 检定任务单 | 任务编号、关联规程、受检器具数 |
| 校准证书 | `certificate` | 校准证书 | 证书编号、受检器具、检定结论 |
| 标准物质 | `stdmaterial` | 标准物质 | 物质编号、物质名称、浓度标称值 |
| 环境条件记录 | `environment` | 环境条件记录 | 记录编号、所在实验室、温度示值 |
| 检定人员资质 | `personnel` | 检定人员 | 人员编号、人员姓名、持证项目 |
| 期间核查 | `interimcheck` | 期间核查记录 | 核查编号、核查对象、核查方式 |
| 不合格处置 | `nonconform` | 不合格处置单 | 处置编号、关联器具、不合格项 |
| 送检委托 | `entrust` | 送检委托单 | 委托单号、委托单位、送检器具数 |
| 量值溯源 | `traceability` | 量值溯源记录 | 溯源编号、溯源项目、上级机构 |
| 器具停用 | `suspension` | 器具停用单 | 停用单号、停用器具、停用原因 |
| 复检提醒 | `recheck` | 复检提醒单 | 提醒编号、关联器具、上次检定日 |
| 检定费用 | `fee` | 检定费用单 | 费用单号、委托单位、器具数量 |
| 原始记录 | `rawrecord` | 原始记录 | 记录编号、关联任务、检定项目 |
| 检定场地 | `site` | 检定场地 | 场地编号、场地名称、使用面积 |
| 抽检复核 | `sampling` | 抽检复核单 | 抽检编号、抽检批次、抽检数量 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
