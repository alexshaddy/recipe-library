# Specification: Create Miso Butter from Title-Only Addendum

**Ticket:** TICKET-016  
**Recipe:** `condiment/miso-butter.md`  
**Objective:** Create a complete miso compound butter recipe from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component: butter, miso, flavorings.

**For the Miso Butter:**
- 1 cup (2 sticks / 226g) unsalted butter, softened to room temperature
- 2 tablespoons white miso (shiro miso) or awase miso
- 1 tablespoon honey or maple syrup (optional, for sweetness)
- 1 tablespoon finely chopped scallions (green part only)
- 1 teaspoon toasted sesame seeds
- ½ teaspoon rice vinegar or lemon juice (optional, for brightness)
- Pinch of white pepper (optional)

**Equipment:**
- Mixing bowl
- Spatula or wooden spoon
- Plastic wrap or parchment paper
- Knife

### 2. Instructions
Write 4–6 steps with bolded action titles, sensory cues, inline timing.

1. **Soften the Butter** – Leave the unsalted butter at room temperature for 30–45 minutes until soft and pliable but not melted. It should yield slightly to finger pressure.
2. **Combine Ingredients** – In a mixing bowl, add the softened butter, white miso, honey/maple syrup (if using), chopped scallions, toasted sesame seeds, and rice vinegar or lemon juice (if using). Mix thoroughly with a spatula until uniformly blended and smooth. Taste and adjust with a pinch of white pepper if desired.
3. **Shape the Butter** – Place a sheet of plastic wrap or parchment paper on a flat surface. Spoon the miso butter mixture onto the center and shape into a log about 1.5 inches in diameter. Twist the ends of the wrap tightly to seal, or fold parchment and twist to form a tight cylinder.
4. **Chill** – Refrigerate the butter log for at least 1 hour to firm up, or until ready to use. For longer storage, keep refrigerated.
5. **Serve** – Slice off rounds of the miso butter as needed. Use to top grilled corn, steak, fish, vegetables, or spread on warm bread.
6. **Optional: Freeze for Longer Storage** – Wrap the butter log tightly and freeze for up to 3 months. Thaw in the refrigerator before use.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Using unsalted butter allows you to control the saltiness, as miso already adds salt.
  2. Toasting the sesame seeds enhances their nutty flavor; toast them in a dry pan over low heat until golden, stirring frequently.
- **Make-Ahead / Storage:**
  - Miso butter keeps refrigerated in an airtight container or wrapped tightly for up to 2 weeks.
  - For longer storage, freeze the butter log for up to 3 months; slice frozen pieces directly onto hot dishes to melt.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of about 2 tbsp miso per cup of butter.
  - For a smaller batch, halve the ingredients and shape into a smaller log.
- **Variations (2):**
  - **Spicy Miso Butter:** Add ½ teaspoon chili flakes or 1 teaspoon sriracha to the mixture.
  - **Herbed Miso Butter:** Mix in 1 tablespoon chopped fresh herbs (such as chives, parsley, or cilantro) along with the scallions.

### 4. Frontmatter & Metadata
- `title`: "Miso Butter"
- `slug`: "miso-butter"
- `meal_type`: condiment
- `cuisine`: japanese-fusion
- `course`: condiment
- `dietary_tags`: [vegetarian] (contains dairy; if using plant-based butter, could be vegan but we'll keep as vegetarian)
- `season`: all-year
- `prep_time`: "10 min [ACTIVE]" (softening and mixing)
- `cook_time`: "0 min [ACTIVE]" (no cooking)
- `inactive_time`: "60 min [PASSIVE]" (chilling)
- `total_time`: "70 min"
- `base_servings`: 1 cup (about 16 servings of 1 tbsp each)
- `serving_unit`: "tablespoon"
- `scaling_notes`: "Butter and miso scale linearly; adjust optional flavorings to taste."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on miso compound butter technique."
- `difficulty`: "easy"
- `key_equipment`: ["mixing bowl", "spatula", "plastic wrap or parchment paper", "knife"]
- `tags`: ["recipe/condiment", "ingredient/butter", "ingredient/miso", "technique/compound-butter"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe includes softened butter, miso, and optional flavorings.
- Ensure instructions have 4–6 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/condiment/miso-butter.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes unsalted butter, white miso, optional honey/maple, scallions, sesame seeds.
- [ ] Instructions are 4–6 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.