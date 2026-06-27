#!/usr/bin/env python3
"""
TICKET-010: Create Miso Soup from Title-Only Addendum.

Validates `recipes/soup/miso-soup.md` against:
  - TICKET-010 requirements
  - Traditional miso soup technique requirements

Requirements from TICKET-010:
  1. File exists at recipes/soup/miso-soup.md
  2. Ingredients: dashi (kombu + katsuobushi), miso paste, tofu, wakame, scallions
  3. Instructions: 5-7 steps with bolded action titles, sensory cues, inline timing
  4. Cook's notes (>=2), variations (>=1), make-ahead/storage, scaling
  5. Frontmatter: cuisine Japanese, dietary_tags [vegetarian-option, vegan-option,
     gluten-free-option], tags include soup/miso, technique [dashi, simmering],
     protein [tofu]
  6. status: reviewed, date_modified: 2026-06-27

Specific content checks:
  - Content mentions "dashi" and "kombu" and "katsuobushi"
  - Content mentions "tofu" and "wakame" and "scallion"
  - Content mentions "miso" and NOT boiling after adding miso
  - Tags include technique/dashi and technique/simmering
  - Protein includes tofu
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

# ── Constants ─────────────────────────────────────────────────────────────────

RECIPE = "soup/miso-soup.md"

EXPECTED_TITLE = "Miso Soup"
EXPECTED_STATUS = "reviewed"
EXPECTED_DATE_MODIFIED = "2026-06-27"
EXPECTED_CUISINE = "japanese"
EXPECTED_DIETARY_TAGS = ["vegetarian-option", "vegan-option", "gluten-free-option"]
EXPECTED_TAGS_SUBSTRINGS = ["recipe/soup", "ingredient/miso", "ingredient/dashi"]
EXPECTED_TECHNIQUE_TAGS = ["technique/dashi", "technique/simmering"]
EXPECTED_PROTEIN = ["tofu"]

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
    """Title must be 'Miso Soup'."""
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


def test_dietary_tags(fm):
    """dietary_tags must include vegetarian-option, vegan-option, gluten-free-option."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t.lower() for t in tags), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )


def test_tags_include_soup_miso_dashi(fm):
    """Tags must include recipe/soup, ingredient/miso, ingredient/dashi."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_TAGS_SUBSTRINGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected a tag containing '{exp}', got {tags}"
        )


def test_technique_tags(fm):
    """Tags must include technique/dashi and technique/simmering."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert exp in tags, (
            f"Expected technique tag '{exp}', got {tags}"
        )


def test_protein_tags(fm):
    """Protein must include tofu."""
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    for exp in EXPECTED_PROTEIN:
        assert exp in protein, (
            f"Expected protein '{exp}', got {protein}"
        )


def test_ingredients_dashi_components(content):
    """Content must mention 'dashi' and 'kombu' and 'katsuobushi'."""
    lower = content.lower()
    assert "dashi" in lower, "Content does not mention 'dashi'"
    assert "kombu" in lower, "Content does not mention 'kombu'"
    assert "katsuobushi" in lower, "Content does not mention 'katsuobushi'"


def test_ingredients_tofu_wakame_scallion(content):
    """Content must mention 'tofu' and 'wakame' and 'scallion'."""
    lower = content.lower()
    assert "tofu" in lower, "Content does not mention 'tofu'"
    assert "wakame" in lower, "Content does not mention 'wakame'"
    assert "scallion" in lower, "Content does not mention 'scallion'"


def test_miso_no_boiling_after_adding(content):
    """Content must mention 'miso' and state NOT to boil after adding."""
    lower = content.lower()
    assert "miso" in lower, "Content does not mention 'miso'"
    # Must contain a warning against boiling after miso is added
    assert "do not boil after adding miso" in lower or \
           "never boil miso" in lower or \
           "never boil after adding miso" in lower or \
           "do not boil after adding" in lower, (
        "Content must warn against boiling after adding miso"
    )


def test_ingredients_grouped_by_component(content):
    """Ingredients must be grouped by component subheadings."""
    assert "### For the Dashi" in content, (
        "Missing '### For the Dashi' ingredient group"
    )
    assert "### For the Miso Paste" in content, (
        "Missing '### For the Miso Paste' ingredient group"
    )
    assert "### For the Solids" in content, (
        "Missing '### For the Solids' ingredient group"
    )


def test_ingredient_core_items(content):
    """Content must include dashi, miso, tofu, wakame, scallions."""
    lower = content.lower()
    core = ["dashi", "miso", "tofu", "wakame", "scallion"]
    missing = [i for i in core if i not in lower]
    assert not missing, f"Missing core ingredients: {missing}"


