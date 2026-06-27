# Inbox

This is the drop zone for all unprocessed recipes. Every new recipe — whether from a handwritten card, cookbook page, URL, dictation, or memory — lands here first before being digitized and filed into `recipes/`.

## How It Works

1. **Intake**: Create a stub file in this folder for each recipe you want to digitize. Use the naming convention `YYYY-MM-DD-description.md` (e.g., `2026-06-26-moms-chicken-paprikash.md`).
2. **Digitize**: Feed the stub + source material to the digitization agent (using `_skills/digitize-recipes-skill.md`). The agent outputs a complete, template-compliant `.md` file.
3. **Review**: Open the output in Obsidian. Scan for `[TO VERIFY]`, `[UNCLEAR]`, and `[ESTIMATED]` flags. Resolve or accept each one. Change `status: draft` → `status: reviewed` when done.
4. **File**: Move the finalized file from `_inbox/` to `recipes/{{meal_type}}/{{slug}}.md`.
5. **Log**: Add an entry to `_meta/Digitization Log.md`.

## Stub Format

```markdown
source_type: handwritten
source_context: "Index card from Mom's recipe box, chicken dish, possibly Hungarian"
```

Keep stubs minimal — just enough context for the digitization agent to understand what it's working with.