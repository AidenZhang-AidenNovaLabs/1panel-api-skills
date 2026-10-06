# 1Panel v2 API endpoints (767 operations, spec version 2.0)

Source: live 1Panel 2.0 instance swagger spec, bundled at [1panel-swagger-v2.json](1panel-swagger-v2.json).
Grep that file for `"<ModelName>"` inside `definitions` to get full request/response schemas (each has a `required` array).

## AI (85)

- `POST /ai/accounts` — Create model account (body: `dto.AgentAccountCreateReq`)
- `POST /ai/accounts/counts` — Count model accounts by provider (body: `dto.AgentAccountProviderCountReq`)
- `POST /ai/accounts/delete` — Delete model account (body: `dto.AgentAccountDeleteReq`)
- `POST /ai/accounts/models` — List model account models (body: `dto.AgentAccountModelReq`)
- `POST /ai/accounts/models/create` — Create model account model (body: `dto.AgentAccountModelCreateReq`)
- `POST /ai/accounts/models/delete` — Delete model account model (body: `dto.AgentAccountModelDeleteReq`)
- `POST /ai/accounts/models/discover` — Discover custom provider models (body: `dto.AgentAccountModelDiscoverReq`)
- `POST /ai/accounts/models/update` — Update model account model (body: `dto.AgentAccountModelUpdateReq`)
- `GET /ai/accounts/providers` — Get model account providers
- `POST /ai/accounts/search` — Page model accounts (body: `dto.AgentAccountSearch`)
- `POST /ai/accounts/update` — Update model account (body: `dto.AgentAccountUpdateReq`)
- `POST /ai/accounts/verify` — Verify model account (body: `dto.AgentAccountVerifyReq`)
- `POST /ai/agents` — Create Agent (body: `dto.AgentCreateReq`)
- `POST /ai/agents/agent/bind` — Bind Agent role channel (body: `dto.AgentRoleBindReq`)
- `POST /ai/agents/agent/channels` — Get Agent role channels from config file (body: `dto.AgentRoleChannelsReq`)
- `POST /ai/agents/agent/create` — Create Agent role (body: `dto.AgentRoleCreateReq`)
- `POST /ai/agents/agent/delete` — Delete Agent role (body: `dto.AgentRoleDeleteReq`)
- `POST /ai/agents/agent/list` — Get configured Agent roles from config file (body: `dto.AgentConfiguredAgentsReq`)
- `POST /ai/agents/agent/md/list` — Get Agent role markdown files (body: `dto.AgentRoleMarkdownFilesReq`)
- `POST /ai/agents/agent/md/update` — Update Agent role markdown file (body: `dto.AgentRoleMarkdownFilesUpdateReq`)
- `POST /ai/agents/agent/unbind` — Unbind Agent role channel (body: `dto.AgentRoleBindReq`)
- `POST /ai/agents/batch/install` — Batch install Agent (body: `dto.AgentBatchInstallReq`)
- `POST /ai/agents/batch/operate` — Batch operate Agent (body: `dto.AgentBatchOperateReq`)
- `POST /ai/agents/batch/skill/install` — Batch install Agent Skill (body: `dto.AgentBatchSkillInstallReq`)
- `POST /ai/agents/batch/upgrade` — Batch upgrade Agent (body: `dto.AgentBatchUpgradeReq`)
- `POST /ai/agents/channel/delete` — Delete Agent channel config (body: `dto.AgentChannelDeleteReq`)
- `POST /ai/agents/channel/dingtalk/get` — Get Agent DingTalk channel config (body: `dto.AgentIDReq`)
- `POST /ai/agents/channel/dingtalk/update` — Update Agent DingTalk channel config (body: `dto.AgentDingTalkConfigUpdateReq`)
- `POST /ai/agents/channel/discord/get` — Get Agent Discord channel config (body: `dto.AgentIDReq`)
- `POST /ai/agents/channel/discord/update` — Update Agent Discord channel config (body: `dto.AgentDiscordConfigUpdateReq`)
- `POST /ai/agents/channel/feishu/get` — Get Agent Feishu channel config (body: `dto.AgentFeishuConfigReq`)
- `POST /ai/agents/channel/feishu/update` — Update Agent Feishu channel config (body: `dto.AgentFeishuConfigUpdateReq`)
- `POST /ai/agents/channel/pairing/approve` — Approve Agent channel pairing code (body: `dto.AgentChannelPairingApproveReq`)
- `POST /ai/agents/channel/qqbot/get` — Get Agent QQ Bot channel config (body: `dto.AgentIDReq`)
- `POST /ai/agents/channel/qqbot/update` — Update Agent QQ Bot channel config (body: `dto.AgentQQBotConfigUpdateReq`)
- `POST /ai/agents/channel/telegram/get` — Get Agent Telegram channel config (body: `dto.AgentTelegramConfigReq`)
- `POST /ai/agents/channel/telegram/update` — Update Agent Telegram channel config (body: `dto.AgentTelegramConfigUpdateReq`)
- `POST /ai/agents/channel/wecom/get` — Get Agent QQ Bot channel config (body: `dto.AgentIDReq`)
- `POST /ai/agents/channel/wecom/update` — Update Agent WeCom channel config (body: `dto.AgentWecomConfigUpdateReq`)
- `POST /ai/agents/channel/weixin/get` — Get Agent Weixin channel config (body: `dto.AgentIDReq`)
- `POST /ai/agents/channel/weixin/login` — Login Agent Weixin channel (body: `dto.AgentWeixinLoginReq`)
- `POST /ai/agents/config-file/get` — Get Agent config file (body: `dto.AgentConfigFileReq`)
- `POST /ai/agents/config-file/update` — Update Agent config file (body: `dto.AgentConfigFileUpdateReq`)
- `POST /ai/agents/delete` — Delete Agent (body: `dto.AgentDeleteReq`)
- `POST /ai/agents/delete/check` — Delete check Agent (body: `dto.AgentIDReq`)
- `POST /ai/agents/hermes/chat/sessions` — Get Hermes chat sessions (body: `dto.AgentIDReq`)
- `POST /ai/agents/hermes/chat/sessions/delete` — Delete Hermes chat session (body: `dto.AgentHermesChatSessionDeleteReq`)
- `POST /ai/agents/hermes/chat/sessions/rename` — Rename Hermes chat session (body: `dto.AgentHermesChatSessionRenameReq`)
- `POST /ai/agents/model/get` — Get Agent model config (body: `dto.AgentIDReq`)
- `POST /ai/agents/model/update` — Update Agent model config (body: `dto.AgentModelConfigUpdateReq`)
- `POST /ai/agents/other/get` — Get Agent Other config (body: `dto.AgentIDReq`)
- `POST /ai/agents/other/update` — Update Agent Other config (body: `dto.AgentOtherConfigUpdateReq`)
- `POST /ai/agents/overview` — Get Agent overview (body: `dto.AgentOverviewReq`)
- `POST /ai/agents/plugin/check` — Check Agent plugin installation status (body: `dto.AgentPluginCheckReq`)
- `POST /ai/agents/plugin/install` — Install Agent plugin (body: `dto.AgentPluginInstallReq`)
- `POST /ai/agents/plugin/uninstall` — Uninstall Agent plugin (body: `dto.AgentPluginUninstallReq`)
- `POST /ai/agents/plugin/upgrade` — Upgrade Agent plugin (body: `dto.AgentPluginUpgradeReq`)
- `POST /ai/agents/plugins/install` — Install an OpenClaw marketplace plugin (body: `dto.AgentPluginMarketInstallReq`)
- `POST /ai/agents/plugins/list` — List OpenClaw plugins (body: `dto.AgentPluginsReq`)
- `POST /ai/agents/plugins/operate` — Operate an OpenClaw plugin (body: `dto.AgentPluginOperateReq`)
- `POST /ai/agents/plugins/search` — Search OpenClaw plugins (body: `dto.AgentPluginSearchReq`)
- `POST /ai/agents/remark` — Update Agent remark (body: `dto.AgentRemarkUpdateReq`)
- `POST /ai/agents/search` — Page Agents (body: `dto.SearchWithPage`)
- `POST /ai/agents/security/get` — Get Agent Security config (body: `dto.AgentIDReq`)
- `POST /ai/agents/security/update` — Update Agent Security config (body: `dto.AgentSecurityConfigUpdateReq`)
- `POST /ai/agents/skills/install` — Install Agent skill (body: `dto.AgentSkillInstallReq`)
- `POST /ai/agents/skills/list` — List Agent skills (body: `dto.AgentIDReq`)
- `POST /ai/agents/skills/search` — Search Agent skills (body: `dto.AgentSkillSearchReq`)
- `POST /ai/agents/skills/uninstall` — Uninstall Agent skill (body: `dto.AgentSkillUninstallReq`)
- `POST /ai/agents/skills/update` — Update Agent skill status (body: `dto.AgentSkillUpdateReq`)
- `POST /ai/agents/token/reset` — Reset Agent token (body: `dto.AgentTokenResetReq`)
- `POST /ai/agents/website/bind` — Bind Agent website (body: `dto.AgentWebsiteBindReq`)
- `POST /ai/agents/website/unbind` — Unbind Agent website (body: `dto.AgentIDReq`)
- `POST /ai/domain/bind` — Bind domain (body: `dto.OllamaBindDomain`)
- `POST /ai/domain/get` — Get bind domain (body: `dto.OllamaBindDomainReq`)
- `POST /ai/domain/update` — Update bind domain (body: `dto.OllamaBindDomain`)
- `GET /ai/gpu/load` — Load gpu / xpu info
- `GET /ai/gpu/options` — Get CPU options
- `POST /ai/ollama/close` — Close Ollama model conn (body: `dto.OllamaModelName`)
- `POST /ai/ollama/model` — Create Ollama model (body: `dto.OllamaModelName`)
- `POST /ai/ollama/model/del` — Delete Ollama model (body: `dto.ForceDelete`)
- `POST /ai/ollama/model/load` — Page Ollama models (body: `dto.OllamaModelName`)
- `POST /ai/ollama/model/recreate` — Rereate Ollama model (body: `dto.OllamaModelName`)
- `POST /ai/ollama/model/search` — Page Ollama models (body: `dto.SearchWithPage`)
- `POST /ai/ollama/model/sync` — Sync Ollama model list

