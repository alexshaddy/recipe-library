# Specification: Fix Dolma Ingredient Mismatch

**Ticket:** TICKET-007  
**Recipe:** `dinner/dolma.md`  
**Objective:** Align the recipe with the notebook source (grape leaves, rice, ground lamb, onion, pine nuts, currants, dill, mint, lemon, olive oil, tomato paste, water) and expand instructions, notes, and variations per skill requirements.

## Changes

### 1. Ingredients
Replace existing ingredient list with notebook-accurate data. Since notebook did not provide quantities, we will use typical dolma proportions for 4 servings:
- Grape leaves: 1 jar (about 60 leaves), rinsed and blanched if necessary
- Rice: 1 cup (short-grain or medium-grain, rinsed)
- Ground lamb: ½ pound (225g)
- Onion: 1 medium, finely chopped
- Pine nuts: ¼ cup, toasted
- Currants: ¼ cup
- Fresh dill: 2 tablespoons, chopped
- Fresh mint: 2 tablespoons, chopped
- Lemon: 1, zest and juice
- Olive oil: ¼ cup plus 2 tbsp for sautéing
- Tomato paste: 2 tablespoons
- Water: 1½ cups (for cooking liquid)
- Salt: 1 teaspoon (adjust to taste)
- Pepper: ½ teaspoon black pepper (optional, not in notebook but typical)
- Allspice and cinnamon from current recipe are NOT in notebook; remove them.

### 2. Instructions
Rewrite as 5–8 steps with bolded action titles, sensory cues, and inline timing:
1. **Prepare the filling** – In a skillet, heat 2 tbsp olive oil over medium heat. Add onion and cook until translucent, 3–4 minutes. Stir in pine nuts and toast until golden, 2 minutes. Remove from heat.
2. **Combine ingredients** – In a large bowl, mix rice, ground lamb, cooked onion-pine nut mixture, currants, dill, mint, lemon zest, lemon juice, tomato paste, salt, and pepper until evenly combined. The mixture should feel moist and fragrant.
3. **Prepare the leaves** – If using preserved grape leaves, rinse thoroughly and blanch in boiling water for 2 minutes to soften, then drain. Pat dry.
4. **Roll the dolma** – Place a leaf flat, stem side up. Place about 1 tablespoon of filling near the stem end. Fold sides over filling, then roll tightly into a cigar shape. Repeat with remaining leaves and filling.
5. **Arrange for cooking** – Line the bottom of a heavy pot with a few torn leaves (to prevent sticking). Pack rolled dolma seam-side down in tight layers. Pour remaining ¼ cup olive oil over the top.
6. **Add cooking liquid** – Mix water and tomato paste (if not already mixed) and pour over dolma until just covered. Place a heatproof plate on top to weigh down.
7. **Simmer** – Bring to a gentle simmer over medium-low heat, then reduce to low. Cook, covered, for 35–40 minutes, until rice is tender and liquid absorbed. Avoid boiling vigorously to keep rolls intact.
8. **Rest and serve** – Remove from heat and let rest 10 minutes before serving. Serve warm or at room temperature with lemon wedges.

### 3. Notes & Variations
Expand to include:
- **Cook's Notes** (minimum 2):
  1. The notebook specifies grape leaves and lamb; using beef alters the traditional flavor profile.
  2. Toasting pine nuts adds a subtle crunch and nutty depth that complements the sweet currants.
- **Make-Ahead / Storage**:
  - Dolma tastes better after resting; refrigerate overnight and reheat gently or serve cold.
  - Store in an airtight container in the refrigerator for up to 4 days.
  - Freeze cooked dolma in a single layer, then transfer to a bag for up to 2 months; thaw in refrigerator before reheating.
- **Scaling**:
  - The filling-to-leaf ratio is key; maintain approximately 1 tbsp filling per leaf.
  - For larger batches, use a wider pot to avoid stacking too high; adjust cooking time slightly if needed.
- **Variations** (minimum 1):
  - **Vegetarian Dolma:** Omit lamb, increase rice to 1½ cups, add ½ cup chopped toasted walnuts and 1 tablespoon pomegranate molasses to the filling.

### 4. Frontmatter & Metadata
- Update `prep_time`: "40 min [ESTIMATED]" (includes prep, mixing, rolling)
- Update `cook_time`: "40 min [ESTIMATED]" (simmering)
- Set `inactive_time`: "10 min [ESTIMATED]" (resting)
- Update `total_time`: "1 hr 30 min [ESTIMATED]"
- Set `date_modified` to "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure tags include `cuisine/middle-eastern`, `dietary_tags/gluten-free`, consider adding `technique/stuffed`
- Keep `source_type`, `source_name`, `source_page`, `origin_notes` (update note to reflect actual transcription? The notebook had title only; we are using the ingredient list from notebook? Actually ticket says notebook specifies those ingredients; we trust that.)

### 5. Verification
- Confirm ingredient list matches notebook items (with reasonable quantities).
- Ensure instructions are clear, action-oriented, with sensory cues and timing.
- Confirm notes and variations meet minimum counts.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes required; this is a content update.
- Implementer should edit the markdown file directly.
- Quality reviewer should verify against notebook source and style guidelines.
- Documentation updater should ensure any related cross-references are updated (none identified).

## Acceptance Criteria
- [ ] Ingredients list matches notebook components (with reasonable quantities).
- [ ] Instructions contain 5–8 steps with bolded titles, sensory cues, inline timing.
- [ ] Notes & Variations include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields are correct and dates updated.
- [ ] Status changed to `reviewed`.
- [ ] No unrelated changes introduced.