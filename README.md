# 1panel-api-skills

1Panel HTTP API 完整接入 Agent Skill：认证签名（HMAC-SHA256 推荐 / 旧版 MD5 回退）、全部 767 个 v2 端点目录（58 个模块分组）、响应信封解读、纯标准库签名调用脚本。供支持 Agent Skills / SKILL.md 约定的 AI 代理（ZCode、Claude Code、OpenCode、Codex CLI 等）直接操作 1Panel v2 实例（网站、应用商店、容器、计划任务、防火墙、文件、数据库、AI 模块等）。

- 官方 API 手册：https://docs.fit2cloud.com/1panel/dev_manual/api_manual/
- 端点目录来源：1Panel v2 实例 swagger（`/1panel/swagger/doc.json`，需面板登录态，API key 不被接受），spec 版本 2.0
- 镜像日期：2026-10-06

## 结构

```
1panel-api-skills/
├── SKILL.md                       # 触发条件 + 环境变量 + 签名算法表 + 端点约定 + 安全边界
├── references/
│   ├── endpoints.md               # 767 个操作：方法/路径/说明/请求体模型，按 58 个模块分组
│   └── 1panel-swagger-v2.json     # 完整 swagger spec（grep 模型名查字段级 schema，含 required 数组）
└── scripts/
    └── 1panel_api.py              # 纯标准库：call（签名调用）/ swagger / self-check（签名向量自检）
```

## 使用

在面板创建 API Key（v2.2.1+ 用户菜单 → 用户信息 → API 接口）并配置 IP 白名单，然后：

```bash
export ONEPANEL_BASE_URL=http://host:port
export ONEPANEL_API_KEY=<key>

python scripts/1panel_api.py self-check
python scripts/1panel_api.py call POST api/v2/websites/search '{"page":1,"pageSize":20,"orderBy":"created_at","order":"descending"}'
```

关键约定：spec 路径需拼 `basePath=/api/v2` 前缀；`:param` 为路径参数需替换真值；`core/*` 为面板会话层、不接受 API key 签名；HTTP 恒为 200，业务结果看 JSON 信封 `code` 字段。

## License

MIT
