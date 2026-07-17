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

Download or clone this repository and run the following commands from its root. To inspect the procedure the agent will follow before installing it, read [skills/global-quant-strategy-builder/SKILL.md](skills/global-quant-strategy-builder/SKILL.md).

### Codex on macOS or Linux

```bash
skill_target="${CODEX_HOME:-$HOME/.codex}/skills/global-quant-strategy-builder"
mkdir -p "$skill_target"
cp -R skills/global-quant-strategy-builder/. "$skill_target/"
test -f "$skill_target/SKILL.md"
```

### Codex on Windows PowerShell

```powershell
$codexRoot = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }
$source = (Resolve-Path ".\skills\global-quant-strategy-builder").Path
$target = Join-Path $codexRoot "skills\global-quant-strategy-builder"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Recurse -Force (Join-Path $source "*") $target
Test-Path (Join-Path $target "SKILL.md")
```

### Claude Code at user scope

On macOS or Linux:

```bash
skill_target="$HOME/.claude/skills/global-quant-strategy-builder"
mkdir -p "$skill_target"
cp -R skills/global-quant-strategy-builder/. "$skill_target/"
test -f "$skill_target/SKILL.md"
```

On Windows PowerShell:

```powershell
$source = (Resolve-Path ".\skills\global-quant-strategy-builder").Path
$target = Join-Path $HOME ".claude\skills\global-quant-strategy-builder"
New-Item -ItemType Directory -Force -Path $target | Out-Null
Copy-Item -Recurse -Force (Join-Path $source "*") $target
Test-Path (Join-Path $target "SKILL.md")
```

For project-only Claude Code use, copy the same directory to `.claude/skills/global-quant-strategy-builder/` inside the target repository. Re-run the copy commands to update an existing installation, then start a new agent session.

### Confirm the installation

- Codex: start a new task with `Use $global-quant-strategy-builder to review this strategy idea and list only the missing strategy-contract details.`
- Claude Code: ask it to use the `global-quant-strategy-builder` skill for the same task.
- Other compatible runtimes: confirm that the runtime scans the installed `SKILL.md`, then invoke the skill with that runtime's syntax.

## Prompt guidance

In Codex, invoke `$global-quant-strategy-builder` directly. In Claude Code or another compatible agent, say “use the `global-quant-strategy-builder` skill.” Strong prompts normally state five things:

1. whether the agent should design, edit code, or perform a read-only review;
2. the market, asset, trading session, and universe;
3. the framework, data source, and repository constraints;
4. non-negotiable risk, cost, fill, and change-scope assumptions; and
5. the tests, backtests, and delivery evidence expected.

Use this template:

```text
Use $global-quant-strategy-builder in [market/instruments] and [framework/repository]
to turn [idea or problem] into [strategy design/minimal code change/read-only review].
Honor [data timing, cost, risk, and change-scope constraints],
and deliver [tests, backtests, sensitivity checks, changed files, and evidence].
```

### Reusable prompts

- `Use $global-quant-strategy-builder to turn a US equity cross-sectional momentum idea into a testable strategy with point-in-time membership, signal lag, turnover, costs, and a minimum validation plan.`
- `Use $global-quant-strategy-builder to review this LEAN strategy for corporate actions, timezone handling, order timing, and risk-model consistency.`
- `Use $global-quant-strategy-builder to turn a Hang Seng Composite constituent-rotation idea into a point-in-time backtest with board lots, odd lots, suspensions, delistings, closing-auction fills, and Hong Kong trading costs.`
- `Use $global-quant-strategy-builder to review this Hong Kong low-volatility strategy for half-days, severe-weather trading, T+2 settlement, designated short-sale eligibility, and Stock Connect calendars.`
- `Use $global-quant-strategy-builder to specify an SPY options rotation strategy with expiry, delta, spread, early-assignment, and stress-test rules.`
- `Use $global-quant-strategy-builder to make this global ETF allocation strategy multi-currency and test FX translation, asynchronous closes, and local holidays.`
- `Use $global-quant-strategy-builder to audit the continuous contract, roll, multiplier, margin, and fee assumptions in this futures trend backtest.`
- `Use $global-quant-strategy-builder to review this Backtrader backtest without editing code. Rank findings across leakage, fills, costs, risk, and evidence quality.`
- `Use $global-quant-strategy-builder to add continuous-contract, roll, overnight-session, multiplier, margin, and fee assumptions to this commodity-futures trend strategy with the smallest safe diff.`

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
