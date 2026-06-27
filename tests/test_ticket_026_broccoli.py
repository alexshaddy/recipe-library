#!/usr/bin/env python3
"""
TICKET-026: Expand Broccoli (Sicilian agrodolce) from notebook source.

Validates `recipes/side/broccoli.md` against:
  - TICKET-026 requirements
  - docs/specs/026-broccoli-agrodolce.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/broccoli.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists")
    return fm, content


def test_frontmatter_fields(fm):
    for field in ["title", "slug", "meal_type", "cuisine", "course",
                  "dietary_tags", "season",
                  "prep_time", "cook_time", "total_time",
                  "base_servings", "serving_unit", "scaling_notes",
                  "source_type", "source_name",
                  "origin_notes",
                  "difficulty", "key_equipment",
                  "tags", "protein",
                  "status", "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    # inactive_time allowed empty for quick dishes
    print("  ✓ All required frontmatter fields present")


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    has_italian = any("italian" in c.lower() for c in cuisines)
    has_sicilian = any("sicilian" in c.lower() for c in cuisines)
    assert has_italian or has_sicilian, \
        f"Expected cuisine Italian/Sicilian, got {cuisines}"
    print("  ✓ Cuisine is Italian/Sicilian")


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
    tags_lower = [t.lower() for t in tags]
    assert any("broccoli" in t for t in tags_lower), \
        f"Missing broccoli tag, got {tags}"
    assert any("agrodolce" in t for t in tags_lower), \
        f"Missing agrodolce tag, got {tags}"
    assert any("blanch" in t for t in tags_lower), \
        f"Missing blanching technique tag, got {tags}"
    assert any("glaze" in t or "glazing" in t for t in tags_lower), \
        f"Missing glazing technique tag, got {tags}"
    print("  ✓ Tags include broccoli, agrodolce, blanching, glazing")


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


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


def test_ingredient_broccoli(content):
    assert "broccoli" in content.lower(), "Missing broccoli"
    print("  ✓ Broccoli present")


def test_ingredient_garlic(content):
    assert "garlic" in content.lower(), "Missing garlic"
    print("  ✓ Garlic present")


def test_ingredient_chili_flakes(content):
    lower = content.lower()
    assert "red pepper" in lower or "chili" in lower or "peperoncino" in lower, \
        "Missing red pepper flakes"
    print("  ✓ Red pepper flakes present")


def test_ingredient_sugar(content):
    assert "sugar" in content.lower(), "Missing sugar"
    print("  ✓ Sugar present")


def test_ingredient_vinegar(content):
    assert "vinegar" in content.lower(), "Missing vinegar"
    print("  ✓ Vinegar present")


def test_ingredient_raisins(content):
    assert "raisin" in content.lower() or "sultana" in content.lower(), \
        "Missing raisins"
    print("  ✓ Raisins present")


def test_ingredient_pine_nuts(content):
    assert "pine nuts" in content.lower(), "Missing pine nuts"
    print("  ✓ Pine nuts present")


def test_agrodolce_technique(content):
    """Verify agrodolce technique: caramelize sugar, deglaze with vinegar."""
    lower = content.lower()
    assert "caramel" in lower, "Missing caramelization step"
    assert "deglaze" in lower, "Missing deglazing step"
    assert "sweet" in lower and "sour" in lower, \
        "Missing sweet-sour reference"
    print("  ✓ Agrodolce technique: caramelize sugar, deglaze with vinegar")


def test_blanch_technique(content):
    assert "blanch" in content.lower(), "Missing blanching step"
    print("  ✓ Blanching technique present")


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


def test_origin_notebook_reference(content):
    """Verify origin references the 6.21 pop-up dinner notebook."""
    lower = content.lower()
    assert "6.21" in lower or "pop-up" in lower or "addendum" in lower or "notebook" in lower, \
        "Missing notebook/addendum reference in origin"
    print("  ✓ Origin references notebook source")


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
        ("Source documented", lambda: test_source_documented(fm)),
        ("Broccoli ingredient", lambda: test_ingredient_broccoli(content)),
        ("Garlic ingredient", lambda: test_ingredient_garlic(content)),
        ("Red pepper flakes", lambda: test_ingredient_chili_flakes(content)),
        ("Sugar ingredient", lambda: test_ingredient_sugar(content)),
        ("Vinegar ingredient", lambda: test_ingredient_vinegar(content)),
        ("Raisins ingredient", lambda: test_ingredient_raisins(content)),
        ("Pine nuts ingredient", lambda: test_ingredient_pine_nuts(content)),
        ("Agrodolce technique", lambda: test_agrodolce_technique(content)),
        ("Blanching technique", lambda: test_blanch_technique(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin notebook reference", lambda: test_origin_notebook_reference(content)),
    ]

    run_tests("TICKET-026", tests)


if __name__ == "__main__":
    run()
