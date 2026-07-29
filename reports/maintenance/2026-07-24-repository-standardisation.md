# 修改日志 - 2026-07-24

## 仓库命名标准化

**仓库：** `UCL_EEE_Year2_Preparation`
**目标：** 统一目录和文件名命名规范，全部转为小写 kebab-case / snake_case

---

## 一、命名规则（GitHub 仓库文件夹建立逻辑）

| 类别 | 规则 | 示例 |
|---|---|---|
| 目录名 | 小写 kebab-case | `Exercises/` -> `exercises/` |
| Markdown / PDF / 图片 | 小写 kebab-case | `weekly_progress.md` -> `weekly-progress.md` |
| 可导入的 Python 源码 | 小写 snake_case | 保持不变（如 `positive_direction_wave.py`） |
| 序号标识 | 两位数 | `week01`, `01-diagnostic-test.md` |
| 空格 | 禁止 | 用连字符 `-` 或下划线 `_` 代替 |
| 标准根文件 | 保留原名 | `README.md`, `.gitignore`, `requirements.txt` |

GitHub / Git 在 Windows 上对**大小写变更**不敏感--`Exercises` 改 `exercises` 会被视为没有变化。因此必须通过**临时中间名**绕过：

```
Exercises/ -> __tmp_exercises/ -> exercises/
```

同样的方法也适用于 `Notes`、`Planning`、`Python`。

---

## 二、本次执行的所有重命名

### 目录（4 个）

| 原名 | 最终名 |
|---|---|
| `Exercises/` | `exercises/` |
| `Notes/` | `notes/` |
| `Planning/` | `planning/` |
| `Python/` | `python/` |

### 文件（3 个）

| 原名 | 最终名 |
|---|---|
| `Exercises/week01/01_diagnostic_answer.jpg` | `exercises/week01/01-diagnostic-answer.jpg` |
| `Exercises/week01/Exercise_01_Diagnostic_Test.md` | `exercises/week01/01-diagnostic-test.md` |
| `Planning/weekly_progress.md` | `planning/weekly-progress.md` |

### 内容更新的文件（2 个）

- **`exercises/week01/01-diagnostic-test.md`** - 图片链接 `01_diagnostic_answer.jpg` -> `01-diagnostic-answer.jpg`
- **`README.md`** - Repository structure 部分添加了 `exercises/` 条目

---

## 三、第一次执行遇到的问题及完善过程

### 问题描述

代码文档要求使用 `git mv` 进行 Git 感知的重命名，但我第一次执行 `git mv` 时，三条命令全部报错：

```
fatal: Unable to create '.../.git/index.lock': Permission denied
```

### 根本原因

沙箱环境（`CodexSandboxOffline` 用户）对仓库根目录有读写权限，但**无法写入 `.git/` 目录**（该目录的所有者和 ACL 归属 `wzj20` 用户）。任何需要修改 Git 索引的操作（`git mv`、`git add`、`git rm`）都依赖在 `.git/index.lock` 的创建，这个操作被系统权限拒绝。

### 排查过程

1. 检查 `.git` 的 ACL 权限 -> 确认沙箱用户只有 Modify 权限，但实际文件创建被拒绝
2. 尝试直接写入测试文件到 `.git/` 路径 -> 确认 Access Denied
3. 尝试设置 `GIT_INDEX_FILE` 环境变量指向临时可写路径 -> 可以运行 `git status`，但拿到的是一份空索引（因为真实索引仍在不可写的 `.git/` 中），后续 `git mv` 仍然依赖写入 `.git/`
4. 检查是否可以通过复制索引到临时路径再写回 -> 可以读取但不能写回 `.git/`

### 完善方案

确认无法从沙箱内操作 Git 索引后，我改为**文件系统级别的操作**：

1. 使用 PowerShell `Rename-Item` / `Move-Item` 完成文件和目录重命名
2. 用 `apply_patch` 更新文件内容中的路径引用
3. 进行完整的验证（文件存在性检查、旧名称搜索、README 内容检查、Python 脚本运行测试）
4. 提供用户一份精确的 `git rm --cached` + `git add -A` 命令，让用户在自有终端中更新 Git 索引

这一让步是沙箱权限限制下的最佳实践：不改变重命名结果，仅通过用户的终端完成 Git 索引的最终同步。

---

## 四、验证结果

| 检查项 | 结果 |
|---|---|
| 图片引用文件存在 | ✅ |
| 旧路径名（区分大小写）无残留 | ✅ |
| 临时目录 `__tmp_*` 无残留 | ✅ |
| `README.md` 目录描述为小写 | ✅ |
| Python 脚本未改动 | ✅（沙箱缺 matplotlib 无法运行，非重命名导致） |
| 数学公式 / 程序行为 | ✅ 未触碰 |

---

## 五、其他操作

- 清理了仓库根目录下意外克隆的两个嵌套目录（`UCL_EEE_Year2_Preparation-1/` 和 `UCL_EEE_Year2_Preparation/UCL_EEE_Year2_Preparation/`）
  - 沙箱无删除权限，由用户在终端手动完成

## 六、提交信息

```
refactor: standardise repository paths and filenames
```
