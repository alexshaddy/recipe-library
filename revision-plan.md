# Recipe Revision Plan

All 75 recipes need a pass. 15 are reviewed but most of those still have thin instructions. 60 are draft with ~208 unresolved flags. This plan covers what to fix and in what order.

---

## The Problem

Most recipes are **skeletal**: 3 vague instruction steps, no sensory cues, missing sub-ingredients, and placeholder notes. The digitization skill spec requires bolded action titles, sensory cues, inline timing, grouped ingredients, and substantive cook's notes — almost none of the 60 drafts meet that bar. Several also have **ingredient mismatches** against the source notebook.

---

## Tier 1 — Source Mismatch Fixes (ingredient data is wrong)

These recipes have specific source data in the notebook transcription but the recipe files diverge from it. Fix the ingredients first, then expand the instructions.

| Recipe | File | Problem |
|--------|------|---------|
| Ricotta | `condiment/ricotta.md` | Notebook says ½ gallon 2% milk + ½ cup lemon juice + 1 tsp salt. Recipe says 1 gallon milk + 1 cup cream [ESTIMATED] + ¼ cup acid [ESTIMATED]. Wrong amounts, invented cream. |
| Sweet Chili Sauce | `condiment/sweet-chili-sauce.md` | Notebook says ¼ cup rice vinegar, ¼ cup water, ¼ cup sugar, 1.5 tbsp sambal oelek, cornstarch slurry. Recipe says 1 cup sugar, ½ cup vinegar, ½ cup water, 2 tbsp chile flakes. Completely different ratios and missing the sambal and cornstarch. Status is "reviewed" but ingredients are wrong. |
| Ryu Confit Egg Yolk | `condiment/ryu-confit-egg-yolk.md` | Notebook describes confit at 160°F/71°C for ~55 min in oil with sesame oil, chili flakes, gochugaru. Recipe is a 2-step stub with just "1 egg yolk" and "salt [TO VERIFY]". The actual method is completely missing. |
| Pickling Base | `condiment/pickling-base.md` | Notebook specifies white wine vinegar or rice wine vinegar plus optional aromatics (peppercorns, bay leaf, garlic, mustard seed, red pepper flakes). Recipe just says "vinegar" and "spices [TO VERIFY]". |
| Yakiniku Salt Slab | `dinner/yakiniku-salt-slab.md` | Notebook describes A5 Wagyu on Himalayan salt slab with bordelaise (¾ cup), thyme (¼ tsp), nori bordelaise variant, negi bed, 2 cups beef stock, shallots. Recipe likely has generic placeholder ingredients. |
| Dolma | `dinner/dolma.md` | Reconstruction addendum confirms grape-leaf dolma with lamb/rice/cinnamon/allspice. Recipe has the right idea but needs lemon juice, fresh herbs (mint, dill), and the technique of lining the pot bottom with extra leaves. |

**Action**: Replace ingredient lists with notebook-accurate data. Expand instructions to 5–8 steps with sensory cues. Update `date_modified` to `2026-06-27`.

---

## Tier 2 — Title-Only Reconstructions (thin but identifiable)

These were title-only notebook pages reconstructed from culinary knowledge. They currently have 3-step placeholder instructions and generic ingredients. Each needs expansion into a real, cookable recipe using the reconstruction addendum and addendum III as guides.

