#!/usr/bin/env python3
"""
TICKET-002: Fix Sweet Chili Sauce ingredient mismatch vs notebook source.

Validates `recipes/condiment/sweet-chili-sauce.md` against:
  - TICKET-002 requirements
  - Notebook source (chef_recipe_notebook.md p.13):
    ¼ cup rice vinegar, ¼ cup water, ¼ cup sugar, 1.5 tbsp sambal oelek,
    ½ tbsp cornstarch + 1 tbsp water (slurry)
  - docs/specs/002-sweet-chili-sauce.md spec
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "condiment/sweet-chili-sauce.md"
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
                  "tags",
                  "status", "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    # inactive_time may be empty for quick-prep sauces
    assert "inactive_time" in fm, "inactive_time field missing"
    print("  ✓ All required frontmatter fields present")


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any("asian" in c.lower() for c in cuisines), \
        f"Expected cuisine 'asian', got {cuisines}"
    print("  ✓ Cuisine is asian")


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
    assert "recipe/condiment" in tags, f"Missing tag 'recipe/condiment', got {tags}"
    assert "technique/simmer" in tags, f"Missing tag 'technique/simmer', got {tags}"
    print("  ✓ Tags include recipe/condiment and technique/simmer")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, \
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_title_slug(fm):
    assert fm.get("title") == "Sweet Chili Sauce", \
        f"Expected title 'Sweet Chili Sauce', got '{fm.get('title')}'"
    assert fm.get("slug") == "sweet-chili-sauce", \
        f"Expected slug 'sweet-chili-sauce', got '{fm.get('slug')}'"
    print("  ✓ Title and slug correct")


def test_source_documented(fm):
    st = fm.get("source_type")
    sn = fm.get("source_name")
    assert st, "source_type empty"
    assert sn, "source_name empty"
    print(f"  ✓ Source documented: {st} — {sn}")


# --- Notebook-accurate ingredient checks ---

def test_ingredient_rice_vinegar(content):
    """Notebook: ¼ cup rice vinegar."""
    lower = content.lower()
    assert "rice vinegar" in lower, \
        "Missing 'rice vinegar' — notebook specifies ¼ cup rice vinegar"
    assert re.search(r'1/4\s*cup.*rice.vinegar|rice.vinegar.*1/4\s*cup', lower), \
        "Expected '¼ cup rice vinegar' per notebook source"
    print("  ✓ Rice vinegar: ¼ cup (notebook-accurate)")


def test_ingredient_sugar_quarter_cup(content):
    """Notebook: ¼ cup sugar (NOT 1 cup)."""
    lower = content.lower()
    # Must NOT have 1 cup sugar — notebook says ¼ cup
    assert not re.search(r'1\s*cup[^s].*sugar|sugar.*1\s*cup[^s]', lower), \
        "Found '1 cup sugar' — notebook specifies ¼ cup sugar, not 1 cup"
    assert re.search(r'1/4\s*cup.*sugar|sugar.*1/4\s*cup', lower), \
        "Missing '¼ cup sugar' — notebook specifies ¼ cup sugar"
    print("  ✓ Sugar: ¼ cup (notebook-accurate, not 1 cup)")


def test_ingredient_water_quarter_cup(content):
    """Notebook: ¼ cup water."""
    lower = content.lower()
    assert re.search(r'1/4\s*cup.*water|water.*1/4\s*cup', lower), \
        "Missing '¼ cup water' — notebook specifies ¼ cup water"
    print("  ✓ Water: ¼ cup (notebook-accurate)")


def test_ingredient_sambal_oelek(content):
    """Notebook: 1.5 tbsp sambal oelek (not generic chile flakes)."""
    lower = content.lower()
    assert "sambal" in lower, \
        "Missing 'sambal oelek' — notebook specifies 1.5 tbsp sambal oelek"
    print("  ✓ Sambal oelek present (notebook-accurate)")


def test_ingredient_cornstarch_slurry(content):
    """Notebook: ½ tbsp cornstarch + 1 tbsp water (slurry)."""
    lower = content.lower()
    assert "cornstarch" in lower, \
        "Missing 'cornstarch' — notebook specifies cornstarch slurry"
    assert "slurry" in lower, \
        "Missing 'slurry' — notebook specifies cornstarch + water slurry"
    print("  ✓ Cornstarch slurry present (notebook-accurate)")


def test_no_unverified_markers(content):
    """No [TO VERIFY] or [UNCLEAR] markers should remain."""
    assert "[TO VERIFY]" not in content, "Unresolved [TO VERIFY] marker"
    assert "[UNCLEAR]" not in content, "Unresolved [UNCLEAR] marker"
    print("  ✓ No [TO VERIFY] or [UNCLEAR] markers")


def test_instructions(content):
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n = len(steps)
    assert 5 <= n <= 8, f"Expected 5-8 instructions, found {n}"

    titles = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(titles) >= 1, "No bolded action titles found"

    sensory = ["sizzle", "brown", "golden", "fragrant", "smooth", "creamy",
               "glossy", "aroma", "bubbly", "melt", "soft", "warm", "tender",
               "crisp", "pink", "wilt", "translucent", "thick", "cloudy",
               "syrupy", "coated"]
    found = [t for t in sensory if t in instr_section.lower()]
    assert len(found) >= 1, f"No sensory cues found in instructions"

    timing = re.findall(r'\d+[–\-]?\d*\s*(?:min|hour|hr|sec|second|minute)s?',
                        instr_section, re.IGNORECASE)
    assert len(timing) >= 2, f"Too few inline timings: found {timing}"

    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, "
          f"{len(found)} sensory cues, {len(timing)} inline timings")


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
        ("Frontmatter: cuisine asian", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: title/slug", lambda: test_frontmatter_title_slug(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Ingredient: ¼ cup rice vinegar", lambda: test_ingredient_rice_vinegar(content)),
        ("Ingredient: ¼ cup sugar (not 1 cup)", lambda: test_ingredient_sugar_quarter_cup(content)),
        ("Ingredient: ¼ cup water", lambda: test_ingredient_water_quarter_cup(content)),
        ("Ingredient: sambal oelek", lambda: test_ingredient_sambal_oelek(content)),
        ("Ingredient: cornstarch slurry", lambda: test_ingredient_cornstarch_slurry(content)),
        ("No [TO VERIFY]/[UNCLEAR] markers", lambda: test_no_unverified_markers(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling", lambda: test_scaling(content)),
        ("Sections", lambda: test_sections(content)),
    ]

    run_tests("TICKET-002", tests)


if __name__ == "__main__":
    run()
