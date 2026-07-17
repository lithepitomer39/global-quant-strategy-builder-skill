# Hong Kong equities and ETFs

Use this reference for securities listed on the Stock Exchange of Hong Kong (SEHK), including equities, REITs, ETFs, and dual-counter instruments. Treat Stock Connect as a distinct access route with its own eligibility and operational rules.

## Identify instruments correctly

- Preserve leading zeroes in Hong Kong stock codes and keep the exchange identifier separate from the display ticker.
- Distinguish ordinary shares, preference shares, stapled securities, REITs, ETFs, depositary receipts, and structured products before applying strategy rules.
- Track listing currency, trading counter, board-lot size, short name, security status, and corporate-action history point in time.
- Map HKD and RMB counters of a dual-counter security to the same economic issuer without treating them as freely interchangeable fills.
- Keep share-class, primary-listing, secondary-listing, and Stock Connect eligibility attributes explicit.

## Model the Hong Kong clock

- Use the `Asia/Hong_Kong` timezone. Hong Kong does not use daylight saving time, but connected overseas markets may.
- Load the official HKEX calendar instead of generating weekdays.
- Represent the pre-opening auction, morning continuous session, lunch break, afternoon continuous session, and Closing Auction Session separately.
- Model the random closing time in the Closing Auction Session. Do not assume every eligible security closes exactly at 16:00.
- Handle half-day markets and the absence of the afternoon session on designated eves.
- Do not infer an exchange closure from a typhoon or rainstorm signal. HKEX severe-weather trading arrangements have kept the securities and derivatives markets operating according to the predetermined calendar since 2024; verify current operational details and broker availability.

Official hours and severe-weather arrangements:

- <https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Trading-Hours/Securities-Market?sc_lang=en>
- <https://www.hkex.com.hk/Services/Trading-hours-and-Severe-Weather-Arrangements/Severe-Weather-Arrangements/Overview?sc_lang=en>

## Preserve point-in-time data

- Use historical index membership and Stock Connect eligibility rather than current lists.
- Include IPOs, suspensions, resumptions, delistings, privatisations, trading halts, and terminal cash flows.
- Apply splits, consolidations, rights issues, bonus issues, special dividends, open offers, and symbol or board-lot changes consistently across prices and positions.
- Distinguish raw executable prices from adjusted signal series and total-return series.
- Timestamp announcements by publication availability. Do not use a later filing, translated announcement, or revised dataset in an earlier decision.
- Define whether bars include auction trades and whether turnover and volume cover the same sessions used by the strategy.

## Apply lots, ticks, and auctions

- Read each security's board-lot size from a point-in-time security master; do not assume a universal number of shares per lot.
- Round normal-market orders to the eligible board lot and route residual quantities through an explicit odd-lot policy.
- Model odd-lot liquidity and price separately from the board-lot market. Do not grant odd lots the normal order book's spread or fill probability.
- Read tick sizes and valid price ranges from the current HKEX spread table or broker adapter.
- Distinguish at-auction, at-auction-limit, and continuous-session order semantics.
- Model auction freezes, cancellation restrictions, price limits, and random matching only where the selected security and session support them.
- Treat the Volatility Control Mechanism and security suspensions as execution-state changes, not missing zero-return bars.

HKEX announced phased board-lot framework changes beginning in 2026. Keep board lots point in time and verify implementation status instead of encoding a timeless list: <https://www.hkex.com.hk/News/Market-Communications/2026/260630news?sc_lang=en>.

## Model settlement and costs

- Model settled and unsettled stock and cash when the account or strategy depends on them.
- HKEX currently describes Exchange Trades and Clearing Agency Transactions as settling on T+2. Verify the rule and exceptions at the strategy's as-of date: <https://www.hkex.com.hk/services/settlement-and-depository/settlement?sc_lang=en>.
- Separate brokerage commission, trading fee, transaction levies, stamp duty where applicable, settlement charges, custody fees, and FX conversion.
- Keep all rates, minimum charges, rounding, exemptions, and effective dates configurable. Do not provide tax or legal conclusions.
- Apply the correct trading currency and the applicable exchange rate source for multi-counter or non-HKD transactions.

## Model short selling

- Permit a short sale only when the security was eligible on the trade date and the execution path supports covered short selling.
- Include stock-borrow availability, borrow cost, recall risk, corporate-action treatment, and buy-in or failed-delivery behavior.
- Apply the current HKEX tick rule and session-specific reference price through the execution adapter.
- Do not assume that selling first and buying back the same day makes an uncovered sale permissible.
- Use the point-in-time designated-securities list: <https://www.hkex.com.hk/Services/Trading/Securities/Securities-Lists/Designated-Securities-Eligible-for-Short-Selling?sc_lang=en>.
- Verify regulated short-selling requirements at <https://www.hkex.com.hk/services/trading/securities/overview/regulated-short-selling?sc_lang=en>.

## Separate Stock Connect

- State whether access is local SEHK trading or Northbound or Southbound Stock Connect.
- Use the route-specific eligible universe, trading calendar, holiday availability, currency, order types, price checks, quota behavior, settlement, and investor restrictions.
- Model the case where the home market is open but Stock Connect is unavailable.
- Keep eligibility additions and removals point in time.
- Do not reuse local Hong Kong short-selling, odd-lot, or settlement assumptions for Stock Connect without verification.

## Minimum evidence

Test at least:

- a leading-zero stock code and a symbol change;
- a full day, half day, lunch break, and random auction close;
- a severe-weather trading day and a broker-unavailable case;
- board-lot rounding plus an odd-lot residual;
- a board-lot change or share consolidation;
- a suspension, resumption, and delisting or privatisation;
- a dividend or rights issue on raw and adjusted data;
- T+2 cash and stock settlement;
- a designated and non-designated short-sale attempt;
- a dual-counter or Stock Connect eligibility transition;
- realistic fees, stamp duty assumptions, spreads, and market impact.
