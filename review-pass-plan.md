# Review Pass Plan

A systematic plan for the review pass across all 75 digitized recipes. Work through one
recipe at a time, verifying against source materials and resolving flags.

## Overview

| Metric             | Count |
| ------------------ | ----- |
| Total recipes      | 75     |
| Reviewed           | 15     |
| Remaining          | 60     |
| Recipes with flags | 65     |
| Flags resolved     | ~25    |
| Total flags        | ~220+  |

## Flag Types

| Flag          | Meaning                              | Typical Use                                                 |
| ------------- | ------------------------------------ | ----------------------------------------------------------- |
| `[ESTIMATED]` | Reasonable guess, needs verification | Timing values, reconstructed ingredient quantities          |
| `[UNCLEAR]`   | Source was illegible or ambiguous    | Cocktail card handwriting, obscured measurements            |
| `[TO VERIFY]` | Critical data missing or guessed     | Missing serving size, unknown cook time, unverified garnish |

## Source Material to Reference

Reviewers should have these available during review:

- **Chef Recipe Notebook** — `assets/chef_recipe_book_draft/chef_recipe_notebook.md`
  (full transcription), plus the original PDF at
  `assets/chef_recipe_book_draft/brw849e563cc961_000414.pdf`
- **Guest-check cocktail cards** — `assets/loose_notes_scans/brw849e563cc961_000402.jpg`
  through `000407.jpg`
- **Carnation booklet** — `assets/loose_notes_scans/brw849e563cc961_000410.pdf`
- **Reconstruction notes** — `assets/chef_recipe_book_draft/chef_reconstruction_addendum.md`
- **Addendum III** — `assets/chef_recipe_book_draft/chef_recipe_addendum_3.md`
  (cultural/archaeological analysis)

## Review Order (Recommended)

### Round 1: Well-Sourced Recipes (easiest — start here)

These have full source content and the flags are mostly on timing estimates:

1. **Carnation booklet recipes** (9)
   - `chiliburgers`, `party-sandwich-loaf`, `savory-meat-loaf`, `snow-capped-meat-loaf`,
     `burgerwiches`, `never-a-lump-turkey-gravy`, `cranberry-cream-mold`,
     `five-minute-fudge`, `never-grainy-carnation-pumpkin-pie`
   - Source: `assets/loose_notes_scans/brw849e563cc961_000410.pdf`
   - Most flags are `[ESTIMATED]` on timing — verify against booklet

2. **Chef notebook — full recipes** (from pages with actual ingredient lists)
    - `buttermilk-biscuits` ✅, `vegan-biscuits` ✅, `rhubarb-syrup` ✅,
      `jiban` ✅, `marinated-olives` ✅, `aioli` ✅, `hummus` ✅, ~~`haydari-laban`~~ → `labneh` ✅,
      `sweet-chili-sauce` ✅, `shortrib-dry-rub` ✅, `kick-ass-cookies`, `budino`,
     `rosemary-syrup`, `curry-lentil-soup`, `spicy-bok-choy`, `open-face-mushroom-sammie`,
     `chimichurri-chicken-empanadas`, `empanada-dough-biscuit-dough`,
      `stuffed-fried-squash-blossoms` ✅, `broccoli`, `cold-smoked-baklava`, `ricotta`,
     `cannoli`, `grilled-radicchio`, `grilled-radicchio-with-carrot-ginger-glaze`,
     `bread-basics-golden-ratio`
   - Source: `assets/chef_recipe_book_draft/chef_recipe_notebook.md` + PDF
   - Cross-check transcription against original notebook images

3. **Classic cocktail standards** (the recipes are known)
   - `old-fashioned`, `manhattan`, `scotch-sour`, `stranahans-salty-stinger`,
     `highball`, `white-horse-replacement`, `op-cherry-blossom`
   - Source: chef notebook p.12, 18
   - Minimal flags — mostly just confirm specs against standard recipes

### Round 2: Title-Only Reconstructions (moderate difficulty)

These come from notebook pages that had only a title (the cook knew them by heart).
They were reconstructed from culinary knowledge but need verification:

