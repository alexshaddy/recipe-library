#!/usr/bin/env python3
"""
TICKET-009: Create Miso-Glazed Salmon from Title-Only Addendum.

Validates `recipes/dinner/miso-glazed-salmon.md` against:
  - TICKET-009 requirements
  - Saikyo-yaki technique requirements

Requirements from TICKET-009:
  1. File exists at recipes/dinner/miso-glazed-salmon.md
  2. Ingredients: saikyo/white miso, mirin, sake, sugar, salmon fillets (saikyo-yaki style)
  3. Instructions: 6-8 steps with bolded action titles, sensory cues, inline timing
  4. Cook's notes (>=2), variations (>=1), make-ahead/storage, scaling
  5. Frontmatter: cuisine Japanese, dietary_tags [gluten-free-option],
     tags include dinner/salmon/miso, technique [marinating, broiling],
     protein [salmon]
  6. status: reviewed, date_modified: 2026-06-27
  7. Ingredients grouped by component (marinade, salmon)

Specific content checks:
  - Mentions "saikyo miso" or "white miso"
  - Mentions "marinate" and "24" and "48" (marinating time)
  - Mentions "wipe" (wiping off excess marinade)
  - Tags include technique/marinating and technique/broiling
  - Tags include protein/salmon
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

# ── Constants ─────────────────────────────────────────────────────────────────

RECIPE = "dinner/miso-glazed-salmon.md"

EXPECTED_TITLE = "Miso-Glazed Salmon"
EXPECTED_STATUS = "reviewed"
EXPECTED_DATE_MODIFIED = "2026-06-27"
EXPECTED_CUISINE = "japanese"
EXPECTED_DIETARY_TAGS = ["gluten-free-option"]
EXPECTED_TAGS_SUBSTRINGS = ["recipe/dinner", "ingredient/salmon", "ingredient/miso"]
EXPECTED_TECHNIQUE_TAGS = ["technique/marinating", "technique/broiling"]
EXPECTED_PROTEIN = ["salmon"]

REQUIRED_FRONTMATTER_FIELDS = [
    "title", "aliases", "slug", "meal_type", "cuisine", "course",
    "dietary_tags", "season",
    "prep_time", "cook_time", "inactive_time", "total_time",
    "base_servings", "serving_unit", "scaling_notes",
    "source_type", "source_name", "origin_notes",
    "difficulty", "key_equipment",
    "tags", "protein", "status",
    "date_added", "date_modified",
]


# ── Test Functions ────────────────────────────────────────────────────────────


def test_title(fm):
    """Title must be 'Miso-Glazed Salmon'."""
    assert fm.get("title") == EXPECTED_TITLE, (
        f"Expected title '{EXPECTED_TITLE}', got '{fm.get('title')}'"
    )


def test_status_reviewed(fm):
    """Status must be 'reviewed'."""
    assert fm.get("status") == EXPECTED_STATUS, (
        f"Expected status '{EXPECTED_STATUS}', got '{fm.get('status')}'"
    )


def test_date_modified(fm):
    """date_modified must be 2026-06-27."""
    dm = fmt_date(fm.get("date_modified"))
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )


def test_cuisine_japanese(fm):
    """Cuisine must include 'japanese'."""
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any(EXPECTED_CUISINE in c.lower() for c in cuisines), (
        f"Expected cuisine to include '{EXPECTED_CUISINE}', got {cuisines}"
    )


def test_dietary_tags_gluten_free(fm):
    """dietary_tags must include 'gluten-free-option'."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t.lower() for t in tags), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )


def test_tags_include_dinner_salmon_miso(fm):
    """Tags must include recipe/dinner, ingredient/salmon, ingredient/miso."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_TAGS_SUBSTRINGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected a tag containing '{exp}', got {tags}"
        )


def test_technique_tags(fm):
    """Tags must include technique/marinating and technique/broiling."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert exp in tags, (
            f"Expected technique tag '{exp}', got {tags}"
        )