## Alert (15)

- `POST /alert` — Create alert (body: `dto.AlertCreate`)
- `GET /alert/clams/list` — Get clams
- `POST /alert/config/del` — Delete alert config (body: `dto.DeleteRequest`)
- `POST /alert/config/info` — Get alert config
- `POST /alert/config/search` — Page alert config (body: `dto.AlertConfigPageReq`)
- `POST /alert/config/test` — Test alert config (body: `dto.AlertConfigTest`)
- `POST /alert/config/update` — Update alert config (body: `dto.AlertConfigUpdate`)
- `POST /alert/cronjob/list` — Get cron jobs (body: `dto.CronJobReq`)
- `POST /alert/del` — Delete alert (body: `dto.DeleteRequest`)
- `GET /alert/disks/list` — Get disks
- `POST /alert/logs/clean` — Clean alert logs
- `POST /alert/logs/search` — Page alert logs (body: `dto.AlertLogSearch`)
- `POST /alert/search` — Page alert (body: `dto.AlertSearch`)
- `POST /alert/status` — Update alert status (body: `dto.AlertUpdateStatus`)
- `POST /alert/update` — Update alert (body: `dto.AlertUpdate`)

## App (33)

- `GET /apps/:key` — Search app by key
- `GET /apps/checkupdate` — Get app list update
- `GET /apps/detail/:appId/:version/:type` — Search app detail by appid
- `GET /apps/detail/node/:appKey/:version` — Search app detail by appkey and version
- `GET /apps/details/:id` — Get app detail by id
- `GET /apps/icon/:key` — Get app icon by app_id
- `POST /apps/ignored/cancel` — Cancel Ignore Upgrade App (body: `request.ReqWithID`)
- `GET /apps/ignored/detail` — List Upgrade Ignored App
- `POST /apps/install` — Install app (body: `request.AppInstallCreate`)
- `POST /apps/installed/check` — Check app installed (body: `request.AppInstalledInfo`)
- `POST /apps/installed/conf` — Search default config by key (body: `dto.OperationWithNameAndType`)
- `POST /apps/installed/config/update` — Update app config (body: `request.AppConfigUpdate`)
- `POST /apps/installed/conninfo` — Search app password by key (body: `dto.OperationWithNameAndType`)
- `GET /apps/installed/delete/check/:appInstallId` — Check before delete
- `POST /apps/installed/ignore` — Ignore Upgrade App (body: `request.AppIgnoreUpgradeReq`)
- `GET /apps/installed/info/:appInstallId` — Get app install info
- `GET /apps/installed/list` — List app installed
- `POST /apps/installed/loadport` — Search app port by key (body: `dto.OperationWithNameAndType`)
- `POST /apps/installed/op` — Operate installed app (body: `request.AppInstalledOperate`)
- `GET /apps/installed/params/:appInstallId` — Search params by appInstallId
- `POST /apps/installed/params/update` — Change app params (body: `request.AppInstalledUpdate`)
- `POST /apps/installed/port/change` — Change app port (body: `request.PortUpdate`)
- `POST /apps/installed/search` — Page app installed (body: `request.AppInstalledSearch`)
- `POST /apps/installed/sort/update` — Update app install sort (body: `request.AppInstallSort`)
- `POST /apps/installed/sync` — Sync app installed
- `POST /apps/installed/update/versions` — Search app update version by install id
- `POST /apps/search` — List apps (body: `request.AppSearch`)
- `GET /apps/services/:key` — Search app service by key
- `POST /apps/sync/local` — Sync local  app list
- `POST /apps/sync/remote` — Sync remote app list
- `GET /apps/tags` — Get app tags
- `GET /core/settings/apps/store/config` — Get appstore config
- `POST /core/settings/apps/store/update` — Update appstore config (body: `dto.AppstoreUpdate`)

## Auth (17)

- `POST /core/auth/api/generate` — generate api key
- `POST /core/auth/api/update` — Update api config (body: `dto.ApiInterfaceConfig`)
- `GET /core/auth/captcha` — Load captcha
- `GET /core/auth/current` — Load current user info
- `POST /core/auth/current/update` — Update current user info (body: `dto.CurrentUserUpdate`)
- `POST /core/auth/expired/reset` — Reset system password expired (body: `dto.PasswordUpdate`)
- `POST /core/auth/login` — User login (body: `dto.Login`)
- `POST /core/auth/logout` — User logout
- `POST /core/auth/mfalogin` — User login with mfa (body: `dto.MFALogin`)
- `POST /core/auth/passkey/begin` — User login with passkey
- `POST /core/auth/passkey/del` — Delete passkey
- `POST /core/auth/passkey/finish` — User login with passkey
- `GET /core/auth/passkey/list` — List passkeys
- `POST /core/auth/passkey/register/begin` — Begin passkey registration (body: `dto.PasskeyRegisterRequest`)
- `POST /core/auth/passkey/register/finish` — Finish passkey registration
- `GET /core/auth/setting` — Get Setting For Login
- `GET /core/auth/welcome` — Get welcome page

## Backup Account (26)

- `POST /backups` — Create backup account (body: `dto.BackupOperate`)
- `POST /backups/backup` — Backup system data (body: `dto.CommonBackup`)
- `POST /backups/buckets` — List buckets (body: `dto.ForBuckets`)
- `GET /backups/check/{name}` — Check backup used
- `POST /backups/conn/check` — Check backup account (body: `dto.BackupOperate`)
- `POST /backups/del` — Delete backup account (body: `dto.OperateByID`)
- `GET /backups/local` — get local backup dir
- `GET /backups/options` — Load backup account options
- `POST /backups/record/del` — Delete backup record (body: `dto.BatchDeleteReq`)
- `POST /backups/record/description/update` — Update backup record description (body: `dto.UpdateDescription`)
- `POST /backups/record/download` — Download backup record (body: `dto.DownloadRecord`)
- `POST /backups/record/search` — Page backup records (body: `dto.RecordSearch`)
- `POST /backups/record/search/bycronjob` — Page backup records by cronjob (body: `dto.RecordSearchByCronjob`)
- `POST /backups/record/size` — Load backup record size (body: `dto.SearchForSize`)
- `POST /backups/recover` — Recover system data (body: `dto.CommonRecover`)
- `POST /backups/recover/byupload` — Recover system data by upload (body: `dto.CommonRecover`)
- `POST /backups/refresh/token` — Refresh token (body: `dto.BackupOperate`)
- `POST /backups/search` — Search backup accounts with page (body: `dto.SearchPageWithType`)
- `POST /backups/search/files` — List files from backup accounts (body: `dto.OperateByID`)
- `POST /backups/update` — Update backup account (body: `dto.BackupOperate`)
- `POST /backups/upload` — Upload file for recover (body: `dto.UploadForRecover`)
- `POST /core/backups` — Create backup account (body: `dto.BackupOperate`)
- `GET /core/backups/client/:clientType` — Load backup account base info
- `POST /core/backups/del` — Delete backup account (body: `dto.OperateByName`)
- `POST /core/backups/refresh/token` — Refresh token (body: `dto.OperateByName`)
- `POST /core/backups/update` — Update backup account (body: `dto.BackupOperate`)

## Clam (12)

