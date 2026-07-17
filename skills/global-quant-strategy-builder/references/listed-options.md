# Listed options

Use this reference for exchange-listed equity, ETF, index, and futures options.

## Identify the contract

Represent each contract with its underlying, venue or clearing convention, expiration, strike, call or put right, exercise style, settlement method, multiplier, currency, and last trading time. Do not infer these fields from a display symbol alone.

Distinguish:

- American, European, and other exercise styles;
- physical and cash settlement;
- standard, weekly, quarterly, adjusted, and non-standard contracts;
- expiration date from the last tradable timestamp;
- equity or ETF options from index and futures options.

## Select contracts without leakage

- Select from the chain observable at the decision timestamp.
- Define expiry using trading sessions or calendar days consistently.
- Define moneyness from an observable underlying or forward price.
- Specify strike selection, delta target, liquidity thresholds, spread limits, and fallback behavior.
- Keep expired, newly listed, and adjusted contracts in historical coverage where needed.
- Avoid selecting today's winner from a chain snapshot obtained after the intended trade time.

## Model prices and fills

- Prefer bid and ask data for executable estimates; do not treat stale midpoints as guaranteed fills.
- Reject or flag crossed, locked, zero-bid, stale, or missing quotes.
- Apply contract multipliers and fees per contract.
- Model multi-leg orders atomically only if the engine and venue support that assumption; otherwise model leg risk and fill sequencing.
- Stress fills from midpoint toward the adverse side of the spread.

## Model lifecycle risk

- Define exercise, assignment, expiration, and auto-exercise behavior.
- Account for early exercise incentives around dividends, rates, and remaining time value.
- Check whether assignment creates stock, cash, futures, margin, or currency exposure.
- Handle corporate-action-adjusted contracts without silently treating them as standard contracts.
- Close or roll positions before data or broker support ends, but do not hide the economic cost of that rule.

## Risk and valuation

- Limit risk by scenario P&L and portfolio exposure, not contract count alone.
- Track relevant delta, gamma, vega, theta, underlying concentration, expiration concentration, and liquidity.
- State the volatility surface, rate, dividend, and pricing-model assumptions when Greeks or fair value drive decisions.
- Stress gaps, volatility shocks, skew changes, spread widening, assignment, and pin risk.
- Do not equate premium received with maximum safe profit or defined risk unless the payoff proves it.

## Minimum evidence

Test at least:

- contract identity and multiplier;
- chain selection at the decision timestamp;
- spread-aware entry and exit;
- expiry and last-trading-time boundaries;
- early assignment or exercise scenarios where applicable;
- multi-leg partial-fill behavior;
- adjusted or non-standard contracts;
- scenario loss and margin assumptions.

Before describing product risks, verify the current contract specification and clearing documentation. OCC publishes the options disclosure document at <https://www.theocc.com/company-information/documents-and-archives/options-disclosure-document>.