def test_protein_tags(fm):
    """Protein must include salmon."""
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    for exp in EXPECTED_PROTEIN:
        assert exp in protein, (
            f"Expected protein '{exp}', got {protein}"
        )


def test_ingredients_saikyo_miso(content):
    """Content must reference 'saikyo miso' or 'white miso'."""
    lower = content.lower()
    assert "saikyo miso" in lower or "white miso" in lower, (
        "Content does not mention 'saikyo miso' or 'white miso'"
    )


def test_marinate_24_48_hours(content):
    """Content must mention 'marinate' and both '24' and '48' (marinating time)."""
    lower = content.lower()
    assert "marinate" in lower, "Content does not mention 'marinate'"
    assert "24" in content, "Content does not mention '24' (marinating time lower bound)"
    assert "48" in content, "Content does not mention '48' (marinating time upper bound)"


def test_wipe_instruction(content):
    """Content must mention 'wipe' (wiping off excess marinade)."""
    lower = content.lower()
    assert "wipe" in lower, (
        "Content does not mention 'wipe' for removing excess marinade"
    )


def test_ingredients_grouped(content):
    """Ingredients must be grouped by component subheadings."""
    assert "### For the Miso Marinade" in content, (
        "Missing '### For the Miso Marinade' ingredient group"
    )
    assert "### For the Salmon" in content, (
        "Missing '### For the Salmon' ingredient group"
    )


def test_ingredient_core_items(content):
    """Content must include miso, mirin, sake, sugar, and salmon."""
    lower = content.lower()
    core = ["miso", "mirin", "sake", "sugar", "salmon"]
    missing = [i for i in core if i not in lower]
    assert not missing, f"Missing core ingredients: {missing}"


def test_instructions(content):
    """Instructions must have 6-8 steps with bolded titles, sensory cues, inline timing."""
    check_instructions(content, min_steps=6, max_steps=8)


def test_notes(content):
    """Must have >=2 cook's notes, >=1 variation, make-ahead/storage, scaling."""
    check_notes(content, min_cooks=2, min_variations=1)


def test_make_ahead(content):
    """Must have a Make-Ahead section."""
    assert "Make-Ahead" in content or "Make Ahead" in content, (
        "Missing 'Make-Ahead' section"
    )


def test_storage(content):
    """Must have a Storage section."""
    lower = content.lower()
    assert "storage" in lower, "Missing 'Storage' in content"


def test_scaling_section(content):
    """Must have a Scaling section."""
    assert "### Scaling" in content, "Missing '### Scaling' section"


def test_content_sections(content):
    """Check all required section headings exist."""
    required = [
        "## Ingredients",
        "## Instructions",
        "## Notes & Variations",
        "### Cook's Notes",
        "### Variations",
        "### Scaling",
    ]
    for heading in required:
        assert heading in content, f"Missing heading: '{heading}'"


def test_key_steps_present(content):
    """Key technique steps must be present: prepare marinade, marinate, wipe, broil, rest, serve."""
    lower = content.lower()
    steps = ["prepare the marinade", "marinate", "wipe", "broil", "rest", "garnish and serve"]
    missing = [s for s in steps if s not in lower]
    assert not missing, f"Missing key technique steps in content: {missing}"


def test_frontmatter_required_fields(fm):
    """All frontmatter fields must be present and non-empty."""
    for field in REQUIRED_FRONTMATTER_FIELDS:
        check_frontmatter_field(fm, field)


