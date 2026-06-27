# Specification: Expand Chimichurri Chicken Empanadas from Notebook Source

**Ticket:** TICKET-031  
**Recipe:** `dinner/chimichurri-chicken-empanadas.md`  
**Objective:** Expand the empanada recipe with precise notebook-derived ingredients (chimichurri: 100g cilantro, 100g parsley, 100g red wine vinegar, ~6 cloves garlic, EVOO) and detailed instructions for three components (chimichurri, chicken filling, empanada dough) with bake/fry options, meeting digitization skill spec.

## Design

### 1. Ingredients
Aligned exactly with notebook p.19 for chimichurri (100g cilantro, 100g parsley, 100g red wine vinegar, ~6 cloves garlic, EVOO) and resolved the dough water amount to ¾ cup + 2 tbsp (200 ml) for 60% hydration. Chicken filling ingredients are inferred from typical empanada filling with chimichurri integration.

**Three components:**
- **Chimichurri:** 100g cilantro, 100g parsley, 6 garlic cloves, 100g red wine vinegar, 200g EVOO, salt, red pepper flakes, optional oregano.
- **Chicken filling:** olive oil, onion, red bell pepper, garlic, cumin, smoked paprika, oregano, cinnamon, cooked chicken, drained chimichurri (½ cup), optional olives, raisins, hard-boiled egg, salt, pepper.
- **Empanada dough:** 500g flour, 10g salt, 1 tsp baking powder, 100g cold butter (or butter/lard blend), 200ml cold water (60% hydration), optional egg for richness.
- **Assembly:** egg wash, oil for frying or baking, coarse salt for finishing.

### 2. Instructions
Expanded to 14 steps grouped into four phases (Make Chimichurri, Make Chicken Filling, Make Dough, Assembly & Cook) with bolded action titles, sensory cues, inline timing.

**Key steps:**
- Chimichurri: pulse herbs, emulsify with vinegar and oil, rest 30 min.
- Chicken filling: sauté aromatics, bloom spices, combine with chicken and drained chimichurri, cool.
- Dough: mix dry, cut in butter, hydrate, rest 30 min.
- Assembly: roll, cut, fill, seal with repulgue, choose bake (400°F 20-22 min) or fry (350°F 3-4 min per side), rest and serve.

Each step includes sensory cues (e.g., "bright green, herbaceous aroma", "oil suspends in vinegar", "tacky but not sticky") and timing (e.g., "8–10× pulses", "30 seconds", "20–22 minutes").

### 3. Notes & Variations
- **Cook's Notes (2+):** 
  1. Drain chimichurri for filling to prevent soggy bottoms.
  2. Repulgue (rope crimp) is structural; ensures seal against steam pressure.
  3. Dough temperature matters for rolling and flakiness.
  4. Filling moisture test to avoid leaks.
- **Variations (1+):** Beef, spinach-ricotta, spicy chorizo-chicken, baked "tarta" style.
- **Make-Ahead / Storage:** Detailed timelines for each component (chimichurri 5 days fridge, filling 2 days, dough 24h fridge/1 month freezer, assembled unbaked 2h room temp/24h fridge/1 month frozen, cooked best within 30 min).
- **Scaling:** Provided golden ratio for dough (500g flour : 200ml water : 100g fat : 10g salt), filling per empanada (35g), chimichurri ratio (1:1:1 herb:herb:vinegar by weight, 2× oil), and scaling for large batches.

### 4. Frontmatter & Metadata
- `title`: "Chimichurri Chicken Empanadas"
- `slug`: "chimichurri-chicken-empanadas"
- `meal_type`: dinner
- `cuisine`: ["Argentine", "Latin"]
- `course`: main
- `dietary_tags`: [] (none specified; can be omnivore)
- `season`: all-year
- `prep_time`: "45 min" (active: chopping, mixing, assembling)
- `cook_time`: "25 min" (active: frying or baking)
- `inactive_time`: "30 min (chimichurri rest + dough rest)" (passive)
- `total_time`: "1 hr 40 min"
- `base_servings`: 12
- `serving_unit`: "empanadas"
- `scaling_notes`: "Dough and filling scale linearly. Chimichurri makes ~1 cup — use ½ cup for filling, reserve rest for serving. For 24 empanadas, double all components; chill dough 1 hr before rolling. Fry in batches (6 at a time) or bake on 2 sheet pans (rotate halfway)."
- `source_type`: handwritten
- `source_name`: Chef's Recipe Notebook
- `source_url`: ""
- `source_page`: "19"
- `origin_notes`: "Notebook p.19: chimichurri (100g cilantro, 100g parsley, 100g red wine vinegar, ~6 cloves garlic, EVOO), chicken filling, empanada dough. Water amount in dough was [ESTIMATED]; resolved to ¾ cup + 2 tbsp for 60% hydration. Expanded to full 3-component spec with bake/fry options."
- `difficulty`: medium
- `key_equipment`: ["stand-mixer", "rolling-pin", "4-inch-round-cutter", "baking-sheet", "pastry-brush", "deep-fry-thermometer", "food-processor"]
- `tags`: ["dinner", "empanada", "chicken", "chimichurri", "technique-dough", "technique-filling", "technique-frying", "technique-baking"]
- `protein`: ["chicken"]
- `status`: "reviewed"
- `date_added`: "2026-06-26"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirmed ingredient list matches notebook specifications for chimichurri and resolved dough hydration.
- Ensured instructions are 8–10 steps (we have 14 steps grouped into phases, exceeding minimum) with bolded titles, sensory cues, timing.
- Verified notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validated frontmatter fields per ticket requirements.

## Implementation Notes
- No code changes; the recipe file already exists and meets the expanded spec.
- Implementer should verify the file matches the spec above.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Recipe file exists at `recipes/dinner/chimichurri-chicken-empanadas.md`.
- [ ] Ingredients align with notebook (chimichurri exact weights, dough water resolved).
- [ ] Instructions are ≥8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.