- `POST /toolbox/clam` — Create clam (body: `dto.ClamCreate`)
- `POST /toolbox/clam/base` — Load clam base info
- `POST /toolbox/clam/del` — Delete clam (body: `dto.ClamDelete`)
- `POST /toolbox/clam/file/search` — Load clam file (body: `dto.ClamFileReq`)
- `POST /toolbox/clam/file/update` — Update clam file (body: `dto.UpdateByNameAndFile`)
- `POST /toolbox/clam/handle` — Handle clam scan (body: `dto.OperateByID`)
- `POST /toolbox/clam/operate` — Operate Clam (body: `dto.Operate`)
- `POST /toolbox/clam/record/clean` — Clean clam record (body: `dto.OperateByID`)
- `POST /toolbox/clam/record/search` — Page clam record (body: `dto.ClamLogSearch`)
- `POST /toolbox/clam/search` — Page clam (body: `dto.SearchClamWithPage`)
- `POST /toolbox/clam/status/update` — Update clam status (body: `dto.ClamUpdateStatus`)
- `POST /toolbox/clam/update` — Update clam (body: `dto.ClamUpdate`)

## Command (9)

- `POST /core/commands` — Create command (body: `dto.CommandOperate`)
- `POST /core/commands/del` — Delete command (body: `dto.OperateByIDs`)
- `POST /core/commands/export` — Export command
- `POST /core/commands/import` — Import command
- `POST /core/commands/list` — List commands (body: `dto.OperateByType`)
- `POST /core/commands/search` — Page commands (body: `dto.SearchWithPage`)
- `POST /core/commands/tree` — Tree commands (body: `dto.OperateByType`)
- `POST /core/commands/update` — Update command (body: `dto.CommandOperate`)
- `POST /core/commands/upload` — Upload command csv for list

## Container (28)

- `POST /containers` — Create container (body: `dto.ContainerOperate`)
- `POST /containers/clean/log` — Clean container log (body: `dto.OperationWithName`)
- `POST /containers/commit` — Commit Container (body: `dto.ContainerCommit`)
- `POST /containers/compose/clean/log` — Clean compose log (body: `dto.ComposeLogClean`)
- `POST /containers/download/log` — Download container logs (body: `dto.ContainerLog`)
- `POST /containers/files/content` — Get container file content (body: `dto.ContainerFileReq`)
- `POST /containers/files/del` — Delete container file (body: `dto.ContainerFileBatchDeleteReq`)
- `POST /containers/files/download` — Download container file (body: `dto.ContainerFileReq`)
- `POST /containers/files/search` — List container files (body: `dto.ContainerFileReq`)
- `POST /containers/files/size` — Get container file size (body: `dto.ContainerFileReq`)
- `POST /containers/files/upload` — Upload container file
- `POST /containers/info` — Load container info (body: `dto.OperationWithName`)
- `POST /containers/inspect` — Container inspect (body: `dto.InspectReq`)
- `POST /containers/item/stats` — Load container stats size (body: `dto.OperationWithName`)
- `GET /containers/limit` — Load container limits
- `POST /containers/list` — List containers
- `POST /containers/list/byimage` — List containers by image
- `GET /containers/list/stats` — Load container stats
- `POST /containers/operate` — Operate Container (body: `dto.ContainerOperation`)
- `POST /containers/prune` — Clean container (body: `dto.ContainerPrune`)
- `POST /containers/rename` — Rename Container (body: `dto.ContainerRename`)
- `POST /containers/search` — Page containers (body: `dto.PageContainer`)
- `GET /containers/search/log` — Container logs
- `GET /containers/stats/:id` — Container stats
- `GET /containers/status` — Load containers status
- `POST /containers/update` — Update container (body: `dto.ContainerOperate`)
- `POST /containers/upgrade` — Upgrade container (body: `dto.ContainerUpgrade`)
- `POST /containers/users` — Load container users (body: `dto.OperationWithName`)

## Container Compose (7)

- `POST /containers/compose` — Create compose (body: `dto.ComposeCreate`)
- `POST /containers/compose/env` — Load compose environment variables (body: `dto.FilePath`)
- `POST /containers/compose/operate` — Operate compose (body: `dto.ComposeOperation`)
- `POST /containers/compose/pin` — Pin compose (body: `dto.ComposePin`)
- `POST /containers/compose/search` — Page composes (body: `dto.SearchWithPage`)
- `POST /containers/compose/test` — Test compose (body: `dto.ComposeCreate`)
- `POST /containers/compose/update` — Update compose (body: `dto.ComposeUpdate`)

## Container Compose-template (6)

- `GET /containers/template` — List compose templates
- `POST /containers/template` — Create compose template (body: `dto.ComposeTemplateCreate`)
- `POST /containers/template/batch` — Bacth compose template (body: `dto.ComposeTemplateBatch`)
- `POST /containers/template/del` — Delete compose template (body: `dto.BatchDelete`)
- `POST /containers/template/search` — Page compose templates (body: `dto.SearchWithPage`)
- `POST /containers/template/update` — Update compose template (body: `dto.ComposeTemplateUpdate`)

## Container Docker (8)

- `GET /containers/daemonjson` — Load docker daemon.json
- `GET /containers/daemonjson/file` — Load docker daemon.json
- `POST /containers/daemonjson/update` — Update docker daemon.json (body: `dto.SettingUpdate`)
- `POST /containers/daemonjson/update/byfile` — Update docker daemon.json by upload file (body: `dto.DaemonJsonUpdateByFile`)
- `POST /containers/docker/operate` — Operate docker (body: `dto.DockerOperation`)
- `GET /containers/docker/status` — Load docker status
- `POST /containers/ipv6option/update` — Update docker daemon.json ipv6 option (body: `dto.LogOption`)
- `POST /containers/logoption/update` — Update docker daemon.json log option (body: `dto.LogOption`)

## Container Image (10)

- `GET /containers/image` — load images options
- `GET /containers/image/all` — List all images
- `POST /containers/image/build` — Build image (body: `dto.ImageBuild`)
- `POST /containers/image/load` — Load image (body: `dto.ImageLoad`)
- `POST /containers/image/pull` — Pull image (body: `dto.ImagePull`)
- `POST /containers/image/push` — Push image (body: `dto.ImagePush`)
- `POST /containers/image/remove` — Delete image (body: `dto.BatchDelete`)
- `POST /containers/image/save` — Save image (body: `dto.ImageSave`)
- `POST /containers/image/search` — Page images (body: `dto.PageImage`)
- `POST /containers/image/tag` — Tag image (body: `dto.ImageTag`)

## Container Image-repo (6)

- `GET /containers/repo` — List image repos
- `POST /containers/repo` — Create image repo (body: `dto.ImageRepoDelete`)
- `POST /containers/repo/del` — Delete image repo (body: `dto.OperateByID`)
- `POST /containers/repo/search` — Page image repos (body: `dto.SearchWithPage`)
- `POST /containers/repo/status` — Load repo status (body: `dto.OperateByID`)
- `POST /containers/repo/update` — Update image repo (body: `dto.ImageRepoUpdate`)

## Container Network (4)

- `GET /containers/network` — List networks
- `POST /containers/network` — Create network (body: `dto.NetworkCreate`)
- `POST /containers/network/del` — Delete network (body: `dto.BatchDelete`)
- `POST /containers/network/search` — Page networks (body: `dto.SearchWithPage`)

## Container Volume (4)

- `GET /containers/volume` — List volumes
- `POST /containers/volume` — Create volume (body: `dto.VolumeCreate`)
- `POST /containers/volume/del` — Delete volume (body: `dto.BatchDelete`)
- `POST /containers/volume/search` — Page volumes (body: `dto.SearchWithPage`)

## Cronjob (16)

- `POST /cronjobs` — Create cronjob (body: `dto.CronjobOperate`)
- `POST /cronjobs/del` — Delete cronjob (body: `dto.CronjobBatchDelete`)
- `POST /cronjobs/export` — Export cronjob list (body: `dto.OperateByIDs`)
- `POST /cronjobs/group/update` — Update cronjob group (body: `dto.ChangeGroup`)
- `POST /cronjobs/handle` — Handle cronjob once (body: `dto.OperateByID`)
- `POST /cronjobs/import` — Import cronjob list (body: `dto.CronjobImport`)
- `POST /cronjobs/load/info` — Load cronjob info (body: `dto.OperateByID`)
- `POST /cronjobs/next` — Load cronjob spec time (body: `dto.CronjobSpec`)
- `POST /cronjobs/records/clean` — Clean job records (body: `dto.CronjobClean`)
- `POST /cronjobs/records/log` — Load Cronjob record log (body: `dto.OperateByID`)
- `GET /cronjobs/script/options` — Load script options
- `POST /cronjobs/search` — Page cronjobs (body: `dto.PageCronjob`)
- `POST /cronjobs/search/records` — Page job records (body: `dto.SearchRecord`)
- `POST /cronjobs/status` — Update cronjob status (body: `dto.CronjobUpdateStatus`)
- `POST /cronjobs/stop` — Handle stop job (body: `dto.OperateByID`)
- `POST /cronjobs/update` — Update cronjob (body: `dto.CronjobOperate`)