def test_tags_include_recipe_meal_type(fm):
    """Check tags include a recipe/ tag."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    has_recipe_tag = any("recipe/" in t for t in tags)
    assert has_recipe_tag, f"Expected a 'recipe/...' tag, got {tags}"


def test_source_documented(fm):
    """Check source_type and source_name are documented."""
    assert fm.get("source_type"), "source_type is missing or empty"
    assert fm.get("source_name"), "source_name is missing or empty"


def test_difficulty_set(fm):
    """Check difficulty is a valid value."""
    diff = fm.get("difficulty")
    assert diff in ["easy", "medium", "hard", "professional"], (
        f"Expected difficulty in [easy, medium, hard, professional], got '{diff}'"
    )


def test_key_equipment_present(fm):
    """Check key_equipment is populated."""
    ke = fm.get("key_equipment", [])
    assert len(ke) > 0, "key_equipment is empty or missing"


def test_origin_notes_present(fm):
    """Check origin_notes is populated."""
    on = fm.get("origin_notes", "")
    assert on, "origin_notes is missing or empty"


def test_slug_matches_filename(fm):
    """Check slug matches filename (without .md extension)."""
    expected_slug = "miso-glazed-salmon"
    actual_slug = fm.get("slug", "")
    assert actual_slug == expected_slug, (
        f"Expected slug '{expected_slug}', got '{actual_slug}'"
    )


def test_base_servings_and_unit(fm):
    """Check base_servings and serving_unit are populated."""
    assert fm.get("base_servings") is not None, "base_servings is missing"
    assert fm.get("serving_unit", "") != "", "serving_unit is empty"


def test_inactive_time_set(fm):
    """Check inactive_time is set (for marinating)."""
    it = fm.get("inactive_time", "")
    assert it, "inactive_time is missing or empty"
    assert "hr" in it or "hour" in it, (
        f"inactive_time does not reference hours: '{it}'"
    )


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Load recipe once; all subsequent tests use the same data
    fm, content = load_recipe(RECIPE)

    tests = [
        # Frontmatter completeness
        ("All required frontmatter fields", lambda: test_frontmatter_required_fields(fm)),
        ("Title", lambda: test_title(fm)),
        ("Status reviewed", lambda: test_status_reviewed(fm)),
        ("date_modified", lambda: test_date_modified(fm)),
        ("Slug matches filename", lambda: test_slug_matches_filename(fm)),

        # Cuisine & dietary
        ("Cuisine Japanese", lambda: test_cuisine_japanese(fm)),
        ("Dietary tags: gluten-free-option", lambda: test_dietary_tags_gluten_free(fm)),

        # Tags
        ("Tags include dinner/salmon/miso", lambda: test_tags_include_dinner_salmon_miso(fm)),
        ("Tags include recipe/ type", lambda: test_tags_include_recipe_meal_type(fm)),
        ("Technique tags: marinating, broiling", lambda: test_technique_tags(fm)),
        ("Protein tags: salmon", lambda: test_protein_tags(fm)),

        # Source & metadata
        ("Source documented", lambda: test_source_documented(fm)),
        ("Difficulty set", lambda: test_difficulty_set(fm)),
        ("Key equipment populated", lambda: test_key_equipment_present(fm)),
        ("Origin notes present", lambda: test_origin_notes_present(fm)),
        ("Base servings and unit", lambda: test_base_servings_and_unit(fm)),
        ("Inactive time set (marinating period)", lambda: test_inactive_time_set(fm)),

        # Ingredients
        ("Core ingredients: miso, mirin, sake, sugar, salmon", lambda: test_ingredient_core_items(content)),
        ("Saikyo miso or white miso referenced", lambda: test_ingredients_saikyo_miso(content)),
        ("Ingredients grouped by component (marinade, salmon)", lambda: test_ingredients_grouped(content)),

        # Instructions
        ("Instructions (6-8 steps, bolded titles, sensory cues, timing)", lambda: test_instructions(content)),
        ("Marinate 24-48 hours mentioned", lambda: test_marinate_24_48_hours(content)),
        ("Wipe instruction present", lambda: test_wipe_instruction(content)),
        ("Key steps: prepare marinade, marinate, wipe, broil, rest, serve", lambda: test_key_steps_present(content)),

        # Notes & variations
        ("Cook's notes, variations, make-ahead, storage, scaling", lambda: test_notes(content)),
        ("Make-Ahead section", lambda: test_make_ahead(content)),
        ("Storage section", lambda: test_storage(content)),
        ("Scaling section heading", lambda: test_scaling_section(content)),

        # Content structure
        ("All required section headings", lambda: test_content_sections(content)),
    ]

    run_tests("TICKET-009", tests)
