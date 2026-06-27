#!/usr/bin/env python3
"""
TICKET-016: Create Miso Butter from title-only addendum.

Validates `recipes/condiment/miso-butter.md` against:
  - TICKET-016 requirements
  - docs/specs/016-miso-butter.md specification

TICKET-016 Requirements:
  1. File exists at recipes/condiment/miso-butter.md
  2. Ingredients: unsalted butter, white miso, optional honey/maple, scallions, sesame seeds
  3. Instructions: 4-6 (accepted range 4-7) steps with bolded action titles,
     sensory cues, inline timing
  4. Cook's notes (>=2), variations (>=1), make-ahead/storage, scaling
  5. Frontmatter: cuisine japanese-fusion, dietary_tags [vegetarian],
     tags include condiment/butter/miso, technique [compound-butter], protein none
  6. status: reviewed, date_modified: 2026-06-27
  7. Recipe includes shaping into log and chilling
"""

import os
import re
import sys

# Import shared test helpers
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *


# ── Constants ─────────────────────────────────────────────────────────────────

RECIPE_RELATIVE = os.path.join("condiment", "miso-butter.md")

EXPECTED_DATE_MODIFIED = "2026-06-27"

EXPECTED_CUISINE = "japanese-fusion"
EXPECTED_DIETARY_TAGS = ["vegetarian"]
EXPECTED_TAGS_CONTAIN = ["recipe/condiment", "technique/compound-butter"]
EXPECTED_PROTEIN = "none"


# ── Test Functions ────────────────────────────────────────────────────────────

def test_recipe_file_exists():
    """Verify the recipe file exists at the expected path."""
    path = os.path.join(RECIPES_DIR, RECIPE_RELATIVE)
    assert os.path.exists(path), f"Recipe file not found at {path}"


def test_frontmatter_cuisine(fm):
    """Check cuisine includes japanese-fusion."""
    cuisine = fm.get("cuisine", [])
    if isinstance(cuisine, str):
        cuisine = [cuisine]
    cuisine_lower = [c.lower() for c in cuisine]
    assert any(EXPECTED_CUISINE in c for c in cuisine_lower), (
        f"Expected cuisine to contain '{EXPECTED_CUISINE}', got {cuisine}"
    )


def test_frontmatter_dietary_tags(fm):
    """Check dietary_tags includes vegetarian."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )


def test_frontmatter_tags_contain(fm):
    """Check tags include recipe/condiment and technique/compound-butter."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_TAGS_CONTAIN:
        assert any(exp in t for t in tags_lower), (
            f"Expected a tag containing '{exp}', got {tags}"
        )


def test_frontmatter_protein_none(fm):
    """Check protein tag is 'none'."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    protein_tags = [t for t in tags if "protein" in t.lower()]
    if protein_tags:
        assert any("none" in t.lower() for t in protein_tags), (
            f"Expected protein:none, got {protein_tags}"
        )
    else:
        # Allow protein field as top-level key
        protein = fm.get("protein", [])
        if isinstance(protein, str):
            protein = [protein]
        protein_lower = [p.lower() for p in protein]
        assert any("none" in p for p in protein_lower), (
            f"Expected protein to be 'none', got {fm.get('protein')}"
        )


def test_status_reviewed(fm):
    """Check status is 'reviewed'."""
    val = check_frontmatter_field(fm, "status")
    assert val == "reviewed", f"Expected status 'reviewed', got '{val}'"


def test_date_modified(fm):
    """Check date_modified is 2026-06-27."""
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )


def test_ingredients_unsalted_butter(content):
    """Check content mentions 'unsalted butter'."""
    assert "unsalted butter" in content.lower(), (
        "Missing required ingredient: unsalted butter"
    )


def test_ingredients_white_miso(content):
    """Check content mentions 'white miso'."""
    assert "white miso" in content.lower(), (
        "Missing required ingredient: white miso"
    )


def test_ingredients_honey_or_maple(content):
    """Check content mentions 'honey' or 'maple'."""
    lower = content.lower()
    assert "honey" in lower or "maple" in lower, (
        "Missing optional sweetener: neither 'honey' nor 'maple' found"
    )


def test_ingredients_scallion_and_sesame(content):
    """Check content mentions 'scallion' and 'sesame'."""
    lower = content.lower()
    assert "scallion" in lower, "Missing ingredient: scallion(s)"
    assert "sesame" in lower, "Missing ingredient: sesame seeds"


def test_shaping_log(content):
    """Check recipe includes shaping into a log."""
    assert "log" in content.lower(), (
        "Recipe must include shaping into a log — 'log' not found in content"
    )


def test_instructions_check(content):
    """Check instructions meet requirements: 4-7 steps, bolded titles,
    sensory cues, inline timing."""
    check_instructions(content, min_steps=4, max_steps=7)


def test_notes_check(content):
    """Check Notes & Variations section: >=2 cook's notes, >=1 variation,
    make-ahead, storage, scaling."""
    check_notes(content, min_cooks=2, min_variations=1)


# ── Test Runner ───────────────────────────────────────────────────────────────

def main():
    """Load recipe and run all TICKET-016 tests."""
    fm, content = load_recipe(RECIPE_RELATIVE)

    tests = [
        ("File exists", test_recipe_file_exists),
        ("Cuisine is japanese-fusion", lambda: test_frontmatter_cuisine(fm)),
        ("Dietary tags include vegetarian", lambda: test_frontmatter_dietary_tags(fm)),
        ("Tags include recipe/condiment and technique/compound-butter",
         lambda: test_frontmatter_tags_contain(fm)),
        ("Protein is none", lambda: test_frontmatter_protein_none(fm)),
        ("Status is reviewed", lambda: test_status_reviewed(fm)),
        ("date_modified is 2026-06-27", lambda: test_date_modified(fm)),
        ("Content mentions unsalted butter", lambda: test_ingredients_unsalted_butter(content)),
        ("Content mentions white miso", lambda: test_ingredients_white_miso(content)),
        ("Content mentions honey or maple", lambda: test_ingredients_honey_or_maple(content)),
        ("Content mentions scallion and sesame", lambda: test_ingredients_scallion_and_sesame(content)),
        ("Recipe includes shaping into a log", lambda: test_shaping_log(content)),
        ("Instructions: 4-7 steps, bolded titles, sensory cues, inline timing",
         lambda: test_instructions_check(content)),
        ("Notes: >=2 cook's notes, >=1 variation, make-ahead, storage, scaling",
         lambda: test_notes_check(content)),
    ]

    run_tests("TICKET-016", tests)


if __name__ == "__main__":
    main()