| Recipe | File | What to expand |
|--------|------|----------------|
| Tabbouleh | `side/tabbouleh.md` | Addendum says 4:1:¼ parsley:tomato:bulgur ratio, heavy lemon and olive oil. Current recipe likely has a generic ratio. Expand to proper Lebanese tabbouleh with mint, green onion, specific lemon/oil amounts. 5–6 steps. |
| Yufka | `side/yufka.md` | Addendum says 500g flour, 325g water, 10g salt, roll extremely thin, cook on convex steel. Expand with resting time, rolling technique, cooking on inverted wok or saj, stacking between towels. |
| Couscous | `side/couscous.md` | "Triad Couscous" — addendum's best guess is pearl couscous + toasted nuts + dried fruit + herbs. Needs a real method: toast the couscous, hydrate, fold in components. Currently has [ESTIMATED] garnish placeholders. |
| Rooz M3 Ful | `dinner/rooz-m3-ful.md` | Addendum says rice with fava beans, onion in butter/ghee, cinnamon, allspice, finish with browned butter and parsley. Needs full pilaf method: rinse rice, soak favas, layer, steam. |
| Mih-Sheh Enis Lah'a | `side/mih-sheh-enis-lah-a.md` | Mahshi bi Lahmeh — stuffed vegetables (zucchini, small eggplant, peppers) with lamb/rice/cinnamon/allspice filling, cooked in tomato broth with lemon. Currently a stub. Needs coring technique, filling ratio, pot arrangement, cooking time. |
| Hind-Seh Mi'lia | `side/hind-seh-milia.md` | Hindbeh Mqliyeh — fried dandelion greens with caramelized onions, olive oil, lemon, pine nuts. Served room temp as mezze. Needs blanching step, caramelization time, assembly. |
| Foie Gras | `dinner/foie-gras.md` | Pop-up dinner menu note. Needs a sear method: score, season, hot dry pan, 90 seconds per side, deglaze with vinegar or port. Currently likely a menu stub. |

**Action**: Rewrite each with full ingredient lists (specific amounts), 5–8 instruction steps with bolded titles and sensory cues, and substantive cook's notes. Reference the reconstruction addendum for cultural context.

---

## Tier 3 — Notebook Recipes Needing Expansion (source exists, instructions thin)

These have real source data in the notebook but the recipe files are skeletal — typically 3 generic steps with no technique detail.

### Condiments & Sauces
| Recipe | File | Expand |
|--------|------|--------|
| Oleo Saccharum | `condiment/oleo-saccharum.md` | Notebook: 50g orange peel + 200g sugar + 200mL hot water. Add muddling detail, timing for oil extraction (1–2 hrs), straining technique. |
| Clarified Juices | `condiment/clarified-juices.md` | Two methods in notebook (acidic agar + freeze-clarification). Both need full step-by-step with temperatures, timing, cheesecloth setup. |
| Hummus | `condiment/hummus.md` | Has notebook ingredients. Expand method: cooking chickpeas, ice bath for skins, tahini-first blending order, lemon/garlic balance, texture cues. |
| Jiban | `condiment/jiban.md` | Already reviewed but check if instructions are still 3-step. |

### Desserts
| Recipe | File | Expand |
|--------|------|--------|
| Kick-Ass Cookies | `dessert/kick-ass-cookies.md` | Notebook p.15. Expand creaming method, chill time, bake temp/time, doneness cues. |
| Budino | `dessert/budino.md` | Notebook p.15. Italian pudding — expand custard cooking, tempering technique, chilling. |
| Cannoli | `dessert/cannoli.md` | Notebook p.24 has filling (ricotta) and shell as separate components. Expand shell frying, filling assembly, serving. Shell amounts are [ESTIMATED]. |

### Sides
| Recipe | File | Expand |
|--------|------|--------|
| Curry Lentil Soup | `side/curry-lentil-soup.md` | Notebook p.17. Expand: bloom spices, sweat aromatics, simmer lentils, blending decision, garnish. |
| Spicy Bok Choy | `side/spicy-bok-choy.md` | Notebook p.18. Add wok technique, heat level, soy/sesame amounts from source. Currently has [TO VERIFY] on chili flakes. |
| Broccoli | `side/broccoli.md` | From 6.21 pop-up dinner. Likely Sicilian-style (sugar + vinegar agrodolce, per addendum III). Currently generic. Add the agrodolce angle. |
| Cold-Smoked Baklava | `side/cold-smoked-baklava.md` | Has 5 [TO VERIFY] flags. This is the most uncertain recipe. Notebook says "Cold Smoked Bok Lava?" — the dish identity itself is uncertain. Decide: is this cold-smoked baklava or something else? Write a real method if baklava, or add a prominent warning. |
| Grilled Radicchio | `side/grilled-radicchio.md` | Simple grill technique but needs timing, char level, dressing detail. |
| Grilled Radicchio w/ Carrot-Ginger Glaze | `side/grilled-radicchio-with-carrot-ginger-glaze.md` | Notebook p.24 lists components including chanterelle powder [TO VERIFY]. Expand glaze-making, grilling, plating. |
| Bread Basics Golden Ratio | `side/bread-basics-golden-ratio.md` | 5:3 flour:water ratio from notebook. Expand into a real bread recipe: mixing, kneading, bulk rise, shaping, bake temp. Currently has [TO VERIFY] on yeast. |

