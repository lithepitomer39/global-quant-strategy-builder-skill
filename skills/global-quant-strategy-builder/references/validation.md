# Strategy validation

Use this reference to choose evidence that is proportionate to the change and honest about what remains unknown.

## Start with invariants

Write deterministic checks for properties that must always hold:

- Signals use only information available at the decision timestamp.
- Warm-up periods cannot open positions prematurely.
- Position, leverage, concentration, and turnover limits are enforced after rounding.
- Orders use valid side, quantity, tick, lot, session, and contract identifiers.
- Missing or stale data cannot silently create a fresh signal.
- Costs reduce, rather than increase, reported performance.
- Corporate actions, rolls, assignment, and currency conversion conserve economic value under stated assumptions.
- Re-running the same inputs produces the same outputs unless randomness is deliberately seeded and recorded.

## Match evidence to the change

| Change | Minimum persuasive evidence |
| --- | --- |
| Parameter or configuration | Parse or load test plus one behavior assertion |
| Pure signal | Hand-worked fixture covering trigger, non-trigger, warm-up, and lag |
| Sizing or risk | Boundary tests, rounding tests, and portfolio invariant checks |
| Order or fill logic | Framework simulation covering order states and adverse cases |
| Data or universe | Schema, timestamp, adjustment, membership, and missing-data fixtures |
| Cost model | Zero-cost baseline plus spread, fee, slippage, borrow, or funding sensitivity |
| Full strategy | Baseline comparison, out-of-sample segment, regime slices, and robustness checks |
| Live adapter | Unit mocks, authorized sandbox or paper check, reconciliation, and kill-path evidence |

## Audit timing and leakage

- Trace one decision from source timestamp through feature, signal, order, and fill.
- Fit transforms, models, and thresholds only on training information.
- Use walk-forward or time-ordered splits; never randomize time-series observations without justification.
- Recreate historical universe eligibility point in time.
- Lag revised fundamentals, economic data, and analyst estimates by publication availability.
- Check that data cleaning does not backfill future values.
- Compare same-bar and next-bar results when execution timing is ambiguous.

## Model costs and capacity

Report components separately:

- commissions and venue or regulatory fees;
- half-spread or quote-based execution;
- market impact or participation assumptions;
- borrow and payments in lieu;
- financing, funding, and FX conversion;
- roll, exercise, assignment, and liquidation costs.

Stress costs above the base case. If the result disappears under a small plausible change, report fragility rather than selecting a friendlier assumption.

## Evaluate behavior, not one headline metric

Include metrics relevant to the strategy:

- sample length, trades, holding period, and turnover;
- return, volatility, drawdown, recovery, and tail loss;
- gross and net exposure, leverage, concentration, and liquidity;
- hit rate, payoff ratio, skew, and contribution by instrument;
- benchmark-relative return and beta when a benchmark is meaningful;
- results by market, regime, subperiod, and out-of-sample window.

Avoid annualizing tiny samples without a warning. Avoid treating Sharpe, win rate, or total return as sufficient alone.

## Test robustness without mining

- Vary parameters over a small predeclared neighborhood.
- Add one-bar or realistic latency.
- Widen spreads and increase costs.
- Remove the best trade, day, instrument, or subperiod.
- Shift start and end dates.
- Test volatile, quiet, trending, and stressed regimes when the sample permits.
- Compare a simpler baseline and explain why complexity earns its place.

Do not search many variants and report only the winner. Record the search space and selection rule when optimization is part of the request.

## Grade the handoff

Use one of these labels:

- **Implemented:** code changed; only basic checks may have run.
- **Unit-tested:** deterministic component behavior passed.
- **Backtested:** a specified historical simulation completed under stated assumptions.
- **Robustness-checked:** meaningful alternative costs, periods, or parameters were tested.
- **Paper-validated:** authorized non-live integration behavior was observed.
- **Production-ready:** use only when operational controls, monitoring, reconciliation, and approval requirements are actually satisfied.

State the exact evidence behind the label.
