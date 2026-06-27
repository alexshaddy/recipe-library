#!/usr/bin/env python3
"""
TICKET-021: Expand Kick-Ass Cookies from notebook source.

Validates `recipes/dessert/kick-ass-cookies.md` against:
  - TICKET-021 requirements
  - docs/specs/021-kick-ass-cookies.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dessert/kick-ass-cookies.md"
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
    assert any("american" in c.lower() for c in cuisines), \
        f"Expected cuisine 'american', got {cuisines}"
    print("  ✓ Cuisine is american")


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
    has_creaming = any("creaming" in t for t in technique_tags)
    has_chilling = any("chilling" in t or "chill" in t for t in technique_tags)
    has_baking = any("baking" in t or "bake" in t for t in technique_tags)
    assert has_creaming and has_chilling and has_baking, \
        f"Expected technique tags (creaming, chilling, baking), got {technique_tags}"
    print("  ✓ Tags: recipe/dessert, technique/creaming, technique/chilling, technique/baking")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert len(protein) == 0 or protein == [""] or "none" in str(protein).lower(), \
        f"Expected protein empty/none, got {protein}"
    print("  ✓ Protein: none")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    assert fm.get("title") == "Kick-Ass Cookies", \
        f"Expected title 'Kick-Ass Cookies', got '{fm.get('title')}'"
    assert fm.get("slug") == "kick-ass-cookies", \
        f"Expected slug 'kick-ass-cookies', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_flour(content):
    assert "flour" in content.lower(), "Missing flour"
    print("  ✓ Flour present")


def test_ingredient_butter(content):
    assert "butter" in content.lower(), "Missing butter"
    print("  ✓ Butter present")


def test_ingredient_sugar(content):
    assert "sugar" in content.lower(), "Missing sugar"
    print("  ✓ Sugar present")


def test_ingredient_eggs(content):
    assert "egg" in content.lower(), "Missing eggs"
    print("  ✓ Eggs present")


def test_ingredient_baking_soda(content):
    assert "baking soda" in content.lower(), "Missing baking soda"
    print("  ✓ Baking soda present")


def test_ingredient_salt(content):
    assert "salt" in content.lower(), "Missing salt"
    print("  ✓ Salt present")


def test_ingredient_vanilla(content):
    assert "vanilla" in content.lower(), "Missing vanilla"
    print("  ✓ Vanilla present")


def test_chill_dough_technique(content):
    assert "chill" in content.lower(), "Missing chilling step"
    print("  ✓ Chilling dough technique present")


def test_doneness_cues(content):
    lower = content.lower()
    has_edge_cue = "golden" in lower and ("edge" in lower or "brown" in lower)
    has_center_cue = "center" in lower and ("soft" in lower or "under" in lower)
    assert has_edge_cue or has_center_cue, \
        "Missing doneness cues (golden edges, soft centers)"
    print("  ✓ Doneness cues: golden edges, soft centers")


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
        ("Flour ingredient", lambda: test_ingredient_flour(content)),
        ("Butter ingredient", lambda: test_ingredient_butter(content)),
        ("Sugar ingredient", lambda: test_ingredient_sugar(content)),
        ("Eggs ingredient", lambda: test_ingredient_eggs(content)),
        ("Baking soda ingredient", lambda: test_ingredient_baking_soda(content)),
        ("Salt ingredient", lambda: test_ingredient_salt(content)),
        ("Vanilla ingredient", lambda: test_ingredient_vanilla(content)),
        ("Chill dough technique", lambda: test_chill_dough_technique(content)),
        ("Doneness cues", lambda: test_doneness_cues(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-021", tests)


if __name__ == "__main__":
    run()
