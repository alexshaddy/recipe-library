# Spec: Guest-Check Cocktails – High UNCLEAR Resolution

## Objective
Resolve all `[UNCLEAR]` ingredient placeholders for the four high‑unclear guest‑check cocktail recipes, expand each recipe into a full cocktail specification, and document editorial reasoning.

## Design
- **Module**: `cocktail-digitization` – responsible for converting scanned handwritten notes into structured markdown recipes.
- **Data Flow**:
  1. Input: Scanned images (`assets/loose_notes_scans/brw849e563cc961_000402.jpg`‑`000407.jpg`).
  2. OCR → Text extraction (existing pipeline).
  3. **Resolution Engine** (architectural component) applies heuristics:
     - Match ingredient names against known cocktail lexicon.
     - Use cocktail name, era (Mockingbird Bar), and typical construction ratios to infer missing parts.
  4. Output: Updated markdown files under `drink/` with full frontmatter and expanded instructions.
- **Interfaces**:
  - `resolveUnclear(recipe: Markdown): Markdown` – returns a recipe with `[UNCLEAR]` replaced and notes added.
  - `expandInstructions(recipe: Markdown): Markdown` – adds build method, glassware, garnish, ice, dilution target, notes, variations, batch guidance, scaling.

## API contracts
*No public API; internal functions are documented for implementer reference.*

## Constraints
- No external data sources may be queried; rely solely on existing cocktail ingredient database.
- All changes must preserve original recipe IDs and file paths.
- Frontmatter must include:
  ```yaml
  cuisine: Cocktail
  dietary_tags: []
  tags: [cocktail, highball, collins, punch]
  technique: [building, shaking, stirring]
  protein: [none]
  ```
- `date_modified` set to `2026-06-27`.

## Parallelizable
yes – each recipe can be processed independently.

## Depends on
None.
