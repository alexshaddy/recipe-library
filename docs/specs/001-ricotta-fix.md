# Technical Spec: Fix Ricotta Ingredient Mismatch

**Ticket:** TICKET-001  
**Status:** Specced  
**Assignee:** Architect  
**Dependencies:** None  
**Parallelizable:** Yes  

## Objective
Correct the ricotta recipe to match the notebook source (½ gallon 2% milk, ½ cup lemon juice, 1 tsp salt) and expand instructions/notes to meet digitization skill spec.

## Design

### Ingredient Changes
- Replace `1 gallon milk` + `1 cup cream` + `¼ cup acid` with:
  - `½ gallon (2 quarts) milk`
  - `½ cup lemon juice (freshly squeezed)`
  - `1 teaspoon salt`
- Remove cream entirely; acid is exclusively lemon juice per notebook.

### Instruction Revision
Expand from 3 steps to 7 steps, each with:
- **Bolded action title** (e.g., **Heat the Milk**)
- **Sensory cues** (visual, tactile, temperature)
- **Inline timing** (active and passive durations)

Steps:
1. Heat the Milk – warm to steaming, small bubbles, 8–10 min.
2. Add Acid – remove from heat, stir in lemon juice, curds form immediately, rest 5 min.
3. Salt the Curds – sprinkle salt, stir gently.
4. Line the Strainer – sieve lined with cheesecloth over bowl.
5. Transfer Curds – slotted spoon curds into sieve, whey drains.
6. Drain to Desired Consistency – twist cheesecloth, 10–15 min (soft) to 1 hr (firm).
7. Use or Store – transfer to container, use immediately or refrigerate.

### Notes & Variations Expansion
- **Cook's Notes (2):**
  1. Notebook indicates fresh-cheese method despite ambiguous acid.
  2. Fresh lemon juice preferred for clean acidity; if using vinegar, choose mild variety.
- **Make-Ahead / Storage:**
  - Refrigerate airtight ≤5 days.
  - Freeze portions ≤2 months; thaw in fridge.
  - Stir separated whey back in or drain for thicker texture.
- **Scaling:**
  - Linear scaling; maintain 4:1 milk-to-acid ratio by volume.
  - Adjust salt proportionally.
  - Use larger pot for big batches to avoid scorching.
- **Variations (2):**
  - **Herbed Ricotta:** Stir in 1 tbsp fresh herbs + pepper after draining.
  - **Sweet Ricotta:** Mix in 1–2 tbsp honey/maple syrup + cinnamon.

### Frontmatter Updates
- `prep_time`: "15 min [ESTIMATED]" (active)
- `cook_time`: "0 min [ESTIMATED]" (no separate cook step)
- `inactive_time`: "40 min [ESTIMATED]" (rest + drain)
- `total_time`: "55 min [ESTIMATED]"
- `date_modified`: "2026-06-27"
- `tags`: add `technique/fresh-cheese`
- `status`: remains `reviewed` (post-edit verification)

### Constraints
- Must preserve notebook provenance note.
- Must not introduce estimated amounts; all quantities precise.
- Must maintain existing metadata structure (cuisine, dietary tags, etc.).
- Must keep recipe under 1 batch scaling note simple.

### Implementation Notes
- No code changes required; pure content edit.
- Implementer should verify frontmatter fields after editing.
- Quality should verify notebook compliance and spec adherence.
- Docs should update any related cross-references if needed (none identified).

### Acceptance Criteria
- [ ] Ingredients match notebook exactly.
- [ ] Instructions are 5–8 steps with bolded titles, sensory cues, timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] No estimated amounts remain (except time estimates).
- [ ] Status remains `reviewed`; date_modified updated.