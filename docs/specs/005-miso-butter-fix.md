# Specification: Fix Miso Butter Ingredient Mismatch

**Ticket:** TICKET-005  
**Recipe:** `condiment/miso-butter.md`  
**Objective:** Align the miso butter recipe with the notebook source (white miso, unsalted butter, mirin, honey) and expand instructions, notes, and variations per digitization skill spec.

## Changes

### 1. Ingredients
Replace existing ingredient list with notebook-accurate data:
- ½ cup (1 stick / 113g) unsalted butter, softened to room temperature
- 2 tablespoons white miso (shiro miso)
- 1 tablespoon mirin
- 1 tablespoon honey

Remove optional scallions, sesame seeds, black pepper. Keep the recipe simple with only these four ingredients.

### 2. Instructions
Expand to 5–8 steps with bolded action titles, sensory cues, inline timing.

1. **Soften the Butter** – Leave the unsalted butter at room temperature for 30–45 minutes until soft and pliable but not melted. It should yield to gentle pressure and leave a faint indentation.
2. **Combine Butter and Miso** – In a mixing bowl, add the softened butter and white miso. Using a spatula, mash and stir until the mixture is uniform and pale yellow, about 1 minute.
3. **Incorporate Mirin and Honey** – Add the mirin and honey to the butter-miso mixture. Continue to mix until fully incorporated, smooth, and glossy, about 1–2 minutes. The mixture should be soft and spreadable.
4. **Taste and Adjust** – Give the butter a quick taste; if a sweeter profile is desired, add a bit more honey (up to 1 extra tablespoon). If more umami is desired, add a bit more miso (up to 1 extra tablespoon). Mix well after any adjustment.
5. **Shape for Storage** – Place a sheet of parchment paper or plastic wrap on a flat surface. Scoop the mixture onto the center and shape into a log about 1.5 inches in diameter. Roll tightly, twisting the ends to seal.
6. **Chill** – Refrigerate the butter log for at least 1 hour to firm up, or until ready to use.
7. **Slice and Serve** – Unwrap and slice off rounds as needed. Use to top grilled corn, steak, bread, vegetables, or melt into sauces.
8. **Optional: Freeze for Longer Storage** – Wrap the butter log tightly and freeze for up to 3 months. Thaw in the refrigerator before use.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Using room-temperature butter ensures smooth incorporation of the miso without lumps or separation.
  2. Mirin adds a subtle sweetness and depth of flavor that complements the miso; honey adds floral sweetness and helps balance the saltiness.
- **Make-Ahead / Storage:**
  - Miso butter keeps refrigerated in an airtight container for up to 2 weeks.
  - For longer storage, freeze the log wrapped tightly in plastic wrap and then foil for up to 3 months; thaw in the refrigerator before slicing.
  - Always use a clean utensil when scooping to prevent contamination.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 4 parts butter to 1 part miso by volume, and equal parts mirin and honey to miso (e.g., for 2 cups butter, use ½ cup miso, ¼ cup mirin, ¼ cup honey).
  - For a softer spread, increase butter slightly; for a firmer sliceable log, reduce butter or chill longer.
- **Variations (1):**
  - **Citrus Miso Butter:** Add 1 teaspoon finely grated yuzu or lemon zest along with the mirin and honey for a bright citrus note.

### 4. Frontmatter & Metadata
- Update `prep_time`: "10 min [ACTIVE]" (softening and mixing)
- `cook_time`: "0 min [ACTIVE]" (no cooking)
- `inactive_time`: "60 min [PASSIVE]" (chilling)
- `total_time`: "70 min"
- `base_servings`: 1 stick (about 16 servings of 1 tbsp each)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Butter, miso, mirin, and honey scale linearly; keep butter at room temperature for easy mixing."
- `date_modified`: "2026-06-27"
- `status`: "reviewed"
- Ensure tags include `technique/compound-butter`.
- Verify existing fields (cuisine: japanese-fusion, dietary_tags: vegetarian) remain accurate.

### 5. Verification
- Confirm ingredient list matches notebook exactly (unsalted butter, white miso, mirin, honey).
- Ensure instructions are 5–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

## Acceptance Criteria
- [ ] Ingredients list matches notebook (unsalted butter, white miso, mirin, honey).
- [ ] Instructions are 5–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.