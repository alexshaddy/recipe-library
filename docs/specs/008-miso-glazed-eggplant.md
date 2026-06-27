# Specification: Create Miso-Glazed Eggplant from Title-Only Addendum

**Ticket:** TICKET-008  
**Recipe:** `dinner/miso-glazed-eggplant.md`  
**Objective:** Create a complete miso-glazed eggplant recipe (nasu dengaku style) from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on standard nasu dengaku ratios (3:2:1 miso:mirin:sake) plus sugar to taste.

**For the Miso Glaze:**
- ¼ cup (60g) white miso (shiro miso) or awase (mixed) miso
- 2 tablespoons mirin
- 1 tablespoon sake
- 1 tablespoon granulated sugar (adjust to taste; can add up to 2 tbsp for sweeter glaze)
- 1 teaspoon rice vinegar (optional, for brightness)

**For the Eggplant:**
- 2 medium Japanese eggplants (or 1 large globe eggplant, about 1 lb total), stem removed
- 1 tablespoon neutral oil (such as grapeseed or canola) for brushing
- Flaky sea salt (for finishing, optional)
- Sesame seeds (toasted, for garnish, optional)
- Thinly sliced scallions (for garnish, optional)

**Equipment:**
- Baking sheet
- Broiler or grill
- Small saucepan
- Pastry brush
- Sharp knife for scoring

### 2. Instructions
Write 6–8 steps with bolded action titles, sensory cues, inline timing.

1. **Prepare the Eggplant** – Slice eggplants in half lengthwise. Score the flesh in a diamond pattern (about ½-inch deep cuts) being careful not to cut through the skin. Place cut-side up on a baking sheet.
2. **Salt and Rest** – Lightly sprinkle the scored flesh with salt and let sit for 10 minutes to draw out moisture and reduce bitterness. Pat dry with paper towels.
3. **Make the Miso Glaze** – In a small saucepan over low heat, whisk together miso, mirin, sake, and sugar until smooth and slightly warmed (do not boil). Remove from heat; stir in rice vinegar if using. The glaze should be thick but spreadable.
4. **First Broil** – Brush the scored eggplant flesh lightly with oil. Place under a preheated broiler or on a hot grill, cut-side down, and cook until the skin is charred and the flesh begins to soften, 4–5 minutes. Flip and broil another 2–3 minutes.
5. **Apply Glaze** – Remove eggplant from heat. Generously brush the miso glaze over the scored flesh, ensuring it seeps into the cuts.
6. **Second Broil** – Return to broiler or grill and cook until the glaze is bubbly, slightly caramelized, and the eggplant is tender throughout, 3–5 minutes. Watch closely to prevent burning.
7. **Rest and Garnish** – Transfer to a serving plate. Let rest 2 minutes. Sprinkle with sesame seeds and scallions if desired. Drizzle with any remaining glaze.
8. **Serve Immediately** – Enjoy while hot, with the glaze glossy and the eggplant creamy.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Scoring the eggplant allows the glaze to penetrate and ensures even cooking; be careful not to pierce the skin.
  2. Watch the glaze closely during the second broil—it can go from caramelized to burnt quickly due to sugar content.
- **Make-Ahead / Storage:**
  - Miso glaze can be made ahead and stored in an airtight container in the refrigerator for up to 1 week.
  - Grilled eggplant is best served immediately but can be kept at room temperature for up to 2 hours; reheat gently if needed.
- **Scaling:**
  - The glaze recipe scales linearly; maintain the 3:2:1 ratio of miso:mirin:sake and adjust sugar to taste.
  - For larger batches, use multiple baking sheets or grill in batches to avoid overcrowding.
- **Variations (2):**
  - **Spicy Miso:** Add 1 teaspoon chili paste (such as gochujang or sambal oelek) to the glaze.
  - **Miso-Tahini Blend:** Replace half the miso with tahini for a nutty twist; reduce salt accordingly.

### 4. Frontmatter & Metadata
- `title`: "Miso-Glazed Eggplant"
- `slug`: "miso-glazed-eggplant"
- `meal_type`: dinner
- `cuisine`: japanese
- `course`: main (or side? but ticket says dinner/main; we'll use main)
- `dietary_tags`: [vegetarian, vegan-option] (note: if using honey or non-vegan sugar, but we can keep vegan option by using sugar; miso, mirin, sake are typically vegan; check mirin sometimes contains sugar but still vegan; we'll keep both)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (includes salting)
- `cook_time`: "10 min [ACTIVE]" (broiling)
- `inactive_time`: "10 min [PASSIVE]" (salting rest)
- `total_time`: "35 min"
- `base_servings`: 2 (serves 2 as main, 4 as side)
- `serving_unit`: "halves"
- `scaling_notes`: "Glaze scales linearly; ensure eggplant pieces are in a single layer for even broiling."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on nasu dengaku technique."
- `difficulty`: "medium"
- `key_equipment`: ["broiler or grill", "baking sheet", "small saucepan", "pastry brush", "knife"]
- `tags`: ["recipe/dinner", "ingredient/eggplant", "ingredient/miso", "technique/glazing", "technique/broiling"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe follows nasu dengaku technique: scoring, broiling, glazing, rebrowning.
- Ensure ingredient list includes all required components.
- Verify instructions have 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/dinner/miso-glazed-eggplant.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes miso, mirin, sake, sugar, eggplant, oil.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.