- ~~`baba-ghanouj`~~ → `baba-ghanoush` — p.8, title only. ✅ REVIEWED: Eggplant cooked through, ratio confirmed.
- `tabbouleh` — p.8, title only. Parsley-to-bulgur ratio correct?
- `yufka` — p.7, title only. Is this flatbread or Turkish pastry?
- `pickling-base` — p.7, title only. Correct pickling formula?
- `dolma` — p.11, title only. Grape leaves or stuffed vegetables?
- `couscous` — p.11, title only ("Triad Couscous"). What three components?
- `rooz-m3-ful` — p.9. Rice with fava? Verify the dish identity.
- ~~`roa-kibbee-niyee`~~ → `kibbeh-niyee` — p.9. Raw kibbeh. ✅ REVIEWED: Lamb and bulgur amounts confirmed, bulgur cooked.
- `mih-sheh-enis-lah-a` — p.10. Stuffed vegetables with lamb? Verify.
- `hind-seh-milia` — p.10. Fried dandelion greens? Verify.
- `foie-gras` — p.21. Menu note, not a full recipe. Verify approach.

Also reference `chef_reconstruction_addendum.md` and
`chef_recipe_addendum_3.md` for cultural context and transliteration notes.

### Round 3: Illegible Cocktail Cards (hardest — need original scans)

These were transcribed from partially obscured handwritten guest checks. The recipe
structure is preserved but ingredients may be wrong:

- `berries-and-cream-highball` — multiple `[UNCLEAR]` ingredients
- `strawberry-cream-collins` — berry and cream components obscured
- `tortuga` — base spirit unclear
- `smith-and-cross-punch` — multiple `[UNCLEAR]` on juices and punch mix
- `dark-rum-pear-brandy-punch` — verify ingredients
- `breezy-beach-collins` — verify recipe
- `citrus-mug-punch` — verify ingredients
- `black-tea-orange-punch` — verify tea and syrup
- `orange-bitters-mug-punch` — syrup and title uncertain
- `mildly-herbaceous-old-fashioned` — verify herb component
- `life-preserver` — verify ingredients
- `road-to-nowhere` — verify recipe
- `ika-punch` — verify squid ink element
- `propane-and-propane-accessories` — verify recipe
- `kimchi-bloody-mary` — verify garnish and base

Source: `assets/loose_notes_scans/brw849e563cc961_000402.jpg` through `000407.jpg`

Also check `assets/recipe-legibility-help-images/` (if still present) for the two
still-unreadable cards.

### Round 4: Menu & Prep Stubs (context-dependent)

These are planning notes digitized as recipes — may need to be reclassified:

- `5-13-kat-dinner` — menu notes for a dinner, not a single recipe
- `6-21-pop-up-dinner-menu` — pop-up tasting menu, plating notes
- `legro-th-meal-prep` — shopping list / meal prep notes
- `oleo-saccharum` — technique note, verify method
- `clarified-juices` — freeze-clarification technique, verify ratio
- `ryu-confit-egg-yolk` — technique, verify method
- `yakiniku-salt-slab` — Wagyu on salt slab, verify approach

## Per-Recipe Review Checklist

For each recipe, resolve these in order:

1. [ ] **Title and identity** — Is the dish correctly identified?
2. [ ] **Source accuracy** — Does `source_name`, `source_page`, `origin_notes` match the source material?
3. [ ] **Ingredients** — Cross-check all amounts and units against source. Resolve `[UNCLEAR]` items.
4. [ ] **Instructions** — Verify technique against source. Ensure sensory cues and timing are correct.
5. [ ] **Timing** — Replace `[ESTIMATED]` with real values or leave as estimate but remove the flag if verified against source.
6. [ ] **Tags** — Confirm `cuisine/`, `diet/`, `technique/`, `protein/` tags are correct.
7. [ ] **Difficulty** — Verify rating against actual complexity.
8. [ ] **Servings & scaling** — Confirm `base_servings` and `scaling_notes`.

After all flags are resolved, change `status: draft` → `status: reviewed` and update
`date_modified`.

## Special Cases

### Transliteration Decisions

The chef notebook uses family spellings for Arabic dishes. `chef_recipe_addendum_3.md`
recommends preserving original notebook spellings (e.g., "Rooz M'Fal-fal" not "Riz ma' Ful").
Decide per recipe whether to standardize or preserve the family spelling. Current recipe
files mostly use notebook spellings — confirm this is intentional.

### Duplicate Sources

`kimchi-bloody-mary` appears in both the guest-check scan and the chef notebook (p.12).
The notebook version won as more complete. Verify no other recipes have this dual-source
situation.

### Missing Recipe

`cucumber-watermelon-tequila-cocktail` is referenced in the source map
(`brw849e563cc961_000404.jpg`) but was never digitized. Decide whether to create it.

## Review Progress

