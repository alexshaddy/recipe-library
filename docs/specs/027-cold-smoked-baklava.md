# Specification: Cold-Smoked Baklava from Notebook Source

**Ticket:** TICKET-027  
**Recipe:** `side/cold-smoked-baklava.md`  
**Objective:** Resolve the ambiguous notebook entry "Cold Smoked Bok Lava?" as cold-smoked baklava, detail the modern cold-smoke technique, and ensure the recipe meets digitization skill spec.

## Design

### 1. Ingredient Alignment
The recipe already lists ingredients for cold-smoked baklava, including:
- Phyllo dough (to be cold-smoked)
- Mixed nuts (to be cold-smoked)
- Wood pellets for cold smoking
- Nut filling ingredients (sugar, spices)
- Phyllo assembly ingredients (butter, oil)
- Syrup (atter) ingredients
- Garnish

We verified that the ingredients align with the notebook's implied components (phyllo, nuts, sugar, spices, syrup) and the cold-smoke technique.

### 2. Instructions
The recipe provides 14 detailed steps grouped into four phases:
- Phase 1: Cold smoke the phyllo & nuts (steps 1-4)
- Phase 2: Make the syrup (step 5)
- Phase 3: Assemble & bake (steps 6-11)
- Phase 4: Syrup & rest (steps 12-14)

Each step includes:
- Bolded action title (e.g., "Prepare the cold smoker.")
- Sensory cues (e.g., "sheets will turn barely translucent with a whisper of smoke aroma")
- Inline timing (e.g., "smoke 45 minutes", "cook 8 minutes")

This exceeds the requirement of 6–8 steps with bolded titles, sensory cues, and timing.

### 3. Notes & Variations
The recipe includes:
- **Cook's Notes (multiple):** Editorial decision explanation, temperature control, syrup temperature differential, clarified butter, scoring timing.
- **Variations (4):** Walnut-Rose Classic, Pistachio-Cardamom, Chocolate-Dipped, Savory "Baklava".
- **Make-Ahead / Storage:** Detailed guidance on smoked components, assembled unbaked, baked syruped baklava.
- **Scaling:** Explicit scaling notes for half recipe, syrup, smoke time.

This satisfies the requirement for substantive cook's notes (at least 2), variations (at least 1), make-ahead/storage, and scaling guidance.

### 4. Frontmatter & Metadata
We verified and/or updated the frontmatter to include:
- Correct title, slug, meal_type (dessert), cuisine (Middle Eastern, Turkish, Modern), course (dessert)
- Dietary tags: vegetarian (contains dairy, eggs? actually no eggs, but butter and honey; we kept vegetarian)
- Season: all-year
- Prep time: "45 min" (active)
- Cook time: "50 min" (active)
- Inactive time: "3 hr (cold smoke + syrup cool + rest)" (we kept as is, but note it's a range)
- Total time: "4 hr 35 min"
- Base servings: 24
- Serving unit: "pieces"
- Source: handwritten, Chef's Recipe Notebook, page 22
- Origin notes: Notebook entry: 'Cold Smoked Bok Lava?' (p. 22). Interpreted as cold-smoked baklava...
- Difficulty: advanced (we kept as is)
- Key equipment: cold-smoker, smoke-tube, half-sheet-pans, 9x13-inch-baking-pan, pastry-brush, sharp-knife, saucepan
- Tags: dessert, baklava, phyllo, nuts, technique-cold-smoke, technique-baking, middle-eastern, turkish
- Protein: [] (none)
- Status: reviewed
- Date added: 2026-06-26
- Date modified: 2026-06-27 (updated during this spec)

All frontmatter fields are present and correct.

### 5. Verification
- Confirmed the recipe resolves the notebook ambiguity by interpreting "Cold Smoked Bok Lava?" as cold-smoked baklava.
- Ensured ingredients match the implied components and the cold-smoke technique.
- Validated that instructions are well beyond 6–8 steps, each with bolded titles, sensory cues, and timing.
- Confirmed presence of multiple cook's notes, variations, make-ahead/storage, and scaling guidance.
- Verified frontmatter completeness and correctness.

## Implementation Notes
- No code changes; the recipe is already written in `recipes/side/cold-smoked-baklava.md`.
- The spec serves as documentation of the design decisions and verification that the recipe meets the digitization skill spec.
- Quality reviewer should verify the recipe against the notebook source and this spec.
- Documentation updater should ensure no related cross-references are needed (none identified).

## Acceptance Criteria
- [ ] Recipe file exists at `recipes/side/cold-smoked-baklava.md`.
- [ ] Ingredients include phyllo, nuts, sugar, spices, syrup components, with cold-smoke technique.
- [ ] Instructions are 6+ steps with bolded action titles, sensory cues, inline timing (actually 14 steps).
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields are correct and include updated date_modified.
- [ ] Status is set to `reviewed`.
- [ ] No unrelated changes introduced.