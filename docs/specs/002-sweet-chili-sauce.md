# Specification: Fix Sweet Chili Sauce Ingredient Mismatch

**Ticket:** TICKET-002  
**Recipe:** `condiment/sweet-chili-sauce.md`  
**Objective:** Align the sweet chili sauce recipe with the notebook source (¼ cup rice vinegar) and expand instructions, notes, and variations per digitization skill spec.

## Changes

### 1. Ingredients
Update the ingredient list to reflect notebook-accurate data:
- 1 cup sugar
- ¼ cup rice vinegar
- ¼ cup water
- 2 tablespoons chile flakes or chopped chiles
- 2 cloves garlic, minced
- 1 teaspoon salt

(Note: The notebook specifies only the vinegar amount; we assume the sugar and water amounts remain as in the current recipe to maintain balance, but we change vinegar to rice vinegar and reduce to ¼ cup.)

### 2. Instructions
Expand to 5–8 steps with bolded action titles, sensory cues, inline timing.

1. **Combine Ingredients** – In a saucepan, whisk together sugar, rice vinegar, water, chile flakes, garlic, and salt until the sugar dissolves. The mixture should look cloudy and slightly thick.
2. **Bring to Simmer** – Place the saucepan over medium-high heat. Bring to a gentle boil, stirring occasionally to prevent scorching. Small bubbles will form around the edges, taking about 3–5 minutes.
3. **Reduce and Thicken** – Reduce heat to medium-low and simmer uncovered, stirring frequently, until the sauce reduces slightly and coats the back of a spoon, about 8–10 minutes. It should be glossy and syrupy, not watery.
4. **Test Consistency** – Dip a spoon into the sauce and run a finger through the coating; the line should hold without bleeding immediately. If too thin, continue simmering; if too thick, add a splash of water.
5. **Cool** – Remove from heat and let the sauce cool in the pan for 5 minutes, then transfer to a clean jar. It will thicken further as it cools.
6. **Store** – Seal and refrigerate. The sauce will keep for up to 2 weeks.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Rice vinegar provides a milder, slightly sweet acidity compared to white vinegar; adjust to taste if using a different vinegar.
  2. The type of chile used (flakes vs. fresh chopped) affects both heat and texture; fresh chilies will yield a brighter, more vegetal flavor.
- **Make-Ahead / Storage:**
  - Sweet chili sauce keeps refrigerated in an airtight container for up to 2 weeks.
  - For longer storage, freeze in ice cube trays and transfer to a freezer bag for up to 3 months; thaw in refrigerator.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 4 parts sugar to 1 part vinegar to 1 part water.
  - When doubling, use a larger saucepan to avoid boil-over.
- **Variations (1):**
  - **Garlic-Chili Sweet Sauce:** Increase garlic to 4 cloves and add 1 teaspoon grated ginger for a deeper aromatic profile.

### 4. Frontmatter & Metadata
- Update `prep_time`: "5 min [ACTIVE]" (measuring and mixing)
- Update `cook_time`: "12 min [ACTIVE]" (simmering and reducing)
- Keep `inactive_time`: "" (none)
- Update `total_time`: "17 min"
- Update `date_modified`: "2026-06-27"
- Keep `status`: "reviewed"
- Ensure tags include `technique/simmer`.
- Verify existing fields (cuisine: asian, dietary_tags: vegan/vegetarian/gluten-free) remain accurate.

### 5. Verification
- Confirm ingredient list matches notebook (¼ cup rice vinegar).
- Ensure instructions are 5–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list includes ¼ cup rice vinegar.
- [ ] Instructions are 5–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.