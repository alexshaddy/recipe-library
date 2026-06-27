# Recipe Vault — Architecture & Setup Spec

A personal recipe library built as an Obsidian vault. Designed for a large, heterogeneous collection (handwritten cards, professional kitchen notes, cookbooks, URLs, family heirlooms) unified into a single searchable `.md` format.

---

## Vault Overview

| Property | Value |
|---|---|
| Vault name | `recipe-library` |
| Primary format | Markdown (`.md`) with YAML frontmatter |
| Navigation model | Folder hierarchy + YAML tags + Dataview queries + MOC hub notes |
| Plugin dependencies | Dataview, Templater, Tag Wrangler *(optional: Obsidian Kanban for digitization queue)* |
| Obsidian theme recommendation | Minimal or AnuPpuccin (clean, high readability for long-form content) |

---

## Folder Structure

```
recipe-library/
│
├── _inbox/                          # Drop zone for all unprocessed recipes
│   └── README.md
│
├── _templates/
│   └── recipe-template.md           # Master template (copy of the unified recipe .md)
│
├── _skills/
│   └── digitize-recipes-skill.md    # Agent skill file
│
├── _mocs/                           # Map of Content hub notes (one per primary axis)
│   ├── MOC — Meal Type.md
│   ├── MOC — Cuisine.md
│   ├── MOC — Dietary Tags.md
│   ├── MOC — Occasion & Season.md
│   ├── MOC — By Ingredient.md
│   └── MOC — Source & Provenance.md
│
├── recipes/
│   ├── breakfast/
│   ├── brunch/
│   ├── lunch/
│   ├── dinner/
│   ├── appetizer/
│   ├── side/
│   ├── soup/
│   ├── salad/
│   ├── dessert/
│   ├── drink/
│   └── condiment/
│
├── assets/
│   └── (reserved for future image support if needed)
│
└── _meta/
    ├── Digitization Log.md           # Track what's been processed, status, source batch
    ├── Tag Index.md                  # Reference list of all canonical tags in use
    └── Vault README.md              # This document (condensed)
```

### Placement Rules

- Every finalized recipe lives in `recipes/{{meal_type}}/{{slug}}.md`
- Recipes with multiple meal types go in the **primary** meal type folder; secondary types are captured via `meal_type` frontmatter array and Dataview picks them up everywhere else
- New/unprocessed recipes always land in `_inbox/` first — never directly into `recipes/`
- The `_inbox/` folder is the agent's working target; processed files get moved to the appropriate subfolder

---

## Frontmatter Tag Taxonomy

All tags use forward-slash namespacing for Obsidian's tag hierarchy. Use these canonical forms — do not invent new namespaces without updating `_meta/Tag Index.md`.

### Namespaces

| Namespace | Examples |
|---|---|
| `recipe/` | `recipe/dinner`, `recipe/dessert`, `recipe/condiment` |
| `cuisine/` | `cuisine/italian`, `cuisine/japanese`, `cuisine/american-southern` |
| `diet/` | `diet/vegan`, `diet/gluten-free`, `diet/dairy-free`, `diet/keto` |
| `technique/` | `technique/braise`, `technique/ferment`, `technique/bake`, `technique/raw` |
| `occasion/` | `occasion/holiday`, `occasion/meal-prep`, `occasion/entertaining`, `occasion/weeknight` |
| `season/` | `season/summer`, `season/winter`, `season/all-year` |
| `source/` | `source/cookbook`, `source/family-heirloom`, `source/professional-kitchen`, `source/url` |
| `status/` | `status/draft`, `status/reviewed`, `status/tested`, `status/archived` |
| `protein/` | `protein/chicken`, `protein/lamb`, `protein/seafood`, `protein/tofu` *(key ingredients only)* |

---

## MOC Structure

Each file in `_mocs/` is a **curated hub note** that combines:
1. A brief description of the category
2. Hand-curated featured/pinned recipes (internal links)
3. An embedded Dataview query that auto-populates the full list

### MOC Template

```markdown
# MOC — [Category Name]

Brief description of this category and how recipes are organized within it.

---

## ⭐ Featured

- [[recipe-slug]] — *one-line description*
- [[recipe-slug]] — *one-line description*

---

## All Recipes

\`\`\`dataview
TABLE meal_type, cuisine, prep_time, total_time, difficulty
FROM "recipes"
WHERE contains(tags, "recipe/dinner")    ← adjust per MOC
AND status != "archived"
SORT title ASC
\`\`\`
```

### MOC Files — Dataview Queries

**MOC — Meal Type.md**
```dataview
TABLE meal_type, cuisine, total_time, difficulty
FROM "recipes"
WHERE status != "archived"
SORT meal_type ASC, title ASC
```

**MOC — Cuisine.md**
```dataview
TABLE cuisine, meal_type, total_time
FROM "recipes"
WHERE status != "archived"
SORT cuisine ASC, title ASC
```

**MOC — Dietary Tags.md**
```dataview
TABLE dietary_tags, meal_type, cuisine
FROM "recipes"
WHERE status != "archived"
SORT title ASC
```

