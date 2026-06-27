#!/usr/bin/env python3
"""
TICKET-011: Create Miso Ramen from title-only addendum.

Validates `recipes/dinner/miso-ramen.md` against:
  - TICKET-011 requirements
  - Sapporo-style miso ramen spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dinner/miso-ramen.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/dinner/miso-ramen.md")
    return fm, content


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any("japanese" in c.lower() for c in cuisines), f"Expected cuisine Japanese, got {cuisines}"
    print("  ✓ Cuisine is Japanese")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in ["dinner", "ramen", "noodles"]:
        assert any(exp in t for t in tags_lower), f"Missing tag containing '{exp}', got {tags}"
    print("  ✓ Tags include dinner, ramen, noodles")


def test_frontmatter_technique(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["broth-making", "tare"]:
        assert any(exp in t.lower() for t in tags), f"Missing technique '{exp}' in tags: {tags}"
    print("  ✓ Technique tags include broth-making, tare")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    for exp in ["chicken", "pork"]:
        assert exp in protein, f"Missing protein '{exp}', got {protein}"
    print("  ✓ Protein includes chicken, pork")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_fields(fm):
    for field in ["title", "slug", "meal_type", "cuisine", "course", "season",
                  "prep_time", "cook_time", "inactive_time", "total_time",
                  "base_servings", "serving_unit", "scaling_notes",
                  "source_type", "source_name", "origin_notes",
                  "difficulty", "key_equipment", "tags", "protein", "status",
                  "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    print("  ✓ All required frontmatter fields present")


def test_ingredient_groups(content):
    assert "### For the Broth" in content, "Missing broth ingredient group"
    assert "### For the Miso Tare" in content or "### For the Tare" in content, "Missing tare ingredient group"
    assert "### For the Noodles" in content or "noodles" in content.lower(), "Missing noodles"
    assert "### For Toppings" in content or "toppings" in content.lower(), "Missing toppings"
    print("  ✓ Ingredient groups: broth, tare, noodles, toppings")


def test_ingredient_broth_chicken_pork(content):
    lower = content.lower()
    assert "chicken" in lower or "pork" in lower, "Broth should mention chicken or pork"
    print("  ✓ Broth mentions chicken/pork")


def test_ingredient_miso_tare(content):
    lower = content.lower()
    assert "white miso" in lower, "Missing white miso in tare"
    assert "red miso" in lower, "Missing red miso in tare"
    print("  ✓ Miso tare includes white miso and red miso")


def test_ingredient_tare_components(content):
    lower = content.lower()
    for comp in ["mirin", "sake", "garlic", "ginger"]:
        assert comp in lower, f"Missing tare component: {comp}"
    print("  ✓ Tare components: mirin, sake, garlic, ginger")


def test_toppings(content):
    lower = content.lower()
    for t in ["chashu", "nori", "corn", "butter"]:
        assert t in lower, f"Missing topping: {t}"
    print("  ✓ Toppings: chashu, nori, corn, butter")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=7, max_steps=9)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, {len(sensory)} sensory cues")


def test_inline_timing(content):
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)
    timing = re.findall(r"\d+\s*(?:min(?:ute)?s?|hour|hr)s?", instr_section, re.IGNORECASE)
    assert len(timing) >= 2, f"Too few timing cues: {len(timing)}"
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


def test_source_documented(fm):
    assert fm.get("source_type"), "source_type empty"
    assert fm.get("source_name"), "source_name empty"
    print(f"  ✓ Source documented: {fm.get('source_type')} — {fm.get('source_name')}")


def test_slug(fm):
    expected = "miso-ramen"
    assert fm.get("slug") == expected, f"Expected slug '{expected}', got '{fm.get('slug')}'"
    print(f"  ✓ Slug: {expected}")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),  # Already loaded
        ("Frontmatter: cuisine Japanese", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: technique tags", lambda: test_frontmatter_technique(fm)),
        ("Frontmatter: protein", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Slug", lambda: test_slug(fm)),
        ("Ingredient groups", lambda: test_ingredient_groups(content)),
        ("Broth: chicken/pork", lambda: test_ingredient_broth_chicken_pork(content)),
        ("Miso tare: white+red", lambda: test_ingredient_miso_tare(content)),
        ("Tare components", lambda: test_ingredient_tare_components(content)),
        ("Toppings", lambda: test_toppings(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Inline timing", lambda: test_inline_timing(content)),
        ("Notes & variations", lambda: test_notes(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-011", tests)


if __name__ == "__main__":
    run()
