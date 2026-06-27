# Specification: Create Miso Eggplant Dip from Title-Only Addendum

**Ticket:** TICKET-013  
**Recipe:** `condiment/miso-eggplant-dip.md`  
**Objective:** Create a complete miso eggplant dip recipe (nasu miso style) from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on miso-glazed eggplant turned into a dip.

**For the Eggplant Base:**
- 2 medium Japanese eggplants (or 1 large globe eggplant, about 1 lb total), stem removed
- 1 tablespoon neutral oil (such as grapeseed or canola)
- Pinch of salt

**For the Miso Glaze (to be mixed in):**
- 2 tablespoons white miso (shiro miso) or awase (mixed) miso
- 1 tablespoon mirin
- 1 tablespoon sake
- 1 teaspoon sugar (adjust to taste)
- 1 teaspoon rice vinegar (optional, for brightness)
- 1 teaspoon sesame oil
- 1 clove garlic, minced (optional)
- 1 teaspoon grated fresh ginger (optional)

**For Optional Creaminess (choose one):**
- 2 tablespoons tahini
- OR 2 tablespoons Greek yogurt (for non-vegan)
- OR 2 tablespoons silken tofu (for vegan)

**For Garnish (optional):**
- 1 teaspoon toasted sesame seeds
- 2 thin slices scallion (green part only), finely sliced
- Chili flakes or shichimi togarashi for heat

**Equipment:**
- Baking sheet
- Broiler or grill
- Food processor or blender
- Knife
- Spoon

### 2. Instructions
Write 6–8 steps with bolded action titles, sensory cues, inline timing.

1. **Prepare the Eggplant** – Preheat broiler (or grill) to high. Slice eggplants in half lengthwise. Score the flesh in a crosshatch pattern (about ½-inch deep cuts) being careful not to cut through the skin. Place cut-side up on a baking sheet. Brush the scored flesh lightly with oil and sprinkle with a pinch of salt.
2. **Roast the Eggplant** – Place under the broiler, about 4 inches from the heat source. Cook until the skin is charred and the flesh is completely soft and collapsed, 12–15 minutes, flipping halfway through if needed. The eggplant should smell smoky and feel very tender when pierced with a knife.
3. **Cool and Scoop** – Remove from the broiler and let cool for 5 minutes. Scoop out the softened flesh into a food processor, discarding the skins. You should have about 1 cup of packed eggplant pulp.
4. **Make the Miso Blend** – In a small bowl, whisk together miso, mirin, sake, sugar, rice vinegar (if using), sesame oil, garlic, and ginger until smooth. Taste and adjust sweetness or saltiness as needed.
5. **Blend the Dip** – Add the miso blend to the eggplant pulp in the food processor. Pulse until smooth and creamy, about 30 seconds. If using, add tahini (or yogurt/tofu) and pulse again until fully incorporated. The dip should be thick but spreadable.
6. **Taste and Adjust** – Give the dip a final taste. If too thick, add a teaspoon of water or lemon juice. If too mild, add a bit more miso or a pinch of salt.
7. **Chill and Serve** – Transfer to a serving bowl. Drizzle with a little sesame oil and sprinkle with sesame seeds and scallions if desired. Serve at room temperature or chilled with vegetables, crackers, or pita.
8. **Store** – Cover and refrigerate for up to 4 days. Bring to room temperature before serving and stir well.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Scoring the eggplant allows heat to penetrate evenly and prevents bursting; it also creates more surface area for the miso to cling to.
  2. The dip can be served warm or cold; chilling allows the flavors to meld and the texture to firm up slightly.
- **Make-Ahead / Storage:**
  - The roasted eggplant can be prepared ahead and stored in the refrigerator for up to 2 days before blending.
  - The finished dip keeps refrigerated in an airtight container for up to 4 days; stir before serving.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of about 2 tbsp miso per cup of eggplant pulp.
  - For larger batches, roast eggplants on multiple sheets or in batches to avoid steaming.
- **Variations (2):**
  - **Spicy Miso Eggplant Dip:** Add 1 teaspoon chili garlic sauce or sriracha to the miso blend.
  - **Miso-Tahini Lemon Dip:** Increase tahini to 3 tablespoons and add 1 tablespoon lemon juice for a tangier, creamier dip.

### 4. Frontmatter & Metadata
- `title`: "Miso Eggplant Dip"
- `slug`: "miso-eggplant-dip"
- `meal_type`: condiment
- `cuisine`: japanese
- `course`: condiment
- `dietary_tags`: [vegetarian, vegan, gluten-free-option] (note: if using yogurt, not vegan; we'll keep option)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (includes slicing and salting)
- `cook_time`: "15 min [ACTIVE]" (broiling)
- `inactive_time`: "5 min [PASSIVE]" (cooling)
- `total_time`: "35 min"
- `base_servings`: 1 cup (about 8 servings of 2 tbsp)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Scales linearly; ensure eggplant is fully collapsed for smooth blending."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on nasu miso technique."
- `difficulty`: "medium"
- `key_equipment`: ["broiler or grill", "baking sheet", "food processor", "knife"]
- `tags`: ["recipe/condiment", "ingredient/eggplant", "ingredient/miso", "technique/roasting", "technique/blending"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe follows technique: roast eggplant until collapsed, blend with miso.
- Ensure ingredient list includes eggplant, miso, mirin, sake, sugar, sesame oil.
- Verify instructions have 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/condiment/miso-eggplant-dip.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes eggplant, miso, mirin, sake, sugar, sesame oil.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.