### Dinner
| Recipe | File | Expand |
|--------|------|--------|
| Chimichurri Chicken Empanadas | `dinner/chimichurri-chicken-empanadas.md` | Notebook p.19 has chimichurri recipe (100g cilantro, 100g parsley, 100g RWV, ~6 cloves garlic, EVOO) plus chicken filling plus dough. Expand all three components. |
| Empanada Dough / Biscuit Dough | `dinner/empanada-dough-biscuit-dough.md` | Notebook p.19. A dough recipe needing mixing, resting, rolling detail. Water amount is [ESTIMATED]. |

### Lunch
| Recipe | File | Expand |
|--------|------|--------|
| Open-Face Mushroom Sammie | `lunch/open-face-mushroom-sammie.md` | Notebook p.18. Expand sautéing technique, bread choice, assembly, herbs [TO VERIFY]. |

**Action**: For each, read the notebook source section, align ingredients exactly, then expand instructions to 5–8 steps. Add sensory cues and timing.

---

## Tier 4 — Guest-Check Cocktails (illegible source, need best-effort resolution)

15 cocktails from scanned guest checks. Many have [UNCLEAR] ingredients. The source images are at `assets/loose_notes_scans/brw849e563cc961_000402.jpg` through `000407.jpg`. These need creative resolution — use the cocktail name, era, bar context (Mockingbird Bar), and standard cocktail construction to resolve unclear ingredients into plausible specs.

### High-UNCLEAR count (4+ unclear items each)
| Recipe | File | Unclear Items |
|--------|------|---------------|
| Berries and Cream Highball | `drink/berries-and-cream-highball.md` | 4 UNCLEAR: strawberry spirit, berry component, cream component, bitters type |
| Strawberry Cream Collins | `drink/strawberry-cream-collins.md` | 4 UNCLEAR: similar berry/cream ambiguity |
| Tortuga | `drink/tortuga.md` | 4 UNCLEAR: base spirit and modifiers |
| Smith and Cross Punch | `drink/smith-and-cross-punch.md` | 5 UNCLEAR: juices and punch mix components |

### Medium-UNCLEAR count (1–2 unclear items)
| Recipe | File | Unclear Items |
|--------|------|---------------|
| Mildly Herbaceous Old Fashioned | `drink/mildly-herbaceous-old-fashioned.md` | 2 UNCLEAR: herb component |
| Black Tea Orange Punch | `drink/black-tea-orange-punch.md` | 1 UNCLEAR |
| Citrus Mug Punch | `drink/citrus-mug-punch.md` | 1 UNCLEAR |
| Dark Rum Pear Brandy Punch | `drink/dark-rum-pear-brandy-punch.md` | 1 UNCLEAR |
| Ika Punch | `drink/ika-punch.md` | 1 UNCLEAR |
| Orange Bitters Mug Punch | `drink/orange-bitters-mug-punch.md` | 1 UNCLEAR |

### No UNCLEAR but still need expansion
| Recipe | File | Issue |
|--------|------|-------|
| Breezy Beach Collins | `drink/breezy-beach-collins.md` | Thin instructions |
| Life Preserver | `drink/life-preserver.md` | Thin instructions |
| Road to Nowhere | `drink/road-to-nowhere.md` | Thin instructions |
| Propane and Propane Accessories | `drink/propane-and-propane-accessories.md` | Thin instructions |

**Action**: For UNCLEAR items, make a best-effort resolution based on cocktail name, era, and standard construction. Replace `[UNCLEAR]` with resolved ingredients and add a cook's note explaining the interpretation. Expand all instructions to include build method, glassware, garnish, and ice specification.

---

## Tier 5 — Notebook Cocktails (source exists, need minor expansion)

These 8 cocktails from notebook p.12 and p.18 have real source data but still need instruction expansion and flag resolution.

