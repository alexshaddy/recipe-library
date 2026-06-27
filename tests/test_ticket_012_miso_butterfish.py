#!/usr/bin/env python3
"""
TICKET-012: Create Miso Butterfish from title-only addendum.

Validates `recipes/dinner/miso-butterfish.md` against:
  - TICKET-012 requirements
  - docs/specs/012-miso-butterfish.md spec
  - Nobu-style saikyo-yaki technique
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "dinner/miso-butterfish.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/dinner/miso-butterfish.md")
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
    # source_url and source_page allowed empty for handwritten/title-only sources
    print("  ✓ All required frontmatter fields present")


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any("japanese" in c.lower() for c in cuisines), \
        f"Expected cuisine Japanese, got {cuisines}"
    print("  ✓ Cuisine is Japanese")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    assert "gluten-free-option" in dt, \
        f"Expected dietary_tags to contain gluten-free-option, got {dt}"
    print("  ✓ Dietary tags: gluten-free-option")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["recipe/dinner", "ingredient/fish", "ingredient/miso",
                "technique/marinating", "technique/broiling"]:
        assert exp in tags, f"Missing tag '{exp}', got {tags}"
    print("  ✓ Tags: dinner, fish, miso, marinating, broiling")


def test_frontmatter_protein(fm):
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    for exp in ["butterfish", "sablefish", "black-cod"]:
        assert exp in protein, f"Missing protein '{exp}', got {protein}"
    print("  ✓ Protein: butterfish, sablefish, black-cod")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_series(fm):
    """Verify title and slug are correct."""
    assert fm.get("title") == "Miso Butterfish", \
        f"Expected title 'Miso Butterfish', got '{fm.get('title')}'"
    assert fm.get("slug") == "miso-butterfish", \
        f"Expected slug 'miso-butterfish', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    assert fm.get("source_type") == "handwritten", \
        f"Expected source_type 'handwritten', got '{fm.get('source_type')}'"
    assert "Notebook" in fm.get("source_name", ""), \
        f"Expected source_name containing 'Notebook', got '{fm.get('source_name')}'"
    print("  ✓ Source documented: handwritten — Chef's Recipe Notebook")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["broiler", "baking sheet", "small bowl"]:
        assert any(tool in eq for eq in ke), \
            f"Missing required equipment '{tool}', got {ke}"
    print("  ✓ Key equipment: broiler, baking sheet, small bowl")


def test_ingredient_groups(content):
    assert "### For the Miso Marinade" in content, \
        "Missing 'Miso Marinade' ingredient group"
    assert "### For the Fish" in content, \
        "Missing 'Fish' ingredient group"
    print("  ✓ Ingredient groups: marinade, fish")


def test_ingredient_marinade(content):
    lower = content.lower()
    for item in ["saikyo miso", "sweet white miso", "mirin", "sake", "sugar"]:
        assert item in lower, f"Missing marinade ingredient: {item}"
    print("  ✓ Marinade: saikyo miso, mirin, sake, sugar")


def test_ingredient_butterfish(content):
    lower = content.lower()
    for name in ["butterfish", "sablefish", "black cod"]:
        assert name in lower, f"Missing fish type: {name}"
    print("  ✓ Fish types: butterfish, sablefish, black cod")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=6, max_steps=8)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, "
          f"{len(sensory)} sensory cues, inline timing present")


def test_saikyo_yaki_technique(content):
    """Verify saikyo-yaki technique: marinating 2-3 days, wiping, broiling."""
    lower = content.lower()
    assert "2 to 3 days" in lower or "2–3 days" in lower or "2-3 days" in lower, \
        "Missing 2-3 day marinade duration"
    assert "wipe" in lower, "Missing step to wipe off excess marinade"
    assert "broil" in lower, "Missing broiling step"
    print("  ✓ Saikyo-yaki technique: 2-3 day marinade, wipe, broil")


def test_notes(content):
    nb, vb = check_notes(content, min_cooks=2, min_variations=1)
    print(f"  ✓ Notes: {nb} cook's notes, {vb} variations, "
          f"make-ahead/storage, scaling")


def test_variations_specific(content):
    """Verify specific variations from the spec."""
    lower = content.lower()
    assert "spicy miso" in lower, "Missing Spicy Miso variation"
    assert "miso-maple" in lower or "miso maple" in lower, \
        "Missing Miso-Maple variation"
    print("  ✓ Variations: Spicy Miso, Miso-Maple")


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


def test_origin_note(content):
    """Verify origin note references addendum / Nobu-style technique."""
    assert "title-only addendum" in content.lower() or \
           "addendum" in content.lower(), "Missing addendum reference"
    assert "nobu" in content.lower() or "saikyo-yaki" in content.lower() or \
           "saikyo yaki" in content.lower(), \
        "Missing Nobu-style / saikyo-yaki reference"
    print("  ✓ Origin note references addendum and technique")


def test_no_corrupted_text(content):
    """Check for text corruption artifacts (duplication, broken formatting)."""
    issues = []
    
    # Check for known corruption: "Take**" broken bold, duplicated sentence fragments
    corrupted_patterns = [
        r"Take\*\* of the refrigerator",  # broken bold
        r"Gently wipe off \w+ out of",     # duplicated sentence fragment
    ]
    for pat in corrupted_patterns:
        if re.search(pat, content):
            issues.append(f"Corrupted text matching pattern")
    
    # Check for consecutive duplicate words
    dup_words = re.findall(r'\b(\w+)\s+\1\b', content)
    if dup_words:
        issues.append(f"Duplicate words found: {dup_words}")
    
    if issues:
        print(f"  ⚠ Content issues detected")
        raise AssertionError("; ".join(issues))
    print("  ✓ No text corruption detected")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),  # already loaded
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Frontmatter: cuisine Japanese", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: title/slug", lambda: test_frontmatter_series(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Ingredient groups", lambda: test_ingredient_groups(content)),
        ("Marinade ingredients", lambda: test_ingredient_marinade(content)),
        ("Fish types", lambda: test_ingredient_butterfish(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Saikyo-yaki technique", lambda: test_saikyo_yaki_technique(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Variations specific", lambda: test_variations_specific(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin note", lambda: test_origin_note(content)),
        ("No corrupted text", lambda: test_no_corrupted_text(content)),
    ]

    run_tests("TICKET-012", tests)


if __name__ == "__main__":
    run()
