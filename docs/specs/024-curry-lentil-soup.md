# Specification: Update Curry Lentil Soup from Notebook Source

**Ticket:** TICKET-024  
**Recipe:** `side/curry-lentil-soup.md`  
**Objective:** Align the curry lentil soup recipe with the notebook source (p.17) and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We will keep the existing ingredient list as it appears to match the notebook (1 cup lentils, 1 onion, 2 cloves garlic, 1 tbsp curry powder, 4 cups stock/water, 1 tbsp oil, 1 tsp salt). Ensure no extra ingredients.

### 2. Instructions
Expand to 6–8 steps with bolded action titles, sensory cues, inline timing, incorporating the key steps: bloom spices, sweat aromatics, add lentils/stock, simmer until tender, blending decision, finish with acid/fat, garnish.

1. **Bloom the Curry Powder** – Heat 1 tablespoon of oil in a medium saucepan over medium heat. Add the curry powder and stir constantly for 30–60 seconds until fragrant and slightly darkened, taking care not to burn. The mixture should smell toasty and aromatic.
2. **Sweat the Aromatics** – Add the diced onion and minced garlic to the pot. Cook, stirring occasionally, until the onion becomes translucent and soft, about 5–7 minutes. The mixture should be sweet-smelling and the onions should be glossy.
3. **Add Lentils and Liquid** – Stir in 1 cup of lentils (rinsed and picked over) and 4 cups of stock or water. Bring the mixture to a gentle boil, then reduce heat to maintain a simmer.
4. **Simmer Until Tender** – Partially cover the pot and let the soup simmer for 25–35 minutes, or until the lentils are soft and starting to break apart. Stir occasionally to prevent sticking. The lentils should be tender but not mushy.
5. **Blend (Optional) **Blend for Creaminess** – For a smoother texture, use an immersion blender to puree part or all of the soup directly in the pot. Alternatively, transfer half of the soup to a countertop blender, blend until smooth, and return to the pot. Blend to your desired consistency.
6. **Finish with Acid and Fat** – Remove the pot from heat. Stir in 1 tablespoon of lemon juice or apple cider vinegar to brighten the flavors, and optionally swirl in 1 tablespoon of olive oil or coconut milk for richness. Adjust salt to taste.
7. **Garnish and Serve** – Ladle the soup into bowls. Top with optional garnishes such as chopped cilantro, a dollop of yogurt, or a drizzle of chili oil. Serve hot.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Blooming the curry powder in oil first unlocks its essential oils and prevents a raw, bitter taste.
  2. If using red lentils, they will break down more quickly and create a naturally thicker soup; green or brown lentils hold their shape better.
- **Make-Ahead / Storage:**
  - The soup keeps refrigerated in an airtight container for up to 4 days.
  - Freeze in portion-sized containers for up to 3 months; thaw and reheat gently, adding a splash of water or stock if needed.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 1 cup lentils to 4 cups liquid.
  - When doubling, use a larger pot to avoid overcrowding and ensure even simmering.
- **Variations (1):**
  - **Coconut Curry Lentil Soup:** Replace half the stock with coconut milk and add a teaspoon of grated ginger with the aromatics for a Thai-inspired twist.

### 4. Frontmatter & Metadata
- Update `prep_time`: "15 min [ACTIVE]" (includes blooming and sweating)
- Update `cook_time`: "35 min [ACTIVE]" (simmering)
- Keep `inactive_time`: "" (none)
- Update `total_time`: "50 min"
- Keep `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure tags include `technique/bloom-spices`, `technique/simmer`, `technique/blend` (optional).
- Verify existing fields (cuisine: indian, dietary_tags: vegan/vegetarian/gluten-free) remain accurate.

### 5. Verification
- Confirm ingredient list matches notebook (lentils, onion, garlic, curry powder, stock/water, oil, salt).
- Ensure instructions are 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

## Acceptance Criteria
- [ ] Ingredients list matches notebook (1 cup lentils, 1 onion, 2 cloves garlic, 1 tbsp curry powder, 4 cups stock/water, 1 tbsp oil, 1 tsp salt).
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.