# Spec: Notebook Cocktails – Alignment & Expansion

## Objective
Align eight notebook‑sourced cocktail recipes with their original specifications, resolve all `[TO VERIFY]` and `[ESTIMATED]` flags, and expand each into a complete cocktail specification.

## Design
- **Module**: `cocktail-notebook-sync` – synchronizes notebook entries with markdown recipes.
- **Data Flow**:
  1. Load notebook pages p.12 and p.18 (digital transcription available in the repo).
  2. For each listed recipe, parse the source entry to extract exact ingredient amounts and any flagged items.
  3. Resolve flags:
     - `[TO VERIFY]` – cross‑reference with known ingredient lists and the notebook context; if ambiguity remains, add a cook’s note indicating the decision.
     - `[ESTIMATED]` – infer quantities based on typical ratios for the cocktail style; document the estimation rationale.
  4. Update the corresponding markdown file under `drink/` with:
     - Precise ingredient list.
     - Full instruction block (build method, glassware, garnish, ice, dilution target).
     - Cook’s notes (≥2), variations (≥1), make‑ahead / batch guidance, scaling guidance.
  5. Ensure frontmatter consistency.
- **Key Interfaces**:
  - `resolveFlags(sourceEntry, markdownRecipe) -> markdownRecipe`.
  - `expandInstructions(recipe) -> recipe`.

## API contracts
Internal only; functions are documented for the implementer.

## Constraints
- All ingredient amounts must match the notebook values; any inferred values must be clearly noted.
- Frontmatter must contain:
  ```yaml
  cuisine: Cocktail
  dietary_tags: []
  tags: [cocktail]
  technique: [shaking, stirring, building]
  protein: [none]
  ```
- `date_modified` set to `2026-06-27`.
- No external data sources; rely on notebook transcription.

## Parallelizable
yes – each recipe can be handled independently.

## Depends on
None.
