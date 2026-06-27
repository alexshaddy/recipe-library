# Specification: Expand Spicy Bok Choy from Notebook Source

**Ticket:** TICKET-025  
**Recipe:** `side/spicy-bok-choy.md`  
**Objective:** Align the bok choy recipe with the notebook source (p.18) and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We will align with the notebook, resolving the [TO VERIFY] and [EST] markers.

Based on typical bok choy stir-fry and the context, we assume:
- 2 bunches bok choy (about 1.5 lbs), trimmed and halved lengthwise (or quartered if large)
- 1 tablespoon oil (peanut or canola for high heat)
- 2 cloves garlic, thinly sliced
- 1 teaspoon chili flakes (we will keep as is, but note to verify)
- 1 tablespoon soy sauce (we will assume this is correct)
- 1 teaspoon sesame oil (we will assume this is correct)

If the notebook differs, the implementer should adjust.

We will also note that the bok choy should be washed and dried thoroughly.

### 2. Instructions
Expand to 5–7 steps with bolded action titles, sensory cues, inline timing, incorporating the key steps: high-heat sear, aromatics, sauce, steam finish.

1. **Heat the Wok** – Place a wok or large skillet over high heat until a drop of water sizzles and evaporates instantly, about 2 minutes. Add 1 tablespoon oil and swirl to coat; the oil should shimmer but not smoke.
2. **Sear the Bok Choy** – Arrange the bok choy halves cut-side down in a single layer (work in batches if needed). Let sit undisturbed for 1–2 minutes until the cut surfaces are deep golden brown and release easily from the pan. You should hear a steady sizzle and see a caramelized crust forming.
3. **Add Aromatics** – Flip the bok choy to cook the leaves side briefly, about 30 seconds. Push the bok choy to the sides of the wok and add the sliced garlic and chili flakes to the center. Stir-fry the aromatics for 15–20 seconds until fragrant and the garlic is just beginning to turn golden at the edges (do not let it brown).
4. **Introduce the Sauce** – Drizzle 1 tablespoon soy sauce over the vegetables and toss everything together to coat. The liquid should sizzle and evaporate quickly, leaving the bok choy glossy.
5. **Steam to Tender-Crisp** – Immediately add 2 tablespoons of water to the wok, then cover tightly with a lid or foil. Let steam for 1–2 minutes until the stems are just tender when pierced with a knife but the leaves remain vibrant green and slightly crisp.
6. **Finish with Sesame Oil** – Remove the lid and drizzle 1 teaspoon sesame oil over the bok choy. Toss once to distribute, then transfer to a serving plate. The dish should look glistening and smell aromatic.
7. **Serve Immediately** – Serve hot, optionally garnished with toasted sesame seeds or sliced scallions.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Starting with the bok choy cut-side down ensures maximum caramelization on the thick stems, which takes longer to cook than the leaves.
  2. The quick steam step at the end finishes cooking the stems without overcooking the leaves, preserving texture and color.
- **Make-Ahead / Storage:**
  - Bok choy is best served immediately after cooking.
  - If needed, blanched and shocked bok choy can be prepared ahead: boil halves for 1 minute, shock in ice water, drain, and store dry in the refrigerator for up to 1 day; then finish with the hot wok method just before serving.
- **Scaling:**
  - The recipe scales linearly; use a wok large enough to avoid overcrowding, or cook in batches.
  - Increase oil proportionally to maintain a thin coating on the pan surface.
- **Variations (1):**
  - **Garlic-Ginger Bok Choy:** Add 1 teaspoon freshly grated ginger with the garlic for a brighter, more aromatic profile.

### 4. Frontmatter & Metadata
- Update `prep_time`: "10 min [ACTIVE]" (washing, trimming, halving)
- Update `cook_time`: "8 min [ACTIVE]" (high-heat cooking)
- Keep `inactive_time`: "" (none)
- Update `total_time`: "18 min"
- Update `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure cuisine is "chinese" (currently asian; we'll change to chinese)
- Ensure tags include `technique/wok`, `technique/high-heat`, `technique/steam`.
- Verify existing dietary_tags (vegan, vegetarian, gluten-free-option) remain accurate.

### 5. Verification
- Confirm ingredient list matches notebook (2 bunches bok choy, 1 tbsp oil, 2 cloves garlic, 1 tsp chili flakes, 1 tbsp soy sauce, 1 tsp sesame oil).
- Ensure instructions are 5–7 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should open notebook page 18 to verify exact ingredients, especially the chili flakes and sauce amounts.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list matches notebook (or verified and updated if needed).
- [ ] Instructions are 5–7 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.