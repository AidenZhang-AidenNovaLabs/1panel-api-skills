---
name: 1panel-api-skills
description: Call the 1Panel HTTP API directly with signed requests — any endpoint on v1/v2 (websites, apps, containers, cronjobs, toolbox, logs, mutations). Use when the user asks to query or operate their 1Panel instance beyond the curated read-only actions in 1panel-skills, or explicitly says "1Panel API". Covers auth-header signing (HMAC-SHA256 / legacy MD5), endpoint conventions, and response-envelope interpretation.
---

# 1panel-api-skills

Signed HTTP access to a 1Panel instance's full REST API. Verified against a live v2 install.

## Setup

Export before calling (never hardcode keys into files):

- `ONEPANEL_BASE_URL` — e.g. `http://host:port`
- `ONEPANEL_API_KEY` — from panel: v2.2.1+ user menu → user info → API 接口；earlier under 面板设置. The key needs an IP whitelist covering the caller.
- `ONEPANEL_API_ALGO` — `hmac-sha256` (default) or `md5`
- `ONEPANEL_SKIP_TLS_VERIFY` — `true` for self-signed https

## Script

`scripts/1panel_api.py` — stdlib-only, three modes:

1. `python scripts/1panel_api.py self-check` — verify signature vectors locally, no network.
2. `python scripts/1panel_api.py call METHOD PATH [JSON_BODY]` — signed call. Write PATH **without** the leading slash (Git Bash mangles `/api/...` into a filesystem path); the script re-adds it. Example: `call POST api/v2/websites/search '{"page":1,"pageSize":20,"orderBy":"created_at","order":"descending"}'`.
3. `python scripts/1panel_api.py swagger` — try to fetch the swagger spec with the API key; most installs gate it behind a browser session (see Endpoint discovery), so prefer the bundled references instead.

## Auth (from official API manual)

Two headers on every API call; timestamp is Unix seconds, keep panel time NTP-synced:

| Algo | 1Panel-Token |
|---|---|
| `hmac-sha256` (recommended) | `hmac_sha256(key=API-Key, msg="1panel:" + timestamp)` |
| `md5` (legacy, being removed) | `md5("1panel" + API-Key + timestamp)` |

If a call returns the 401-JSON envelope, retry with the other algo before suspecting the whitelist.

## Reading responses

HTTP status is almost always 200; the business result is in the JSON envelope:

- `{"code": 200, "data": ...}` — success. `data` may be `null` or `{"total": 0, "items": null}` on an empty panel.
- `code: 400` — validation error; `message` names the missing/invalid fields (e.g. `OrderBy ... required`).
- `code: 401` `用户未登录` — signed request rejected: wrong algo, bad key, expired key validity, or caller IP not in the key's whitelist.

## Endpoint discovery

- Full catalog of **767 operations** (1Panel 2.0): [references/endpoints.md](references/endpoints.md) — every method/path/summary grouped into 58 modules (AI, Website, File, System Setting, App, Container, Firewall, Database, Cronjob, …).
- Spec paths omit the prefix; `basePath` is `/api/v2`, so spec path `/websites/search` = `api/v2/websites/search` in the caller.
- For field-level request/response schemas, grep the bundled spec [references/1panel-swagger-v2.json](references/1panel-swagger-v2.json) for `"<ModelName>"` (e.g. `dto.CronjobOperate`) — every definition has a `required` array.
- Fresh spec from a running panel: the swagger UI at `{base}/1panel/swagger/index.html` needs a **browser login session** (API key is not accepted). In a browser with an active panel session, fetch `/1panel/swagger/doc.json`; regenerate endpoints.md the same way if the panel version differs.

## Endpoint conventions

- API prefix `/api/v1` (1Panel v1) or `/api/v2` (1Panel v2).
- Most list endpoints are `POST <prefix>/<module>/search` with a JSON body; `page`, `pageSize`, `orderBy`, `order` are required on many of them even when the filters are optional.
- Detail/config endpoints are usually `GET <prefix>/<module>/<id>`; operations are `POST` with a JSON body.
- `:name` segments in the catalog are path params — substitute real values (`/dashboard/base/:ioOption/:netOption` → `api/v2/dashboard/base/all/all`).
- `core/*` endpoints (login, captcha, user info, login logs) are the panel's own session layer and reject API-key signing with the 401 envelope — they need a browser session; everything else works signed.
- The officially documented example is `POST api/v2/toolbox/device/base` with `{}` — returns DNS/hosts/device info, good first smoke test.

## Safety

- Mutations (create/update/delete/restart) take effect immediately — confirm scope with the user before destructive ones, and prefer `search`/`list` first to name the exact target id.
- The base URL must be the user's own panel; the script only accepts `http://` / `https://` targets.
