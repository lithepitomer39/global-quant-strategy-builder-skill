# Global market foundations

Use this reference when a strategy crosses venues, countries, currencies, or data domains.

## Build a market profile

Create one profile per venue and asset class. Record:

| Dimension | Questions to resolve |
| --- | --- |
| Identity | Which exchange, MIC, symbol namespace, share class, and listing currency identify the instrument? |
| Calendar | Which holidays, half-days, auctions, breaks, and daylight-saving rules apply? |
| Trading | Which sessions and order types are eligible, and what are the tick and lot rules? |
| Data | Are timestamps event time, exchange time, or receipt time? Are bars start- or end-labeled? |
| Lifecycle | How are symbol changes, listings, delistings, mergers, distributions, and contract expiries represented? |
| Funding | What base currency, FX conversion, interest, borrow, margin, or financing applies? |
| Regulation | Which current venue, broker, account, and jurisdiction constraints affect the strategy? |

Do not assume that two instruments with the same ticker, local time, or currency are interchangeable. Preserve a stable internal identifier and map vendor symbols at the boundary.

## Align time correctly

- Store event timestamps with timezone information and retain the original venue timezone.
- Use an exchange calendar rather than weekdays to generate sessions.
- Model daylight-saving transitions by named timezone, not by a fixed UTC offset.
- Define how asynchronous closes are joined. Never let a later-closing market leak into an earlier decision timestamp.
- Decide whether daily data becomes available at the official close, after an auction, or after vendor publication.
- Treat unscheduled closures and data outages as explicit missing sessions, not zero returns.

## Preserve point-in-time truth

- Construct universes from membership known at each decision date.
- Include delisted instruments and terminal returns when the data supports them.
- Lag fundamentals, estimates, classifications, and corporate actions by their actual availability time.
- Keep raw prices for executable levels and adjusted series for research calculations when appropriate.
- Apply splits, cash dividends, stock dividends, rights, spin-offs, and symbol changes consistently across prices, positions, and orders.
- Record vendor revision and restatement behavior for fundamental or macro data.

## Handle currencies and capital

- Declare the portfolio base currency.
- Track local-market exposure, cash balances, FX translation, and FX trading separately.
- Use timestamp-aligned FX rates; do not translate all history with a current rate.
- Include conversion spread, financing, withholding assumptions, and non-trading days when material.
- Distinguish economic P&L from base-currency translation P&L.

## Make mutable rules configurable

Regulations, exchange schedules, broker margin, and account restrictions change. Keep rule values in configuration or broker adapters, record the as-of date, and verify primary sources before claiming compliance. Do not encode legal conclusions in signal logic.

## Global validation cases

Include focused cases for:

- a daylight-saving transition where markets move on different dates;
- a local holiday while another market remains open;
- a corporate action and symbol change;
- a delisting or universe removal;
- an FX move with unchanged local price;
- an order rounded to venue tick and lot rules;
- an asynchronous close that could otherwise introduce look-ahead.