### Workflow Used

Each session processes one meal-type directory at a time. The reviewer (human + AI agent) works
through recipes using the **Per-Recipe Review Checklist** above. Common operations:
- Resolving `[ESTIMATED]`, `[UNCLEAR]`, `[TO VERIFY]` flags
- Renaming recipes for clarity (file moves + cross-reference updates across the full vault)
- Restructuring multi-batch recipes into variations
- Approving clean recipes with no flags

After each recipe, `status` is set to `reviewed` in the file frontmatter and the
`_meta/Digitization Log.md` is updated. All vault cross-references (MOCs, source files,
audit trail) are updated in the same session.

### Current Progress

| Metric | Count |
|--------|-------|
| Total recipes | 75 |
| Reviewed | 15 (21%) |
| Remaining | 60 |
| Empty directories | brunch, salad, soup |

### Completed

| # | Recipe | Slug | Action |
|---|--------|------|--------|
| 1 | Marinated Olives | `marinated-olives` | Clove resolved (ground), heating/blooming step added ✅ |
| 2 | Labneh | `labneh` | Renamed from Haydari/Laban, cheesecloth-strain method added ✅ |
| 3 | Stuffed Fried Squash Blossoms | `stuffed-fried-squash-blossoms` | Cheese → labneh, timing verified ✅ |
| 4 | Baba Ghanoush | `baba-ghanoush` | Renamed from Baba Ghanouj, eggplant cooked through ✅ |
| 5 | Kibbeh Ni'yee | `kibbeh-niyee` | Renamed from Roa Kibbee Ni'yee, bulgur cooked ✅ |
| 6 | Buttermilk Biscuits | `buttermilk-biscuits` | Clean transcription, approved ✅ |
| 7 | Vegan Biscuits | `vegan-biscuits` | Melted butter removed, approved ✅ |
| 8 | Rosemary Syrup | `rosemary-syrup` | No flags, approved ✅ |
| 9 | Shortrib Dry Rub | `shortrib-dry-rub` | Renamed from Jus BBQ Dry Rub, cayenne verified ✅ |
| 10 | Sweet Chili Sauce | `sweet-chili-sauce` | Approved ✅ |
| 11 | Hummus | `hummus` | Approved ✅ |
| 12 | Aioli | `aioli` | Renamed from Aioli Emé, timing verified ✅ |
| 13 | Jiban | `jiban` | Renamed from Jiban / Maza Cheese, timing verified ✅ |
| 14 | Rhubarb Syrup | `rhubarb-syrup` | Renamed from Rhubarb Syrup Experiment, restructured into Batch 1 (no water) and Batch 2 (with water) variations ✅ |
| 15 | Ricotta | `ricotta` | Approved ✅ |

### Remaining by Directory

| Directory | Total | Reviewed | Remaining | Status |
|-----------|-------|----------|-----------|--------|
| appetizer | 5 | 5 | 0 | 🟢 Done |
| breakfast | 2 | 2 | 0 | 🟢 Done |
| brunch | 0 | — | 0 | ⚪ Empty |
| condiment | 13 | 8 | 5 | 🟡 In progress |
| dessert | 6 | 0 | 6 | 🔴 Not started |
| dinner | 11 | 0 | 11 | 🔴 Not started |
| drink | 22 | 0 | 22 | 🔴 Not started |
| lunch | 4 | 0 | 4 | 🔴 Not started |
| salad | 0 | — | 0 | ⚪ Empty |
| side | 12 | 0 | 12 | 🔴 Not started |
| soup | 0 | — | 0 | ⚪ Empty |

### Remaining Condiment Recipes (next up)

| Recipe | Round | Flags |
|--------|-------|-------|
| Never-A-Lump Turkey Gravy | R1 Carnation | `[ESTIMATED]` timing & servings |
| Pickling Base | R2 Title-Only | `[TO VERIFY]` spices, `[ESTIMATED]` timing |
| Oleo Saccharum | R4 Prep Stub | `[ESTIMATED]` prep time |
| Clarified Juices | R4 Prep Stub | `[ESTIMATED]` timing |
| Ryu Confit Egg Yolk | R4 Prep Stub | `[TO VERIFY]` salt, low-confidence |

## Post-Review

After all flags are resolved:

1. Update `_meta/Digitization Log.md` — change status column from `draft` to `reviewed`
2. Verify all MOC Dataview queries pick up the reviewed recipes correctly
3. Archive the source scan files if no longer needed for reference