**MOC — Occasion & Season.md**
```dataview
TABLE occasion, season, meal_type
FROM "recipes"
WHERE status != "archived"
SORT occasion ASC
```

**MOC — By Ingredient.md**
*(Manually curated — Dataview full-text search on ingredients is unreliable. Maintain as a hand-linked index by primary protein or star ingredient.)*

**MOC — Source & Provenance.md**
```dataview
TABLE source_type, source_name, origin_notes, date_added
FROM "recipes"
WHERE status != "archived"
SORT source_type ASC, date_added DESC
```

---

## Obsidian Plugin Configuration

### Required Plugins

**Dataview**
- Enable JavaScript queries: `off` (standard DQL is sufficient)
- Inline queries: `on`
- Automatic view refreshing: `on`

**Templater**
- Template folder: `_templates/`
- Trigger on new file creation: `on`
- Auto-jump to cursor after insertion: `on`

### Recommended Plugins

| Plugin | Purpose |
|---|---|
| Tag Wrangler | Rename/merge tags across the vault without breaking links |
| Obsidian Kanban | Optional: visualize `_inbox/` as a digitization queue board |
| Natural Language Dates | Quick date entry in frontmatter |
| Linter | Auto-format YAML frontmatter on save (enforce consistent tag casing, date format, etc.) |

### Linter Configuration (if used)
```yaml
# Enforce in Linter settings:
yaml_key_sort: true
yaml_timestamp_date_modified: true
yaml_timestamp_format: "YYYY-MM-DD"
remove_yaml_keys_with_null_values: false   # keep empty fields — agents rely on them as targets
```

---

## Digitization Workflow

### Step 1 — Intake
Place raw source material reference (or description) into `_inbox/`. One file per recipe. Use the stub format:

```
_inbox/YYYY-MM-DD-source-description.md
```

Include a brief note at the top indicating the source type and any context:
```
source_type: handwritten
source_context: "Index card from Mom's recipe box, chicken dish, possibly Hungarian"
```

### Step 2 — Agent Processing
Feed the inbox file + source material (image, URL, text) to an AI agent with `digitize-recipes-skill.md` loaded. The agent outputs a complete, template-compliant `.md` file.

### Step 3 — Review
Open the output in Obsidian. Scan for `[TO VERIFY]`, `[UNCLEAR]`, and `[ESTIMATED]` flags. Resolve or accept each one. Change `status: draft` → `status: reviewed` when done.

### Step 4 — File
Move the file from `_inbox/` to `recipes/{{meal_type}}/{{slug}}.md`.

### Step 5 — Log
Add an entry to `_meta/Digitization Log.md`:

```markdown
| Date | Slug | Source Type | Source | Status |
|------|------|-------------|--------|--------|
| 2026-01-15 | braised-short-ribs | cookbook | The French Laundry Cookbook, p.142 | reviewed |
```

---

## Search Strategy

Obsidian's native search + Dataview covers all primary discovery paths:

| Discovery Intent | Method |
|---|---|
| "What's for dinner tonight?" | Open `MOC — Meal Type.md` → filter by `dinner` |
| "Something vegan and quick" | Tag search: `#diet/vegan` + `total_time < 30 min` (Dataview) |
| "Italian food" | Open `MOC — Cuisine.md` → scan `cuisine/italian` section |
| "What can I make with chicken?" | Open `MOC — By Ingredient.md` → `protein/chicken` section |
| "Holiday recipes" | Tag search: `#occasion/holiday` |
| "Recipes from Grandma" | Open `MOC — Source & Provenance.md` → filter `source_type: family-heirloom` |
| "Everything still in draft" | Dataview query: `WHERE status = "draft"` |
| "Recently added" | Dataview query: `SORT date_added DESC` |

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Recipe files | `kebab-case-title.md` | `braised-lamb-shoulder.md` |
| Inbox stubs | `YYYY-MM-DD-description.md` | `2026-06-01-moms-chicken-paprikash.md` |
| MOC files | `MOC — Category Name.md` | `MOC — Meal Type.md` |
| Tags | `namespace/value` all lowercase, hyphens for spaces | `cuisine/american-southern` |
| Dates in frontmatter | `YYYY-MM-DD` | `2026-06-26` |

---

## Initial Setup Checklist

- [ ] Create vault folder: `recipe-library/`
- [ ] Create all folders per structure above
- [ ] Copy `recipe-template.md` into `_templates/`
- [ ] Copy `digitize-recipes-skill.md` into `_skills/`
- [ ] Install Dataview, Templater plugins
- [ ] Configure Templater to point at `_templates/`
- [ ] Create each MOC file in `_mocs/` with baseline Dataview queries
- [ ] Create `_meta/Digitization Log.md` with header row
- [ ] Create `_meta/Tag Index.md` with canonical tag list (seed from Tag Taxonomy above)
- [ ] Create `_meta/Vault README.md` (condensed version of this spec)
- [ ] Add first batch of inbox stubs from physical collection
- [ ] Run first digitization pass with agent + skill file
