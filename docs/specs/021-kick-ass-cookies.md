# Specification: Update Kick-Ass Cookies from Notebook Source

**Ticket:** TICKET-021  
**Recipe:** `dessert/kick-ass-cookies.md`  
**Objective:** Align the cookie recipe with the notebook source (p.15) and enhance instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We will keep the current ingredient list as it appears to be a standard cookie recipe and likely matches the notebook. However, we will verify that the notebook includes both granulated and brown sugar? The current list shows only sugar. To be safe, we will note that if the notebook specifies brown sugar, we adjust; but since we don't have the notebook, we assume the given is correct. We'll add a note in the spec that the implementer should verify against the notebook.

For the spec, we will keep the ingredients as:
- 2 cups flour
- 1 cup butter, softened
- 1 cup sugar (granulated)
- 2 eggs
- 1 tsp baking soda
- 1 tsp salt
- 1 tsp vanilla
(Optional: 1 cup chocolate chips or nuts if notebook includes)

But the ticket says align exactly with notebook. We'll instruct the implementer to check the notebook and adjust if needed.

### 2. Instructions
Rewrite as 6–8 steps with bolded action titles, sensory cues, inline timing, incorporating key steps: cream butter/sugars, add eggs/vanilla, fold dry ingredients, chill dough (critical), portion, bake, cool.

Proposed steps:

1. **Cream Butter and Sugar** – In a large mixing bowl, beat 1 cup softened butter and 1 cup granulated sugar together with an electric mixer on medium speed until the mixture is pale yellow, light, and fluffy, about 3–4 minutes. The volume should visibly increase, and the texture should resemble soft whipped cream.
2. **Incorporate Eggs and Vanilla** – Add 2 eggs one at a time, beating well after each addition, then mix in 1 teaspoon vanilla extract. Continue mixing for another 30 seconds until the mixture is smooth and slightly glossy.
3. **Combine Dry Ingredients** – In a separate bowl, whisk together 2 cups all-purpose flour, 1 teaspoon baking soda, and 1 teaspoon salt. This ensures even distribution of leavening.
4. **Mix Wet and Dry** – Gradually add the dry ingredients to the wet mixture, mixing on low speed or stirring with a spatula just until no flour streaks remain. Do not overmix; the dough should look slightly shaggy but hold together when pressed.
5. **Chill the Dough** – Transfer the dough to a sheet of plastic wrap, flatten into a disc, wrap tightly, and refrigerate for at least 1 hour, or up to 24 hours. Chilling is critical: it solidifies the fat, preventing spread and yielding a chewy center with crisp edges.
6. **Portion and Preheat** – After chilling, preheat oven to 375°F (190°C). Scoop the dough by rounded tablespoons (about 1.5 oz each) onto a parchment-lined baking sheet, spacing 2 inches apart. For uniform cookies, use a cookie scoop.
7. **Bake** – Place the sheet in the center of the oven and bake for 10–12 minutes, until the edges are golden brown and set, but the centers still look soft and slightly underdone. The cookies will continue to cook on the hot sheet.
8. **Cool** – Remove from oven and let the cookies rest on the baking sheet for 5 minutes to firm up, then transfer to a wire rack to cool completely. This step ensures the perfect texture: crisp outside, chewy inside.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Chilling the dough is not optional; it allows the flour to hydrate fully and prevents excessive spreading, resulting in thicker, chewier cookies.
  2. For an extra depth of flavor, substitute half the granulated sugar with packed light brown sugar and increase vanilla to 1½ teaspoons.
- **Make-Ahead / Storage:**
  - Cookie dough can be refrigerated for up to 3 days or frozen for up to 3 months; thaw in refrigerator before baking.
  - Baked cookies keep fresh in an airtight container at room temperature for 5 days, or frozen for up to 2 months.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 2 parts flour to 1 part butter to 1 part sugar.
  - When doubling, use a larger mixing bowl and consider chilling the dough in batches if space is limited.

### 4. Frontmatter & Metadata
- Update `prep_time`: "20 min [ACTIVE]" (plus chilling)
- Update `cook_time`: "12 min [ACTIVE]" (baking)
- Set `inactive_time`: "60 min [PASSIVE]" (chilling)
- Update `total_time`: "1 hr 32 min"
- Keep `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure tags include `technique/creaming`, `technique/chilling`, `technique/bake`.
- Verify existing fields (cuisine: american, dietary_tags: vegetarian) remain accurate.

### 5. Verification
- Confirm ingredient list matches notebook (if notebook differs, adjust accordingly).
- Ensure instructions are 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should open the notebook page 15 to verify ingredients and adjust if needed.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list matches notebook (or verified and updated if needed).
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.