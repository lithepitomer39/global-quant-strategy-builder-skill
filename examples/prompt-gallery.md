# Prompt gallery

These prompts are agent-neutral. In Codex, invoke `$global-quant-strategy-builder` explicitly. In another compatible runtime, ask it to use the `global-quant-strategy-builder` skill.

## 如何寫出更好的提示詞 / How to write a stronger prompt

先選擇代理要執行的動作：策略設計、最小程式碼變更，或只讀審查。接著交代市場與標的、框架與資料、不可妥協的風險或成交假設，以及你希望看到的驗證證據。若正在處理既有倉庫，請明確要求沿用現有擴充點並避免無關重寫。

Start by choosing the action: strategy design, a minimal code change, or a read-only review. Then state the market and instruments, framework and data, non-negotiable risk or fill assumptions, and the validation evidence you expect. For an existing repository, explicitly request reuse of current extension points and no unrelated rewrites.

### 繁體中文模板

```text
使用 $global-quant-strategy-builder，在 [市場／標的] 的 [框架／倉庫] 中，
把 [策略想法或問題] 收斂成 [策略設計／最小程式碼變更／只讀審查]。
請遵守 [資料時點、成本、風險和不可改動範圍]，
並交付 [測試、回測、敏感度檢查、修改檔案和證據]。
```

### English template

```text
Use $global-quant-strategy-builder in [market/instruments] and [framework/repository]
to turn [idea or problem] into [strategy design/minimal code change/read-only review].
Honor [data timing, cost, risk, and change-scope constraints],
and deliver [tests, backtests, sensitivity checks, changed files, and evidence].
```

## US equities and ETFs

### 繁體中文

- `使用 $global-quant-strategy-builder，把「每月買入過去 12 個月最強的標普 500 股票」收斂成時點一致的可回測策略，處理歷史成分股、跳過月、除牌、換手和交易成本。`
- `使用 $global-quant-strategy-builder，為這個美股均值回歸策略增加盤前過濾、開市成交假設、借券供應和單一股票風險上限，並保持最小變更。`
- `使用 $global-quant-strategy-builder，審查全球 ETF 輪動回測，找出匯率、派息、非同步收市和當地假期造成的偏差。`

### English

- `Use $global-quant-strategy-builder to turn a 12-minus-1 month S&P 500 momentum idea into a point-in-time backtest with constituent history, delistings, turnover, and costs.`
- `Use $global-quant-strategy-builder to add pre-market filtering, open-fill assumptions, borrow availability, and per-name risk limits to this US mean-reversion strategy with the smallest safe diff.`
- `Use $global-quant-strategy-builder to audit this global ETF rotation backtest for FX, distributions, asynchronous closes, and local-market holidays.`

## Hong Kong equities and ETFs

### 繁體中文

- `使用 $global-quant-strategy-builder，把恒生綜合指數成分股動量想法整理成時點一致的回測，處理歷史成分股、每手股數、碎股、停牌、除牌、收市競價和交易費用。`
- `使用 $global-quant-strategy-builder，為這個港股均值回歸策略加入午休時段、半日市、隨機收市、惡劣天氣交易和成交量限制，並保持最小變更。`
- `使用 $global-quant-strategy-builder，審查港股多空策略是否只在指定證券進行有抵押賣空，並正確模擬借券成本、賣空價規則和 T+2。`
- `使用 $global-quant-strategy-builder，檢查港股通策略的歷史合資格名單、兩地交易日、交易貨幣、下單限制和不可交易日期。`

### English

- `Use $global-quant-strategy-builder to turn a Hang Seng Composite momentum idea into a point-in-time backtest with constituent history, board lots, odd lots, suspensions, delistings, closing-auction fills, and fees.`
- `Use $global-quant-strategy-builder to add the lunch break, half-days, random close, severe-weather trading, and volume limits to this Hong Kong mean-reversion strategy with the smallest safe diff.`
- `Use $global-quant-strategy-builder to review whether this Hong Kong long-short strategy uses covered short sales only in designated securities and models borrow cost, the tick rule, and T+2 correctly.`
- `Use $global-quant-strategy-builder to audit this Stock Connect strategy for point-in-time eligibility, both markets' calendars, trading currency, order restrictions, and unavailable trading days.`

## Listed options

### 繁體中文

- `使用 $global-quant-strategy-builder，為 SPY 備兌策略明確合約到期、Delta、流動性、除息日前提前指派、交易成本和壓力測試。`
- `使用 $global-quant-strategy-builder，審查這個期權價差回測是否錯誤使用中間價、當日完整期權鏈或不現實的多腿同時成交。`

### English

- `Use $global-quant-strategy-builder to specify an SPY covered-call strategy with expiry, delta, liquidity, ex-dividend assignment, costs, and stress tests.`
- `Use $global-quant-strategy-builder to review this options-spread backtest for midpoint fills, future chain leakage, and unrealistic atomic execution.`

## Futures, FX, and crypto

### 繁體中文

- `使用 $global-quant-strategy-builder，修正商品期貨趨勢策略的連續合約、轉倉、乘數、逐日盯市、手續費和交割風險。`
- `使用 $global-quant-strategy-builder，把 G10 外匯策略改成多幣種會計，加入點差、展期、假期和基準貨幣損益。`
- `使用 $global-quant-strategy-builder，審查永續合約策略的資金費率、標記價格、槓桿、清算和交易所服務中斷處理。`

### English

- `Use $global-quant-strategy-builder to correct the continuous-series, roll, multiplier, variation-margin, fee, and delivery assumptions in this commodity futures trend strategy.`
- `Use $global-quant-strategy-builder to convert this G10 FX strategy to multi-currency accounting with spreads, rollover, holidays, and base-currency P&L.`
- `Use $global-quant-strategy-builder to review this perpetual-futures strategy for funding, mark price, leverage, liquidation, and venue outage handling.`

## Framework-focused work

### 繁體中文

- `使用 $global-quant-strategy-builder，把這個 LEAN 單檔案策略按現有結構拆分至 Alpha、Portfolio Construction、Risk 和 Execution 模組，避免無關重寫。`
- `使用 $global-quant-strategy-builder，為 Backtrader 策略補齊訂單狀態、部分成交、手續費、Sizer 和 Analyzer 的最小驗證。`
- `使用 $global-quant-strategy-builder，檢查 vectorbt 訊號對齊是否存在同一根 K 線偷看，並用一個手算範例驗證。`

### English

- `Use $global-quant-strategy-builder to map this LEAN strategy onto the repository's existing Alpha, Portfolio Construction, Risk, and Execution modules without unrelated rewrites.`
- `Use $global-quant-strategy-builder to add focused order-state, partial-fill, commission, sizer, and analyzer validation to this Backtrader strategy.`
- `Use $global-quant-strategy-builder to audit vectorbt signal alignment for same-bar leakage and verify it with one hand-worked example.`

## Review and evidence

### 繁體中文

- `使用 $global-quant-strategy-builder，只審查這個回測，不修改程式碼。按資料洩漏、成交、成本、風險和統計證據排序列出問題。`
- `使用 $global-quant-strategy-builder，為這次策略參數變更選擇成本最低但足以令人信服的驗證，不要啟動完整最佳化。`

### English

- `Use $global-quant-strategy-builder to review this backtest without editing code. Rank findings across leakage, fills, costs, risk, and statistical evidence.`
- `Use $global-quant-strategy-builder to choose the cheapest persuasive validation for this parameter change without launching a broad optimization.`
