# Spec: Guest-Check Cocktails – Thin Instruction Expansion

## Objective
Take four guest‑check cocktail recipes that already have complete ingredient lists but only thin instructions, and expand them into full, publish‑ready cocktail specifications.

## Design
- **Module**: `cocktail-enhancement` – focuses on enriching existing recipes.
- **Data Flow**:
  1. Load each target markdown file (`drink/breezy-beach-collins.md`, `drink/life-preserver.md`, `drink/road-to-nowhere.md`, `drink/propane-and-propane-accessories.md`).
  2. Parse frontmatter and ingredient list.
  3. Generate detailed instruction block:
     - Build method (shake, stir, build).
     - Glassware selection.
     - Garnish recommendation.
     - Ice type and dilution target.
     - Cook’s notes (≥2) and variations (≥1).
     - Make‑ahead / batch guidance and scaling notes.
  4. Write back updated markdown.
- **Interfaces**:
  - `expandThinInstructions(recipe: Markdown): Markdown`.

## API contracts
Internal utility; no external API.

## Constraints
- Preserve any existing custom tags.
- Frontmatter must include:
  ```yaml
  cuisine: Cocktail
  dietary_tags: []
  tags: [cocktail]
  technique: [shaking, stirring, building]
  protein: [none]
  ```
- Set `date_modified` to `2026-06-27`.

## Parallelizable
yes – each recipe can be processed separately.

## Depends on
None.
