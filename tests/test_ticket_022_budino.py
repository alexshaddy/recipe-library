#!/usr/bin/env python3
"""
TICKET-022: Expand Budino from notebook source.

Validates `recipes/dessert/budino.md` against:
  - TICKET-022 requirements
  - docs/specs/022-budino.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dessert/budino.md"
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
    for exp in ["vegetarian", "gluten-free"]:
        assert exp in dt, f"Missing dietary_tag '{exp}', got {dt}"
    print("  ✓ Dietary tags: vegetarian, gluten-free")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["recipe/dessert"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    technique_tags = [t for t in tags if t.startswith("technique/")]
    assert any("tempering" in t or "temper" in t for t in technique_tags), \
        f"Expected tempering technique tag, got {technique_tags}"
    assert any("custard" in t for t in technique_tags), \
        f"Expected custard technique tag, got {technique_tags}"
    print(f"  ✓ Technique tags include tempering and custard: {technique_tags}")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert "egg" in protein, f"Expected protein 'egg', got {protein}"
    print("  ✓ Protein: egg")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    assert fm.get("title") == "Budino", \
        f"Expected title 'Budino', got '{fm.get('title')}'"
    assert fm.get("slug") == "budino", \
        f"Expected slug 'budino', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_milk(content):
    assert "milk" in content.lower(), "Missing milk"
    print("  ✓ Milk present")


def test_ingredient_cream(content):
    assert "cream" in content.lower(), "Missing cream"
    print("  ✓ Cream present")


def test_ingredient_sugar(content):
    assert "sugar" in content.lower(), "Missing sugar"
    print("  ✓ Sugar present")


def test_ingredient_egg_yolks(content):
    lower = content.lower()
    assert "yolk" in lower, "Missing egg yolks"
    print("  ✓ Egg yolks present")


def test_ingredient_cornstarch(content):
    assert "cornstarch" in content.lower() or "corn starch" in content.lower(), \
        "Missing cornstarch"
    print("  ✓ Cornstarch present")


def test_ingredient_vanilla(content):
    assert "vanilla" in content.lower(), "Missing vanilla"
    print("  ✓ Vanilla present")


def test_tempering_technique(content):
    assert "temper" in content.lower(), "Missing tempering technique"
    print("  ✓ Tempering technique present")


def test_nappe_technique(content):
    lower = content.lower()
    assert "nappe" in lower or "coat" in lower or "spoon" in lower, \
        "Missing nappe/coating technique"
    print("  ✓ Nappe/coating spoon technique present")


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
        ("Milk ingredient", lambda: test_ingredient_milk(content)),
        ("Cream ingredient", lambda: test_ingredient_cream(content)),
        ("Sugar ingredient", lambda: test_ingredient_sugar(content)),
        ("Egg yolks ingredient", lambda: test_ingredient_egg_yolks(content)),
        ("Cornstarch ingredient", lambda: test_ingredient_cornstarch(content)),
        ("Vanilla ingredient", lambda: test_ingredient_vanilla(content)),
        ("Tempering technique", lambda: test_tempering_technique(content)),
        ("Nappe technique", lambda: test_nappe_technique(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-022", tests)


if __name__ == "__main__":
    run()
