# Specification: Expand Jiban Recipe from Notebook Source

**Ticket:** TICKET-020  
**Recipe:** `condiment/jiban.md`  
**Objective:** Ensure the jiban (labneh-style cheese) recipe meets digitization skill spec by enhancing instructions with bolded action titles, sensory cues, inline timing, and adding sufficient cook's notes, variations, make-ahead/storage, and scaling guidance.

## Current State
The recipe currently has 4 steps with bolded action titles but lacks sensory cues and precise timing. Notes include one cook's note, brief make-ahead/storage, and scaling guidance.

## Required Enhancements

### 1. Instructions
Upgrade each step to include:
- **Bolded action title** (already present)
- **Sensory cues** (visual, tactile, olfactory indicators)
- **Inline timing** (active and passive durations)

Proposed revised steps:

1. **Warm the Dairy** – In a large, heavy-bottomed pot, combine 3 gallons whole milk and 1.5 cups heavy cream. Heat over medium-low, stirring occasionally to prevent scorching, until the mixture reaches 70–80°F (21–27°C). It should feel warm to the wrist but not hot, with a slight sheen on the surface and no bubbles forming. This takes about 15–20 minutes.
2. **Prepare and Add Rennet** – While the dairy warms, crush 1 rennet tablet and dissolve it in ¼ cup cool, non-chlorinated water. Once the dairy is at temperature, pour in the rennet solution and stir gently with a clean spoon for about 30 seconds to distribute evenly. The mixture should remain still. The liquid will look uniform and slightly thicker.
3. **Set the Curd** – Cover the pot and let it sit undisturbed in a warm place (like an oven with the light on) for 12–24 hours. During this time, the milk will coagulate into a gel-like custard that pulls away slightly from the sides of the pot. When you tilt the pot, the mass should move as a single piece and leave a clean break when a finger is slid through it.
4. **Cut and Drain the Curd** – Using a long knife or spatula, cut the set curd into a 1-inch checkerboard pattern, reaching to the bottom of the pot. Let the cut curd rest for 5 minutes to release whey. Then, using a slotted spoon, transfer the curds to a cheesecloth-lined colander set over a bowl. Gather the corners of the cheesecloth and tie into a bundle. Hang the bundle over the bowl to drain for 6–8 hours in the refrigerator, or until the desired thickness is reached (the longer it drains, the drier the cheese).
5. **Salt and Shape** – After draining, untie the cheesecloth and place the cheese in a bowl. Sprinkle with 1–2 teaspoons of fine sea salt (to taste) and gently fold in with a spatula. The cheese should be soft and spreadable, like thick Greek yogurt. For a firmer texture, reshape into a disk or log, wrap tightly in cheesecloth or parchment, and refrigerate for another 2 hours.
6. **Serve or Store** – Serve the jiban drizzled with extra-virgin olive oil, sprinkled with za'atar, and accompanied by warm pita. For storage, keep in an airtight container in the refrigerator.

### 2. Notes & Variations
- **Cook's Notes (2):**
  1. Using ultra-pasteurized milk may hinder proper coagulation; for best results, use pasteurized (not ultra-pasteurized) whole milk.
  2. The draining time determines the final texture: 6 hours yields a soft, spreadable cheese; 12+ hours produces a firmer, sliceable cheese suitable for grilling.
- **Make-Ahead / Storage:**
  - Fresh jiban keeps refrigerated in an airtight container for up to 1 week.
  - For longer storage, form into small balls, submerge in olive oil with herbs (e.g., thyme, garlic), and refrigerate for up to 2 weeks.
  - Freezing is not recommended as it alters texture.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of 2 parts milk to 1 part cream by volume.
  - Adjust rennet proportionally: use 1 tablet per 3 liters (about 100 oz) of milk.
- **Variations (1):**
  - **Herbed Labneh:** After salting, mix in 1 tablespoon each of finely chopped fresh mint and dill, plus ½ teaspoon garlic powder. Serve with a drizzle of olive oil and sumac.

### 3. Frontmatter & Metadata Updates
- `prep_time`: "20 min [ACTIVE]" (includes heating and preparing rennet)
- `cook_time`: "0 min [ACTIVE]" (no active cooking after heating)
- `inactive_time`: "12 to 24 hr [PASSIVE]" (setting) + "6 to 8 hr [PASSIVE]" (draining) – we'll combine as "18 to 32 hr [PASSIVE]" or give a range. We'll set as "18 hr [PASSIVE]" as an average, but better to note range. We'll set `inactive_time`: "18 to 32 hr [PASSIVE]" but the field expects a string; we'll put "18–32 hr [PASSIVE]".
- `total_time`: "18 to 32 hr 20 min"
- `date_modified`: "2026-06-27"
- `status`: "reviewed" (already reviewed, but we confirm)
- Ensure tags include `technique/fermentation` or `technique/cheese-making`.
- Verify existing fields (cuisine: middle-eastern, dietary_tags: vegetarian/gluten-free) remain accurate.

### 4. Verification
- Confirm instructions have 5–7 steps (we have 6) with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should update the file with the above content.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

## Acceptance Criteria
- [ ] Instructions are 5–7 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status remains `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.