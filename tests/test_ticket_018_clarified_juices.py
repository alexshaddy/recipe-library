#!/usr/bin/env python3
"""
TICKET-018: Expand Clarified Juices from notebook source (two methods).

Validates `recipes/condiment/clarified-juices.md` against:
  - TICKET-018 requirements
  - docs/specs/018-clarified-juices.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "condiment/clarified-juices.md"
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
    assert any("international" in c.lower() for c in cuisines), \
        f"Expected cuisine 'international', got {cuisines}"
    print("  ✓ Cuisine is international")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    for exp in ["vegetarian", "vegan", "gluten-free"]:
        assert exp in dt, f"Missing dietary_tag '{exp}', got {dt}"
    print("  ✓ Dietary tags: vegetarian, vegan, gluten-free")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["recipe/condiment", "technique/clarification",
                "technique/agar", "technique/freeze-thaw"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    print("  ✓ Tags: condiment, clarification, agar, freeze-thaw")


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
    assert fm.get("title") == "Clarified Juices", \
        f"Expected title 'Clarified Juices', got '{fm.get('title')}'"
    assert fm.get("slug") == "clarified-juices", \
        f"Expected slug 'clarified-juices', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["cheesecloth", "saucepan"]:
        assert any(tool in eq.lower() for eq in ke), \
            f"Missing equipment '{tool}', got {ke}"
    has_strainer = any("strain" in eq.lower() for eq in ke)
    has_sieve = any("sieve" in eq.lower() for eq in ke)
    assert has_strainer or has_sieve, \
        f"Missing strainer or sieve equipment, got {ke}"
    print("  ✓ Key equipment includes strainer/sieve, cheesecloth, saucepan")


def test_ingredient_base_juice(content):
    assert re.search(r'\d+\s*(?:liter|ml|milliliter|cup)s?\s*.*juice',
                     content, re.IGNORECASE), \
        "Missing base juice ingredient (liter/ml of juice)"
    print("  ✓ Base juice ingredient present")


def test_ingredient_agar(content):
    assert "agar" in content.lower(), "Missing agar for clarification method 1"
    print("  ✓ Agar present for method 1")


def test_ingredient_lemon_or_acid(content):
    lower = content.lower()
    assert "lemon" in lower or "citric acid" in lower or "acid" in lower, \
        "Missing acid (lemon/citric) for method 1"
    print("  ✓ Acid/lemon present for method 1")


def test_both_methods_present(content):
    lower = content.lower()
    assert "agar" in lower, "Missing agar clarification method"
    assert "freeze" in lower or "thaw" in lower, "Missing freeze-thaw method"
    print("  ✓ Both clarification methods present (agar + freeze-thaw)")


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
        ("Frontmatter: cuisine international", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein none", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: title/slug", lambda: test_frontmatter_series(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Base juice ingredient", lambda: test_ingredient_base_juice(content)),
        ("Agar ingredient", lambda: test_ingredient_agar(content)),
        ("Acid/lemon ingredient", lambda: test_ingredient_lemon_or_acid(content)),
        ("Both methods (agar + freeze-thaw)", lambda: test_both_methods_present(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-018", tests)


if __name__ == "__main__":
    run()
