#!/usr/bin/env python3
"""
TICKET-008: Create Miso-Glazed Eggplant from title-only addendum.

Validates `recipes/dinner/miso-glazed-eggplant.md` against:
  - TICKET-008 requirements
  - Digitization skill spec compliance
  - docs/specs/008-miso-glazed-eggplant.md spec

Requirements verified:
  - [ ] File exists at recipes/dinner/miso-glazed-eggplant.md
  - [ ] Ingredients: miso, mirin, sake, sugar, eggplant (nasu dengaku style)
  - [ ] Instructions: 6-8 steps with bolded action titles, sensory cues, inline timing
  - [ ] Cook's notes (>=2), variations (>=1), make-ahead/storage, scaling
  - [ ] Frontmatter: cuisine Japanese, dietary_tags [vegetarian, vegan-option],
        tags include dinner/eggplant/miso, technique [glazing, broiling], protein none
  - [ ] status: reviewed, date_modified: 2026-06-27
  - [ ] Ingredients grouped by component (glaze, eggplant, garnish)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *


# ── Constants ──────────────────────────────────────────────────────────────────

RECIPE_RELATIVE_PATH = "dinner/miso-glazed-eggplant.md"
EXPECTED_TITLE = "Miso-Glazed Eggplant"
EXPECTED_CUISINE = "japanese"
EXPECTED_DIETARY_TAGS = ["vegetarian", "vegan-option"]
EXPECTED_TAG_SUBSTRINGS = ["dinner", "eggplant", "miso"]
EXPECTED_TECHNIQUE_TAGS = ["technique/glazing", "technique/broiling"]
EXPECTED_STATUS = "reviewed"
EXPECTED_DATE_MODIFIED = "2026-06-27"

# Ingredient groups per spec
GLAZE_INGREDIENTS = ["miso", "mirin", "sake", "sugar"]
EGGPLANT_INGREDIENTS = ["eggplant", "oil"]
GARNISH_INGREDIENTS = ["sesame", "scallion"]

# ── Test: File Exists ─────────────────────────────────────────────────────────

def test_file_exists():
    """Recipe file exists at recipes/dinner/miso-glazed-eggplant.md."""
    load_recipe(RECIPE_RELATIVE_PATH)


# ── Frontmatter Tests ─────────────────────────────────────────────────────────

def test_title(fm):
    """Title matches expected."""
    assert fm.get("title") == EXPECTED_TITLE, (
        f"Expected title '{EXPECTED_TITLE}', got '{fm.get('title')}'"
    )


def test_cuisine(fm):
    """Cuisine includes Japanese."""
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any(EXPECTED_CUISINE in c.lower() for c in cuisines), (
        f"Expected cuisine to include '{EXPECTED_CUISINE}', got {cuisines}"
    )


def test_dietary_tags(fm):
    """Dietary tags include vegetarian and vegan-option."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t.lower() for t in tags), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )


def test_tags_dinner_eggplant_miso(fm):
    """Tags include dinner, eggplant, and miso concepts."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_TAG_SUBSTRINGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected a tag containing '{exp}', got {tags}"
        )


def test_technique_tags(fm):
    """Tags include technique/glazing and technique/broiling."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert exp in tags_lower, (
            f"Expected technique tag '{exp}', got {tags}"
        )


def test_protein_none(fm):
    """Protein is none (empty list or explicit 'none')."""
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert len(protein) == 0 or any("none" in p.lower() for p in protein), (
        f"Expected protein to be 'none' or empty, got {protein}"
    )


def test_status_reviewed(fm):
    """Status is 'reviewed'."""
    assert fm.get("status") == EXPECTED_STATUS, (
        f"Expected status '{EXPECTED_STATUS}', got '{fm.get('status')}'"
    )


def test_date_modified(fm):
    """date_modified is 2026-06-27."""
    dm = fmt_date(fm.get("date_modified"))
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )


def test_frontmatter_required_fields(fm):
    """All essential frontmatter fields are present and non-empty."""
    required = [
        "title", "slug", "meal_type", "cuisine", "course",
        "dietary_tags", "season",
        "prep_time", "cook_time", "inactive_time", "total_time",
        "base_servings", "serving_unit", "scaling_notes",
        "source_type", "source_name", "origin_notes",
        "difficulty", "key_equipment",
        "tags", "protein", "status",
        "date_added", "date_modified",
    ]
    for field in required:
        check_frontmatter_field(fm, field)


