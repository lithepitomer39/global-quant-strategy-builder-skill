# US equities and ETFs

Use this reference for US-listed stocks, ADRs, closed-end funds, and exchange-traded products.

## Sessions and clocks

- Use the listing venue's official calendar and named US Eastern timezone.
- Separate pre-market, core, closing auction, and after-hours liquidity. Do not assume the same fill model across sessions.
- Treat early closes and unscheduled halts explicitly.
- Align signals with the data actually observable before the intended auction or continuous-session order.
- Verify current hours and holiday calendars with the relevant exchange. NYSE publishes its current schedule at <https://www.nyse.com/trade/hours-calendars>.

## Data and universe

- Use stable security identifiers where possible; tickers can be reused or changed.
- Build point-in-time index and liquidity universes. A current constituent list is not historical membership.
- Include delisted securities, acquisitions, bankruptcies, and terminal distributions when evaluating historical selection strategies.
- State whether OHLCV is consolidated or venue-specific and whether volume includes extended hours.
- Separate raw prices used for orders from adjusted data used for signals.
- For ADRs, model listing currency, ratio changes, home-market timing, and depositary fees when material.

## ETFs and exchange-traded products

- Distinguish fund distributions from price return.
- Check exposure type, leverage or inverse reset, derivatives use, and index methodology.
- Treat premium or discount, indicative value, creation/redemption effects, and thin secondary-market liquidity as separate concepts.
- Do not use an ETF as a frictionless proxy for its index without testing tracking difference and trading costs.

## Execution and settlement

- Model spread, commissions and regulatory fees, slippage, participation, partial fills, and auction behavior at the strategy's frequency.
- Keep order eligibility and price increments in the broker or venue layer.
- Model unsettled cash when the account or strategy depends on it. Most applicable US securities transactions moved to T+1 settlement on May 28, 2024; verify the current rule and exceptions at <https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/new-t1-settlement-cycle-what-investors-need-know-investor-bulletin>.
- Treat broker buying power and account restrictions as mutable inputs, not universal constants.

## Short sales

- Require shortable status or locate availability when the execution model exposes it.
- Include borrow fees, hard-to-borrow changes, recall risk, buy-ins, and payments in lieu of dividends.
- Model asymmetric loss and gap risk in sizing and portfolio limits.
- Account for price-test and order-marking constraints where relevant. Re-check the current Regulation SHO requirements at <https://www.sec.gov/investor/pubs/regsho.htm>.

## Minimum evidence

Test at least:

- split and dividend handling;
- signal-to-fill timing at open, close, or next bar;
- point-in-time universe membership;
- missing, halted, or delisted symbols;
- fractional versus whole-share rounding;
- long and short cost asymmetry;
- core versus extended-hours fills;
- cost sensitivity at realistic turnover.