## Dashboard (12)

- `GET /dashboard/app/launcher` — Load app launcher
- `POST /dashboard/app/launcher/option` — Load app launcher options (body: `dto.SearchByFilter`)
- `POST /dashboard/app/launcher/show` — Update app Launcher (body: `dto.SettingUpdate`)
- `GET /dashboard/base/:ioOption/:netOption` — Load dashboard base info
- `GET /dashboard/base/os` — Load os info
- `GET /dashboard/current/:ioOption/:netOption` — Load dashboard current info
- `GET /dashboard/current/node` — Load dashboard current info for node
- `GET /dashboard/current/top/cpu` — Load top cpu processes
- `GET /dashboard/current/top/mem` — Load top memory processes
- `POST /dashboard/quick/change` — Update quick jump (body: `dto.ChangeQuicks`)
- `GET /dashboard/quick/option` — Load quick jump options
- `POST /dashboard/system/restart/:operation` — System restart

## Database (9)

- `POST /databases/db` — Create database (body: `dto.DatabaseCreate`)
- `GET /databases/db/:name` — Get databases
- `POST /databases/db/check` — Check database (body: `dto.DatabaseCreate`)
- `POST /databases/db/del` — Delete database (body: `dto.DatabaseDelete`)
- `POST /databases/db/del/check` — Check before delete remote database (body: `dto.OperateByID`)
- `GET /databases/db/item/:type` — List databases
- `GET /databases/db/list/:type` — List databases
- `POST /databases/db/search` — Page databases (body: `dto.DatabaseSearch`)
- `POST /databases/db/update` — Update database (body: `dto.DatabaseUpdate`)

## Database Common (3)

- `POST /databases/common/info` — Load base info (body: `dto.OperationWithNameAndType`)
- `POST /databases/common/load/file` — Load Database conf (body: `dto.OperationWithNameAndType`)
- `POST /databases/common/update/conf` — Update conf by upload file (body: `dto.DBConfUpdateByFile`)

## Database Mongodb (11)

- `POST /databases/mongodb` — Create mongodb database (body: `dto.MongodbDBCreate`)
- `POST /databases/mongodb/bind` — Bind mongodb database user info (body: `dto.MongodbBind`)
- `POST /databases/mongodb/del` — Delete mongodb database (body: `dto.MongodbDBDelete`)
- `POST /databases/mongodb/del/check` — Check before delete mongodb database (body: `dto.MongodbDBDeleteCheck`)
- `POST /databases/mongodb/description` — Update mongodb database description (body: `dto.UpdateDescription`)
- `POST /databases/mongodb/load` — Load mongodb database from remote (body: `dto.MongodbLoadDB`)
- `POST /databases/mongodb/password` — Change mongodb database password (body: `dto.MongodbPassword`)
- `POST /databases/mongodb/privileges` — Load mongodb privileges (body: `dto.MongodbPrivilegesLoad`)
- `POST /databases/mongodb/privileges/change` — Change mongodb privileges (body: `dto.MongodbPrivileges`)
- `POST /databases/mongodb/root/password` — Change mongodb root password (body: `dto.ChangeDBInfo`)
- `POST /databases/mongodb/search` — Page mongodb databases (body: `dto.MongodbDBSearch`)

## Database Mysql (23)

- `POST /databases` — Create mysql database (body: `dto.MysqlDBCreate`)
- `POST /databases/change/access` — Change mysql root access (body: `dto.ChangeDBInfo`)
- `POST /databases/change/password` — Change mysql root password (body: `dto.ChangeDBInfo`)
- `POST /databases/del` — Delete mysql database (body: `dto.MysqlDBDelete`)
- `POST /databases/del/check` — Check before delete mysql database (body: `dto.MysqlDBDeleteCheck`)
- `POST /databases/description/update` — Update mysql database description (body: `dto.UpdateDescription`)
- `POST /databases/format/options` — List mysql database format collation options (body: `dto.OperationWithName`)
- `POST /databases/grants` — Grant mysql user (body: `dto.MysqlGrantCreate`)
- `POST /databases/grants/del` — Revoke mysql grant (body: `dto.MysqlGrantDelete`)
- `POST /databases/grants/search` — List mysql grants (body: `dto.MysqlUserSearch`)
- `POST /databases/grants/summary` — List mysql grant summary (body: `dto.MysqlGrantSummarySearch`)
- `POST /databases/load` — Load mysql database from remote (body: `dto.MysqlLoadDB`)
- `POST /databases/remote` — Load mysql remote access (body: `dto.OperationWithNameAndType`)
- `POST /databases/search` — Page mysql databases (body: `dto.MysqlDBSearch`)
- `POST /databases/status` — Load mysql status info (body: `dto.OperationWithNameAndType`)
- `POST /databases/users` — Create mysql user (body: `dto.MysqlUserCreate`)
- `POST /databases/users/del` — Delete mysql user (body: `dto.MysqlUserDelete`)
- `POST /databases/users/password` — Change mysql user password (body: `dto.MysqlUserPassword`)
- `POST /databases/users/password/save` — Save mysql user password locally (body: `dto.MysqlUserPassword`)
- `POST /databases/users/search` — List mysql users (body: `dto.MysqlUserSearch`)
- `POST /databases/users/update` — Update mysql user (body: `dto.MysqlUserUpdate`)
- `POST /databases/variables` — Load mysql variables info (body: `dto.OperationWithNameAndType`)
- `POST /databases/variables/update` — Update mysql variables (body: `dto.MysqlVariablesUpdate`)

## Database PostgreSQL (9)

- `POST /databases/pg` — Create postgresql database (body: `dto.PostgresqlDBCreate`)
- `POST /databases/pg/:database/load` — Load postgresql database from remote (body: `dto.PostgresqlLoadDB`)
- `POST /databases/pg/bind` — Bind postgresql user (body: `dto.PostgresqlBindUser`)
- `POST /databases/pg/del` — Delete postgresql database (body: `dto.PostgresqlDBDelete`)
- `POST /databases/pg/del/check` — Check before delete postgresql database (body: `dto.PostgresqlDBDeleteCheck`)
- `POST /databases/pg/description` — Update postgresql database description (body: `dto.UpdateDescription`)
- `POST /databases/pg/password` — Change postgresql password (body: `dto.ChangeDBInfo`)
- `POST /databases/pg/privileges` — Change postgresql privileges (body: `dto.ChangeDBInfo`)
- `POST /databases/pg/search` — Page postgresql databases (body: `dto.PostgresqlDBSearch`)

## Database Redis (8)

- `GET /databases/redis/check` — Check has cli
- `POST /databases/redis/conf` — Load redis conf (body: `dto.LoadRedisStatus`)
- `POST /databases/redis/conf/update` — Update redis conf (body: `dto.RedisConfUpdate`)
- `POST /databases/redis/install/cli` — Install redis-cli
- `POST /databases/redis/password` — Change redis password (body: `dto.ChangeRedisPass`)
- `POST /databases/redis/persistence/conf` — Load redis persistence conf (body: `dto.LoadRedisStatus`)
- `POST /databases/redis/persistence/update` — Update redis persistence conf (body: `dto.RedisConfPersistenceUpdate`)
- `POST /databases/redis/status` — Load redis status info (body: `dto.LoadRedisStatus`)

## Device (12)

- `POST /toolbox/clean` — Clean system
- `POST /toolbox/device/base` — Load device base info
- `POST /toolbox/device/check/dns` — Check device DNS conf (body: `dto.SettingUpdate`)
- `POST /toolbox/device/conf` — load conf (body: `dto.OperationWithName`)
- `POST /toolbox/device/update/byconf` — Update device conf by file (body: `dto.UpdateByNameAndFile`)
- `POST /toolbox/device/update/conf` — Update device (body: `dto.SettingUpdate`)
- `POST /toolbox/device/update/host` — Update device hosts
- `POST /toolbox/device/update/passwd` — Update device passwd (body: `dto.ChangePasswd`)
- `POST /toolbox/device/update/swap` — Update device swap (body: `dto.SwapHelper`)
- `GET /toolbox/device/users` — Load user list
- `GET /toolbox/device/zone/options` — list time zone options
- `POST /toolbox/scan` — Scan system

## Disk Management (4)

- `GET /hosts/disks` — Get complete disk information
- `POST /hosts/disks/mount` — Mount disk (body: `request.DiskMountRequest`)
- `POST /hosts/disks/partition` — Partition disk (body: `request.DiskPartitionRequest`)
- `POST /hosts/disks/unmount` — Unmount disk (body: `request.DiskUnmountRequest`)

## FTP (8)

