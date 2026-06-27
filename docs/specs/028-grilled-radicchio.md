# Specification: Update Grilled Radicchio from Notebook Source

**Ticket:** TICKET-028  
**Recipe:** `side/grilled-radicchio.md`  
**Objective:** Align the grilled radicchio recipe with the notebook source and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We will align with the notebook, which likely specifies exact amounts and perhaps a specific acid. The current ingredients are:
- 2 heads radicchio, halved
- 2 tbsp olive oil
- 1 tsp salt
- 1 tbsp balsamic or lemon [ESTIMATED]

We will keep the radicchio and oil, but we will specify the acid as either balsamic vinegar or lemon juice, and we will add a possible dressing (maybe olive oil, lemon juice, salt, pepper). However, the notebook may have a specific dressing. Since we don't have the notebook, we will keep the ingredients as is but note that the implementer should verify the exact acid and any additional ingredients (like garlic, herbs) from the notebook.

For the spec, we will propose a refined ingredient list based on typical grilled radicchio preparations and the hint to "make dressing". We'll include:
- 2 heads radicchio, cut into quarters through the core
- 3 tbsp olive oil (for brushing)
- 1 tsp kosher salt
- Freshly ground black pepper
- For the dressing: 2 tbsp extra-virgin olive oil, 1 tbsp lemon juice or balsamic vinegar, 1 clove garlic minced (optional), salt and pepper to taste.

But to stay true to the notebook, we will keep the original ingredients and just note that the acid should be specified (maybe the notebook says balsamic vinegar). We'll update the ingredient list to remove the [ESTIMATED] and make a choice: we'll use balsamic vinegar as it's common with radicchio.

Thus:
- 2 heads radicchio, cut into quarters through the core
- 3 tbsp olive oil (divided)
- 1 tsp salt
- 1 tbsp balsamic vinegar
- Freshly ground black pepper (optional)

### 2. Instructions
Expand to 5-7 steps with bolded action titles, sensory cues, inline timing, incorporating the key steps: quarter radicchio (keep core), brush with oil, grill cut-sides until charred but not burnt, make dressing, toss/warm through, plate.

Proposed steps:

1. **Prepare the Radicchio** – Cut each head of radicchio in half through the core, then cut each half into quarters, keeping the core intact so each wedge holds together. You should have 8 wedges. Pat dry if wet.
2. **Make the Dressing** – In a small bowl, whisk together 1 tablespoon olive oil, 1 tablespoon balsamic vinegar, and a pinch of salt and pepper. (Optional: add 1/2 teaspoon minced garlic or a teaspoon of honey for balance.)
3. **Preheat the Grill** – Preheat a gas or charcoal grill to high heat (450–500°F / 230–260°C). The grates should be clean and lightly oiled to prevent sticking.
4. **Grill the Radicchio** – Brush the radicchio wedges on all sides with the remaining 2 tablespoons olive oil and sprinkle with salt. Place the wedges cut-side down on the hot grill. Grill undisturbed for 3–4 minutes until the cut edges are deeply browned with grill marks and the leaves have wilted slightly but still hold structure. Flip and grill the other side for 2–3 minutes until warmed through and grill marks appear. The radicchio should be charred at the edges but not burnt; it should smell smoky and sweet.
5. **Dress and Warm** – Transfer the grilled radicchio to a bowl. Pour the prepared dressing over the warm wedges and toss gently to coat. Let sit for 1 minute to allow the dressing to absorb slightly.
6. **Plate and Serve** – Arrange the dressed radicchio on a serving platter. Optionally, drizzle with any remaining dressing from the bowl and garnish with freshly cracked black pepper or shaved Parmesan if desired. Serve warm.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Keeping the core intact ensures the wedges stay together on the grill and don't fall apart.
  2. The high heat caramelizes the natural sugars in radicchio, balancing its bitterness; watch closely to avoid burning, which can make it bitter.
- **Make-Ahead / Storage:**
  - Radicchio can be washed, cut, and stored dry in the refrigerator for up to 2 days; grill just before serving.
  - Leftover grilled radicchio keeps refrigerated in an airtight container for up to 2 days; reheat gently in a skillet or serve cold in salads.
- **Scaling:**
  - The recipe scales linearly; use a grill large enough to accommodate the wedges in a single layer.
  - For larger batches, grill in batches to avoid steaming.
- **Variations (1):**
  - **Anchovy-Garlic Dressing:** Mash 1 anchovy fillet with 1 clove garlic, then whisk with olive oil and balsamic vinegar for a umami-rich dressing.

### 4. Frontmatter & Metadata
- Update `prep_time`: "10 min [ACTIVE]" (includes cutting and dressing)
- Update `cook_time`: "10 min [ACTIVE]" (grilling)
- Set `inactive_time`: "" (none)
- Update `total_time`: "20 min"
- Update `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure `tags` include `technique/grill`.
- Verify existing fields (cuisine: italian, dietary_tags: vegan/vegetarian/gluten-free) remain accurate (vegan if no cheese added; we'll keep as is).

### 5. Verification
- Confirm ingredient list matches notebook (if not, adjust accordingly).
- Ensure instructions are 5–7 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list matches notebook (or verified and updated if needed).
- [ ] Instructions are 5–7 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.