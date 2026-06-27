# Spec: Guest-Check Cocktails – Medium UNCLEAR Resolution

## Objective
Resolve the 1‑2 `[UNCLEAR]` ingredient placeholders for six medium‑unclear guest‑check cocktail recipes, expand each to a complete cocktail spec, and record editorial decisions.

## Design
- **Module**: `cocktail-digitization` (same as 034) – reuse the `resolveUnclear` and `expandInstructions` utilities.
- **Data Flow**:
  1. Input images (`assets/loose_notes_scans/brw849e563cc961_000402.jpg`‑`000407.jpg`).
  2. OCR → raw text.
  3. Apply heuristic resolution focusing on single‑ingredient ambiguities (herb, citrus, bitters, etc.).
  4. Produce updated markdown files under `drink/`.
- **Key Interfaces**:
  - `resolveUnclearSingle(recipe)` – targets 1‑2 missing items.
  - `expandInstructions` – as defined in 034.

## API contracts
Internal only; see module documentation.

## Constraints
- Must not introduce ingredients outside the era/style of the Mockingbird Bar.
- Frontmatter must contain:
  ```yaml
  cuisine: Cocktail
  dietary_tags: []
  tags: [cocktail, old-fashioned, punch, mug]
  technique: [stirring, building, batching]
  protein: [none]
  ```
- Update `date_modified` to `2026-06-27`.

## Parallelizable
yes – recipes are independent.

## Depends on
None.
