# Specification: Create Miso-Glazed Salmon from Title-Only Addendum

**Ticket:** TICKET-009  
**Recipe:** `dinner/miso-glazed-salmon.md`  
**Objective:** Create a complete miso-glazed salmon recipe (saikyo-yaki style) from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component, based on standard saikyo-yaki ratio (3:2:1 miso:mirin:sake) plus sugar to taste.

**For the Miso Marinade:**
- ¼ cup (60g) saikyo miso (sweet white miso) or white miso (shiro miso)
- 2 tablespoons mirin
- 1 tablespoon sake
- 1 tablespoon granulated sugar (adjust to taste; can add up to 2 tbsp for sweeter marinade)
- 1 teaspoon grated fresh ginger (optional, for aroma)

**For the Salmon:**
- 4 salmon fillets (about 5-6 oz / 150-170g each), skin-on or skinless as preferred
- 1 teaspoon neutral oil (such as grapeseed or canola) for brushing the pan
- Flaky sea salt (for finishing, optional)
- Lemon wedges (for serving, optional)
- Toasted sesame seeds (for garnish, optional)
- Thinly sliced scallions (for garnish, optional)

**Equipment:**
- Baking sheet or broiler pan
- Small bowl for mixing marinade
- Plastic wrap or airtight container for marinating
- Pastry brush
- Knife

### 2. Instructions
Write 6–8 steps with bolded action titles, sensory cues, inline timing.

1. **Prepare the Marinade** – In a small bowl, whisk together miso, mirin, sake, and sugar until smooth. Stir in grated ginger if using. The mixture should be thick but spreadable.
2. **Marinate the Salmon** – Pat salmon fillets dry with paper towels. Spread a thin, even layer of the miso mixture on all sides of each fillet (about 1 tablespoon per fillet). Place the fillets in a single layer in a shallow dish or on a plate, cover tightly with plastic wrap, and refrigerate for 24 to 48 hours. (Do not exceed 48 hours or the salmon may become overly salty.)
3. **Preheat the Broiler** – About 15 minutes before cooking, adjust oven rack to the top position and preheat the broiler to high. Line a baking sheet with foil for easy cleanup.
4. **Remove Excess Marinade** – Take the salmon out of the refrigerator. Gently wipe off most of the miso marinade with your fingers or a paper towel, leaving only a very thin layer (the marinade will burn if too thick). Discard used marinade.
5. **Broil the Salmon** – Place the salmon skin-side down (if skin-on) or simply lay the fillets on the prepared baking sheet. Brush lightly with oil. Broil 4–5 inches from the heat source until the surface is bubbly and caramelized, and the salmon is cooked through to your liking, 6–8 minutes for medium (internal temperature 125°F/52°C for medium-rare, 130°F/54°C for medium). Watch closely; the sugar can cause rapid browning.
6. **Rest** – Remove from the broiler and let rest for 2 minutes.
7. **Garnish and Serve** – Transfer to serving plates. Sprinkle with sesame seeds and scallions if desired. Serve with lemon wedges on the side.
8. **Optional Pan-Sear** – For a crispier skin, after broiling skin-side up, flip and sear skin-side down in a hot skillet with a drop of oil for 1–2 minutes.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Wiping off excess marinade before broiling prevents burning and allows the sugar to caramelize without charring.
  2. Saikyo miso is traditionally used for its sweetness; if using regular white miso, you may need to add a bit more sugar.
- **Make-Ahead / Storage:**
  - The miso marinade can be made ahead and stored in an airtight container in the refrigerator for up to 1 week.
  - Marinated salmon (before cooking) keeps in the refrigerator for up to 2 days; do not freeze as the texture may change.
  - Cooked miso-glazed salmon is best served immediately but can be kept at room temperature for up to 2 hours; reheat gently if needed.
- **Scaling:**
  - The marinade recipe scales linearly; maintain the 3:2:1 ratio of miso:mirin:sake and adjust sugar to taste.
  - For larger batches, use multiple baking sheets or broil in batches to avoid overcrowding.
- **Variations (2):**
  - **Spicy Miso:** Add 1 teaspoon chili paste (such as gochujang or sambal oelek) to the marinade.
  - **Miso-Maple:** Replace half the sugar with maple syrup for a deeper sweetness.

### 4. Frontmatter & Metadata
- `title`: "Miso-Glazed Salmon"
- `slug`: "miso-glazed-salmon"
- `meal_type`: dinner
- `cuisine`: japanese
- `course`: main
- `dietary_tags`: [gluten-free-option] (note: the dish is naturally gluten-free if using gluten-free mirin; some mirin contains wheat, so we note option)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (plus 24–48 hrs marinating, which is inactive)
- `cook_time`: "10 min [ACTIVE]" (broiling)
- `inactive_time`: "24 hrs [PASSIVE]" (marinating) – we'll represent as "24 hr" but spec may need a format; we'll use "24 hr [INACTIVE]" but the spec expects a string; we'll put "24 hr [INACTIVE]" but the ticket expects a time; we'll adjust: we can set prep_time to "15 min", cook_time to "10 min", inactive_time to "24 hr", total_time to "24 hr 25 min". However, the digitization skill spec may expect times in minutes? We'll follow the style of other recipes: they use "[ESTIMATED]" and times like "10 min". For inactive time we can put "24 hr [INACTIVE]". We'll see.
- `total_time`: "24 hr 25 min [ESTIMATED]" (including marinating)
- `base_servings`: 4
- `serving_unit`: "fillets"
- `scaling_notes`: "Marinade scales linearly; ensure salmon fillets are in a single layer for even marinating and broiling."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on saikyo-yaki technique."
- `difficulty`: "medium"
- `key_equipment`: ["broiler", "baking sheet", "small bowl", "plastic wrap", "pastry brush"]
- `tags`: ["recipe/dinner", "ingredient/salmon", "ingredient/miso", "technique/marinating", "technique/broiling"]
- `protein`: ["salmon"]
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe follows saikyo-yaki technique: marinating 24–48 hrs, wiping, broiling.
- Ensure ingredient list includes all required components.
- Verify instructions have 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/dinner/miso-glazed-salmon.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes miso, mirin, sake, sugar, salmon.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.