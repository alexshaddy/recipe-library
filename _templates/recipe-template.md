---
# ── IDENTITY ──────────────────────────────────────────────
title: "Recipe Title"
aliases: []                          # alternate names, nicknames
slug: recipe-title                   # kebab-case, used for filename

# ── CLASSIFICATION ────────────────────────────────────────
meal_type:                           # primary sort axis
  - dinner                           # breakfast | brunch | lunch | dinner | snack | dessert | drink | condiment | side | appetizer
cuisine: []                          # italian | mexican | american | japanese | french | etc.
course: []                           # soup | salad | main | bread | sauce | pastry | etc.
dietary_tags: []                     # vegan | vegetarian | gluten-free | dairy-free | keto | paleo | nut-free | etc.
occasion: []                         # weeknight | meal-prep | holiday | entertaining | comfort | quick | etc.
season: []                           # spring | summer | fall | winter | all-year

# ── TIMING ────────────────────────────────────────────────
prep_time: ""                        # e.g. "20 min"
cook_time: ""                        # e.g. "45 min"
inactive_time: ""                    # rest, marinate, chill, proof — e.g. "1 hr"
total_time: ""                       # sum of above

# ── SERVINGS & SCALING ────────────────────────────────────
base_servings: 4
serving_unit: "portions"             # portions | cups | pieces | oz | etc.
scaling_notes: ""                    # "dough does not scale above 2x" | "sauce scales freely" | etc.

# ── SOURCE & PROVENANCE ───────────────────────────────────
source_type: ""                      # handwritten | magazine-clipping | cookbook | url | memory | professional-kitchen | family-heirloom | dictation
source_name: ""                      # cookbook title, publication, website name, person's name
source_url: ""                       # leave blank if not applicable
source_page: ""                      # page number if from a book
origin_notes: ""                     # "Grandma Ruth's recipe, circa 1970s" | "from my time at XYZ restaurant" | etc.

# ── DIFFICULTY & EQUIPMENT ────────────────────────────────
difficulty: ""                       # easy | medium | hard | professional
key_equipment: []                    # stand-mixer | dutch-oven | wok | cast-iron | sheet-pan | etc.

# ── METADATA ──────────────────────────────────────────────
tags: []                             # free-form Obsidian tags, prefixed: recipe/dinner, technique/braise, etc.
status: draft                        # draft | reviewed | tested | archived
date_added: 2026-01-01
date_modified: 2026-01-01
---

# {{title}}

> [!NOTE] Origin
> {{origin_notes}}

---

## Ingredients

*Base servings: {{base_servings}} {{serving_unit}}*

### Group Name *(remove if single group)*

- [ ] `amount` unit — ingredient name, prep note *(e.g. 2 cups all-purpose flour, sifted)*
- [ ] `amount` unit — ingredient name
- [ ] `amount` unit — ingredient name

### Group Name

- [ ] `amount` unit — ingredient name
- [ ] `amount` unit — ingredient name

---

## Instructions

1. **Step title.** Detailed instruction. Include visual and sensory cues where relevant — color, texture, smell, sound. Note timing inline *(~5 min)*.

2. **Step title.** Detailed instruction.

3. **Step title.** Detailed instruction.

---

## Notes & Variations

### Cook's Notes
- Key technique insight, professional tip, or pitfall to avoid.

### Variations
- **Variation name:** Description of the variation and what changes.

### Make-Ahead / Storage
- Storage instructions and shelf life.
- Freezer guidance if applicable.

### Scaling
- {{scaling_notes}}

---

## Linked Recipes

- [[recipe-slug]] — *brief description of relationship (e.g. "base dough used here")*

---

*Source: {{source_name}}{{#source_page}}, p.{{source_page}}{{/source_page}} · Added: {{date_added}}*
