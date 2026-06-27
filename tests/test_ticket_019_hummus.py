#!/usr/bin/env python3
"""
TICKET-019: Expand Hummus from notebook source.

Validates `recipes/condiment/hummus.md` against:
  - TICKET-019 requirements
  - docs/specs/019-hummus.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "condiment/hummus.md"
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
    assert any("middle-eastern" in c.lower() for c in cuisines), \
        f"Expected cuisine 'middle-eastern', got {cuisines}"
    print("  ✓ Cuisine is middle-eastern")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    for exp in ["vegan", "vegetarian", "gluten-free"]:
        assert exp in dt, f"Missing dietary_tag '{exp}', got {dt}"
    print("  ✓ Dietary tags: vegan, vegetarian, gluten-free")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["recipe/condiment", "ingredient/chickpea", "ingredient/tahini",
                "technique/blending", "technique/cooking-legumes"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    print("  ✓ Tags: chickpea, tahini, blending, cooking-legumes")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert "chickpea" in protein, f"Expected protein 'chickpea', got {protein}"
    print("  ✓ Protein: chickpea")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    assert fm.get("title") == "Hummus", \
        f"Expected title 'Hummus', got '{fm.get('title')}'"
    assert fm.get("slug") == "hummus", \
        f"Expected slug 'hummus', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_chickpeas(content):
    assert "chickpea" in content.lower() or "garbanzo" in content.lower(), \
        "Missing chickpeas/garbanzo beans"
    print("  ✓ Chickpeas/garbanzo beans present")


def test_ingredient_tahini(content):
    assert "tahini" in content.lower(), "Missing tahini"
    print("  ✓ Tahini present")


def test_ingredient_lemon(content):
    assert "lemon" in content.lower(), "Missing lemon juice"
    print("  ✓ Lemon juice present")


def test_ingredient_garlic(content):
    assert "garlic" in content.lower(), "Missing garlic"
    print("  ✓ Garlic present")


def test_ingredient_olive_oil(content):
    assert "olive oil" in content.lower(), "Missing olive oil"
    print("  ✓ Olive oil present")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=6, max_steps=8)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, "
          f"{len(sensory)} sensory cues, inline timing present")


def test_tahini_lemon_base_technique(content):
    """Verify tahini + lemon are blended first (key technique)."""
    lower = content.lower()
    assert "tahini" in lower and "lemon" in lower, "Missing tahini or lemon"
    print("  ✓ Tahini-lemon base technique present")


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
        ("Chickpeas ingredient", lambda: test_ingredient_chickpeas(content)),
        ("Tahini ingredient", lambda: test_ingredient_tahini(content)),
        ("Lemon juice ingredient", lambda: test_ingredient_lemon(content)),
        ("Garlic ingredient", lambda: test_ingredient_garlic(content)),
        ("Olive oil ingredient", lambda: test_ingredient_olive_oil(content)),
        ("Tahini-lemon base technique", lambda: test_tahini_lemon_base_technique(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-019", tests)


if __name__ == "__main__":
    run()
