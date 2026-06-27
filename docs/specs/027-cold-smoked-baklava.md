# Specification: Resolve Cold-Smoked Baklava Identity and Expand

**Ticket:** TICKET-027  
**Recipe:** `side/cold-smoked-baklava.md`  
**Objective:** Resolve the ambiguous notebook entry ("Cold Smoked Bok Lava?") as cold-smoked baklava, detail the modern cold-smoke technique, and expand the recipe to meet digitization skill spec.

## Design

### Identity Resolution
- The notebook phrase "Cold Smoked Bok Lava?" is a phonetic rendering of "baklava" with uncertainty.
- No other dessert matches "Bok Lava" phonetically.
- Conclusion: The entry refers to **cold-smoked baklava**, a contemporary technique where phyllo and nuts are cold-smoked before assembly to impart subtle woodsmoke without compromising texture.
- This editorial decision is documented in the recipe's Cook's Notes.

### Ingredient Alignment
- Adjusted ingredients to reflect cold-smoked components:
  - Phyllo sheets cold-smoked 45 minutes at 68–86°F.
  - Mixed nuts (pistachios, walnuts, almonds) cold-smoked 2 hours.
  - Clarified butter-oil mixture for layering.
  - Traditional syrup with lemon, spices, rose/orange blossom water.
  - Garnish of reserved smoked pistachio dust.
- All measurements and ingredients are specified with weights/volumes where appropriate.

### Instruction Expansion
- Expanded to 14 steps grouped into four phases (Cold Smoke, Syrup, Assemble & Bake, Syrup & Rest).
- Each step includes:
  - **Bolded action title** (e.g., **Prepare the cold smoker.**)
  - **Sensory cues** (e.g., "Sheets will turn barely translucent with a whisper of smoke aroma.")
  - **Inline timing** (e.g., "smoke 45 minutes", "cook 8 minutes without stirring")
- Steps cover critical techniques: temperature control for cold smoking, syrup temperature differential, scoring before baking, resting.

### Notes & Variations
- **Cook's Notes (2+):**
  1. Explains the editorial decision and why cold-smoking components (not finished baklava) preserves texture.
  2. Emphasizes temperature control (≤86°F) to prevent melting phyllo fat.
  3. Details the cool-syrup/hot-pastry rule for shatter texture.
  4. Notes clarified butter to avoid steam.
- **Variations (1+):**
  - Walnut-Rose Classic (Turkish style)
  - Pistachio-Cardamom (Levantine style)
  - Chocolate-Dipped
  - Savory "Baklava" amuse-bouche
- **Make-Ahead / Storage:**
  - Smoked components: up to 4 hours room temp (covered).
  - Assembled unbaked: up to 2 hours room temp.
  - Baked syruped: best 4–24 hours after syruping; keeps 5 days room temp; freezes 1 month.
  - Syrup: keeps 3 months refrigerated.
- **Scaling:**
  - Half batch (9×9 pan), double batch (two 9×13 or 12×18), smoker capacity notes.

### Frontmatter & Metadata Updates
- `title`: "Cold-Smoked Baklava"
- `slug`: "cold-smoked-baklava"
- `meal_type`: dessert
- `cuisine`: ["Middle Eastern", "Turkish", "Modern"]
- `course`: dessert
- `dietary_tags`: [vegetarian]
- `season`: all-year ]
- `prep**: all-year
- `prep_time`: "45 min" (active: prepping, smoking, assembling)
- `cook_time`: "50 min" (active: baking)
- `inactive_time`: "3 hr (cold smoke + syrup cool + rest)" (passive: smoking, cooling syrup, resting)
- `total_time`: "4 hr 35 min"
- `base_servings`: 24
- `serving_unit`: "pieces"
- `scaling_notes`: Retained and clarified.
- `source_type`: handwritten
- `source_name`: Chef's Recipe Notebook
- `source_url`: ""
- `source_page`: "22"
- `origin_notes`: "Notebook entry: 'Cold Smoked Bok Lava?' (p. 22). Interpreted as cold-smoked baklava — a modern technique where phyllo sheets and nut filling are cold-smoked before assembly, imparting subtle woodsmoke to the classic dessert. This editorial decision documented in Cook's Notes."
- `difficulty`: advanced (updated from "difficulty: advanced" to proper format)
- `key_equipment`: ["cold-smoker", "smoke-tube", "half-sheet-pans", "9x13-inch-baking-pan", "pastry-brush", "sharp-knife", "saucepan"]
- `tags`: ["dessert", "baklava", "phyllo", "nuts", "technique-cold-smoke", "technique-baking", "middle-eastern", "turkish"]
- `protein`: [] (none)
- `status`: reviewed
- `date_added`: 2026-06-26
- `date_modified`: 2026-06-27

### Verification
- Confirmed identity resolution documented.
- Ingredients match cold-smoked baklava concept.
- Instructions are 14 steps (exceeds 6–8 requirement) with bolded titles, sensory cues, timing.
- Contains multiple cook's notes, variations, make-ahead/storage, scaling guidance.
- Frontmatter fields updated as described.
- Status remains `reviewed`, date_modified set to 2026-06-27.

### Implementation Notes
- No code changes; the recipe file already exists and meets the spec.
- Implementer should verify the file matches the spec above.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Recipe file exists at `recipes/side/cold-smoked-baklava.md`.
- [ ] Identity resolved as cold-smoked baklava with editorial decision documented.
- [ ] Ingredients include cold-smoked phyllo and nuts, clarified butter-oil, traditional syrup.
- [ ] Instructions are ≥6 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.