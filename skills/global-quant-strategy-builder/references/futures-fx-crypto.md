# Futures, FX, and crypto

Use this reference for expiring contracts, leveraged derivatives, around-the-clock sessions, and venue-specific funding.

## Futures

- Identify exchange, root, exact contract month, multiplier, quote convention, tick size, tick value, currency, session, expiry, first notice, and settlement.
- Use individual contracts for execution. Treat a continuous series as a research transformation, not a tradable instrument.
- Define the roll trigger from observable volume, open interest, calendar, or expiry data and prevent backward-looking contract selection.
- State the adjustment method for continuous prices and avoid calculating returns across an unadjusted roll gap.
- Model commissions, exchange and clearing fees, spread, margin changes, daily variation margin, and delivery risk.
- Respect session breaks, price limits, special settlement windows, and holiday schedules.

## FX

- State base and quote currencies and the sign of each exposure.
- Distinguish spot, forward, non-deliverable forward, futures, CFD, and rolling broker products.
- Use bid and ask prices and define rollover, value date, financing, and holiday treatment.
- Align cross rates without using future fixes or later-closing data.
- Track cash and P&L in both local currencies and portfolio base currency.
- Stress weekend gaps, central-bank events, spread widening, and broken or pegged regimes.

## Crypto

- Identify venue, spot or derivative product, collateral, settlement currency, contract type, and custody model.
- Treat each venue as a distinct market with its own symbols, fees, outages, liquidity, and counterparty risk.
- For perpetuals, model funding timestamps, sign, caps, mark price, index price, and liquidation mechanics.
- For dated futures and options, model expiry and settlement like other derivatives while preserving venue-specific rules.
- Do not interpret 24/7 trading as continuous data availability; define maintenance, outage, and stale-feed behavior.
- Separate on-chain events, exchange timestamps, and data-provider receipt times.

## Cross-asset risk

- Normalize exposure by contract multiplier, volatility, currency, and liquidity before aggregation.
- Distinguish initial margin, maintenance margin, economic risk, and broker liquidation thresholds.
- Prevent leverage from rising accidentally when volatility falls, correlations change, or contract prices move.
- Cap concentration by underlying risk, not merely by symbol count.
- Define a kill path for rejected orders, stale marks, disconnects, funding spikes, and margin shortfalls.

## Minimum evidence

Test at least:

- a contract roll or expiry;
- tick and multiplier arithmetic;
- a session boundary or weekend gap;
- base-currency P&L conversion;
- margin or liquidation stress;
- funding or financing accrual;
- a venue outage or stale price;
- cost sensitivity under thin liquidity.