- `POST /toolbox/ftp` — Create FTP user (body: `dto.FtpCreate`)
- `GET /toolbox/ftp/base` — Load FTP base info
- `POST /toolbox/ftp/del` — Delete FTP user (body: `dto.BatchDeleteReq`)
- `POST /toolbox/ftp/log/search` — Load FTP operation log (body: `dto.FtpLogSearch`)
- `POST /toolbox/ftp/operate` — Operate FTP (body: `dto.Operate`)
- `POST /toolbox/ftp/search` — Page FTP user (body: `dto.SearchWithPage`)
- `POST /toolbox/ftp/sync` — Sync FTP user (body: `dto.BatchDeleteReq`)
- `POST /toolbox/ftp/update` — Update FTP user (body: `dto.FtpUpdate`)

## Fail2ban (7)

- `GET /toolbox/fail2ban/base` — Load fail2ban base info
- `GET /toolbox/fail2ban/load/conf` — Load fail2ban conf
- `POST /toolbox/fail2ban/operate` — Operate fail2ban (body: `dto.Operate`)
- `POST /toolbox/fail2ban/operate/sshd` — Operate sshd of fail2ban (body: `dto.Fail2BanSet`)
- `POST /toolbox/fail2ban/search` — Page fail2ban ip list (body: `dto.Fail2BanSearch`)
- `POST /toolbox/fail2ban/update` — Update fail2ban conf (body: `dto.Fail2BanUpdate`)
- `POST /toolbox/fail2ban/update/byconf` — Update fail2ban conf by file (body: `dto.UpdateByFile`)

## File (58)

- `POST /files` — Create file (body: `request.FileCreate`)
- `POST /files/ai-search` — File search: content grep + optional AI summary (body: `request.FileAISearch`)
- `POST /files/batch/check` — Batch check file exist (body: `request.FilePathsCheck`)
- `POST /files/batch/del` — Batch delete file (body: `request.FileBatchDelete`)
- `POST /files/batch/role` — Batch change file mode and owner (body: `request.FileRoleReq`)
- `POST /files/check` — Check file exist (body: `request.FilePathCheck`)
- `POST /files/chunkdownload` — Chunk Download file (body: `request.FileDownload`)
- `POST /files/chunkupload` — ChunkUpload file
- `POST /files/compress` — Compress file (body: `request.FileCompress`)
- `POST /files/compress/stop` — Stop compress task (body: `request.FileCompressStopReq`)
- `POST /files/content` — Load file content (body: `request.FileContentReq`)
- `POST /files/convert` — Convert file (body: `request.FileConvert`)
- `POST /files/convert/log` — Convert file (body: `dto.PageInfo`)
- `POST /files/decompress` — Decompress file (body: `request.FileDeCompress`)
- `POST /files/decompress/stop` — Stop decompress task (body: `request.FileDeCompressStopReq`)
- `POST /files/del` — Delete file (body: `request.FileDelete`)
- `POST /files/depth/size` — Multi file size (body: `request.DirSizeReq`)
- `GET /files/download` — Download file
- `POST /files/favorite` — Create favorite (body: `request.FavoriteCreate`)
- `POST /files/favorite/del` — Delete favorite (body: `request.FavoriteDelete`)
- `POST /files/favorite/search` — List favorites (body: `dto.PageInfo`)
- `POST /files/history/content` — Load file history content (body: `request.FileHistoryContentReq`)
- `POST /files/history/del` — Delete file history record (body: `request.FileHistoryDeleteReq`)
- `POST /files/history/restore` — Restore file history record (body: `request.FileHistoryRestoreReq`)
- `POST /files/history/search` — Load file history list (body: `request.FileHistorySearchReq`)
- `POST /files/mode` — Change file mode (body: `request.FileCreate`)
- `POST /files/mount` — system mount
- `POST /files/move` — Move file (body: `request.FileMove`)
- `POST /files/move/stop` — Stop file move task (body: `request.FileMoveStopReq`)
- `POST /files/owner` — Change file owner (body: `request.FileRoleUpdate`)
- `POST /files/preview` — Preview file content (body: `request.FileContentReq`)
- `POST /files/read/{type}` — Read file by Line (body: `request.FileReadByLineReq`)
- `POST /files/recycle/clear` — Clear RecycleBin files
- `POST /files/recycle/reduce` — Reduce RecycleBin files (body: `request.RecycleBinReduce`)
- `POST /files/recycle/search` — List RecycleBin files (body: `dto.PageInfo`)
- `GET /files/recycle/status` — Get RecycleBin status
- `POST /files/remark` — Set file remark (body: `request.FileRemarkUpdate`)
- `POST /files/remarks` — Batch get file remarks (body: `request.FileRemarkBatch`)
- `POST /files/rename` — Change file name (body: `request.FileRename`)
- `POST /files/save` — Update file content (body: `request.FileEdit`)
- `POST /files/search` — List files (body: `request.FileOption`)
- `GET /files/share/check` — Check file share code (no login)
- `POST /files/share/create` — Create temporary file share link (body: `request.FileShareCreate`)
- `POST /files/share/del` — Delete file share by path (body: `dto.FilePath`)
- `POST /files/share/detail` — Get file share detail by path (body: `dto.FilePath`)
- `GET /files/share/download` — Download file by share code (no login)
- `GET /files/share/info` — Get file share detail by code (no login)
- `GET /files/share/qrcode` — Get file share QR code image
- `POST /files/share/search` — List file shares (body: `dto.PageInfo`)
- `POST /files/size` — Load file size (body: `request.DirSizeReq`)
- `POST /files/tree` — Load files tree (body: `request.FileOption`)
- `POST /files/upload` — Upload file
- `POST /files/upload/search` — Page file (body: `request.SearchUploadWithPage`)
- `POST /files/user/group` — system user and group
- `POST /files/wget` — Wget file (body: `request.FileWget`)
- `GET /files/wget/process` — Wget process
- `GET /files/wget/process/keys` — Process keys
- `POST /files/wget/stop` — Stop wget file download (body: `request.FileProcessReq`)

## Firewall (24)

- `POST /hosts/firewall/base` — Load firewall base info (body: `dto.OperationWithName`)
- `POST /hosts/firewall/docker/operate` — Operate Docker port guard (body: `dto.DockerPortGuardOperation`)
- `POST /hosts/firewall/docker/policies/batch` — Batch upsert Docker port guard policies (body: `dto.DockerPortGuardPolicyBatch`)
- `POST /hosts/firewall/docker/policies/delete/batch` — Delete Docker port guard policies (body: `dto.DockerPortGuardPolicyBatchDelete`)
- `GET /hosts/firewall/docker/ports` — List Docker port guard status and policies
- `POST /hosts/firewall/docker/sync` — Sync Docker port guard rules
- `POST /hosts/firewall/filter/operate` — Apply/Unload/Init firewall filter chain (body: `dto.FilterChainOperation`)
- `POST /hosts/firewall/forward/base` — Load forwarding base info
- `POST /hosts/firewall/forward/enable` — Enable forwarding (body: `dto.FirewallInitializationTask`)
- `POST /hosts/firewall/forward/operate` — Operate forwarding rules (body: `dto.ForwardRuleOperate`)
- `POST /hosts/firewall/forward/search` — Page forwarding rules (body: `dto.ForwardRuleSearch`)
- `POST /hosts/firewall/operate` — Operate firewall (body: `dto.FirewallLifecycleOperation`)
- `POST /hosts/firewall/rules` — Queue firewall rule creation (body: `dto.FirewallRuleCreate`)
- `POST /hosts/firewall/rules/adopt` — Adopt an external firewall rule (body: `dto.FirewallRuleAdopt`)
- `POST /hosts/firewall/rules/delete` — Queue firewall rule deletion (body: `dto.FirewallRuleDelete`)
- `POST /hosts/firewall/rules/native/detail` — Load one provider-native firewall object definition (body: `dto.FirewallNativeDetail`)
- `POST /hosts/firewall/rules/reorder` — Reorder a managed unified firewall v2 rule (body: `dto.FirewallRuleReorder`)
- `POST /hosts/firewall/rules/search` — List unified firewall v2 rules (body: `dto.FirewallRuleInventory`)
- `POST /hosts/firewall/rules/update` — Update a managed unified firewall v2 rule (body: `dto.FirewallRuleUpdate`)
- `GET /hosts/firewall/settings` — Load firewall settings
- `POST /hosts/firewall/settings/operate` — Operate firewall backend (body: `dto.FirewallBackendOperation`)
- `POST /hosts/firewall/settings/whitelist` — Create firewall port whitelist rules (body: `dto.FirewallPortWhitelistCreate`)
- `POST /hosts/firewall/settings/whitelist/delete` — Delete firewall port whitelist rules (body: `dto.FirewallPortWhitelistDelete`)
- `POST /hosts/firewall/settings/whitelist/update` — Update firewall port whitelist rules (body: `dto.FirewallPortWhitelistUpdate`)