| Recipe | File | Issue |
|--------|------|-------|
| Highball | `drink/highball.md` | Spirit is [TO VERIFY] — notebook says spirit is unclear. Resolve or note. Expand build method. |
| White Horse Replacement | `drink/white-horse-replacement.md` | Umeshu/plum wine tea [TO VERIFY], simple syrup [ESTIMATED]. Resolve from notebook. |
| OP Cherry Blossom | `drink/op-cherry-blossom.md` | Notebook: OGD bourbon + sakura tea syrup + Regans' bitters. Verify alignment, expand. |
| Kimchi Bloody Mary | `drink/kimchi-bloody-mary.md` | Notebook is HIGH confidence: 4oz kimchi base, 2oz vodka, 0.5oz ginger, 0.5oz lemon, optional spicy sauce. Garnish [ESTIMATED]. Expand with batch bloody mix method. |
| Manhattan | `drink/manhattan.md` | Standard cocktail, just needs instruction expansion. |
| Old Fashioned | `drink/old-fashioned.md` | Standard cocktail, just needs instruction expansion. |
| Scotch Sour | `drink/scotch-sour.md` | Egg white [ESTIMATED]. Standard sour build, expand with dry shake technique. |
| Stranahan's Salty Stinger | `drink/stranahans-salty-stinger.md` | Citrus [TO VERIFY], honey syrup [ESTIMATED]. Resolve from notebook context. |

**Action**: Align with notebook, resolve flags, expand instructions to proper cocktail spec format (build, shake/stir, strain, glassware, garnish).

---

## Tier 6 — Carnation Booklet Recipes (full source, timing flags only)

9 recipes from the Carnation evaporated milk pamphlet. Source PDF is at `assets/loose_notes_scans/brw849e563cc961_000410.pdf`. These have complete ingredient lists and instructions but [ESTIMATED] timing values.

| Recipe | File |
|--------|------|
| Chiliburgers | `dinner/chiliburgers.md` |
| Party Sandwich Loaf | `lunch/party-sandwich-loaf.md` |
| Savory Meat Loaf | `dinner/savory-meat-loaf.md` |
| Snow-Capped Meat Loaf | `dinner/snow-capped-meat-loaf.md` |
| Burgerwiches | `lunch/burgerwiches.md` |
| Never-a-Lump Turkey Gravy | `condiment/never-a-lump-turkey-gravy.md` |
| Cranberry Cream Mold | `dessert/cranberry-cream-mold.md` |
| Five-Minute Fudge | `dessert/five-minute-fudge.md` |
| Never-Grainy Carnation Pumpkin Pie | `dessert/never-grainy-carnation-pumpkin-pie.md` |

**Action**: Verify timing against the Carnation PDF source. Even if we can't read the PDF programmatically, these are standard mid-century American recipes — the timings are conventional and can be confirmed. Expand instructions if they're still 3-step. Add sensory cues. Remove [ESTIMATED] flags from timing if confirmed reasonable.

---

## Tier 7 — Menu Stubs & Prep Notes (structural decisions needed)

These aren't single recipes — they're planning documents digitized as recipes. They need a decision: keep as-is with a clear "menu note" designation, or extract individual components.

| Recipe | File | Decision |
|--------|------|----------|
| 5-13 Kat Dinner | `dinner/5-13-kat-dinner.md` | Menu planning note. Keep as reference, ensure it links to the extracted recipes (yakiniku, confit egg yolk, chimichurri). Mark as `status: archived` or add a menu tag. |
| 6-21 Pop-Up Dinner Menu | `dinner/6-21-pop-up-dinner-menu.md` | Pop-up tasting menu. Same treatment — keep as reference, link to extracted components (foie gras, broccoli, cold-smoked baklava, squash blossoms). |
| Legro-th Meal Prep | `lunch/legro-th-meal-prep.md` | Shopping list / meal prep notes. Expand into a real prep guide with the three components (bacon fried rice, pasta, sautéed mushrooms+veg) written as actual mini-recipes within the file. |

**Action**: Add `occasion: menu-planning` tag to the dinner menus. Ensure linked recipes exist and are cross-referenced. Expand Legro-th into a usable prep guide.

---

## Tier 8 — Already Reviewed (spot-check only)

15 recipes already marked `status: reviewed`. Spot-check that instructions aren't still 3-step stubs despite being "reviewed."

