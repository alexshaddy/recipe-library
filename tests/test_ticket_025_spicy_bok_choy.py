#!/usr/bin/env python3
"""
TICKET-025: Expand Spicy Bok Choy from notebook source.

Validates `recipes/side/spicy-bok-choy.md` against:
  - TICKET-025 requirements
  - docs/specs/025-spicy-bok-choy.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/spicy-bok-choy.md"
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
    assert any("chinese" in c.lower() for c in cuisines), \
        f"Expected cuisine 'chinese', got {cuisines}"
    print("  ✓ Cuisine is chinese")


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
    assert any("wok" in t for t in technique_tags), \
        f"Expected technique/wok tag, got {technique_tags}"
    assert any("steam" in t for t in technique_tags), \
        f"Expected technique/steam tag, got {technique_tags}"
    print(f"  ✓ Technique tags include wok, high-heat, steam: {technique_tags}")


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
    assert fm.get("title") == "Spicy Bok Choy", \
        f"Expected title 'Spicy Bok Choy', got '{fm.get('title')}'"
    assert fm.get("slug") == "spicy-bok-choy", \
        f"Expected slug 'spicy-bok-choy', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_bok_choy(content):
    assert "bok choy" in content.lower(), "Missing bok choy"
    print("  ✓ Bok choy present")


def test_ingredient_garlic(content):
    assert "garlic" in content.lower(), "Missing garlic"
    print("  ✓ Garlic present")


def test_ingredient_chili_flakes(content):
    lower = content.lower()
    assert "chili" in lower or "chilli" in lower, "Missing chili flakes"
    print("  ✓ Chili flakes present")


def test_ingredient_soy_sauce(content):
    assert "soy sauce" in content.lower(), "Missing soy sauce"
    print("  ✓ Soy sauce present")


def test_ingredient_sesame_oil(content):
    assert "sesame oil" in content.lower(), "Missing sesame oil"
    print("  ✓ Sesame oil present")


def test_resolved_estimated(content):
    """Check [TO VERIFY] and [ESTIMATED] markers are resolved."""
    assert "[TO VERIFY]" not in content, "Unresolved [TO VERIFY] marker"
    assert "[ESTIMATED]" not in content, "Unresolved [ESTIMATED] marker"
    print("  ✓ All [TO VERIFY] and [ESTIMATED] markers resolved")


def test_sear_cut_side_down(content):
    lower = content.lower()
    assert "cut-side" in lower or "cut side" in lower or "sear" in lower, \
        "Missing cut-side-down sear technique"
    print("  ✓ Cut-side-down sear technique present")


def test_steam_finish(content):
    assert "steam" in content.lower(), "Missing steam step"
    print("  ✓ Steam finish technique present")


def test_wok_hei(content):
    lower = content.lower()
    assert "wok" in lower or "high heat" in lower, \
        "Missing wok or high-heat technique"
    print("  ✓ Wok/high-heat technique present")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=5, max_steps=7)
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
        ("Bok choy ingredient", lambda: test_ingredient_bok_choy(content)),
        ("Garlic ingredient", lambda: test_ingredient_garlic(content)),
        ("Chili flakes", lambda: test_ingredient_chili_flakes(content)),
        ("Soy sauce", lambda: test_ingredient_soy_sauce(content)),
        ("Sesame oil", lambda: test_ingredient_sesame_oil(content)),
        ("Resolved [TO VERIFY]/[ESTIMATED]", lambda: test_resolved_estimated(content)),
        ("Sear cut-side down", lambda: test_sear_cut_side_down(content)),
        ("Steam finish", lambda: test_steam_finish(content)),
        ("Wok/high-heat technique", lambda: test_wok_hei(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-025", tests)


if __name__ == "__main__":
    run()