## Health (1)

- `GET /health/check` — Check health

## Host (10)

- `POST /hosts` — Create host (body: `dto.HostOperate`)
- `GET /hosts/components/{name}` — Check if a system component exists
- `POST /hosts/del` — Delete host (body: `dto.OperateByIDs`)
- `POST /hosts/info` — Get host by ID (body: `dto.OperateByID`)
- `POST /hosts/search` — Search host (body: `dto.SearchPageWithGroup`)
- `POST /hosts/test/byid` — Test by ID (body: `dto.OperateByID`)
- `POST /hosts/test/byinfo` — Test by info (body: `dto.HostConnTest`)
- `POST /hosts/tree` — Host tree (body: `dto.SearchForTree`)
- `POST /hosts/update` — Update host (body: `dto.HostOperate`)
- `POST /hosts/update/group` — Update host group (body: `dto.ChangeGroup`)

## Host tool (9)

- `POST /hosts/tool/config/get` — Get tool config (body: `request.HostToolTypeReq`)
- `POST /hosts/tool/config/set` — Update tool config (body: `request.HostToolConfigUpdate`)
- `POST /hosts/tool/init` — Create Host tool Config (body: `request.HostToolCreate`)
- `POST /hosts/tool/operate` — Operate tool (body: `request.HostToolOperateReq`)
- `POST /hosts/tool/status` — Get tool status (body: `request.HostToolTypeReq`)
- `GET /hosts/tool/supervisor/process` — Get Supervisor process config
- `POST /hosts/tool/supervisor/process` — Create Supervisor process (body: `request.SupervisorProcessConfig`)
- `POST /hosts/tool/supervisor/process/file` — Operate Supervisor process config file (body: `request.HostSupervisorProcessFileOperateReq`)
- `POST /hosts/tool/supervisor/process/file/get` — Get Supervisor process config file (body: `request.HostSupervisorProcessFileGetReq`)

## Logs (7)

- `POST /core/logs/clean` — Clean operation logs (body: `dto.CleanLog`)
- `POST /core/logs/login` — Page login logs (body: `dto.SearchLgLogWithPage`)
- `POST /core/logs/operation` — Page operation logs (body: `dto.SearchOpLogWithPage`)
- `GET /logs/system/files` — Load system log files
- `POST /logs/system/read` — Read host logs (body: `dto.SystemLogReq`)
- `GET /logs/system/services` — List running host services
- `GET /logs/system/status` — Get host system log status

## McpServer (11)

- `POST /ai/mcp/domain/bind` — Bind Domain for mcp server (body: `request.McpBindDomain`)
- `GET /ai/mcp/domain/get` — Get bin Domain for mcp server
- `POST /ai/mcp/domain/update` — Update bind Domain for mcp server (body: `request.McpBindDomainUpdate`)
- `POST /ai/mcp/search` — List mcp servers (body: `request.McpServerSearch`)
- `POST /ai/mcp/server` — Create mcp server (body: `request.McpServerCreate`)
- `POST /ai/mcp/server/connection/test` — Test mcp server connection (body: `request.McpServerConnectionTest`)
- `POST /ai/mcp/server/del` — Delete mcp server (body: `request.McpServerDelete`)
- `POST /ai/mcp/server/detail` — Load mcp server detail (body: `request.McpServerDetail`)
- `POST /ai/mcp/server/op` — Operate mcp server (body: `request.McpServerOperate`)
- `POST /ai/mcp/server/status/sync` — Sync mcp server status (body: `request.McpServerStatusSync`)
- `POST /ai/mcp/server/update` — Update mcp server (body: `request.McpServerUpdate`)

## Menu Setting (1)

- `POST /core/settings/menu/default` — Default menu

## Monitor (7)

- `POST /ai/gpu/search` — Load monitor data (body: `dto.MonitorGPUSearch`)
- `POST /hosts/monitor/clean` — Clean monitor data
- `GET /hosts/monitor/iooptions` — Get IO options
- `GET /hosts/monitor/netoptions` — Get network options
- `POST /hosts/monitor/search` — Load monitor data (body: `dto.MonitorSearch`)
- `GET /hosts/monitor/setting` — Load monitor setting
- `POST /hosts/monitor/setting/update` — Update monitor setting (body: `dto.MonitorSettingUpdate`)

## OpenResty (10)

- `GET /openresty` — Load OpenResty conf
- `POST /openresty/build` — Build OpenResty (body: `request.NginxBuildReq`)
- `POST /openresty/file` — Update OpenResty conf by upload file (body: `request.NginxConfigFileUpdate`)
- `GET /openresty/https` — Get default HTTPs status
- `POST /openresty/https` — Operate default HTTPs (body: `request.NginxDefaultHTTPSUpdate`)
- `GET /openresty/modules` — Get OpenResty modules
- `POST /openresty/modules/update` — Update OpenResty module (body: `request.NginxModuleUpdate`)
- `POST /openresty/scope` — Load partial OpenResty conf (body: `request.NginxScopeReq`)
- `GET /openresty/status` — Load OpenResty status info
- `POST /openresty/update` — Update OpenResty conf (body: `request.NginxConfigUpdate`)

## PHP Extensions (4)

- `POST /runtimes/php/extensions` — Create Extensions (body: `request.PHPExtensionsCreate`)
- `POST /runtimes/php/extensions/del` — Delete Extensions (body: `request.PHPExtensionsDelete`)
- `POST /runtimes/php/extensions/search` — Page Extensions (body: `request.PHPExtensionsSearch`)
- `POST /runtimes/php/extensions/update` — Update Extensions (body: `request.PHPExtensionsUpdate`)

## Process (4)

- `POST /process/listening` — Get Listening Process
- `POST /process/stop` — Stop Process (body: `request.ProcessReq`)
- `GET /process/ws` — Process ws
- `GET /process/{pid}` — Get Process Info By PID

## Runtime (25)

- `POST /runtimes` — Create runtime (body: `request.RuntimeCreate`)
- `GET /runtimes/:id` — Get runtime
- `POST /runtimes/node/modules` — Get Node modules (body: `request.NodeModuleReq`)
- `POST /runtimes/node/modules/operate` — Operate Node modules (body: `request.NodeModuleReq`)
- `POST /runtimes/node/package` — Get Node package scripts (body: `request.NodePackageReq`)
- `POST /runtimes/operate` — Operate runtime (body: `request.RuntimeOperate`)
- `GET /runtimes/php/:id/extensions` — Get php runtime extension
- `POST /runtimes/php/config` — Update runtime php conf (body: `request.PHPConfigUpdate`)
- `GET /runtimes/php/config/:id` — Load php runtime conf
- `GET /runtimes/php/container/:id` — Get PHP container config
- `POST /runtimes/php/container/update` — Update PHP container config (body: `request.PHPContainerConfig`)
- `POST /runtimes/php/extensions/install` — Install php extension (body: `request.PHPExtensionInstallReq`)
- `POST /runtimes/php/extensions/uninstall` — UnInstall php extension (body: `request.PHPExtensionInstallReq`)
- `POST /runtimes/php/file` — Get php conf file (body: `request.PHPFileReq`)
- `POST /runtimes/php/fpm/config` — Update fpm config (body: `request.FPMConfig`)
- `GET /runtimes/php/fpm/config/:id` — Get fpm config
- `GET /runtimes/php/fpm/status/:id` — Get PHP runtime status
- `POST /runtimes/php/update` — Update php conf file (body: `request.PHPFileUpdate`)
- `POST /runtimes/remark` — Update runtime remark (body: `request.RuntimeRemark`)
- `POST /runtimes/search` — List runtimes (body: `request.RuntimeSearch`)
- `POST /runtimes/supervisor/process` — Operate supervisor process (body: `request.PHPSupervisorProcessConfig`)
- `GET /runtimes/supervisor/process/:id` — Get supervisor process
- `POST /runtimes/supervisor/process/file` — Operate supervisor process file (body: `request.PHPSupervisorProcessFileReq`)
- `POST /runtimes/sync` — Sync runtime status
- `POST /runtimes/update` — Update runtime (body: `request.RuntimeUpdate`)

## RuntimeDiagnostics (6)

- `GET /core/hosts/diagnostics/goroutines` — Load Core grouped goroutine snapshot
- `POST /core/hosts/diagnostics/profiles` — Capture Core runtime profile (body: `dto.RuntimeProfileCreate`)
- `GET /core/hosts/diagnostics/summary` — Load Core runtime diagnostics summary
- `GET /hosts/diagnostics/goroutines` — Load grouped goroutine snapshot
- `POST /hosts/diagnostics/profiles` — Capture runtime profile (body: `dto.RuntimeProfileCreate`)
- `GET /hosts/diagnostics/summary` — Load runtime diagnostics summary

## SSH (13)

