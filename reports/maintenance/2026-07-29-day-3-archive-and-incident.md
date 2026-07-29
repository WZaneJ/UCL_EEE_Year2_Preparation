# Repository Maintenance Log - 2026-07-29

## Repository
`UCL_EEE_Year2_Preparation` - local clone at `C:\Users\wzj20\OneDrive\Github_documents\UCL_EEE_Year2_Preparation`

## Commits Made This Session

| Hash | Message |
|---|---|
| `2eaadee` | feat: complete week 1 day 3 dynamic systems study |
| `ff3d6ad` | fix: restore weekly-progress day 2 section and move sim png |
| *(pending)* | fix: repair corrupted latex, strip bom and align day 3 progress style |

---

## Part 1: Tasks Completed

### 1.1 Day 3 Archive (commit `2eaadee`)
- Created `notes/week01/day03-dynamic-systems-circuit-odes.md`
- Created `exercises/week01/06-circuit-ode-diagnostic.md` + answer image
- Created `exercises/week01/07-circuit-ode-practice.md` + answer image
- Created `exercises/week01/08-circuit-ode-exit-test.md` + answer image
- Updated `README.md` (Day 3 [x], materials link block)
- Updated `planning/weekly-progress.md` (Day 3 checkboxes, Key results, Review queue, Day 4 stub)
- Verified `python/week01/circuit_ode_sim.py` and `.png` exist

### 1.2 Deploy Fix (commit `ff3d6ad`)
- Restored missing Day 2 section in `planning/weekly-progress.md`
- Moved `circuit_ode_sim.png` from repo root to `python/week01/`

### 1.3 Pending Fix (deploy script ready: `outputs/deploy_fix_day3.py`)
- Replace `planning/weekly-progress.md` with repaired copy (fixes 0x0C/0x0B corruption, removes BOM, aligns Day 3 style)
- Replace `exercises/week01/04-electric-fields-practice.md` with repaired copy (fixes `\;` -> `~` on line 7)
- Edit `notes/week01/day03-dynamic-systems-circuit-odes.md` title: dash -> colon + Title Case

---

## Part 2: Defects and Root Causes

### Defect 1: Day 2 Section Deleted from weekly-progress.md
**Root cause:** A generated Python deployment script parsed `weekly-progress.md` with a fragile state machine and silently dropped the entire Day 2 section. The script's line-scanning logic (`if "Day 2:" in line and "###" in line -> in_day2 = True`) ate the section and never restored it.
**Fix:** Extracted Day 2 from `git show HEAD~1:planning/weekly-progress.md`, reinserted it via script.

### Defect 2: LaTeX Corruption in Day 2 Key Results (0x0C / 0x0B)
**Root cause:** During the Day 2 restoration fix, LaTeX source was embedded in a normal Python triple-quoted string (`"""..."""`). Python interpreted `\f` in `\frac` as form-feed character (0x0C, 6 occurrences) and `\v` in `\varepsilon` as vertical-tab character (0x0B, 2 occurrences). The corruption was invisible in local editors but rendered as garbage on GitHub.
**Fix:** Binary replace 0x0C -> `\f` and 0x0B -> `\v` in the file. Submitted as a byte-repaired attachment.

### Defect 3: UTF-8 BOM in Written Files
**Root cause:** Using `Out-File -Encoding UTF8` in PowerShell adds a UTF-8 BOM (EF BB BF) by default. All files created with PowerShell had BOM.
**Fix:** Use `[System.IO.File]::WriteAllText($path, $content, [System.Text.UTF8Encoding]::new($false))` or Python `open(path, "w", encoding="utf-8")`.

### Defect 4: Surviving `\;` in 04-electric-fields-practice.md
**Root cause:** Line 7 had `$Q = +1\;\mu\text{C}$` where `\;` before `\mu` (a math symbol, not `\text`) was incorrectly judged as safe. GitHub renders `\;` as a literal semicolon in all contexts.
**Fix:** `\;` -> `~` (tilde) everywhere, regardless of what follows.

### Defect 5: circuit_ode_sim.png Wrong Path
**Root cause:** The simulation PNG was generated in the repository root instead of `python/week01/`.
**Fix:** Manual move.

### Defect 6: Day 3 Progress Style Downgrade
**Root cause:** The deployment script wrote Day 3's Key results and Review queue in plain text ("tau = RC", "e^{-500t}") instead of `$...$` math delimiters, and used a numbered list (`1. ... 2. ...`) for the review queue instead of the house style (`- [ ] ...` checkboxes).
**Fix:** Supplied as part of the repaired `weekly-progress.md` attachment.

