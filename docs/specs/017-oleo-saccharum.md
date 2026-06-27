# Specification: Update Oleo Saccharum from Notebook Source

**Ticket:** TICKET-017  
**Recipe:** `condiment/oleo-saccharum.md`  
**Objective:** Align the oleo saccharum recipe with the notebook source (peel, sugar, hot water) and expand instructions, notes, and variations per digitization skill spec.

## Changes

### 1. Ingredients
Keep the existing ingredient list (50g orange peel, 200g sugar, 200ml hot water) as it matches the notebook source (assuming). Ensure no extra ingredients.

### 2. Instructions
Expand to 5–8 steps with bolded action titles, sensory cues, inline timing, focusing on the muddling/resting technique.

1. **Prepare the Peel** – Wash an orange thoroughly. Using a vegetable peeler or sharp knife, remove the zest in wide strips, avoiding the white pith as much as possible. You should have about 50 grams of fragrant orange peel.
2. **Combine with Sugar** – Place the peel in a non-reactive bowl. Add the 200 grams of granulated sugar and toss to coat the peel evenly. The sugar should look dry and sandy.
3. **Muddle and Release Oils** – Using a muddler or the back of a wooden spoon, gently crush the sugared peel against the side of the bowl. Press and twist for 1–2 minutes until the sugar looks damp and fragrant, and you can see tiny oil droplets glistening on the surface.
4. **Rest for Oil Extraction** – Cover the bowl with a clean cloth or plastic wrap and let the mixture sit at room temperature for 1 to 2 hours. During this time, the sugar will draw out the essential oils, becoming wet and syrupy, and the peel will soften.
5. **Add Hot Water** – Heat 200 milliliters of water to just below boiling (about 190°F/88°C). Pour it over the sugared peel mixture and stir vigorously until the sugar dissolves completely, forming a cloudy, aromatic syrup.
6. **Strain** – Place a fine-mesh strainer lined with cheesecloth over a clean measuring cup or jar. Pour the mixture through, pressing gently on the solids to extract as much liquid as possible. Discard the spent peel.
7. **Cool and Store** – Allow the oleo saccharum to cool to room temperature, then transfer to a sealed bottle or jar. Refrigerate.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Avoiding the pith is crucial; it contributes bitterness that can ruin the delicate citrus aroma.
  2. The muddling step breaks the oil glands in the peel, releasing fragrance; you should smell a bright citrus perfume as you work.
- **Make-Ahead / Storage:**
  - Oleo saccharum keeps refrigerated in an airtight container for up to 2 weeks.
  - For longer storage, freeze in ice cube trays and transfer to a freezer bag for up to 3 months.
- **Scaling:**
  - The ratio of peel to sugar is key; maintain approximately 1 part peel to 4 parts sugar by weight (e.g., 25g peel, 100g sugar). Ensure the peel is fully coated.
  - Adjust water proportionally to achieve a pourable syrup; start with equal parts water to sugar by volume and adjust as needed.
- **Variations (1):**
  - **Lemon Oleo Saccharum:** Substitute lemon peel for orange, or use a mix of citrus peels for a more complex aroma.

### 4. Frontmatter & Metadata
- Update `prep_time`: "15 min [ACTIVE]" (includes peeling and muddling)
- Keep `cook_time`: "5 min [ACTIVE]" (heating water)
- Keep `inactive_time`: "1 to 2 hr [PASSIVE]" (resting)
- Update `total_time`: "1 to 2 hr 20 min"
- Keep `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure tags include `technique/muddle` or similar; we'll add `technique/macerate` already present.
- Verify existing fields (cuisine: american, dietary_tags: vegetarian/vegan/gluten-free) remain accurate.

### 5. Verification
- Confirm ingredient amounts match notebook (50g peel, 200g sugar, 200ml water).
- Ensure instructions are 5–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

## Acceptance Criteria
- [ ] Ingredients list matches notebook (50g orange peel, 200g sugar, 200ml hot water).
- [ ] Instructions are 5–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status changed to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.