- `POST /hosts/ssh/cert` — Generate host SSH secret (body: `dto.RootCertOperate`)
- `POST /hosts/ssh/cert/delete` — Delete host SSH secret (body: `dto.ForceDelete`)
- `POST /hosts/ssh/cert/search` — Load host SSH secret (body: `dto.SearchWithPage`)
- `POST /hosts/ssh/cert/sync` — Sycn host SSH secret
- `POST /hosts/ssh/cert/update` — Update host SSH secret (body: `dto.RootCertOperate`)
- `POST /hosts/ssh/file` — Load host SSH conf (body: `dto.OperationWithName`)
- `POST /hosts/ssh/file/update` — Update host SSH setting by file (body: `dto.SSHConfUpdate`)
- `POST /hosts/ssh/log` — Load host SSH logs (body: `dto.SearchSSHLog`)
- `POST /hosts/ssh/log/clean` — Clean host SSH logs
- `POST /hosts/ssh/log/export` — Export host SSH logs (body: `dto.SearchSSHLog`)
- `POST /hosts/ssh/operate` — Operate SSH (body: `dto.Operate`)
- `POST /hosts/ssh/search` — Load host SSH setting info
- `POST /hosts/ssh/update` — Update host SSH setting (body: `dto.SSHUpdate`)

## ScriptLibrary (6)

- `POST /core/script` — Add script (body: `dto.ScriptOperate`)
- `POST /core/script/del` — Delete script (body: `dto.OperateByIDs`)
- `GET /core/script/run` — Run script
- `POST /core/script/search` — Page script (body: `dto.SearchPageWithGroup`)
- `POST /core/script/sync` — Sync script from remote (body: `dto.OperateByTaskID`)
- `POST /core/script/update` — Update script (body: `dto.ScriptOperate`)

## System Group (8)

- `POST /core/groups` — Create group (body: `dto.GroupCreate`)
- `POST /core/groups/del` — Delete group (body: `dto.OperateByID`)
- `POST /core/groups/search` — List groups (body: `dto.GroupSearch`)
- `POST /core/groups/update` — Update group (body: `dto.GroupUpdate`)
- `POST /groups` — Create group (body: `dto.GroupCreate`)
- `POST /groups/del` — Delete group (body: `dto.OperateByID`)
- `POST /groups/search` — List groups (body: `dto.GroupSearch`)
- `POST /groups/update` — Update group (body: `dto.GroupUpdate`)

## System Setting (50)

- `POST /core/auth/mfa` — Load mfa info (body: `dto.MfaCredential`)
- `POST /core/auth/mfa/bind` — Bind mfa (body: `dto.MfaCredential`)
- `POST /core/auth/mfa/close` — Close mfa
- `POST /core/settings/bind/update` — Update system bind info (body: `dto.BindInfo`)
- `GET /core/settings/interface` — Load system address
- `GET /core/settings/memo` — Load dashboard memo
- `POST /core/settings/memo` — Update dashboard memo (body: `dto.MemoUpdate`)
- `POST /core/settings/menu/update` — Update system setting (body: `dto.SettingUpdate`)
- `POST /core/settings/port/update` — Update system port (body: `dto.PortUpdate`)
- `POST /core/settings/proxy/update` — Update proxy setting (body: `dto.ProxyUpdate`)
- `POST /core/settings/search` — Load system setting info
- `GET /core/settings/search/available` — Load system available status
- `POST /core/settings/search/base` — Load base system setting info
- `POST /core/settings/ssl/download` — Download system cert
- `GET /core/settings/ssl/info` — Load system cert info
- `POST /core/settings/ssl/reload` — Reload SSL
- `POST /core/settings/ssl/update` — Update system ssl (body: `dto.SSLUpdate`)
- `POST /core/settings/terminal/search` — Load system terminal setting info
- `POST /core/settings/terminal/update` — Update system terminal setting (body: `dto.TerminalUpdate`)
- `POST /core/settings/update` — Update system setting (body: `dto.SettingUpdate`)
- `GET /core/settings/upgrade` — Load upgrade info
- `POST /core/settings/upgrade` — Upgrade (body: `dto.Upgrade`)
- `POST /core/settings/upgrade/notes` — Load release notes by version (body: `dto.Upgrade`)
- `GET /core/settings/upgrade/releases` — Load upgrade notes
- `GET /settings/basedir` — Load local backup dir
- `POST /settings/description/save` — Save common description (body: `dto.CommonDescription`)
- `POST /settings/file-history/search` — Load file history setting info
- `POST /settings/file-history/update` — Update file history setting (body: `request.FileHistorySettingUpdate`)
- `POST /settings/files/ai/search` — Get file manage AI setting info
- `POST /settings/files/ai/update` — Update file manage AI setting (body: `dto.FileManageAIInfo`)
- `POST /settings/search` — Load system setting info
- `GET /settings/search/available` — Load system available status
- `POST /settings/snapshot` — Create system snapshot (body: `dto.SnapshotCreate`)
- `POST /settings/snapshot/del` — Delete system backup (body: `dto.SnapshotBatchDelete`)
- `POST /settings/snapshot/description/update` — Update snapshot description (body: `dto.UpdateDescription`)
- `POST /settings/snapshot/import` — Import system snapshot (body: `dto.SnapshotImport`)
- `GET /settings/snapshot/load` — Load system snapshot data
- `POST /settings/snapshot/recover` — Recover system backup (body: `dto.SnapshotRecover`)
- `POST /settings/snapshot/recreate` — Recreate system snapshot (body: `dto.OperateByID`)
- `POST /settings/snapshot/rollback` — Rollback system backup (body: `dto.SnapshotRecover`)
- `POST /settings/snapshot/search` — Page system snapshot (body: `dto.PageSnapshot`)
- `POST /settings/ssh` — Save local conn info
- `POST /settings/ssh/check` — Check local conn
- `POST /settings/ssh/check/info` — Check local conn info
- `GET /settings/ssh/conn` — Load local conn
- `POST /settings/ssh/default` — Update local is conn (body: `dto.SSHDefaultConn`)
- `POST /settings/terminal/ai/search` — Get terminal AI setting info
- `POST /settings/terminal/ai/update` — Update terminal AI setting (body: `dto.TerminalAIInfo`)
- `POST /settings/update` — Update system setting (body: `dto.AgentSettingUpdate`)
- `GET /settings/website/dir` — Load website dir

## TaskLog (3)

- `GET /logs/tasks/executing/count` — Get the number of executing tasks
- `POST /logs/tasks/read` — Read task log by Line (body: `request.TaskLogReadReq`)
- `POST /logs/tasks/search` — Page task logs (body: `dto.SearchTaskLogReq`)

## TensorRT LLM (5)

- `POST /ai/tensorrt/create` — Create TensorRT LLM (body: `request.TensorRTLLMCreate`)
- `POST /ai/tensorrt/delete` — Delete TensorRT LLM (body: `request.TensorRTLLMDelete`)
- `POST /ai/tensorrt/operate` — Operate TensorRT LLM (body: `request.TensorRTLLMOperate`)
- `POST /ai/tensorrt/search` — Page TensorRT LLMs (body: `request.TensorRTLLMSearch`)
- `POST /ai/tensorrt/update` — Update TensorRT LLM (body: `request.TensorRTLLMUpdate`)

## Terminal (3)

- `GET /hosts/terminal/container` — Ws container terminal
- `GET /hosts/terminal/local` — Ws local terminal
- `GET /hosts/terminal/ssh` — Ws host SSH

## Website (59)