### Defect 7: Day 3 Notes Title Format
**Root cause:** Used dash (`-`) instead of colon (`:`) and sentence case instead of Title Case, inconsistent with Day 1/Day 2 notes.
**Fix:** Single-line edit: `# Week 1 Day 3 - Dynamic systems and circuit ODEs` -> `# Week 1 Day 3: Dynamic Systems and Circuit ODEs`

---

## Part 3: Standing Rules (For All Future Tasks)

These rules are derived from the incidents above. Follow them for every task on this repository.

### Rule 1: No Script-Mediated Markdown Transformations
Edit repository files directly from exact templates provided in the task. Do NOT write parser/state-machine scripts that read, transform, and rewrite Markdown. If a script is unavoidable, it must print a full unified diff and stop for user confirmation before writing.

### Rule 2: Never Retype LaTeX in Code
To restore LaTeX content, always read the exact bytes from Git history (`git show <ref>:<path>`) or copy from a task-provided template. If string literals are truly unavoidable, use Python raw strings (`r"..."` / `r"""..."""`) and run the byte audit after writing. Never embed LaTeX in normal Python strings - `\f` (form feed 0x0C), `\v` (vertical tab 0x0B), and other escape sequences will silently corrupt the content.

### Rule 3: UTF-8 Without BOM Always
- All writes must be UTF-8 without BOM.
- Python: `open(path, "w", encoding="utf-8")`
- .NET: `[System.IO.File]::WriteAllText($path, $text, [System.Text.UTF8Encoding]::new($false))`
- PowerShell `Set-Content` / `Out-File` are forbidden for Markdown files (they add BOM or corrupt non-ASCII bytes).
- BOM absence is part of every post-change audit.

### Rule 4: Post-Change Byte Audit Is Mandatory
After every change, run ALL of the following on every modified file:
1. BOM scan: no file starts with `EF BB BF`
2. Control-byte scan: no byte below 0x20 other than 0x09 (tab), 0x0A (LF), 0x0D (CR)
3. Forbidden-macro grep: zero matches for `\;`, `\!`, `\operatorname`, `$$$`, `\(`, `\[`, `\]`, `\)`
4. Display-math balance: count of `$$` lines is even per file
5. Display-math indentation: every `$$` line starts at column 0
6. ASCII purity: no non-ASCII bytes in `.md` files (except pre-existing em-dashes etc.)

### Rule 5: A P0 Defect Is a Blocker, Not a Follow-Up
An unrepaired defect that breaks a public GitHub page is a BLOCKER. Tasks end in one of two states: "verified good" or "blocked, defect described precisely". Never mark a task "done with known issues" if the public page is broken.

### Rule 6: Generated Artifacts Go Directly to Final Path
Any generated artifact (image, file, simulation output) must be written directly to its final repository path and verified there with an existence check. Do not write to a staging directory and move later.

### Rule 7: Never Strip or Downgrade Math Delimiters
If source content uses `$...$` or `$$...$$`, the output must use the same delimiters. Flattening `$\tau = RC$` to plain text "tau = RC" is a rendering defect. If a transformation would change how anything renders, stop and report instead of applying it.

---

## Part 4: Sandbox Limitation (Codex Context)

The Codex sandbox (`CodexSandboxOffline` user) has restricted filesystem permissions:
- Read access: all paths (`:root`)
- Write access limited to: `C:\Users\wzj20\Documents\Codex\*`, `C:\Users\wzj20\.codex\visualizations\*`, temp directories
- The repository at `C:\Users\wzj20\OneDrive\Github_documents\UCL_EEE_Year2_Preparation` is NOT in the default writable roots.

A built-in `request_permissions` tool exists to temporarily extend write access, but after conversation compaction (automatic context compression) the tool may become unavailable. When this happens, Codex cannot write to the repository and must generate deploy scripts for the user to run locally.

**Workaround:** Generate a Python deploy script in a writable location (`outputs/`), verify it with syntax check and SHA256 checksums, then have the user run it from their terminal.

---

## Part 5: Deploy Scripts and Fixes Awaiting Execution

### Pending: `outputs/deploy_fix_day3.py`
SHA256-verified replacements:
- `weekly-progress.md`: expected SHA256 `211b7a75fadbd4fbd531ea284c95360048c51be7e4f435b27e8498b088a5e5d0`, 2999 bytes
- `04-electric-fields-practice.md`: expected SHA256 `656c320862ea0228d109c289bf8a2c3c8215ee181e9a7e61dbea0a001b47f195`, 986 bytes
- Day 3 notes title: single-line edit

Run: `python "C:\Users\wzj20\Documents\Codex\2026-07-24\new-chat\outputs\deploy_fix_day3.py"`
Then: `git diff --stat` -> verify exactly 3 files modified
Then: `git add -A && git commit -m "fix: repair corrupted latex, strip bom and align day 3 progress style"`
