#!/usr/bin/env python3
"""
TICKET-023: Expand Cannoli from notebook source.

Validates `recipes/dessert/cannoli.md` against:
  - TICKET-023 requirements
  - docs/specs/023-cannoli.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dessert/cannoli.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists")
    return fm, content


def test_frontmatter_fields(fm):
    for field in ["title", "slug", "meal_type", "cuisine", "course",
                  "dietary_tags", "season",
                  "prep_time", "cook_time", "inactive_time", "total_time",
                  "base_servings", "serving_unit", "scaling_notes",
                  "source_type", "source_name",
                  "origin_notes",
                  "difficulty", "key_equipment",
                  "tags", "protein",
                  "status", "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    print("  ✓ All required frontmatter fields present")


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any("italian" in c.lower() for c in cuisines), \
        f"Expected cuisine 'italian', got {cuisines}"
    print("  ✓ Cuisine is italian")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    assert "vegetarian" in dt, f"Missing dietary_tag 'vegetarian', got {dt}"
    print("  ✓ Dietary tags: vegetarian")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["recipe/dessert"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    technique_tags = [t for t in tags if t.startswith("technique/")]
    assert any("dough" in t for t in technique_tags), \
        f"Expected technique/dough tag, got {technique_tags}"
    assert any("fry" in t or "frying" in t for t in technique_tags), \
        f"Expected technique/fry tag, got {technique_tags}"
    assert any("pipe" in t or "piping" in t for t in technique_tags), \
        f"Expected technique/pipe tag, got {technique_tags}"
    print(f"  ✓ Technique tags: dough, fry, pipe — {technique_tags}")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert "ricotta" in protein, f"Expected protein 'ricotta', got {protein}"
    print("  ✓ Protein: ricotta")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    assert fm.get("title") == "Cannoli", \
        f"Expected title 'Cannoli', got '{fm.get('title')}'"
    assert fm.get("slug") == "cannoli", \
        f"Expected slug 'cannoli', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_flour(content):
    assert "flour" in content.lower(), "Missing flour for shell dough"
    print("  ✓ Flour present for shell")


def test_ingredient_ricotta(content):
    assert "ricotta" in content.lower(), "Missing ricotta for filling"
    print("  ✓ Ricotta present for filling")


def test_ingredient_sugar(content):
    assert "sugar" in content.lower(), "Missing sugar"
    print("  ✓ Sugar present")


def test_ingredient_oil_frying(content):
    assert "oil" in content.lower(), "Missing oil for frying"
    print("  ✓ Frying oil present")


def test_shell_and_filling_sections(content):
    lower = content.lower()
    assert "shell" in lower, "Missing shell component"
    assert "fill" in lower or "ricotta" in lower, "Missing filling component"
    print("  ✓ Both shell and filling components present")


def test_frying_technique(content):
    assert "fry" in content.lower(), "Missing frying technique"
    print("  ✓ Frying technique present")


def test_fill_just_before_serving(content):
    lower = content.lower()
    assert "before serving" in lower or "last minute" in lower or "just before" in lower, \
        "Missing 'fill just before serving' instruction"
    print("  ✓ Fill-just-before-serving guidance present")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=8, max_steps=10)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, "
          f"{len(sensory)} sensory cues, inline timing present")


def test_notes(content):
    nb, vb = check_notes(content, min_cooks=2, min_variations=1)
    print(f"  ✓ Notes: {nb} cook's notes, {vb} variations, "
          f"make-ahead/storage, scaling")


def test_make_ahead_storage(content):
    assert "Make-Ahead" in content or "Make Ahead" in content, \
        "Missing Make-Ahead heading"
    assert "Storage" in content or "storage" in content, \
        "Missing Storage information"
    print("  ✓ Make-Ahead / Storage present")


def test_scaling(content):
    assert "### Scaling" in content, "Missing Scaling section"
    print("  ✓ Scaling section present")


def test_sections(content):
    required = ["## Ingredients", "## Instructions", "## Notes & Variations",
                "### Cook's Notes", "### Variations", "### Scaling"]
    for h in required:
        assert h in content, f"Missing heading: {h}"
    print("  ✓ All required sections present")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Frontmatter: cuisine", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: title/slug", lambda: test_frontmatter_series(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Flour for shell", lambda: test_ingredient_flour(content)),
        ("Ricotta for filling", lambda: test_ingredient_ricotta(content)),
        ("Sugar", lambda: test_ingredient_sugar(content)),
        ("Frying oil", lambda: test_ingredient_oil_frying(content)),
        ("Shell + filling components", lambda: test_shell_and_filling_sections(content)),
        ("Frying technique", lambda: test_frying_technique(content)),
        ("Fill just before serving", lambda: test_fill_just_before_serving(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-023", tests)


if __name__ == "__main__":
    run()