def test_instructions(content):
    """Instructions must have 5-7 steps with bolded titles, sensory cues, inline timing."""
    check_instructions(content, min_steps=5, max_steps=7)


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
    """Key technique steps must be present: make dashi, prepare solids, temper miso, finish, serve."""
    lower = content.lower()
    steps = ["make the dashi", "prepare the solids", "temper the miso",
             "combine and heat", "add tofu and wakame", "finish the soup"]
    missing = [s for s in steps if s not in lower]
    assert not missing, f"Missing key technique steps in content: {missing}"


def test_frontmatter_required_fields(fm):
    """All frontmatter fields must be present and non-empty."""
    for field in REQUIRED_FRONTMATTER_FIELDS:
        check_frontmatter_field(fm, field)


def test_tags_include_recipe_type(fm):
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
    expected_slug = "miso-soup"
    actual_slug = fm.get("slug", "")
    assert actual_slug == expected_slug, (
        f"Expected slug '{expected_slug}', got '{actual_slug}'"
    )


def test_base_servings_and_unit(fm):
    """Check base_servings and serving_unit are populated."""
    assert fm.get("base_servings") is not None, "base_servings is missing"
    assert fm.get("serving_unit", "") != "", "serving_unit is empty"


def test_dashi_method_content(content):
    """Content must describe the dashi-making process (soak kombu, heat, remove kombu, add katsuobushi, strain)."""
    lower = content.lower()
    assert "soak" in lower or "steep" in lower, "Dashi method must mention soaking/steeping kombu"
    assert "remove kombu" in lower or "remove" in lower, "Dashi method must mention removing kombu"
    assert "strain" in lower or "fine-mesh" in lower or "cheesecloth" in lower, (
        "Dashi method must mention straining"
    )


def test_miso_tempering_method(content):
    """Content must describe tempering miso in a ladle of hot dashi before adding to pot."""
    lower = content.lower()
    assert "ladle" in lower and "whisk" in lower and "smooth" in lower, (
        "Content must describe tempering miso: ladle, whisk, smooth"
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
        ("Dietary tags: vegetarian, vegan, gluten-free options",
         lambda: test_dietary_tags(fm)),

        # Tags
        ("Tags include recipe/soup, ingredient/miso, ingredient/dashi",
         lambda: test_tags_include_soup_miso_dashi(fm)),
        ("Tags include recipe/ type", lambda: test_tags_include_recipe_type(fm)),
        ("Technique tags: dashi, simmering", lambda: test_technique_tags(fm)),
        ("Protein tags: tofu", lambda: test_protein_tags(fm)),

        # Source & metadata
        ("Source documented", lambda: test_source_documented(fm)),
        ("Difficulty set", lambda: test_difficulty_set(fm)),
        ("Key equipment populated", lambda: test_key_equipment_present(fm)),
        ("Origin notes present", lambda: test_origin_notes_present(fm)),
        ("Base servings and unit", lambda: test_base_servings_and_unit(fm)),

        # Ingredients
        ("Core ingredients: dashi, miso, tofu, wakame, scallions",
         lambda: test_ingredient_core_items(content)),
        ("Dashi components: kombu + katsuobushi mentioned",
         lambda: test_ingredients_dashi_components(content)),
        ("Tofu, wakame, scallion mentioned",
         lambda: test_ingredients_tofu_wakame_scallion(content)),
        ("Ingredients grouped by component (dashi, miso, solids)",
         lambda: test_ingredients_grouped_by_component(content)),

        # Miso-specific techniques
        ("Miso mentioned with no-boil-after rule",
         lambda: test_miso_no_boiling_after_adding(content)),

        # Instructions
        ("Instructions (5-7 steps, bolded titles, sensory cues, timing)",
         lambda: test_instructions(content)),
        ("Key technique steps: make dashi, prepare, combine, temper, finish, serve",
         lambda: test_key_steps_present(content)),

        # Dashi method
        ("Dashi-making process described (soak, remove kombu, add katsuobushi, strain)",
         lambda: test_dashi_method_content(content)),

        # Miso tempering
        ("Miso tempering method described (ladle, whisk, smooth)",
         lambda: test_miso_tempering_method(content)),

        # Notes & variations
        ("Cook's notes, variations, make-ahead, storage, scaling",
         lambda: test_notes(content)),
        ("Make-Ahead section", lambda: test_make_ahead(content)),
        ("Storage section", lambda: test_storage(content)),
        ("Scaling section heading", lambda: test_scaling_section(content)),

        # Content structure
        ("All required section headings", lambda: test_content_sections(content)),
    ]

    run_tests("TICKET-010", tests)
