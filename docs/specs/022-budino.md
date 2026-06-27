# Specification: Expand Budino from Notebook Budino from Notebook Source

**Ticket:** TICKET-022  
**Recipe:** `dessert/budino.md`  
**Objective:** Align the budino (Italian custard pudding) recipe with the notebook source (p.15) and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
Based on typical budino recipe and likely notebook: milk, cream, sugar, egg yolks, cornstarch, flavoring (vanilla or chocolate), salt.

We'll assume the notebook provides exact amounts; we'll use a classic recipe and note that the implementer should verify against notebook p.15.

**For the Budino (makes about 4 servings):**
- 2 cups (480ml) whole milk
- 1 cup (240ml) heavy cream
- 1/2 cup (100g) granulated sugar
- 4 large egg yolks
- 3 tablespoons (24g) cornstarch
- 1 teaspoon vanilla extract (or 2 oz melted dark chocolate for chocolate budino)
- 1/4 teaspoon salt
- Optional: zest of 1 lemon or orange

**Equipment:**
- Medium saucepan
- Mixing bowls
- Whisk
- Fine-mesh strainer
- Rubber spatula
- Measuring cups/spoons
- Serving glasses or ramekins

### 2. Instructions
Expand to 6–8 steps with bolded action titles, sensory cues, inline timing, incorporating key steps: heat dairy, mix yolks/sugar/starch, temper, cook to nappe, strain, chill, set.

1. **Heat the Dairy** – In a medium saucepan, combine 2 cups milk and 1 cup cream. Add the sugar and salt. Heat over medium heat, stirring occasionally to dissolve sugar, until the mixture is steaming and small bubbles form around the edges (about 180°F/82°C), 5–7 minutes. Do not boil.
2. **Mix Yolks and Thickener** – While the dairy heats, whisk together 4 egg yolks and 3 tablespoons cornstarch in a bowl until smooth and pale yellow, pale yellow. The mixture should be thick and ribbon when lifted. (this is the "ribbon stage.
3. **Temper the Egg Mixture** – Slowly pour about 1 cup of the hot dairy into the yolk mixture while whisking constantly. This tempers, about 1 minute. The mixture should look thick and lemon-colored.
3. **Temper the Yolks** – Gradually pour about 1/2 cup of the hot dairy into the yolk mixture while whisking constantly to raise the temperature without curdling. Once combined, pour the warmed yolk mixture back into the saucepan with the remaining dairy, whisking continuously.
4. **Cook to Nappe** – Continue cooking over medium heat, stirring constantly with a wooden spoon or silicone spatula, until the mixture thickens and coats the back of the spoon (nappe stage). This should take about 5–8 minutes. When you run your finger across the coated spoon, the line should hold without dripping. The pudding will be thick enough to leave a clear trail.
5. **Strain and Flavor** – Remove the saucepan from heat. Stir in the vanilla extract (or melted chocolate) and any optional zest. Pour the mixture through a fine-mesh strainer into a clean bowl to remove any cooked egg bits or lumps. Use a spatula to press through if needed.
6. **Chill and Set** – Divide the strained pudding evenly among 4 serving glasses or ramekins. Cover each with plastic wrap pressed directly onto the surface to prevent a skin from forming. Refrigerate for at least 4 hours, or preferably overnight, until fully set and cold.
7. **Serve** – Before serving, remove the plastic wrap. Top with whipped cream, fresh berries, caramel sauce, or crushed amaretti cookies as desired. Serve chilled.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Tempering the eggs is essential to prevent curdling; the hot liquid must be added gradually while whisking constantly.
  2. The nappe stage is reached when the coating on the spoon is thick enough that a finger drawn across leaves a clean line that does not bleed or drip.
- **Make-Ahead / Storage:**
  - Budino keeps refrigerated in an airtight container for up to 3 days.
  - For longer storage, freeze individual portions (without toppings) for up to 1 month; thaw in refrigerator before serving.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 2 parts liquid to 1 part egg yolk by volume (e.g., for 6 cups liquid, use 6 egg yolks).
  - Adjust cornstarch proportionally: use 1 tablespoon per cup of liquid.
- **Variations (1):**
  - **Chocolate Budino:** Omit vanilla; melt 4 oz (115g) dark chocolate with the hot dairy in step 1, then proceed with the custard base. Increase sugar to 2/3 cup if using bittersweet chocolate.

### 4. Frontmatter & Metadata
- `title`: "Budino"
- `slug`: "budino"
- `meal_type`: dessert
- `cuisine`: italian
- `course`: dessert
- `dietary_tags`: [vegetarian, gluten-free]
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (measuring, mixing)
- `cook_time`: "10 min [ACTIVE]" (heating and cooking)
- `inactive_time`: "4 hr [PASSIVE]" (chilling)
- `total_time`: "4 hr 25 min"
- `base_servings`: 4
- `serving_unit`: "serving"
- `scaling_notes`: "Scale ingredients linearly; ensure saucepan size accommodates volume to prevent boil-over."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "15"
- `origin_notes`: "Notebook page 15 budino recipe."
- `difficulty`: "medium"
- `key_equipment`: ["saucepan", "whisk", "mixing bowl", "fine-mesh strainer", "spatula", "measuring cups"]
- `tags`: ["recipe/dessert", "ingredient/milk", "ingredient/egg", "technique/tempering", "technique/custard", "technique/chilling"]
- `protein`: ["egg"]
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm ingredient list matches notebook (if differs, adjust accordingly).
- Ensure instructions are 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; create new markdown file at `dessert/budino.md`.
- Implementer should open notebook page 15 to verify exact ingredients and adjust if needed.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes milk, cream, sugar, egg yolks, cornstarch, flavoring.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.