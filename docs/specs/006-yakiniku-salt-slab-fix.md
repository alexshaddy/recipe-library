# Specification: Fix Yakiniku Salt Slab Ingredient Mismatch

**Ticket:** TICKET-006  
**Recipe:** `dinner/yakiniku-salt-slab.md`  
**Objective:** Align the recipe with the notebook source (A5 Wagyu, Himalayan salt slab, bordelaise components, negi bed, beef stock, shallots, thyme, nori) and expand instructions, notes, and variations per skill requirements.

## Changes

### 1. Ingredients
Replace existing ingredient list with notebook-accurate data, grouped by component:

**For the A5 Wagyu:**
- 1 lb A5 Wagyu beef, thinly sliced (for yakiniku)

**For the Himalayan salt slab:**
- 1 Himalayan salt slab (approximately 10x6x1 inch) – *equipment, not consumed*

**For the Bordelaise sauce:**
- ¾ cup dry red wine (such as Bordeaux)
- ½ cup beef stock
- 1 shallot, finely minced
- 1 sprig fresh thyme (or ¼ tsp dried thyme)
- 1 tbsp unsalted butter
- Salt and freshly ground black pepper to taste

**For the Nori Bordelaise variant (optional):**
- 1 sheet nori, finely shredded (to be added to bordelaise)

**For the Negi bed:**
- 2 negi (Welsh onion) or scallions, white and light green parts only, thinly sliced lengthwise

**For serving:**
- Flaky sea salt (for finishing)
- Lemon wedges (optional)

*Note: The salt slab is heated and used as a cooking surface; it is not an ingredient but essential equipment.*

### 2. Instructions
Rewrite as 5–8 steps with bolded action titles, sensory cues, and inline timing, covering preparation of bordelaise, negi bed, heating salt slab, grilling meat, and assembling.

1. **Prepare the Bordelaise** – In a small saucepan, combine red wine, beef stock, minced shallot, and thyme. Bring to a simmer over medium heat and reduce until slightly thickened and volume is halved (about 8–10 minutes). Remove thyme sprig, whisk in butter, season with salt and pepper. Keep warm. (Optional: stir in shredded nori for nori bordelaise variant.)
2. **Make the Negi bed** – Slice negi lengthwise into thin ribbons; toss with a few drops of oil and a pinch of salt. Set aside.
3. **Heat the Salt slab** – Place Himalayan salt slab on grill over medium-high heat. Allow to heat gradually for 15–20 minutes until surface is hot (a few drops of water should sizzle and evaporate quickly). Do not overheat or it may crack.
4. **Grill the Wagyu** – Arrange sliced A5 Wagyu in a single layer on the hot salt slab. Grill 1–2 minutes per side, depending on thickness, until browned but still pink inside. The meat will sizzle and release a rich aroma.
5. **Rest the meat** – Transfer grilled Wagyu to a warm plate; let rest 2 minutes.
6. **Assemble the Negi bed** – Spread negi ribbons on a serving platter or individual plates.
7. **Serve** – Place rested Wagyu atop the negi bed. Drizzle with warm bordelaise (or nori bordelaise). Finish with a light sprinkle of flaky sea salt and lemon wedges if desired. Eat immediately while the salt slab retains heat.

### 3. Notes & Variations
Expand to include:
- **Cook's Notes** (minimum 2): importance of gradual salt slab heating to prevent cracking; using A5 Wagyu for optimal marbling and flavor.
- **Make-Ahead / Storage**: bordelaise can be made ahead and reheated; negi bed best fresh; Wagyu should be grilled to order.
- **Scaling**: recipe scales linearly for meat and sauces; ensure salt slab size accommodates quantity without overcrowding.
- **Variations** (minimum 2): nori bordelaise variant (add shredded nori to sauce); miso-bordelaise (whisk in 1 tbsp white miso at end).

### 4. Frontmatter & Metadata
- Update `prep_time`, `cook_time`, `inactive_time`, `total_time` based on new procedure.
- Set `date_modified` to 2026-06-27.
- Change `status` from `draft` to `reviewed`.
- Ensure tags include appropriate technique tags (e.g., technique/grill, technique/sauce).
- Verify existing fields (cuisine: japanese, dietary_tags: gluten-free) remain accurate; note that bordelaise may contain gluten if using regular flour? Actually bordelaise is typically gluten-free; we'll keep gluten-free.

### 5. Verification
- Confirm ingredient amounts match notebook description.
- Ensure instructions are clear, action-oriented, with sensory cues.
- Confirm notes and variations meet minimum counts.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes required; this is a content update.
- Implementer should edit the markdown file directly.
- Quality reviewer should verify against notebook source and style guidelines.
- Documentation updater should ensure any related cross-references are updated (none identified).

## Acceptance Criteria
- [ ] Ingredients list matches notebook components (with reasonable interpretations).
- [ ] Instructions contain 5–8 steps with bolded titles, sensory cues, inline timing.
- [ ] Notes & Variations include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields are correct and dates updated.
- [ ] Status changed to `reviewed`.
- [ ] No unrelated changes introduced.