# Specification: Create Miso Eggplant Dip from Title-Only Addendum

**Ticket:** TICKET-013  
**Recipe:** `condiment/miso-eggplant-dip.md`  
**Objective:** Create a complete miso eggplant dip recipe (nasu miso style) from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on roasted eggplant blended with miso glaze.

**For the Eggplant:**
- 2 medium Japanese eggplants (or 1 large globe eggplant, about 1 lb total), stem removed
- 1 tablespoon neutral oil (such as grapeseed or canola)
- Pinch of salt

**For the Miso Blend:**
- 2 tablespoons white miso (shiro miso) or awase (mixed) miso
- 1 tablespoon mirin
- 1 tablespoon sake
- 1 teaspoon sugar (adjust to taste)
- 1 teaspoon rice vinegar (optional, for brightness)
- 1 teaspoon sesame oil
- 1 clove garlic, minced (optional)
- 1 teaspoon grated fresh ginger (optional)

**For Optional Creaminess (choose one to adjust texture):**
- 2 tablespoons tahini
- OR 2 tablespoons plain Greek yogurt (for non-vegan)
- OR 2 tablespoons silken tofu (for vegan)

**For Garnish (optional):**
- 1 teaspoon toasted sesame seeds
- 2 thin slices scallion (green part only), finely sliced
- Chili flakes or shaved nori for topping

**Equipment:**
- Baking sheet
- Parchment paper
- Knife
- Food processor or blender
- Spatula
- Airtight container for storage

### 2. Instructions
Write 6–8 steps with bolded action titles, sensory cues, inline timing.

1. **Prep the Eggplant** – Preheat oven to 425°F (220°C). Line a baking sheet with parchment. Slice the eggplants in half lengthwise. Score the flesh in a crosshatch pattern, being careful not to cut through the skin. Brush the cut side with oil and sprinkle with a pinch of salt. Place cut-side down on the sheet.
2. **Roast Until Collapsed** – Roast for 35–45 minutes, until the eggplant is very soft, collapsed, and the skin is wrinkled and slightly charred at the edges. The flesh should scoop out easily. Remove from oven and let cool for 10 minutes.
3. **Scoop the Flesh** – Once cool enough to handle, scoop out the softened eggplant flesh into a food processor, discarding the skins. You should have about 1 cup of packed pulp.
4. **Make the Miso Blend** – In a small bowl, whisk together miso, mirin, sake, sugar, rice vinegar (if using), sesame oil, garlic, and ginger until smooth. Set aside.
5. **Blend the Dip** – Add the miso blend to the eggplant in the food processor. Pulse until smooth, scraping down sides as needed. If the dip is too thick, add water a teaspoon at a time or incorporate one of the optional creaminess agents (tahini, yogurt, or tofu) until desired consistency is reached.
6. **Taste and Adjust** – Give the dip a taste. Adjust salt, lemon juice (or extra vinegar), or miso as needed. For more brightness, add a squeeze of lemon juice. For more umami, add a bit more miso.
7. **Chill for Flavor Development** – Transfer the dip to a serving bowl, cover, and refrigerate for at least 30 minutes (or up to 2 hours) to allow flavors to meld.
8. **Garnish and Serve** – Before serving, drizzle with a little sesame oil, sprinkle with toasted sesame seeds and scallions, and add a pinch of chili flakes if desired. Serve with pita chips, vegetable crudités, or as a spread for sandwiches.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Roasting the eggplant until fully collapsed concentrates its flavor and removes excess water, preventing a watery dip.
  2. Adding tahini or yogurt creates a creamier texture and balances the umami richness of the miso.
- **Make-Ahead / Storage:**
  - The dip keeps refrigerated in an airtight container for up to 4 days.
  - For longer storage, freeze in a sealed container for up to 1 month; thaw in refrigerator and stir well before serving (may need a splash of water).
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 2 parts eggplant to 1 part miso blend by volume.
  - For larger batches, use a larger baking sheet and roast in batches to avoid steaming.
- **Variations (1):**
  - **Smoky Miso Eggplant Dip:** Add ½ teaspoon smoked paprika or a few drops of liquid smoke to the miso blend for a deeper, grilled flavor.

### 4. Frontmatter & Metadata
- `title`: "Miso Eggplant Dip"
- `slug`: "miso-eggplant-dip"
- `meal_type`: condiment
- `cuisine`: japanese
- `course`: condiment
- `dietary_tags`: [vegetarian, vegan, gluten-free-option] (note: if using yogurt, not vegan; we'll note option)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (prepping eggplant, mixing miso)
- `cook_time`: "45 min [ACTIVE]" (roasting)
- `inactive_time`: "10 min [PASSIVE]" (cooling) + "30 min [PASSIVE]" (chilling) – we'll combine as "40 min [PASSIVE]"
- `total_time`: "1 hr 40 min"
- `base_servings`: 1 cup (about 8 servings of 2 tbsp)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Scales linearly; ensure adequate baking sheet space for even roasting."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on nasu miso (miso eggplant) technique."
- `difficulty`: "medium"
- `key_equipment`: ["oven", "baking sheet", "parchment paper", "knife", "food processor", "bowl"]
- `tags`: ["recipe/condiment", "ingredient/eggplant", "ingredient/miso", "technique/roasting", "technique/blending"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe includes eggplant, miso, mirin, sake, sugar, sesame oil.
- Ensure instructions are 6–8 steps with bolded titles, sensory cues, timing.
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