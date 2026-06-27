#!/usr/bin/env python3
"""
TICKET-027: Expand Cold-Smoked Baklava from notebook source.

Validates `recipes/side/cold-smoked-baklava.md` against:
  - TICKET-027 requirements
  - docs/specs/027-cold-smoked-baklava.md spec
  - Notebook p.22 ambiguous entry "Cold Smoked Bok Lava?"
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/cold-smoked-baklava.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/side/cold-smoked-baklava.md")
    return fm, content


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    cuisines_lower = [c.lower() for c in cuisines]
    for exp in ["middle eastern", "turkish", "modern"]:
        assert any(exp in c for c in cuisines_lower), \
            f"Expected cuisine containing '{exp}', got {cuisines}"
    print("  ✓ Cuisine: Middle Eastern, Turkish, Modern")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    assert "vegetarian" in dt, f"Expected dietary_tags to contain 'vegetarian', got {dt}"
    print("  ✓ Dietary tags: vegetarian")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["dessert", "baklava", "phyllo", "nuts", "technique-cold-smoke", "technique-baking"]:
        assert any(exp in t.lower() for t in tags), f"Missing tag containing '{exp}', got {tags}"
    print("  ✓ Tags: dessert, baklava, phyllo, nuts, cold-smoke, baking")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert len(protein) == 0, f"Expected protein to be empty, got {protein}"
    print("  ✓ Protein: [none]")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_difficulty(fm):
    diff = fm.get("difficulty", "")
    assert diff == "advanced", f"Expected difficulty 'advanced', got '{diff}'"
    print("  ✓ Difficulty: advanced")


def test_frontmatter_fields(fm):
    for field in ["title", "slug", "meal_type", "cuisine", "course",
                  "dietary_tags", "season",
                  "prep_time", "cook_time", "inactive_time", "total_time",
                  "base_servings", "serving_unit", "scaling_notes",
                  "source_type", "source_name", "origin_notes",
                  "difficulty", "key_equipment", "tags", "protein",
                  "status", "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    print("  ✓ All required frontmatter fields present")


def test_source_documented(fm):
    assert fm.get("source_type") == "handwritten", \
        f"Expected source_type 'handwritten', got '{fm.get('source_type')}'"
    assert "Notebook" in fm.get("source_name", ""), \
        f"Expected source_name containing 'Notebook', got '{fm.get('source_name')}'"
    assert fm.get("source_page") == "22", \
        f"Expected source_page '22', got '{fm.get('source_page')}'"
    print("  ✓ Source documented: handwritten — Chef's Recipe Notebook p.22")


def test_ingredient_groups(content):
    assert "### For the Cold Smoke" in content, "Missing 'Cold Smoke' ingredient group"
    assert "### Nut Filling" in content, "Missing 'Nut Filling' ingredient group"
    assert "### Phyllo Assembly" in content, "Missing 'Phyllo Assembly' ingredient group"
    assert "### Syrup (Atter)" in content, "Missing 'Syrup (Atter)' ingredient group"
    assert "### Garnish" in content, "Missing 'Garnish' ingredient group"
    print("  ✓ Ingredient groups: Cold Smoke, Nut Filling, Phyllo Assembly, Syrup, Garnish")


def test_ingredients_content(content):
    lower = content.lower()
    for item in ["phyllo", "nuts", "sugar", "cinnamon", "butter", "rose water"]:
        assert item in lower, f"Missing ingredient: {item}"
    print("  ✓ Key ingredients present: phyllo, nuts, sugar, cinnamon, butter, rose water")


def test_resolves_bok_lava(content):
    """Verify the recipe addresses the notebook's ambiguous "Cold Smoked Bok Lava?" entry."""
    assert "cold smoked bok lava" in content.lower() or "bok lava" in content.lower(), \
        "Missing reference to notebook's 'Bok Lava' ambiguity"
    assert "editorial" in content.lower(), "Missing editorial decision documentation"
    print("  ✓ Resolves notebook ambiguous entry 'Cold Smoked Bok Lava?'")


