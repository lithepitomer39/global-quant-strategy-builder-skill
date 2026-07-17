# Global Quant Strategy Builder

For the primary Traditional Chinese documentation, see [README.md](README.md).

`global-quant-strategy-builder` is a reusable agent skill for Codex, Claude Code, and other runtimes that support `SKILL.md`. It turns an underspecified market idea into a smaller, safer, testable strategy change with explicit coverage of universe selection, data, signals, positions, risk, execution, backtesting, and delivery evidence.

The core workflow is market- and framework-neutral. The current release gives first-class treatment to US and Hong Kong equities, ETFs, listed options, futures, FX, and crypto while remaining extensible to European, Asian, and other global markets.

## What problem does it solve?

Many quantitative prompts stop at strategy ideation. They do not establish where code should change, when data is observable, how orders can fill, or what evidence is persuasive. This skill directs an agent to:

- identify the existing framework, data boundaries, and extension points before editing;
- define an explicit contract for instruments, data, clocks, signals, entries, exits, sizing, risk, and execution;
- reuse parameters and local architecture before adding parallel abstractions;
- handle timezones, daylight saving, corporate actions, delistings, currencies, shorting, assignment, and futures rolls explicitly;
- validate from cheap deterministic checks up to focused simulations and robustness tests;
- distinguish implemented, tested, backtested, and production-ready states.

## Market coverage

| Scope | First-class concerns |
| --- | --- |
| Global markets | Exchange calendars, timezones, currencies, identifiers, corporate actions, asynchronous data |
| US equities and ETFs | Extended hours, auctions, T+1, point-in-time universes, short borrow, ETF tracking differences |
| [Hong Kong equities and ETFs](skills/global-quant-strategy-builder/references/hong-kong-equities.md) | HKEX sessions, closing auction, half-days, severe-weather trading, board lots, odd lots, T+2, short selling, Stock Connect |
| Listed options | Contract selection, quotes and spreads, Greeks, early exercise, assignment, expiry, multi-leg fills |
| Futures | Multipliers, variation margin, sessions, continuous series, rolls, delivery, margin |
| FX | Base and quote currency, rollover, financing, holidays, cross rates, multi-currency P&L |
| Crypto | Venue fragmentation, 24/7 clocks, perpetuals, funding, mark prices, liquidation risk |

Regulations, exchange rules, and broker restrictions change. The skill requires the agent to verify current primary sources for compliance-sensitive behavior instead of hard-coding mutable limits into the core workflow.

## Supported frameworks

The bundled references currently cover:

- LEAN / QuantConnect
- Backtrader
- vectorbt
- Zipline and compatible forks
- Freqtrade
- broker and data APIs, including custom execution adapters
- custom engines through the generic `data -> signal -> target -> risk -> order -> fill -> accounting` map

## Compatible agents

- Codex through `skills/global-quant-strategy-builder/agents/openai.yaml`
- Claude Code through the same `SKILL.md`
- other agent runtimes compatible with `SKILL.md`

## Installation

### Codex on macOS or Linux

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/global-quant-strategy-builder "${CODEX_HOME:-$HOME/.codex}/skills/"
```

### Codex on Windows PowerShell

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
New-Item -ItemType Directory -Force -Path (Join-Path $codexRoot "skills") | Out-Null
Copy-Item -Recurse -Force ".\skills\global-quant-strategy-builder" (Join-Path $codexRoot "skills\global-quant-strategy-builder")
```

### Claude Code

Copy `skills/global-quant-strategy-builder/` to the user-level `$HOME/.claude/skills/` directory or to a project's `.claude/skills/` directory.

## Example prompts

- `Use $global-quant-strategy-builder to turn a US equity cross-sectional momentum idea into a testable strategy with point-in-time membership, signal lag, turnover, costs, and a minimum validation plan.`
- `Use $global-quant-strategy-builder to review this LEAN strategy for corporate actions, timezone handling, order timing, and risk-model consistency.`
- `Use $global-quant-strategy-builder to turn a Hang Seng Composite constituent-rotation idea into a point-in-time backtest with board lots, odd lots, suspensions, delistings, closing-auction fills, and Hong Kong trading costs.`
- `Use $global-quant-strategy-builder to review this Hong Kong low-volatility strategy for half-days, severe-weather trading, T+2 settlement, designated short-sale eligibility, and Stock Connect calendars.`
- `Use $global-quant-strategy-builder to specify an SPY options rotation strategy with expiry, delta, spread, early-assignment, and stress-test rules.`
- `Use $global-quant-strategy-builder to make this global ETF allocation strategy multi-currency and test FX translation, asynchronous closes, and local holidays.`
- `Use $global-quant-strategy-builder to audit the continuous contract, roll, multiplier, margin, and fee assumptions in this futures trend backtest.`

See [examples/prompt-gallery.md](examples/prompt-gallery.md) for more prompts in English and Traditional Chinese.

## Repository layout

```text
.
|-- README.md
|-- README_EN.md
|-- LICENSE
|-- AGENTS.md
|-- examples/prompt-gallery.md
|-- scripts/validate_skill.py
|-- .github/workflows/validate-skill.yml
`-- skills/global-quant-strategy-builder/
    |-- SKILL.md
    |-- agents/openai.yaml
    `-- references/
```

## Validation

Run before submitting changes:

```bash
python scripts/validate_skill.py
```

The validator uses only the Python standard library and checks repository structure, frontmatter, agent metadata, local Markdown links, and unresolved placeholders.

## Design principles

- Keep human-facing distribution material at the repository root and agent-facing instructions inside the installable skill.
- Keep the core `SKILL.md` stable and concise; load market and framework details only when relevant.
- Never present a historical backtest as proof of future profitability.
- Do not enable live trading by default; validate broker integrations in simulation or paper environments first.
- Do not provide personalized investment, legal, tax, or regulatory advice.

## Independent implementation and acknowledgement

This repository is an independently written, clean implementation. Its product direction was inspired by [itsadrianxv/quant-strategy-builder-skill](https://github.com/itsadrianxv/quant-strategy-builder-skill), but no source files or prose were copied, and this project is not affiliated with the original project.

## License

[MIT License](LICENSE)