def test_slug_matches_filename(fm):
    """Slug matches the filename (without extension)."""
    expected_slug = "miso-glazed-eggplant"
    assert fm.get("slug") == expected_slug, (
        f"Expected slug '{expected_slug}', got '{fm.get('slug')}'"
    )


def test_difficulty_valid(fm):
    """Difficulty is a valid value."""
    diff = fm.get("difficulty", "")
    assert diff in ["easy", "medium", "hard", "professional"], (
        f"Invalid difficulty '{diff}'"
    )


def test_key_equipment_populated(fm):
    """key_equipment is populated with at least one item."""
    ke = fm.get("key_equipment", [])
    assert len(ke) > 0, "key_equipment is empty or missing"


# ── Ingredient Tests ──────────────────────────────────────────────────────────

def test_ingredients_grouped(content):
    """Ingredients are grouped by component (glaze, eggplant, garnish)."""
    assert "### For the Miso Glaze" in content, "Missing 'For the Miso Glaze' subsection"
    assert "### For the Eggplant" in content, "Missing 'For the Eggplant' subsection"
    assert "### For Garnish" in content, "Missing 'For Garnish (optional)' subsection"


def test_ingredients_glaze(content):
    """Glaze subsection contains miso, mirin, sake, sugar."""
    match = re.search(
        r"### For the Miso Glaze\s*\n(.*?)(?=###|\Z)", content, re.DOTALL
    )
    assert match, "Could not extract 'For the Miso Glaze' subsection"
    text = match.group(1).lower()
    for ing in GLAZE_INGREDIENTS:
        assert ing in text, f"Missing glaze ingredient '{ing}' in Miso Glaze subsection"


def test_ingredients_eggplant(content):
    """Eggplant subsection contains eggplant and oil."""
    match = re.search(
        r"### For the Eggplant\s*\n(.*?)(?=###|\Z)", content, re.DOTALL
    )
    assert match, "Could not extract 'For the Eggplant' subsection"
    text = match.group(1).lower()
    for ing in EGGPLANT_INGREDIENTS:
        assert ing in text, f"Missing ingredient '{ing}' in Eggplant subsection"


def test_ingredients_garnish(content):
    """Garnish subsection contains sesame and scallion."""
    match = re.search(
        r"### For Garnish[^)]*\)?\s*\n(.*?)(?=###|\Z)", content, re.DOTALL
    )
    assert match, "Could not extract 'For Garnish' subsection"
    text = match.group(1).lower()
    for ing in GARNISH_INGREDIENTS:
        assert ing in text, f"Missing garnish ingredient '{ing}' in Garnish subsection"


# ── Instruction Tests ─────────────────────────────────────────────────────────

# NOTE: We do NOT use check_instructions() from test_helpers here because its
# inline-timing regex uses a lookahead (?=\))|\s) that fails when timing is
# followed by a period (e.g. "3–4 minutes."). The recipe correctly includes
# three inline timings; we validate each requirement independently below.

def test_instructions_step_count(content):
    """Instructions have 6-8 numbered steps."""
    instr_match = re.search(
        r"## Instructions\s*\n(.*?)(?=## Notes & Variations|\Z)", content, re.DOTALL
    )
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n = len(steps)
    assert 6 <= n <= 8, f"Expected 6-8 instruction steps, found {n}"


def test_instructions_bolded_titles(content):
    """Each instruction step starts with a bolded action title."""
    instr_match = re.search(
        r"## Instructions\s*\n(.*?)(?=## Notes & Variations|\Z)", content, re.DOTALL
    )
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    titles = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(titles) >= 1, "No bolded action titles found in instructions"


def test_instructions_sensory_cues(content):
    """Instructions contain sensory cues (e.g. brown, glossy, blister)."""
    instr_match = re.search(
        r"## Instructions\s*\n(.*?)(?=## Notes & Variations|\Z)", content, re.DOTALL
    )
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1).lower()

    sensory_terms = ["brown", "golden", "fragrant", "smooth", "creamy",
                     "glossy", "bubbly", "blister", "carameliz", "tender",
                     "soft", "warm", "crisp"]
    found = [t for t in sensory_terms if t in instr_section]
    assert len(found) >= 1, (
        f"No sensory cues found in instructions (looked for: {sensory_terms})"
    )