- `POST /runtimes/del` — Delete runtime (body: `request.RuntimeDelete`)
- `GET /runtimes/installed/delete/check/:id` — Delete runtime
- `POST /websites` — Create website (body: `request.WebsiteCreate`)
- `GET /websites/:id` — Search website by id
- `POST /websites/auths` — Get AuthBasic conf (body: `request.NginxAuthReq`)
- `POST /websites/auths/path` — Get AuthBasic conf (body: `request.NginxAuthReq`)
- `POST /websites/auths/path/update` — Get AuthBasic conf (body: `request.NginxPathAuthUpdate`)
- `POST /websites/auths/update` — Get AuthBasic conf (body: `request.NginxAuthUpdate`)
- `POST /websites/batch/group` — Batch set website group (body: `request.BatchWebsiteGroup`)
- `POST /websites/batch/operate` — Batch operate websites (body: `request.BatchWebsiteOp`)
- `POST /websites/batch/ssl` — Batch set HTTPS for websites (body: `request.BatchWebsiteHttps`)
- `POST /websites/check` — Check before create website (body: `request.WebsiteInstallCheckReq`)
- `POST /websites/cors/update` — Update CORS Config (body: `request.CorsConfigReq`)
- `GET /websites/cors/{id}` — Get CORS Config
- `POST /websites/crosssite` — Operate Cross Site Access (body: `request.CrossSiteAccessOp`)
- `GET /websites/databases` — Get databases
- `POST /websites/databases` — Change website database (body: `request.ChangeDatabase`)
- `GET /websites/default/html/:type` — Get default html
- `POST /websites/default/html/update` — Update default html (body: `request.WebsiteHtmlUpdate`)
- `POST /websites/default/server` — Change default server (body: `request.WebsiteDefaultUpdate`)
- `POST /websites/del` — Delete website (body: `request.WebsiteDelete`)
- `POST /websites/dir` — Get website dir (body: `request.WebsiteCommonReq`)
- `POST /websites/dir/permission` — Update Site Dir permission (body: `request.WebsiteUpdateDirPermission`)
- `POST /websites/dir/update` — Update Site Dir (body: `request.WebsiteUpdateDir`)
- `POST /websites/exec/composer` — Exec Composer (body: `request.ExecComposerReq`)
- `POST /websites/group/change` — Change website group (body: `dto.UpdateGroup`)
- `POST /websites/lbs/create` — Create website upstream (body: `request.WebsiteLBCreate`)
- `POST /websites/lbs/del` — Delete website upstream (body: `request.WebsiteLBDelete`)
- `POST /websites/lbs/file` — Update website upstream file (body: `request.WebsiteLBUpdateFile`)
- `POST /websites/lbs/update` — Update website upstream (body: `request.WebsiteLBUpdate`)
- `POST /websites/leech` — Get AntiLeech conf (body: `request.NginxCommonReq`)
- `POST /websites/leech/update` — Update AntiLeech (body: `request.NginxAntiLeechUpdate`)
- `GET /websites/list` — List websites
- `POST /websites/log/operate` — Operate website log (body: `request.WebsiteLogReq`)
- `POST /websites/log/search` — Get website log (body: `request.WebsiteLogSearchReq`)
- `POST /websites/operate` — Operate website (body: `request.WebsiteOp`)
- `POST /websites/options` — List website names
- `POST /websites/proxies` — Get proxy conf (body: `request.WebsiteProxyReq`)
- `POST /websites/proxies/delete` — Delete proxy config (body: `request.WebsiteProxyDel`)
- `POST /websites/proxies/file` — Update proxy file (body: `request.NginxProxyUpdate`)
- `POST /websites/proxies/status` — Update proxy config status (body: `request.WebsiteProxyStatusUpdate`)
- `POST /websites/proxies/update` — Update proxy conf (body: `request.WebsiteProxyConfig`)
- `POST /websites/proxy/clear` — Clear Website proxy cache
- `POST /websites/proxy/config` — update website proxy cache config (body: `request.NginxProxyCacheUpdate`)
- `GET /websites/proxy/config/{id}` — Get website proxy cache config
- `POST /websites/realip/config` — Set Real IP (body: `request.WebsiteRealIP`)
- `GET /websites/realip/config/{id}` — Get Real IP Config
- `POST /websites/redirect` — Get redirect conf (body: `request.WebsiteProxyReq`)
- `POST /websites/redirect/file` — Update redirect file (body: `request.NginxRedirectUpdate`)
- `POST /websites/redirect/update` — Update redirect conf (body: `request.NginxRedirectReq`)
- `GET /websites/resource/{id}` — Get website resource
- `POST /websites/rewrite` — Get rewrite conf (body: `request.NginxRewriteReq`)
- `GET /websites/rewrite/custom` — List custom rewrite
- `POST /websites/rewrite/custom` — Operate custom rewrite (body: `request.CustomRewriteOperate`)
- `POST /websites/rewrite/update` — Update rewrite conf (body: `request.NginxRewriteUpdate`)
- `POST /websites/search` — Page websites (body: `request.WebsiteSearch`)
- `POST /websites/stream/update` — Update Stream Config (body: `request.StreamUpdate`)
- `POST /websites/update` — Update website (body: `request.WebsiteUpdate`)
- `GET /websites/{id}/lbs` — Get website upstreams

## Website Acme (4)

- `POST /websites/acme` — Create website acme account (body: `request.WebsiteAcmeAccountCreate`)
- `POST /websites/acme/del` — Delete website acme account (body: `request.WebsiteResourceReq`)
- `POST /websites/acme/search` — Page website acme accounts (body: `dto.PageInfo`)
- `POST /websites/acme/update` — Update website acme account (body: `request.WebsiteAcmeAccountUpdate`)

## Website CA (7)

- `POST /websites/ca` — Create website ca (body: `request.WebsiteCACreate`)
- `POST /websites/ca/del` — Delete website ca (body: `request.WebsiteCommonReq`)
- `POST /websites/ca/download` — Download CA file (body: `request.WebsiteResourceReq`)
- `POST /websites/ca/obtain` — Obtain SSL (body: `request.WebsiteCAObtain`)
- `POST /websites/ca/renew` — Obtain SSL (body: `request.WebsiteCAObtain`)
- `POST /websites/ca/search` — Page website ca (body: `request.WebsiteCASearch`)
- `GET /websites/ca/{id}` — Get website ca

## Website DNS (4)

- `POST /websites/dns` — Create website dns account (body: `request.WebsiteDnsAccountCreate`)
- `POST /websites/dns/del` — Delete website dns account (body: `request.WebsiteResourceReq`)
- `POST /websites/dns/search` — Page website dns accounts (body: `dto.PageInfo`)
- `POST /websites/dns/update` — Update website dns account (body: `request.WebsiteDnsAccountUpdate`)

## Website Domain (4)

- `POST /websites/domains` — Create website domain (body: `request.WebsiteDomainCreate`)
- `GET /websites/domains/:websiteId` — Search website domains by websiteId
- `POST /websites/domains/del` — Delete website domain (body: `request.WebsiteDomainDelete`)
- `POST /websites/domains/update` — Update website domain (body: `request.WebsiteDomainUpdate`)

## Website HTTPS (2)

- `GET /websites/:id/https` — Load https conf
- `POST /websites/:id/https` — Update https conf (body: `request.WebsiteHTTPSOp`)

## Website Nginx (4)

- `GET /websites/:id/config/:type` — Search website nginx by id
- `POST /websites/config` — Load nginx conf (body: `request.NginxScopeReq`)
- `POST /websites/config/update` — Update nginx conf (body: `request.NginxConfigUpdate`)
- `POST /websites/nginx/update` — Update website nginx conf (body: `request.WebsiteNginxUpdate`)

## Website PHP (1)

- `POST /websites/php/version` — Update php version (body: `request.WebsitePHPVersionReq`)

## Website SSL (14)

- `POST /websites/ssl` — Create website ssl (body: `request.WebsiteSSLCreate`)
- `GET /websites/ssl/:id` — Search website ssl by id
- `POST /websites/ssl/del` — Delete website ssl (body: `request.WebsiteBatchDelReq`)
- `POST /websites/ssl/download` — Download SSL  file (body: `request.WebsiteResourceReq`)
- `POST /websites/ssl/import` — Import master SSL (body: `model.WebsiteSSL`)
- `POST /websites/ssl/list` — List website ssl (body: `request.WebsiteSSLListReq`)
- `POST /websites/ssl/obtain` — Apply  ssl (body: `request.WebsiteSSLApply`)
- `POST /websites/ssl/push` — Push ssl to nodes (body: `request.WebsiteSSLPush`)
- `POST /websites/ssl/resolve` — Resolve website ssl (body: `request.WebsiteDNSReq`)
- `POST /websites/ssl/search` — Page website ssl (body: `request.WebsiteSSLSearch`)
- `POST /websites/ssl/update` — Update ssl (body: `request.WebsiteSSLUpdate`)
- `POST /websites/ssl/upload` — Upload ssl (body: `request.WebsiteSSLUpload`)
- `POST /websites/ssl/upload/file` — Upload SSL file
- `GET /websites/ssl/website/:websiteId` — Search website ssl by website id

## Website Template (11)

- `POST /websites/templates` — Create website template (body: `request.WebsiteTemplateCreate`)
- `POST /websites/templates/del` — Delete website template (body: `dto.OperateByID`)
- `POST /websites/templates/get` — Get website template (body: `dto.OperateByID`)
- `POST /websites/templates/outputs` — Create website template output (body: `request.WebsiteTemplateOutputCreate`)
- `POST /websites/templates/outputs/del` — Delete website template output (body: `dto.OperateByID`)
- `POST /websites/templates/outputs/get` — Get website template output (body: `dto.OperateByID`)
- `POST /websites/templates/outputs/search` — Page website template outputs (body: `request.WebsiteTemplateOutputSearch`)
- `POST /websites/templates/preview` — Preview website template (body: `request.WebsitePreviewReq`)
- `POST /websites/templates/search` — Page website templates (body: `request.WebsiteTemplateSearch`)
- `POST /websites/templates/update` — Update website template (body: `request.WebsiteTemplateUpdate`)
- `POST /websites/templates/upload` — Upload website template zip

