# Specification: Create Miso Caramel from Title-Only Addendum

**Ticket:** TICKET-014  
**Recipe:** `condiment/miso-caramel.md`  
**Objective:** Create a complete miso caramel sauce recipe from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on classic caramel with miso added at the end.

**For the Caramel Base:**
- 1 cup (200g) granulated sugar
- 1/4 cup (60ml) water
- 1/2 cup (120ml) heavy cream, at room temperature
- 4 tablespoons (60g) unsalted butter, cut into pieces, at room temperature
- 1 teaspoon pure vanilla extract
- 1/2 teaspoon flaky sea salt (or to taste)
- 1 tablespoon white miso (shiro miso) or awase miso

**Equipment:**
- Medium heavy-bottomed saucepan
- Whisk or heatproof spatula
- Measuring cups and spoons
- Heatproof container for storage (jar)

### 2. Instructions
Write 5–7 steps with bolded action titles, sensory cues, inline timing.

1. **Dissolve the Sugar** – In a medium saucepan, combine the sugar and water. Stir over medium heat just until the sugar dissolves, about 2–3 minutes. The mixture should be clear and bubbling slightly at the edges.
2. **Cook the Caramel** – Increase heat to medium-high and bring to a boil. Do not stir; instead, gently swirl the pan occasionally to ensure even cooking. Cook until the syrup turns a deep amber color, about 6–8 minutes. It should smell nutty and toasty, and the bubbles will become slower and larger.
3. **Add the Butter** – Remove the pan from the heat. Carefully add the butter pieces (the mixture will bubble vigorously). Stir until the butter is completely melted and incorporated, about 30 seconds.
4. **Incorporate the Cream** – Slowly pour in the warm cream while stirring constantly (the mixture will steam and bubble). Continue stirring until smooth and fully combined, about 1 minute. The caramel should be glossy and pourable.
5. **Finish with Miso and Vanilla** – Stir in the vanilla extract and white miso until completely smooth, about 30 seconds. Taste and add sea salt if desired. The caramel should be rich, sweet, with a savory umami depth from the miso.
6. **Cool and Store** – Let the caramel cool slightly in the pan for 5 minutes, then transfer to a clean jar. It will thicken as it cools. Store at room temperature for up to 2 weeks or refrigerate for up to 1 month (rewarm gently before use).

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Adding the miso at the end preserves its delicate flavor and prevents it from breaking or becoming grainy due to prolonged heat.
  2. Using a wet sugar method (sugar + water) helps prevent crystallization and gives more control over the caramelization process.
- **Make-Ahead / Storage:**
  - Miso caramel keeps at room temperature in an airtight container for up to 2 weeks.
  - For longer storage, refrigerate for up to 1 month; warm gently in a microwave or hot water bath before pouring.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 2 parts sugar to 1 part cream by volume.
  - Use a larger saucepan if doubling to prevent boil-over.
- **Variations (1):**
  - **Spicy Miso Caramel:** Add 1/4 teaspoon cayenne pepper or a few drops of chili oil with the miso for a sweet-heat kick.

### 4. Frontmatter & Metadata
- `title`: "Miso Caramel"
- `slug`: "miso-caramel"
- `meal_type`: condiment
- `cuisine`: japanese-fusion
- `course`: condiment
- `dietary_tags`: [vegetarian]
- `season`: all-year
- `prep_time`: "5 min [ACTIVE]" (measuring)
- `cook_time`: "10 min [ACTIVE]" (caramelizing)
- `inactive_time`: "5 min [PASSIVE]" (cooling)
- `total_time`: "20 min"
- `base_servings`: 1 cup (about 16 servings of 1 tbsp)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Scales linearly; use a heavy-bottomed pan to prevent hot spots."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on caramel technique with miso finish."
- `difficulty`: "medium"
- `key_equipment`: ["saucepan", "whisk", "measuring cups", "heatproof jar"]
- `tags`: ["recipe/condiment", "ingredient/sugar", "ingredient/butter", "ingredient/cream", "ingredient/miso", "technique/caramel-making"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe includes sugar, butter, cream, miso, vanilla, salt.
- Ensure instructions are 5–7 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/condiment/miso-caramel.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes sugar, butter, cream, miso, vanilla, salt.
- [ ] Instructions are 5–7 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.