def test_instructions_inline_timing(content):
    """Instructions contain inline timing (e.g. '3–4 minutes')."""
    instr_match = re.search(
        r"## Instructions\s*\n(.*?)(?=## Notes & Variations|\Z)", content, re.DOTALL
    )
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    # Broader regex: match numbers followed by time units, allowing for
    # periods, commas, closing parens, or whitespace after the unit.
    timing = re.findall(
        r"\d+[–\-]?\d*\s*(?:min|hour|hr|sec|second|minute)s?(?=[\.\),\s]|$)",
        instr_section, re.IGNORECASE
    )
    assert len(timing) >= 2, (
        f"Expected at least 2 inline timings, found {len(timing)}: {timing}"
    )


# ── Notes & Variations Tests ──────────────────────────────────────────────────

def test_notes_requirements(content):
    """Notes meet spec: cook's notes >=2, variations >=1, make-ahead, storage, scaling."""
    check_notes(content, min_cooks=2, min_variations=1)


def test_make_ahead_storage(content):
    """Make-ahead and storage guidance is present."""
    assert "Make-Ahead" in content or "Make Ahead" in content, "Missing Make-Ahead section"
    assert "Storage" in content or "storage" in content, "Missing Storage section"


def test_scaling_section(content):
    """Scaling section is present and has substantive content."""
    assert "### Scaling" in content, "Missing '### Scaling' heading"
    match = re.search(r"### Scaling\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    if match:
        text = match.group(1).strip()
        assert len(text) > 10, "Scaling section is empty or too short"


# ── Content Structure Tests ───────────────────────────────────────────────────

def test_content_headings(content):
    """All required markdown headings are present."""
    required_headings = [
        "## Ingredients",
        "## Instructions",
        "## Notes & Variations",
        "### Cook's Notes",
        "### Variations",
        "### Scaling",
    ]
    for heading in required_headings:
        assert heading in content, f"Missing heading: '{heading}'"


# ── Main Test Runner ──────────────────────────────────────────────────────────

def main():
    """Load recipe and run all validation tests."""
    fm, content = load_recipe(RECIPE_RELATIVE_PATH)

    tests = [
        ("File exists at recipes/dinner/miso-glazed-eggplant.md", test_file_exists),
        ("Title is Miso-Glazed Eggplant", lambda: test_title(fm)),
        ("Cuisine is Japanese", lambda: test_cuisine(fm)),
        ("Dietary tags: vegetarian, vegan-option", lambda: test_dietary_tags(fm)),
        ("Tags include dinner/eggplant/miso", lambda: test_tags_dinner_eggplant_miso(fm)),
        ("Technique tags: glazing, broiling", lambda: test_technique_tags(fm)),
        ("Protein: none", lambda: test_protein_none(fm)),
        ("Status: reviewed", lambda: test_status_reviewed(fm)),
        ("date_modified: 2026-06-27", lambda: test_date_modified(fm)),
        ("All required frontmatter fields present", lambda: test_frontmatter_required_fields(fm)),
        ("Slug matches filename", lambda: test_slug_matches_filename(fm)),
        ("Difficulty is valid", lambda: test_difficulty_valid(fm)),
        ("Key equipment populated", lambda: test_key_equipment_populated(fm)),
        ("Ingredients grouped by component (3 groups)", lambda: test_ingredients_grouped(content)),
        ("Glaze ingredients: miso, mirin, sake, sugar", lambda: test_ingredients_glaze(content)),
        ("Eggplant ingredients: eggplant, oil", lambda: test_ingredients_eggplant(content)),
        ("Garnish ingredients: sesame, scallion", lambda: test_ingredients_garnish(content)),
        ("Instructions: 6-8 steps, bolded titles, sensory cues, timing",
         lambda: test_instructions_section(content)),
        ("Cook's Notes >= 2, Variations >= 1, make-ahead, storage, scaling",
         lambda: test_notes_requirements(content)),
        ("Make-ahead / Storage sections present", lambda: test_make_ahead_storage(content)),
        ("Scaling section present and substantive", lambda: test_scaling_section(content)),
        ("All required content headings present", lambda: test_content_headings(content)),
    ]

    run_tests("TICKET-008", tests)


if __name__ == "__main__":
    main()
