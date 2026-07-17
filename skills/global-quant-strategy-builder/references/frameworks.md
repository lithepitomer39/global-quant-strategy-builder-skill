# Framework and integration adapters

Use this reference only after inspecting dependencies, imports, configuration, and strategy entry points. Confirm installed versions locally because APIs can change.

## LEAN / QuantConnect

- Detect `QCAlgorithm`, `Initialize`, event handlers, security subscriptions, consolidators, scheduled events, and model classes.
- Reuse Algorithm Framework modules when the repository already separates universe selection, alpha, portfolio construction, risk, and execution.
- Put brokerage, fee, slippage, fill, margin, and buying-power behavior in the relevant models rather than in signal code.
- Preserve symbol, resolution, normalization, mapping, and market-hour settings.
- Test with the existing LEAN configuration and data permissions; do not assume cloud datasets exist locally.

Official starting point: <https://www.quantconnect.com/docs/v2/writing-algorithms/key-concepts/algorithm-engine>.

## Backtrader

- Detect `bt.Strategy`, `Cerebro`, feeds, broker setup, sizers, commission schemes, analyzers, and `next` or timer hooks.
- Keep indicator construction and warm-up semantics consistent with the current strategy.
- Use order and trade notifications to track submitted, accepted, partial, completed, canceled, and rejected states.
- Verify bar timestamp and broker fill semantics before changing same-bar logic.
- Add a sizer or commission model instead of hiding sizing or costs inside the signal when practical.

Official strategy lifecycle: <https://www.backtrader.com/docu/strategy/>.

## vectorbt

- Detect array, indicator, signal, and `Portfolio` construction pipelines.
- Preserve index alignment, broadcasting, grouping, cash sharing, frequency, and call sequence.
- Shift signals explicitly when fills occur after information becomes available.
- Validate vectorized results against a small hand-worked or event-driven fixture for stateful logic.
- Do not force path-dependent order management into a simple boolean signal matrix if the simulator cannot represent it.

Official documentation: <https://vectorbt.dev/>.

## Zipline and compatible forks

- Detect bundles, trading calendars, asset finders, pipelines, scheduled functions, and algorithm callbacks.
- Reuse the registered calendar and bundle instead of synthesizing weekdays or current constituents.
- Check adjustment readers, asset lifetimes, minute versus daily labels, and order simulation.
- Match the exact fork and version in the repository; do not assume legacy Zipline APIs.

Documentation for a maintained distribution: <https://zipline.ml4trading.io/>.

## Freqtrade

- Detect strategy interface version, configuration, pairlists, informative data, protections, pricing, and exchange capabilities.
- Keep signal generation in strategy hooks and exchange or stake behavior in configuration where the framework expects it.
- Respect candle availability, startup count, fee assumptions, and look-ahead-analysis tooling.
- Treat futures mode, leverage, funding, and liquidation as separate from spot behavior.

Official documentation: <https://www.freqtrade.io/en/stable/>.

## Broker and data APIs

- Treat broker SDK code as an execution adapter, not a backtest engine.
- Preserve idempotent client order IDs, order-state reconciliation, timezone handling, rate limits, and reconnect behavior.
- Keep credentials outside source control and tests.
- Default new execution paths to simulation or paper mode.
- Mock deterministic unit boundaries, then use an explicitly authorized sandbox for integration checks.

## Custom engines

Map the repository to these roles even if names differ:

`data -> features -> signal -> target -> risk -> order -> fill -> accounting -> report`

Change the narrowest existing role. If several roles are entangled, add a testable seam before adding more strategy logic.
