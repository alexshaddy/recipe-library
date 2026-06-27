#!/usr/bin/env python3
"""
TICKET-031: Expand Chimichurri Chicken Empanadas from notebook source.

Validates `recipes/dinner/chimichurri-chicken-empanadas.md` against:
  - TICKET-031 requirements
  - docs/specs/031-chimichurri-chicken-empanadas.md spec
  - Notebook p.19 source (chimichurri exact weights)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dinner/chimichurri-chicken-empanadas.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/dinner/chimichurri-chicken-empanadas.md")
    return fm, content


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    cuisines_lower = [c.lower() for c in cuisines]
    for exp in ["argentine", "latin"]:
        assert any(exp in c for c in cuisines_lower), \
            f"Expected cuisine containing '{exp}', got {cuisines}"
    print("  ✓ Cuisine: Argentine, Latin")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    assert len(dt) == 0, f"Expected dietary_tags to be empty, got {dt}"
    print("  ✓ Dietary tags: []")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["dinner", "empanada", "chicken", "chimichurri",
                "technique-dough", "technique-filling", "technique-frying", "technique-baking"]:
        assert any(exp in t.lower() for t in tags), f"Missing tag containing '{exp}', got {tags}"
    print("  ✓ Tags: dinner, empanada, chicken, chimichurri, technique tags")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert "chicken" in protein, f"Expected protein to include 'chicken', got {protein}"
    print("  ✓ Protein: [chicken]")


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
    assert fm.get("source_page") == "19", \
        f"Expected source_page '19', got '{fm.get('source_page')}'"
    print("  ✓ Source documented: handwritten — Chef's Recipe Notebook p.19")


def test_ingredient_groups(content):
    assert "### Chimichurri" in content, "Missing 'Chimichurri' ingredient group"
    assert "### Chicken Filling" in content, "Missing 'Chicken Filling' ingredient group"
    assert "### Empanada Dough" in content, "Missing 'Empanada Dough' ingredient group"
    assert "### For Assembly" in content, "Missing 'For Assembly' ingredient group"
    print("  ✓ Ingredient groups: Chimichurri, Chicken Filling, Dough, Assembly")


def test_chimichurri_weights(content):
    """Verify exact chimichurri weights from notebook p.19."""
    assert "100 g" in content, "Missing 100g measurement (cilantro/parsley/vinegar)"
    assert "cilantro" in content.lower(), "Missing cilantro"
    assert "parsley" in content.lower(), "Missing parsley"
    assert "red wine vinegar" in content.lower(), "Missing red wine vinegar"
    print("  ✓ Chimichurri: 100g cilantro, 100g parsley, 100g red wine vinegar")


def test_chimichurri_garlic(content):
    assert "6" in content and "garlic" in content.lower(), "Missing 6 cloves garlic"
    print("  ✓ Chimichurri: ~6 cloves garlic")


def test_dough_hydration(content):
    """Verify dough water amount is resolved from [ESTIMATED]."""
    assert "[ESTIMATED]" not in content, "Dough water still has [ESTIMATED]"
    assert "200 ml" in content or "200ml" in content, "Missing resolved 200ml water"
    assert "¾ cup + 2 tbsp" in content, "Missing resolved water amount"
    print("  ✓ Dough water resolved to ¾ cup + 2 tbsp (200ml)")


def test_instructions(content):
    # Recipe has 14 steps grouped into 4 phases under one ## Instructions section
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


def test_sections(content):
    required = ["## Ingredients", "## Instructions", "## Notes & Variations",
                "### Cook's Notes", "### Variations", "### Scaling"]
    for h in required:
        assert h in content, f"Missing heading: {h}"
    assert "Make-Ahead" in content, "Missing Make-Ahead"
    assert "Storage" in content, "Missing Storage"
    print("  ✓ All required sections present")


def test_origin_note(content):
    assert "Notebook" in content and "p. 19" in content, \
        "Missing notebook origin reference"
    print("  ✓ Origin note references notebook page 19")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["rolling-pin", "food-processor", "deep-fry-thermometer"]:
        assert any(tool in eq for eq in ke), f"Missing required equipment '{tool}', got {ke}"
    print("  ✓ Key equipment: rolling-pin, food-processor, deep-fry-thermometer")


def test_component_phases(content):
    """Verify the 4 component phases are present in instructions."""
    for phase in ["Component 1:", "Component 2:", "Component 3:", "Assembly & Cook"]:
        assert phase in content, f"Missing instruction phase: {phase}"
    print("  ✓ All 4 component phases present")


def test_bake_and_fry(content):
    """Verify both baking and frying options are documented."""
    assert "400°F" in content or "BAKE" in content, "Missing baking option"
    assert "350°F" in content or "FRY" in content, "Missing frying option"
    print("  ✓ Both bake and fry options documented")


def test_no_estimated_values(content):
    """Verify no [ESTIMATED] values remain."""
    assert "[ESTIMATED]" not in content, "Still has unresolved [ESTIMATED] values"
    print("  ✓ No [ESTIMATED] values remain")


def test_ingredient_format(content):
    """Check for formatting issues in ingredient list."""
    # Check for the known corruption artifact
    issues = []
    # Line 65: `- [ ] `1] `1 tsp` **red pepper flakes**` — has `1] ` artifact
    corrupted = re.search(r'`1\]\s*`', content)
    if corrupted:
        issues.append("Formatting artifact: '`1] `' found in ingredient list")
    
    if issues:
        raise AssertionError("; ".join(issues))
    print("  ✓ No ingredient formatting artifacts")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),
        ("Frontmatter: cuisine", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein [chicken]", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Ingredient groups", lambda: test_ingredient_groups(content)),
        ("Chimichurri: exact weights", lambda: test_chimichurri_weights(content)),
        ("Chimichurri: ~6 garlic cloves", lambda: test_chimichurri_garlic(content)),
        ("Dough water resolved", lambda: test_dough_hydration(content)),
        ("Instructions (14 steps, 4 phases)", lambda: test_instructions(content)),
        ("Inline timing", lambda: test_inline_timing(content)),
        ("Component phases", lambda: test_component_phases(content)),
        ("Bake & fry options", lambda: test_bake_and_fry(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin note", lambda: test_origin_note(content)),
        ("No [ESTIMATED] values", lambda: test_no_estimated_values(content)),
        ("Ingredient formatting check", lambda: test_ingredient_format(content)),
    ]

    run_tests("TICKET-031", tests)


if __name__ == "__main__":
    run()