| Recipe | File |
|--------|------|
| Buttermilk Biscuits | `breakfast/buttermilk-biscuits.md` |
| Vegan Biscuits | `breakfast/vegan-biscuits.md` |
| Rhubarb Syrup | `condiment/rhubarb-syrup.md` |
| Jiban | `condiment/jiban.md` |
| Marinated Olives | `appetizer/marinated-olives.md` |
| Aioli | `condiment/aioli.md` |
| Hummus | `condiment/hummus.md` |
| Labneh | `appetizer/labneh.md` |
| Baba Ghanoush | `appetizer/baba-ghanoush.md` |
| Kibbeh Ni'yee | `appetizer/kibbeh-niyee.md` |
| Stuffed Fried Squash Blossoms | `appetizer/stuffed-fried-squash-blossoms.md` |
| Rosemary Syrup | `condiment/rosemary-syrup.md` |
| Shortrib Dry Rub | `condiment/shortrib-dry-rub.md` |
| Sweet Chili Sauce | `condiment/sweet-chili-sauce.md` |
| Ricotta | `condiment/ricotta.md` |

> [!WARNING]
> Sweet Chili Sauce and Ricotta are marked "reviewed" but have **wrong ingredient amounts** vs the notebook source. These need to go back to Tier 1.

**Action**: Read each reviewed recipe. If instructions are 3 steps or fewer, expand. Fix any remaining source mismatches (Sweet Chili Sauce, Ricotta are confirmed wrong).

---

## Per-Recipe Expansion Checklist

When expanding any recipe, apply all of these:

1. **Ingredients**: Align with source. Remove [ESTIMATED] / [UNCLEAR] / [TO VERIFY] by resolving them. Group into sub-components if multi-part. Use the format `- [ ] \`amount\` — ingredient, prep note`.
2. **Instructions**: Minimum 5 steps for any real recipe. Each step gets a **bolded action title**, a sensory cue (color, texture, sound, aroma), and inline timing in italics.
3. **Cook's Notes**: At least 2 substantive notes — technique tips, pitfalls, or cultural context. Not just "this recipe is from a notebook."
4. **Variations**: At least 1 meaningful variation.
5. **Make-Ahead / Storage**: Specific fridge/freezer life, not "refrigerate and use quickly."
6. **Scaling**: Specific guidance on what breaks when you scale.
7. **Timing**: Replace [ESTIMATED] with resolved values. For title-only reconstructions, provide realistic estimates and drop the flag.
8. **Frontmatter**: Verify `cuisine`, `dietary_tags`, `tags` are correct. Add `technique/` and `protein/` tags where missing.
9. **Status**: Change `draft` → `reviewed` after expansion. Update `date_modified`.

---

## Execution Order

1. **Tier 1** first — these have wrong data and are the most urgent
2. **Tier 2** next — these are the thinnest recipes
3. **Tier 3** in batches by category (condiments → desserts → sides → dinner → lunch)
4. **Tier 4–5** cocktails as a batch
5. **Tier 6** Carnation recipes as a batch
6. **Tier 7** menu stubs last
7. **Tier 8** spot-check pass at the end

---

## Summary

| Tier | Count | Severity | Work |
|------|-------|----------|------|
| 1 — Source mismatches | 6 | 🔴 Wrong data | Fix ingredients, rewrite instructions |
| 2 — Title-only reconstructions | 7 | 🔴 Skeletal | Full recipe creation from addendum |
| 3 — Thin notebook recipes | 17 | 🟡 Incomplete | Expand from source, 5–8 steps |
| 4 — Guest-check cocktails | 15 | 🟡 Illegible source | Best-effort resolution + expansion |
| 5 — Notebook cocktails | 8 | 🟢 Minor flags | Align + expand |
| 6 — Carnation recipes | 9 | 🟢 Timing only | Verify timing, expand if thin |
| 7 — Menu stubs | 3 | 🟢 Structural | Decide format, link, tag |
| 8 — Reviewed spot-check | 15 | 🟢 Verify | Quick read, fix if thin |
| **Total** | **75** (some counted in multiple tiers) | | |

*Estimated scope: every recipe file gets touched. ~45 need substantive rewrites, ~20 need moderate expansion, ~10 need minor fixes.*
