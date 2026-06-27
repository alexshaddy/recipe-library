# Specification: Create Miso Glaze from Title-Only Addendum

**Ticket:** TICKET-015  
**Recipe:** `condiment/miso-glaze.md`  
**Objective:** Create a complete miso glaze recipe from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on a versatile miso glaze (white miso, mirin, sake, sugar, rice vinegar, sesame oil).

**For the Miso Glaze:**
- ¼ cup (60g) white miso (shiro miso) or awase (mixed) miso
- 2 tablespoons mirin
- 1 tablespoon sake
- 1 tablespoon granulated sugar (adjust to taste; can add up to 2 tbsp for sweeter glaze)
- 1 teaspoon rice vinegar (optional, for brightness)
- ½ teaspoon toasted sesame oil
- 1–2 tablespoons water (to adjust consistency)

**Equipment:**
- Small saucepan
- Whisk
- Measuring spoons
- Airtight container for storage

### 2. Instructions
Write 5–6 steps with bolded action titles, sensory cues, inline timing.

1. **Combine Base Ingredients** – In a small saucepan, whisk together the miso, mirin, sake, and sugar until smooth. The mixture should be thick but uniform, with no visible lumps of miso.
2. **Simmer to Thicken** – Place the saucepan over medium-low heat. Bring to a gentle simmer, stirring constantly to prevent sticking. Cook for 3–5 minutes, or until the glaze thickens slightly and coats the back of a spoon. It should be glossy and pourable, not stiff.
3. **Add Acid and Oil** – Remove the pan from the heat. Stir in the rice vinegar (if using) and sesame oil. The glaze may loosen slightly; if it becomes too thick, add water a teaspoon at a time until it reaches a brushable consistency.
4. **Taste and Adjust** – Give the glaze a quick taste. If a sweeter profile is desired, add a bit more sugar (up to 1 extra tablespoon). If more tang is needed, add a few more drops of rice vinegar. Mix well after any adjustment.
5. **Cool and Store** – Let the glaze cool to room temperature, then transfer to a clean jar. It will thicken further as it cools; thin with warm water before use if needed.
6. **Use** – Brush onto fish, vegetables, tofu, or eggplant during the last few minutes of grilling, broiling, or roasting. Apply in layers for deeper flavor.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Simmering the miso blend too long or at too high a heat can cause it to separate or become grainy; keep the heat low and stir constantly.
  2. The glaze is versatile: use it as a marinade (apply 30 minutes before cooking), a glaze (apply during cooking), or a finishing drizzle.
- **Make-Ahead / Storage:**
  - Miso glaze keeps refrigerated in an airtight container for up to 2 weeks.
  - For longer storage, freeze in ice cube trays and transfer to a freezer bag for up to 3 months; thaw in refrigerator.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 4 parts miso to 2 parts mirin to 1 part sake to 1 part sugar.
  - For larger batches, use a larger saucepan to avoid overheating.
- **Variations (1):**
  - **Spicy Miso Glaze:** Add ½ teaspoon chili garlic sauce or sriracha to the mixture in step 1.

### 4. Frontmatter & Metadata
- `title`: "Miso Glaze"
- `slug`: "miso-glaze"
- `meal_type`: condiment
- `cuisine`: japanese
- `course`: condiment
- `dietary_tags`: [vegetarian, vegan, gluten-free-option] (note: miso, mirin, sake are typically vegan; check labels)
- `season`: all-year
- `prep_time`: "5 min [ACTIVE]" (measuring and mixing)
- `cook_time`: "5 min [ACTIVE]" (simmering)
- `inactive_time`: "5 min [PASSIVE]" (cooling)
- `total_time`: "15 min"
- `base_servings`: ½ cup (about 8 servings of 1 tbsp)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Scales linearly; ensure adequate saucepan size to prevent boil-over."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on versatile miso glaze technique."
- `difficulty`: "easy"
- `key_equipment`: ["saucepan", "whisk", "measuring spoons", "jar"]
- `tags`: ["recipe/condiment", "ingredient/miso", "ingredient/mirin", "ingredient/sake", "technique/simmering"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe includes miso, mirin, sake, sugar, rice vinegar, sesame oil.
- Ensure instructions are 5–6 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/condiment/miso-glaze.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes miso, mirin, sake, sugar, rice vinegar, sesame oil.
- [ ] Instructions are 5–6 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.