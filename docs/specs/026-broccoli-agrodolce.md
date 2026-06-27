# Specification: Update Broccoli to Sicilian Agrodolce from Notebook Source

**Ticket:** TICKET-026  
**Recipe:** `side/broccoli.md`  
**Objective:** Transform the generic broccoli recipe into a Sicilian agrodolce (sweet-sour) preparation based on notebook 6.21 pop-up dinner and addendum III, and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
Replace the generic ingredient list with the agrodolce components:
- Broccoli florets
- Olive oil
- Garlic
- Red pepper flakes (optional, for heat)
- Sugar (for caramel)
- Vinegar (red wine or sherry)
- Golden raisins
- Pine nuts
- Salt

Remove butter and lemon (unless notebook includes them; but per ticket, we use agrodolce). We'll keep the amounts typical for 4 servings.

**Proposed ingredient list:**
- 2 heads broccoli, cut into florets (about 4 cups)
- 3 tablespoons olive oil
- 3 cloves garlic, thinly sliced
- 1/2 teaspoon red pepper flakes (optional)
- 1 tablespoon granulated sugar
- 2 tablespoons red wine vinegar (or sherry vinegar)
- 2 tablespoons golden raisins
- 2 tablespoons pine nuts, toasted
- Salt to taste

### 2. Instructions
Expand to 6–8 steps with bolded action titles, sensory cues, inline timing, incorporating the key steps: blanch broccoli, make agrodolce (sugar → caramel → vinegar → raisins/pine nuts), toss broccoli in glaze, finish.

1. **Blanch the Broccoli** – Bring a large pot of salted water to a boil. Add the broccoli florets and cook until bright green and just tender-crisp, about 2–3 minutes. Immediately transfer to an ice water bath to stop cooking, then drain thoroughly and pat dry. The florets should be vibrant green and still have a slight snap.
2. **Toast the Pine Nuts** – In a dry skillet over medium-low heat, add the pine nuts and toast, stirring frequently, until golden brown and fragrant, about 2–3 minutes. Transfer to a small bowl to cool.
3. **Make the Agrodolce Base** – In the same skillet, heat 2 tablespoons of olive oil over medium heat. Add the sliced garlic and red pepper flakes (if using) and cook, stirring constantly, until the garlic is fragrant and just beginning to turn golden at the edges, about 30 seconds. Be careful not to burn.
4. **Caramelize the Sugar** – Sprinkle the granulated sugar evenly over the garlic and oil. Let it sit undisturbed for about 45 seconds until the edges start to melt, then stir gently. Continue cooking, stirring constantly, until the sugar melts completely and turns a deep amber color, about 1–2 minutes. The mixture will smell nutty and caramel-like.
5. **Deglaze with Vinegar** – Carefully pour in the vinegar (it will steam and sputter). Stir vigorously to combine; the mixture will bubble rapidly. Continue to cook for 1–2 minutes until the sauce thickens slightly and becomes glossy.
6. **Add Fruit and Nuts** – Stir in the raisins and toasted pine nuts. Cook for another 30 seconds to plump the raisins and toast the nuts further in the glaze.
7. **Coat the Broccoli** – Add the blanched broccoli florets to the skillet. Toss to coat evenly with the agrodolce sauce, cooking for 1–2 minutes just to heat through. The broccoli should be glistening and evenly coated.
8. **Season and Serve** – Remove from heat. Season with salt to taste. Transfer to a serving platter and serve warm or at room temperature.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Watch the caramel closely; sugar can go from amber to burnt in seconds. Keep the heat medium and stir constantly once it starts melting.
  2. Blanching the broccoli first ensures a tender-crisp texture and vibrant color, preventing overcooking during the quick toss in the hot glaze.
- **Make-Ahead / Storage:**
  - The agrodolce sauce (without broccoli) can be made ahead and stored in a jar in the refrigerator for up to 1 week; reheat gently before tossing with fresh-blanched broccoli.
  - Blanched broccoli can be stored in an airtight container in the refrigerator for up to 2 days; refresh in ice water before use.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 1 tbsp sugar to 2 tbsp vinegar per pound of broccoli.
  - When doubling, use a larger skillet to avoid overcrowding, which can steam the broccoli instead of glazing it.
- **Variations (1):**
  - **Citrus-Infused Agrodolce:** Add the zest of 1/2 orange or lemon to the pan with the garlic for a bright citrus note that complements the sweet-sour balance.

### 4. Frontmatter & Metadata
- Update `prep_time`: "15 min [ACTIVE]" (includes blanching and toasting)
- Update `cook_time`: "10 min [ACTIVE]" (agrodolce and tossing)
- Set `inactive_time`: "5 min [PASSIVE]" (ice bath)
- Update `total_time`: "30 min"
- Update `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Update `cuisine`: italian (or specifically sicilian; we'll keep italian and note in origin)
- Ensure `tags` include `technique/blanch`, `technique/glaze`, `ingredient/pine-nuts`, `ingredient/raisins`.
- Verify existing fields (dietary_tags: vegan/vegetarian/gluten-free) remain accurate (no animal products).
- Update `origin_notes` to reflect the specific notebook source.

### 5. Verification
- Confirm ingredient list matches agrodolce components.
- Ensure instructions are 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list includes broccoli, olive oil, garlic, red pepper flakes, sugar, vinegar, raisins, pine nuts, salt.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.