def test_instructions(content):
    # Recipe has 14 steps grouped into 4 phases — exceeds usual bounds
    n, titles, sensory = check_instructions(content, min_steps=12, max_steps=16)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, {len(sensory)} sensory cues")


def test_inline_timing(content):
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)
    timing = re.findall(r"\d+\s*(?:min(?:ute)?s?|hour|hr|sec)s?", instr_section, re.IGNORECASE)
    assert len(timing) >= 4, f"Too few timing cues: {len(timing)}"
    print(f"  ✓ Inline timing: {len(timing)} instances")


def test_notes(content):
    nb, vb = check_notes(content, min_cooks=2, min_variations=1)
    print(f"  ✓ Notes: {nb} cook's notes, {vb} variations, make-ahead, storage, scaling")


def test_variations_specific(content):
    lower = content.lower()
    for var in ["walnut-rose", "pistachio-cardamom", "chocolate-dipped", "savory"]:
        assert var in lower, f"Missing variation: {var}"
    print("  ✓ Variations: Walnut-Rose, Pistachio-Cardamom, Chocolate-Dipped, Savory")


def test_cold_smoke_technique(content):
    lower = content.lower()
    for term in ["cold smoke", "68", "86", "phyllo", "nut"]:
        assert term in lower, f"Missing cold smoke technique reference: {term}"
    assert "temperature" in lower, "Missing temperature discussion"
    print("  ✓ Cold smoke technique with temperature control")


def test_syrup_technique(content):
    lower = content.lower()
    assert "hot baklava" in lower or "cool syrup" in lower, \
        "Missing hot baklava + cool syrup temperature differential"
    assert "shatter" in lower, "Missing 'shatter' texture description"
    print("  ✓ Syrup temperature differential technique")


def test_sections(content):
    required = ["## Ingredients", "## Instructions", "## Notes & Variations",
                "### Cook's Notes", "### Variations", "### Scaling"]
    for h in required:
        assert h in content, f"Missing heading: {h}"
    assert "Make-Ahead" in content, "Missing Make-Ahead"
    assert "Storage" in content, "Missing Storage"
    print("  ✓ All required sections present")


def test_origin_note(content):
    assert "Notebook" in content and "p. 22" in content, \
        "Missing notebook origin reference"
    print("  ✓ Origin note references notebook page 22")


def test_phases_in_instructions(content):
    """Verify the 4 phases are present in the instructions."""
    for phase in ["Phase 1:", "Phase 2:", "Phase 3:", "Phase 4:"]:
        assert phase in content, f"Missing instruction phase: {phase}"
    print("  ✓ All 4 instruction phases present")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["cold-smoker", "smoke-tube"]:
        assert any(tool in eq for eq in ke), f"Missing required equipment '{tool}', got {ke}"
    print("  ✓ Key equipment includes cold-smoker and smoke-tube")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),
        ("Frontmatter: cuisine", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein [none]", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: difficulty", lambda: test_frontmatter_difficulty(fm)),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Ingredient groups", lambda: test_ingredient_groups(content)),
        ("Key ingredients", lambda: test_ingredients_content(content)),
        ("Resolves 'Bok Lava' ambiguity", lambda: test_resolves_bok_lava(content)),
        ("Instructions (14 steps, 4 phases)", lambda: test_instructions(content)),
        ("Inline timing", lambda: test_inline_timing(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Variations specific", lambda: test_variations_specific(content)),
        ("Cold smoke technique", lambda: test_cold_smoke_technique(content)),
        ("Syrup technique", lambda: test_syrup_technique(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin note", lambda: test_origin_note(content)),
        ("Phases in instructions", lambda: test_phases_in_instructions(content)),
    ]

    run_tests("TICKET-027", tests)


if __name__ == "__main__":
    run()
