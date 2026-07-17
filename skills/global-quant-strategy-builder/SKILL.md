---
name: global-quant-strategy-builder
description: Design, implement, review, or validate quantitative trading strategy changes for global markets, with first-class coverage of US and Hong Kong equities, ETFs, listed options, futures, FX, and crypto. Use when an agent must turn a market hypothesis into repository-aware code or a testable specification; define universe, data, signals, positions, risk, and execution assumptions; audit a backtest; adapt a strategy to an existing framework; or produce evidence for a safe research handoff. Do not use for personalized investment advice or authorization of live trades.
---

# Global Quant Strategy Builder

Turn a market idea into the smallest repository-aware strategy change that can be tested honestly. Treat the work as research engineering, not as a promise of returns.

## Operating contract

- Match the requested action. Design when asked to design, diagnose when asked to diagnose, and edit only when asked to implement.
- Inspect the repository before choosing an architecture. Preserve its framework, naming, configuration, and extension points unless they block the request.
- Prefer one coherent, reversible change over a broad rewrite.
- Separate known facts, assumptions, decisions, and unresolved risks.
- Require evidence for claims about correctness, fills, risk, or performance.
- Keep research, paper execution, and live execution boundaries explicit. Never place or enable live orders without clear authorization and existing safeguards.
- Avoid personal investment, legal, tax, or regulatory advice. For mutable market rules, verify current primary sources instead of relying on memory.

## Route references

Read only the references needed for the request:

- Read [global-markets.md](references/global-markets.md) for multi-market, multi-currency, calendar, corporate-action, or point-in-time data concerns.
- Read [us-equities-etfs.md](references/us-equities-etfs.md) for US stocks, ETFs, sessions, settlement, shorting, or equity execution.
- Read [hong-kong-equities.md](references/hong-kong-equities.md) for Hong Kong stocks, REITs, ETFs, board lots, auctions, settlement, short selling, dual counters, or Stock Connect.
- Read [listed-options.md](references/listed-options.md) for option chains, contract selection, exercise, assignment, expiration, or Greeks.
- Read [futures-fx-crypto.md](references/futures-fx-crypto.md) for futures rolls, margin, FX conventions, perpetuals, funding, or continuous markets.
- Read [frameworks.md](references/frameworks.md) after identifying the repository's engine or broker integration.
- Read [validation.md](references/validation.md) when implementing, reviewing, or making any performance claim.

## Workflow

### 1. Frame the request

Restate the requested outcome in one sentence and classify it as design, implementation, review, diagnosis, or validation. Record constraints that limit the change: framework, asset class, venue, frequency, data, execution environment, and acceptable validation cost.

Ask only for information that would materially change the design and cannot be discovered locally. Otherwise, state a conservative assumption and continue.

### 2. Write the strategy contract

Define each field before editing code. Mark unknown fields instead of silently inventing them.

| Field | Required definition |
| --- | --- |
| Universe | Instruments, venues, eligibility, liquidity, and point-in-time membership |
| Data | Fields, vendor or feed, frequency, timestamps, adjustments, and availability delay |
| Clock | Exchange calendar, timezone, daylight-saving handling, and decision time |
| Signal | Formula, lookback, warm-up, cross-sectional or time-series scope, and lag |
| Entry and exit | Trigger, order intent, holding period, rebalance, and invalidation |
| Positioning | Sizing rule, rounding, leverage, cash, currency, and concentration limits |
| Risk | Pre-trade gates, portfolio limits, stops or exits, stale-data behavior, and kill conditions |
| Execution | Order type, session, spread, slippage, fees, borrow, partial fills, and latency |
| Evaluation | Benchmark, metrics, test periods, stress cases, and acceptance criteria |

Reject ambiguous same-bar logic. State exactly when information becomes observable and which later price may fill an order.

### 3. Map the repository

Locate the smallest existing path from configuration to data, signal, portfolio construction, risk, execution, tests, and reporting. Inspect:

- dependency and environment files;
- strategy base classes, interfaces, and lifecycle hooks;
- current parameters and configuration loading;
- data schemas, symbol identifiers, clocks, and calendars;
- order, fill, fee, slippage, and portfolio abstractions;
- analyzers, reports, fixtures, and tests.

Name the extension point to reuse. If no clean extension point exists, explain the smallest new seam required.

### 4. Choose the minimum viable change

Keep the signal, sizing, risk, and execution responsibilities distinct even if the framework stores them in one class. Prefer:

- adding or reusing a parameter over duplicating a strategy;
- extending a current model over introducing a parallel engine;
- a pure signal or sizing function that can be tested without a full backtest;
- configuration defaults that preserve current behavior;
- focused fixtures over broad production-data downloads.

Do not mix unrelated optimization, cleanup, dependency upgrades, or deployment work into the strategy change.

### 5. Implement market reality

Model only what the strategy needs, but model it explicitly:

- Use venue-aware calendars and timezone-aware timestamps.
- Distinguish raw, split-adjusted, and total-return data.
- Prevent look-ahead, survivorship, selection, and delisting bias.
- Convert exposures and P&L into a declared base currency.
- Apply contract multipliers, tick sizes, lot sizes, price increments, and rounding.
- Treat fees, spread, slippage, borrow, funding, and market impact as separate cost components when relevant.
- Define behavior for missing data, stale quotes, halts, rejected orders, partial fills, and reconnects.
- Keep broker and venue constraints configurable when they can change.

### 6. Validate proportionally

Run the cheapest test that can disprove the change first, then escalate:

1. Parse, compile, lint, or import the touched surface.
2. Test signal timing, sizing, rounding, and risk invariants with deterministic fixtures.
3. Run the smallest framework-level simulation that exercises order and fill behavior.
4. Compare against a baseline with identical data and cost assumptions.
5. Stress important assumptions across costs, lags, parameters, and market regimes.
6. Use paper or shadow execution only when the request and environment support it.

Do not interpret a passing backtest as proof of profitability. Report sample size, turnover, drawdown, costs, exposure, and out-of-sample status alongside returns.

### 7. Deliver evidence

End with:

- **Changed:** files, parameters, and behavior.
- **Assumed:** market, data, timing, cost, and account assumptions.
- **Verified:** commands or tests run and their observed results.
- **Not verified:** unavailable data, broker behavior, mutable rules, and live execution.
- **Next evidence:** the single most useful next test, if any.

Use calibrated language: distinguish implemented, tested, simulated, and production-ready.
