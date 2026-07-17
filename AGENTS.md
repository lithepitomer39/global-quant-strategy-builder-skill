# Repository guidance

## Scope

Maintain an independently written, market-neutral core with first-class global, US-market, and Hong Kong-market references. Do not copy source text or files from the acknowledged inspiration repository.

## Content rules

- Keep `README.md` Traditional Chinese-first and keep `README_EN.md` semantically synchronized.
- Keep `skills/global-quant-strategy-builder/SKILL.md` under 500 lines and focused on stable procedure.
- Use imperative language in the skill body.
- Put asset-, market-, framework-, and validation-specific detail in one-level `references/` files.
- Link every reference directly from `SKILL.md` and avoid reference-to-reference routing.
- Prefer configurable, as-of-dated rules over hard-coded regulatory or broker limits.
- Do not present backtests as guarantees or enable live trading by default.
- Never add credentials, account identifiers, proprietary datasets, or copied licensed material.

## Validation

Run `python scripts/validate_skill.py` after every content or structure change. Keep the validator dependency-free and compatible with Python 3.9 or newer.
