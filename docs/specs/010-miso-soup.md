# Specification: Create Miso Soup from Title-Only Addendum

**Ticket:** TICKET-010  
**Recipe:** `soup/miso-soup.md`  
**Objective:** Create a complete miso soup recipe from title-only addendum, following digitization skill spec.

## Design

### 1. Ingredients
Grouped by component: dashi base, miso paste, solids.

**For Dashi (makes about 4 cups):**
- 4 cups (960ml) water
- 1 piece (about 4x6 inches) kombu (dried kelp)
- 1/2 cup (15g) katsuobushi (bonito flakes)  
*(Alternative: 1 tsp instant dashi powder + 4 cups water)*

**For Miso Paste:**
- 3 tablespoons (about 45g) white miso (shiro miso) or awase (mixed) miso  
*(Can use red miso for stronger flavor, or combine)*

**For Solids (per serving):**
- 2 oz (60g) silken tofu, cut into 1/2-inch cubes
- 1 teaspoon dried wakame seaweed (rehydrates to about 1 tbsp)
- 2 scallions (green onions), thinly sliced (green parts only or both)
- Optional: 1/2 small carrot, thinly sliced; 4-5 sliced shiitake mushrooms

### 2. Instructions
Write 5–7 steps with bolded action titles, sensory cues, inline timing.

1. **Make the Dashi** – Place water and kombu in a saucepan. Let soak 20–30 minutes (or up to 2 hours). Heat over medium-low until just below boiling (tiny bubbles form around edges, about 160°F/70°C), 5–7 minutes. Remove kombu (reserve for other uses if desired). Add katsuobushi, bring to a simmer, then immediately remove from heat. Let sit 5 minutes, then strain through a fine-mesh sieve or cheesecloth. You should have about 4 cups clear broth.
2. **Prepare the Solids** – While dashi steeps, rehydrate wakame in a bowl of cold water for 5 minutes, then squeeze dry and set aside. Cube tofu. Slice scallions.
3. **Combine and Heat** – Return strained dashi to the pot. Add any optional vegetables (carrot, mushrooms) and simmer gently until tender, 5–7 minutes. Keep the soup at a low simmer; do not boil.
4. **Add Tofu and Wakame** – Stir in tofu and rehydrated wakame. Heat through gently, 1–2 minutes.
5. **Temper the Miso** – Ladle about 1/2 cup of hot dashi into a small bowl. Add miso paste and whisk until completely smooth. This prevents clumping.
6. **Finish the Soup** – Reduce heat to low (or turn off). Stir the miso mixture back into the pot. Do not boil after adding miso, as it can degrade flavor and nutrients. Warm through just until steaming, about 1 minute.
7. **Serve** – Ladle soup into bowls. Top with sliced scallions. Serve immediately.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Never boil miso; high heat kills its delicate aroma and beneficial enzymes. Always add off-heat.
  2. Dashi is the soul of miso soup; homemade dashi from kombu and katsuobushi yields far superior flavor than instant powders.
- **Make-Ahead / Storage:**
  - Dashi can be made ahead and stored in the refrigerator for up to 3 days or frozen for 1 month.
  - Prepared miso soup (without miso added) can be refrigerated for 1 day; reheat gently, then add miso just before serving.
  - Miso paste keeps refrigerated for months.
- **Scaling:**
  - The recipe scales linearly; maintain the ratio of about 1 tbsp miso per cup of dashi.
  - For larger batches, use a larger pot and adjust simmering time accordingly.
- **Variations (2):**
  - **Vegetarian Dashi:** Use kombu only (simmer 10 minutes, then remove) or substitute with dried shiitake mushrooms (a handful) for umami.
  - **Hearty Miso Soup:** Add cooked noodles (soba or udon), sliced pork, or clams for a more substantial meal.

### 4. Frontmatter & Metadata
- `title`: "Miso Soup"
- `slug`: "miso-soup"
- `meal_type`: soup (could also be breakfast; we'll put soup)
- `cuisine`: japanese
- `course`: soup
- `dietary_tags`: [vegetarian-option, vegan-option, gluten-free-option] (note: dashi with katsuobushi is not vegetarian; we'll note that vegetarian option uses kombu-only dashi; miso is typically vegan; we'll keep both options)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (includes soaking kombu)
- `cook_time`: "10 min [ACTIVE]" (simmering)
- `inactive_time`: "20 min [PASSIVE]" (soaking)
- `total_time`: "45 min"
- `base_servings`: 4
- `serving_unit`: "bowls"
- `scaling_notes`: "Miso quantity scales with dashi volume; aim for 1 tbsp miso per cup of dashi."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on traditional miso soup technique."
- `difficulty`: "easy"
- `key_equipment`: ["saucepan", "fine-mesh sieve or cheesecloth", "bowl", "whisk", "knife"]
- `tags`: ["recipe/soup", "ingredient/miso", "ingredient/dashi", "technique/simmering", "technique/dashi"]
- `protein`: ["tofu"] (can be adjusted)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe follows technique: dashi first, never boil miso.
- Ensure ingredient list includes dashi components, miso, tofu, wakame, scallions.
- Verify instructions have 5–7 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/soup/miso-soup.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes dashi (kombu, katsuobushi or instant), miso, tofu, wakame, scallions.
- [ ] Instructions are 5–7 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.