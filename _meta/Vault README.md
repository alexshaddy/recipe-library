# Recipe Library — Vault README

A personal recipe library built as an Obsidian vault. Designed for a large, heterogeneous collection (handwritten cards, professional kitchen notes, cookbooks, URLs, family heirlooms) unified into a single searchable `.md` format.

## Quick Start

1. **Add a recipe**: Drop a stub file into `_inbox/` with source context.
2. **Digitize**: Use the digitization agent with `_skills/digitize-recipes-skill.md` to convert it to a full recipe.
3. **Review**: Open in Obsidian, resolve `[TO VERIFY]` flags, change status to `reviewed`.
4. **File**: Move to `recipes/{{meal_type}}/{{slug}}.md`.
5. **Log**: Add an entry to `_meta/Digitization Log.md`.

## Folder Structure

| Folder | Purpose |
|---|---|
| `_inbox/` | Drop zone for unprocessed recipes |
| `_templates/` | Master recipe template |
| `_skills/` | Agent skill files for digitization |
| `_mocs/` | Map of Content hub notes (browse by meal type, cuisine, diet, etc.) |
| `recipes/` | Finalized recipes organized by meal type |
| `assets/` | Reserved for future image support |
| `_meta/` | Vault metadata — digitization log, tag index, this README |

## Navigation

- **By meal type**: Open `_mocs/MOC — Meal Type.md`
- **By cuisine**: Open `_mocs/MOC — Cuisine.md`
- **By dietary needs**: Open `_mocs/MOC — Dietary Tags.md`
- **By occasion/season**: Open `_mocs/MOC — Occasion & Season.md`
- **By ingredient**: Open `_mocs/MOC — By Ingredient.md`
- **By source**: Open `_mocs/MOC — Source & Provenance.md`

## Required Plugins

- **Dataview** — powers the MOC auto-populating queries
- **Templater** — auto-applies `_templates/recipe-template.md` on new recipe creation

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Recipe files | `kebab-case-title.md` | `braised-lamb-shoulder.md` |
| Inbox stubs | `YYYY-MM-DD-description.md` | `2026-06-01-moms-chicken-paprikash.md` |
| MOC files | `MOC — Category Name.md` | `MOC — Meal Type.md` |
| Tags | `namespace/value` lowercase, hyphens | `cuisine/american-southern` |
| Dates | `YYYY-MM-DD` | `2026-06-26` |