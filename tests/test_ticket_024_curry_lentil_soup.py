#!/usr/bin/env python3
"""
TICKET-024: Expand Curry Lentil Soup from notebook source.

Validates `recipes/side/curry-lentil-soup.md` against:
  - TICKET-024 requirements
  - docs/specs/024-curry-lentil-soup.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/curry-lentil-soup.md"
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
    assert any("indian" in c.lower() for c in cuisines), \
        f"Expected cuisine 'indian' or 'indian-inspired', got {cuisines}"
    print("  ✓ Cuisine is indian/indian-inspired")


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
    for exp in ["recipe/side"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    technique_tags = [t for t in tags if t.startswith("technique/")]
    assert any("bloom" in t for t in technique_tags), \
        f"Expected bloom-spices technique tag, got {technique_tags}"
    assert any("simmer" in t for t in technique_tags), \
        f"Expected simmer technique tag, got {technique_tags}"
    print(f"  ✓ Technique tags include bloom-spices, simmer: {technique_tags}")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert "lentil" in protein, f"Expected protein 'lentil', got {protein}"
    print("  ✓ Protein: lentil")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    assert fm.get("title") == "Curry Lentil Soup", \
        f"Expected title 'Curry Lentil Soup', got '{fm.get('title')}'"
    assert fm.get("slug") == "curry-lentil-soup", \
        f"Expected slug 'curry-lentil-soup', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_lentils(content):
    assert "lentil" in content.lower(), "Missing lentils"
    print("  ✓ Lentils present")


def test_ingredient_onion(content):
    assert "onion" in content.lower(), "Missing onion"
    print("  ✓ Onion present")


def test_ingredient_garlic(content):
    assert "garlic" in content.lower(), "Missing garlic"
    print("  ✓ Garlic present")


def test_ingredient_curry_powder(content):
    assert "curry" in content.lower(), "Missing curry powder"
    print("  ✓ Curry powder present")


def test_ingredient_stock(content):
    lower = content.lower()
    assert "stock" in lower or "water" in lower, "Missing stock or water"
    print("  ✓ Stock/water present")


def test_bloom_spices_technique(content):
    lower = content.lower()
    assert "bloom" in lower, "Missing blooming spices technique"
    print("  ✓ Blooming spices technique present")


def test_simmer_technique(content):
    assert "simmer" in content.lower(), "Missing simmering technique"
    print("  ✓ Simmering technique present")


def test_blending_option(content):
    lower = content.lower()
    assert "blend" in lower or "puree" in lower or "immersion" in lower, \
        "Missing blending/pureeing option"
    print("  ✓ Blending option present")


def test_finish_with_acid(content):
    lower = content.lower()
    assert "lemon" in lower or "vinegar" in lower or "acid" in lower or "lime" in lower, \
        "Missing acid finish (lemon/vinegar)"
    print("  ✓ Acid finish present")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=6, max_steps=8)
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
        ("Lentils ingredient", lambda: test_ingredient_lentils(content)),
        ("Onion ingredient", lambda: test_ingredient_onion(content)),
        ("Garlic ingredient", lambda: test_ingredient_garlic(content)),
        ("Curry powder", lambda: test_ingredient_curry_powder(content)),
        ("Stock/water", lambda: test_ingredient_stock(content)),
        ("Bloom spices technique", lambda: test_bloom_spices_technique(content)),
        ("Simmer technique", lambda: test_simmer_technique(content)),
        ("Blending option", lambda: test_blending_option(content)),
        ("Acid finish", lambda: test_finish_with_acid(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-024", tests)


if __name__ == "__main__":
    run()
