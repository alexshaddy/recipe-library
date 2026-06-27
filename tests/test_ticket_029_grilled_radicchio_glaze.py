#!/usr/bin/env python3
"""
TICKET-029: Expand Grilled Radicchio with Carrot-Ginger Glaze from notebook source.

Validates `recipes/side/grilled-radicchio-with-carrot-ginger-glaze.md` against:
  - TICKET-029 requirements
  - Notebook p.24 source
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/grilled-radicchio-with-carrot-ginger-glaze.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/side/grilled-radicchio-with-carrot-ginger-glaze.md")
    return fm, content


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    cuisines_lower = [c.lower() for c in cuisines]
    for exp in ["italian", "modern"]:
        assert any(exp in c for c in cuisines_lower), \
            f"Expected cuisine containing '{exp}', got {cuisines}"
    print("  ✓ Cuisine: Italian, Modern")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    for tag in ["vegan", "vegetarian", "gluten-free"]:
        assert tag in dt, f"Expected dietary_tags to contain '{tag}', got {dt}"
    print("  ✓ Dietary tags: vegan, vegetarian, gluten-free")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["side", "vegetable", "radicchio", "grilled", "glaze",
                "technique-grilling", "technique-glazing"]:
        assert any(exp in t.lower() for t in tags), f"Missing tag containing '{exp}', got {tags}"
    print("  ✓ Tags: side, vegetable, radicchio, grilled, glaze, technique tags")


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
    assert fm.get("source_page") == "24", \
        f"Expected source_page '24', got '{fm.get('source_page')}'"
    print("  ✓ Source documented: handwritten — Chef's Recipe Notebook p.24")


def test_ingredient_groups(content):
    assert "### Carrot-Ginger Glaze" in content, "Missing 'Carrot-Ginger Glaze' ingredient group"
    assert "### Radicchio" in content, "Missing 'Radicchio' ingredient group"
    assert "### Garnish" in content, "Missing 'Garnish' ingredient group"
    print("  ✓ Ingredient groups: Glaze, Radicchio, Garnish")


def test_ingredients_content(content):
    lower = content.lower()
    for item in ["carrot", "ginger", "radicchio", "nori", "sesame", "chanterelle"]:
        assert item in lower, f"Missing ingredient: {item}"
    print("  ✓ Key ingredients: carrot, ginger, radicchio, nori, sesame, chanterelle")


def test_chanterelle_resolved(content):
    """Verify the [TO VERIFY] on chanterelle powder is resolved."""
    assert "chanterelle powder" in content.lower(), "Missing chanterelle powder"
    assert "[TO VERIFY]" not in content, "Chanterelle powder still has [TO VERIFY]"
    print("  ✓ Chanterelle powder [TO VERIFY] resolved")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=7, max_steps=9)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, {len(sensory)} sensory cues")


def test_inline_timing(content):
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)
    timing = re.findall(r"\d+\s*(?:min(?:ute)?s?|hour|hr|sec)s?", instr_section, re.IGNORECASE)
    assert len(timing) >= 3, f"Too few timing cues: {len(timing)}"
    print(f"  ✓ Inline timing: {len(timing)} instances")


def test_notes(content):
    nb, vb = check_notes(content, min_cooks=2, min_variations=1)
    print(f"  ✓ Notes: {nb} cook's notes, {vb} variations, make-ahead, storage, scaling")


def test_sections(content):
    required = ["## Ingredients", "## Instructions", "## Notes & Variations",
                "### Cook's Notes", "### Variations", "### Scaling"]
    for h in required:
        assert h in content, f"Missing heading: {h}"
    assert "Make-Ahead" in content, "Missing Make-Ahead"
    assert "Storage" in content, "Missing Storage"
    print("  ✓ All required sections present")


def test_origin_note(content):
    assert "Notebook" in content and "p. 24" in content, \
        "Missing notebook origin reference"
    print("  ✓ Origin note references notebook page 24")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["grill", "juicer", "blender"]:
        assert any(tool in eq for eq in ke), f"Missing required equipment '{tool}', got {ke}"
    print("  ✓ Key equipment: grill, juicer, blender")


def test_no_estimated_values(content):
    """Verify no [ESTIMATED] values remain."""
    assert "[ESTIMATED]" not in content, "Still has unresolved [ESTIMATED] values"
    print("  ✓ No [ESTIMATED] values remain")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),
        ("Frontmatter: cuisine", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein [none]", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Ingredient groups", lambda: test_ingredient_groups(content)),
        ("Key ingredients", lambda: test_ingredients_content(content)),
        ("Chanterelle resolved", lambda: test_chanterelle_resolved(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Inline timing", lambda: test_inline_timing(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin note", lambda: test_origin_note(content)),
        ("No [ESTIMATED] values", lambda: test_no_estimated_values(content)),
    ]

    run_tests("TICKET-029", tests)


if __name__ == "__main__":
    run()
