# Global Quant Strategy Builder

繁體中文說明為主，英文版本見 [README_EN.md](README_EN.md)。

`global-quant-strategy-builder` 是一個面向全球金融市場的可重用 agent skill，適用於 Codex、Claude Code 和其他相容 `SKILL.md` 的程式編碼代理。它協助代理把模糊的交易想法收斂為更小、更安全、可驗證的策略變更，涵蓋標的池、資料、訊號、部位、風險、執行、回測和交付證據。

核心流程保持框架與市場無關，當前版本優先涵蓋美國股票、香港股票、ETF、場內期權、期貨、外匯和加密資產，同時支援擴充至歐洲、亞洲及其他市場。

## 這個 Skill 解決甚麼問題

很多量化提示詞只負責提出策略，卻沒有回答程式碼應該改在哪裡、資料何時可用、訂單如何成交，以及甚麼證據足以證明變更有效。這個 skill 會引導代理：

- 先識別現有框架、資料邊界和擴充點，再決定變更方案
- 把策略寫成明確的標的、資料、時鐘、訊號、開平倉、部位、風險和執行契約
- 優先重用參數和現有結構，避免不必要的重寫
- 明確處理時區、夏令時間、公司行動、除牌、匯率、賣空、期權指派和期貨轉倉
- 使用成本最低但足以令人信服的測試逐級驗證
- 區分「已實作」、「已測試」、「已回測」和「可供生產使用」

## 市場涵蓋範圍

| 範圍 | 重點 |
| --- | --- |
| 全球市場 | 交易所日曆、時區、多幣種、標的映射、公司行動、跨市場資料對齊 |
| 美國股票與 ETF | 盤前盤後、開收市競價、T+1、時點一致的標的池、賣空與借券、ETF 追蹤差異 |
| [香港股票與 ETF](skills/global-quant-strategy-builder/references/hong-kong-equities.md) | 港交所時段、收市競價、半日市、惡劣天氣交易、每手股數、碎股、T+2、賣空與港股通 |
| 場內期權 | 合約選擇、報價與價差、Greeks、提前行權、指派、到期和多腿成交 |
| 期貨 | 合約乘數、逐日盯市、交易時段、連續合約、轉倉、交割和保證金 |
| 外匯 | 基礎／報價貨幣、展期、融資、假期、交叉匯率和多幣種損益 |
| 加密資產 | 交易所差異、7×24 時鐘、永續合約、資金費率、標記價格和清算風險 |

法規、交易所規則和券商限制會變動。skill 要求代理在涉及合規或帳戶限制時檢查當時有效的一手資料，而不是把容易過期的數字寫死在核心流程中。

## 適用框架

目前參考涵蓋：

- LEAN / QuantConnect
- Backtrader
- vectorbt
- Zipline 及相容分支
- Freqtrade
- 券商與資料 API，包括自行開發的執行介接器
- 未列出的自行開發框架：退回通用的 `data -> signal -> target -> risk -> order -> fill -> accounting` 映射

## 適用代理

- Codex：使用 `skills/global-quant-strategy-builder/agents/openai.yaml`
- Claude Code：重用同一個 `SKILL.md`
- 其他支援 `SKILL.md` 的 agent runtime

## 安裝

### Codex（macOS / Linux）

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/global-quant-strategy-builder "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Codex（Windows PowerShell）

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
New-Item -ItemType Directory -Force -Path (Join-Path $codexRoot "skills") | Out-Null
Copy-Item -Recurse -Force ".\skills\global-quant-strategy-builder" (Join-Path $codexRoot "skills\global-quant-strategy-builder")
```

### Claude Code

把 `skills/global-quant-strategy-builder/` 複製到使用者層級的 `$HOME/.claude/skills/`，或專案層級的 `.claude/skills/`。

## 可直接重用的提示詞

- `使用 $global-quant-strategy-builder，把一個美股橫截面動量想法整理成可測試策略，明確時點一致的標的池、訊號滯後、換倉、成本和最小驗證計劃。`
- `使用 $global-quant-strategy-builder，審查這個 LEAN 美股策略的公司行動、時區、下單時點和風險模型是否一致。`
- `使用 $global-quant-strategy-builder，把恒生綜合指數成分股輪動想法整理成可回測策略，處理歷史成分股、每手股數、碎股、停牌、除牌、收市競價和交易費用。`
- `使用 $global-quant-strategy-builder，檢查港股低波動策略是否正確處理半日市、惡劣天氣交易、T+2、指定賣空證券和港股通交易日。`
- `使用 $global-quant-strategy-builder，為 SPY 場內期權輪動策略定義到期日、Delta、價差、提前指派和壓力測試規則。`
- `使用 $global-quant-strategy-builder，把全球 ETF 配置策略改成多幣種淨值，並測試匯率、非同步收市和當地假期。`

更多繁體中文及英文範例見 [examples/prompt-gallery.md](examples/prompt-gallery.md)。

## 倉庫結構

```text
.
|-- README.md
|-- README_EN.md
|-- LICENSE
|-- AGENTS.md
|-- examples/
|   `-- prompt-gallery.md
|-- scripts/
|   `-- validate_skill.py
|-- .github/workflows/
|   `-- validate-skill.yml
`-- skills/
    `-- global-quant-strategy-builder/
        |-- SKILL.md
        |-- agents/openai.yaml
        `-- references/
            |-- global-markets.md
            |-- us-equities-etfs.md
            |-- hong-kong-equities.md
            |-- listed-options.md
            |-- futures-fx-crypto.md
            |-- frameworks.md
            `-- validation.md
```

## 驗證

提交前執行：

```bash
python scripts/validate_skill.py
```

驗證腳本只使用 Python 標準函式庫，會檢查目錄結構、frontmatter、代理中繼資料、本機 Markdown 連結和殘留佔位符。

## 設計原則

- 根目錄面向使用者，`skills/global-quant-strategy-builder/` 面向代理。
- 核心 `SKILL.md` 只保留穩定工作流程；市場與框架細節放在按需載入的 references 中。
- 不把一次歷史回測描述成獲利證明。
- 不預設啟用真實交易；券商整合優先從模擬或 paper 環境驗證。
- 不提供個人化投資、法律、稅務或監管建議。

## 獨立實作與致謝

本倉庫是從零編寫的獨立實作。概念定位受到 [itsadrianxv/quant-strategy-builder-skill](https://github.com/itsadrianxv/quant-strategy-builder-skill) 啟發，但未複製其原始檔案或原文，本專案亦不隸屬於原專案。

## 授權條款

[MIT License](LICENSE)
