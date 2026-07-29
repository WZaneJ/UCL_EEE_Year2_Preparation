# 修改日志 - 2026-07-24（第三次）

## 完成 Week 1 Day 2 Electric Fields and Potential

**仓库：** `UCL_EEE_Year2_Preparation`
**目标：** 补全 Week 1 Day 2（电场与电势）的学习笔记、练习、答案图片，并更新进度记录和 README

---

## 一、本次改动的完整文件清单

### 新建文件（5 个）

| 路径 | 大小 | 说明 |
|---|---|---|
| `notes/week01/day02-electric-fields-potential.md` | 3.4 KB | Day 2 学习笔记，匹配 Day 1 的章节结构和数学格式 |
| `exercises/week01/04-electric-fields-practice.md` | 1.0 KB | Exercise 4：电场练习（3 道题） |
| `exercises/week01/04-electric-fields-practice-answer.jpg` | 196 KB | 练习答案手写图片（优化后） |
| `exercises/week01/05-electric-fields-exit-test.md` | 1.2 KB | Exercise 5：退出测试（5 道题） |
| `exercises/week01/05-electric-fields-exit-test-answer.jpg` | 172 KB | 退出测试答案手写图片（优化后） |

### 修改文件（2 个）

| 文件 | 变更类型 | 说明 |
|---|---|---|
| `README.md` | 内容新增 | Day 2 进度标记为 [x]；新增 "Week 1 Day 2 materials" 链接块 |
| `planning/weekly-progress.md` | 内容重写 | Day 2 全部 9 项标记 [x]；新增 Key results / Review queue / Day 3 占位 |

### 未修改的文件

- `python/week01/electric_field_potential.py` - 声明不可触碰
- `python/week01/electric_field_potential.png` - 声明不可触碰
- 所有 Day 1 文件（`01-*` 到 `03-*`）

---

## 二、遇到的三个问题及解决方案

### 问题 1：PowerShell 反引号转义导致 README 中的代码片消失

**现象：** 第一次写入 README 时，`` `planning/` `` 中的反引号被 PowerShell 当作转义字符吃掉，变成 `planning/`。

**解决方案：** 放弃用 PowerShell 字符串拼接 `$lines` 数组的方式，改用 .NET 的 `[System.IO.File]::WriteAllText()` 写入。其中需要反引号的字符串用单引号包围（PowerShell 不对单引号字符串做变量展开和转义处理）。

### 问题 2：沙箱无法写入 `.git/` 目录

**现象：** `git mv`、`git add`、`git rm` 等所有需要创建 `.git/index.lock` 的操作均因权限拒绝而失败（延续上次的问题）。

**解决方案：** 本次无需 `git mv`（新文件创建不涉及重命名），所有文件通过 `Out-File` / `WriteAllText` 直接在 working tree 中创建。Git 索引更新留由用户在终端执行 `git add -A`。

### 问题 3：沙箱无法删除文件（`Remove-Item` 被策略拒绝）

**现象：** 用户已放置源文件 `1.jpg` 和 `2.jpg` 在 `exercises/week01/` 中，处理完成后无法删除它们。

**解决方案：** 这两个文件是 untracked 状态，不影响 Git 跟踪和提交。在最终报告中标注为需用户手动清理的残留文件。

---

## 三、笔记内容结构说明

`day02-electric-fields-potential.md` 严格匹配 Day 1 笔记的格式：

1. **Related modules** - 与 Day 1 相同的 4 个模块引用
2. **Coulomb's law and electric field** - 库仑定律与电场定义，含 `1/(4πε₀) = 9×10⁹`
3. **Electric potential and potential energy** - 电势与势能，含 eV 单位转换
4. **Relation between field and potential** - `E_x = -dV/dx` 与减号物理含义
5. **Sign traps with the electron** - `F = -eE`、`U = -eV`、eV 单位
6. **Parallel-plate capacitor worked example** - `d=5mm, V₀=20V -> |E|=4000 V/m`
7. **Gauss's law preview** - 球/柱/平面对称性分类
8. **Key conceptual reminders** - V 的常数自由度、V=0 不意味 E=0、E=0 不意味 V=0
9. **Reflection** - "What I understood" / "What I need to review"

数学格式：`$$...$$` 显示数学 + `$...$` 内联数学，无 `\(...\)`。

---

## 四、练习内容设计

### Exercise 4：电场练习（3 题）

- Q1：点电荷 Q=+1μC，求 r=0.1m 处的 E 大小/方向、V、电子受力方向和势能(eV)
- Q2：`V(x)=5x²-3x+2`，求 E_x(x)、方向、电势增减判断
- Q3：概念判断：V=0 是否意味 E=0？E=0 是否意味 V=0？

### Exercise 5：退出测试（5 题）

- Q1：点电荷 E(r) 和 V(r) 公式及 SI 单位
- Q2：平行板电容器 d=5mm, V₀=20V，求 |E|
- Q3：`V(x)=3x²`，求 E_x(x) 及电子受力方向
- Q4：概念："静电平衡导体内部 E=0 所以 V=0"--对错？
- Q5：Day 1 回顾：`exp(j(ωt+βx))` 传播方向 + sinθ 的复指数恒等式

---

## 五、需要再次检查的内容（在 GitHub 上推送后确认）

1. **数学公式渲染**
   - 笔记中所有的 `$$` 显示数学是否正常渲染（尤其是分式 `\frac`）
   - 内联 `$...$` 是否正常（尤其是 `x\to+\infty`、`\hat{\mathbf{r}}`）

2. **图片显示**
   - `04-electric-fields-practice-answer.jpg` 在 GitHub 上是否可读
   - `05-electric-fields-exit-test-answer.jpg` 在 GitHub 上是否可读
   - 图片链接为相对路径 `./xxx.jpg`，确认无 404

3. **README 导航**
   - "Week 1 Day 2 materials" 下的 4 个链接是否跳转到对应文件
   - 进度勾选框是否正确显示 [x]

4. **进度文件**
   - `planning/weekly-progress.md` 中全部 9 个 Day 2 复选框是否为 [x]
   - "Key results" 公式块是否渲染正常
   - Day 3 占位标题存在但无伪造的复选框

5. **清理残留**
   - 确认 `exercises/week01/1.jpg` 和 `exercises/week01/2.jpg` 已手动删除

---

## 六、验证清单

| 检查项 | 状态 |
|---|---|
| 5 个新文件存在且非空 | ✅ |
| 旧文件无 04/05 的引用 | ✅ |
| 所有 Markdown 图片链接解析到实际文件 | ✅ |
| 无 `\(`, `\)`, `\[`, `\]`, `\operatorname` 残留 | ✅ |
| 所有代码围栏平衡 | ✅ |
| 所有 `$$` 显示数学平衡 | ✅ |
| README Day-2 链接全部有效 | ✅ |
| `planning/weekly-progress.md` 无 `\(` 残留 | ✅ |
| Python 脚本未被触碰 | ✅ |

## 七、建议的提交信息

```
feat: complete week 1 day 2 electric field study
```
