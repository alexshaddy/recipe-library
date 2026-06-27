#!/usr/bin/env python3
"""
TICKET-005: Fix Miso Butter ingredient mismatch vs notebook source.

Validates `recipes/condiment/miso-butter.md` against:
  - TICKET-005 requirements
  - Digitization skill spec compliance
  - Recipe template conformance

Notebook source specifies:
  - White miso
  - Unsalted butter
  - Mirin
  - Honey

Per TICKET-016 (companion spec):
  - Japanese-fusion cuisine
  - Dietary: vegetarian
  - Tags: condiment, butter, miso
  - Technique: compound-butter
  - Protein: none
  - Optional: honey/maple, scallions, sesame seeds
"""

import os
import re
import sys
import yaml

RECIPE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recipes")
RECIPE_PATH = os.path.join(RECIPE_DIR, "condiment", "miso-butter.md")

# ── Expected values ──────────────────────────────────────────────────────────

EXPECTED_FRONTMATTER = {
    "title": "Miso Butter",
    "status": "reviewed",
}

REQUIRED_FRONTMATTER_FIELDS = [
    "title", "aliases", "slug", "meal_type", "cuisine", "course",
    "dietary_tags", "occasion", "season",
    "prep_time", "cook_time", "inactive_time", "total_time",
    "base_servings", "serving_unit", "scaling_notes",
    "source_type", "source_name", "source_url", "source_page", "origin_notes",
    "difficulty", "key_equipment",
    "tags", "status",
    "date_added", "date_modified",
]

# Expected cuisine/dietary/tags from TICKET-016 spec
EXPECTED_CUISINE = "japanese-fusion"
EXPECTED_DIETARY_TAGS = ["vegetarian"]  # at minimum
EXPECTED_TAGS_SUBSTRINGS = ["condiment", "butter", "miso"]
EXPECTED_TECHNIQUE_TAGS = ["compound-butter"]
EXPECTED_PROTEIN_TAGS = ["none"]

# Expected notebook-specified ingredients (these are what the ticket says the notebook specifies)
NOTEBOOK_INGREDIENTS = ["white miso", "unsalted butter", "mirin", "honey"]

# Expected instruction count range
MIN_INSTRUCTIONS = 5
MAX_INSTRUCTIONS = 8

# Expected notes sections
MIN_COOKS_NOTES = 2
MIN_VARIATIONS = 1

EXPECTED_DATE_MODIFIED = "2026-06-27"

# Required sections in the recipe
REQUIRED_SECTIONS = [
    "Make-Ahead", "Storage", "Scaling",
]


def parse_frontmatter(content):
    """Parse YAML frontmatter from a markdown file."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


def test_file_exists():
    """Check that the recipe file exists at the expected path."""
    assert os.path.exists(RECIPE_PATH), (
        f"Recipe file not found at {RECIPE_PATH}. "
        "The implementer must create recipes/condiment/miso-butter.md"
    )
    print(f"  ✓ File exists at {RECIPE_PATH}")


def test_frontmatter_present():
    """Check that YAML frontmatter can be parsed."""
    with open(RECIPE_PATH) as f:
        content = f.read()
    fm = parse_frontmatter(content)
    assert fm is not None, "Could not parse YAML frontmatter (missing or invalid)"
    print("  ✓ Frontmatter is valid YAML")
    return fm, content


def test_frontmatter_all_fields_present(fm):
    """Check that all required frontmatter fields are present."""
    missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fm]
    assert not missing, f"Missing frontmatter fields: {missing}"
    print("  ✓ All required frontmatter fields present")


def test_title(fm):
    """Check title matches expected."""
    assert fm.get("title") == EXPECTED_FRONTMATTER["title"], (
        f"Expected title '{EXPECTED_FRONTMATTER['title']}', got '{fm.get('title')}'"
    )
    print(f"  ✓ Title is '{EXPECTED_FRONTMATTER['title']}'")


def test_status_reviewed(fm):
    """Check status is 'reviewed'."""
    assert fm.get("status") == EXPECTED_FRONTMATTER["status"], (
        f"Expected status '{EXPECTED_FRONTMATTER['status']}', got '{fm.get('status')}'"
    )
    print(f"  ✓ Status is '{EXPECTED_FRONTMATTER['status']}'")


def test_date_modified(fm):
    """Check date_modified is set to 2026-06-27."""
    dm = fm.get("date_modified", "")
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )
    print(f"  ✓ date_modified is '{EXPECTED_DATE_MODIFIED}'")


def test_cuisine(fm):
    """Check cuisine includes Japanese-fusion."""
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    matched = any(EXPECTED_CUISINE in c.lower() for c in cuisines)
    assert matched, (
        f"Expected cuisine to include '{EXPECTED_CUISINE}', got {cuisines}"
    )
    print(f"  ✓ Cuisine includes '{EXPECTED_CUISINE}'")


def test_dietary_tags(fm):
    """Check dietary_tags include vegetarian."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t.lower() for t in tags), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )
    print(f"  ✓ dietary_tags includes {EXPECTED_DIETARY_TAGS}")


def test_tags(fm):
    """Check tags include condiment, butter, miso, and technique tags."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]

    for exp in EXPECTED_TAGS_SUBSTRINGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected a tag containing '{exp}', got {tags}"
        )
    print(f"  ✓ Tags include {EXPECTED_TAGS_SUBSTRINGS}")

    # Check technique tags
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected technique tag containing '{exp}', got {tags}"
        )
    print(f"  ✓ Technique tags include {EXPECTED_TECHNIQUE_TAGS}")

    # Check protein: none
    protein_tags = [t for t in tags_lower if "protein" in t]
    if protein_tags:
        assert any("none" in t for t in protein_tags), (
            f"Expected protein:none tag, got {protein_tags}"
        )
        print("  ✓ Protein tag is 'none'")


def test_ingredients_notebook_specified(content):
    """Check that notebook-specified ingredients are present."""
    content_lower = content.lower()

    for ing in NOTEBOOK_INGREDIENTS:
        assert ing in content_lower, (
            f"Missing notebook-specified ingredient: '{ing}'. "
            f"Notebook specifies: white miso, unsalted butter, mirin, honey"
        )
    print(f"  ✓ All notebook ingredients found: {NOTEBOOK_INGREDIENTS}")


def test_ingredients_format(content):
    """Check ingredients follow the template format with checkboxes."""
    # Find ingredients section
    ing_match = re.search(r"## Ingredients\s*\n(.*?)(?=##|\Z)", content, re.DOTALL)
    assert ing_match, "Could not find Ingredients section"
    ing_section = ing_match.group(1)

    # Check for checkbox format
    checkbox_lines = re.findall(r"- \[ \].*", ing_section)
    assert len(checkbox_lines) >= 2, (
        f"Ingredients should use checkbox format, found {len(checkbox_lines)} checkbox lines"
    )
    print(f"  ✓ Ingredients use checkbox format ({len(checkbox_lines)} items)")


def test_instructions_count(content):
    """Check instructions have 5-8 steps with bolded action titles."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=##|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    # Count numbered steps
    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n_steps = len(steps)
    assert MIN_INSTRUCTIONS <= n_steps <= MAX_INSTRUCTIONS, (
        f"Expected {MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS} instructions, "
        f"found {n_steps}"
    )
    print(f"  ✓ Instructions count: {n_steps} ({MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS})")


def test_instructions_bolded_titles(content):
    """Check each instruction step starts with a bolded title."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=##|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(steps) >= 1, "No bolded action titles found in instructions"
    print(f"  ✓ All instructions have bolded action titles: {[s.strip() for s in steps]}")


def test_instructions_sensory_cues(content):
    """Check that instructions contain sensory cues (color, texture, smell, sound)."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=##|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)
    instr_lower = instr_section.lower()

    sensory_terms = ["golden", "brown", "fragrant", "smooth", "creamy", "thick",
                     "glossy", "aroma", "smell", "texture", "bubbly", "melt",
                     "soft", "warm", "combined", "uniform"]
    found = [t for t in sensory_terms if t in instr_lower]
    assert len(found) >= 1, (
        f"No sensory cues found in instructions. "
        f"Look for terms like: color, texture, smell, sound cues"
    )
    print(f"  ✓ Sensory cues found: {found[:5]}...")


def test_instructions_inline_timing(content):
    """Check that instructions contain inline timing like (~X min)."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=##|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)

    timing_matches = re.findall(r"\(~?\s*\d+[\s-]*\d*\s*(?:min|hour|hr|sec|second|minute)s?\)",
                                instr_section, re.IGNORECASE)
    assert len(timing_matches) >= 1, (
        "No inline timing found in instructions (e.g., '~5 min')"
    )
    print(f"  ✓ Inline timing found: {len(timing_matches)} instance(s)")


def test_cooks_notes(content):
    """Check for at least MIN_COOKS_NOTES cook's notes entries."""
    notes_match = re.search(r"### Cook's Notes\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert notes_match, "Could not find 'Cook's Notes' section"

    notes_section = notes_match.group(1)
    bullet_points = re.findall(r"^- ", notes_section, re.MULTILINE)
    assert len(bullet_points) >= MIN_COOKS_NOTES, (
        f"Expected at least {MIN_COOKS_NOTES} cook's notes, "
        f"found {len(bullet_points)}"
    )
    print(f"  ✓ Cook's Notes: {len(bullet_points)} entries (≥{MIN_COOKS_NOTES})")


def test_variations(content):
    """Check for at least MIN_VARIATIONS variation."""
    var_match = re.search(r"### Variations\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert var_match, "Could not find 'Variations' section"

    var_section = var_match.group(1)
    variations = re.findall(r"^- \*\*", var_section, re.MULTILINE)
    assert len(variations) >= MIN_VARIATIONS, (
        f"Expected at least {MIN_VARIATIONS} variation(s), "
        f"found {len(variations)}"
    )
    print(f"  ✓ Variations: {len(variations)} entries (≥{MIN_VARIATIONS})")


def test_make_ahead_storage(content):
    """Check for make-ahead and storage guidance."""
    lower = content.lower()
    has_make_ahead = "make-ahead" in lower or "make ahead" in lower
    has_storage = "storage" in lower
    assert has_make_ahead, "Missing 'Make-Ahead' section"
    assert has_storage, "Missing 'Storage' section"
    print("  ✓ Make-Ahead / Storage guidance present")


def test_scaling(content):
    """Check for scaling guidance."""
    assert "Scaling" in content, "Missing 'Scaling' section"
    # Check it's substantive, not just the heading
    scaling_match = re.search(r"### Scaling\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    if scaling_match:
        scaling_text = scaling_match.group(1).strip()
        assert len(scaling_text) > 10, "Scaling section is empty or too short"
        print(f"  ✓ Scaling guidance present: '{scaling_text[:60]}...'")
    else:
        print("  ✓ Scaling section present")


def test_slug(filename):
    """Check slug matches filename."""
    with open(RECIPE_PATH) as f:
        content = f.read()
    fm = parse_frontmatter(content)
    expected_slug = os.path.splitext(os.path.basename(RECIPE_PATH))[0]
    actual_slug = fm.get("slug", "")
    assert actual_slug == expected_slug, (
        f"Expected slug '{expected_slug}' (matching filename), got '{actual_slug}'"
    )
    print(f"  ✓ Slug matches filename: '{expected_slug}'")


def test_source_documented(fm):
    """Check source is documented."""
    source_type = fm.get("source_type", "")
    source_name = fm.get("source_name", "")
    assert source_type, "source_type is missing or empty"
    assert source_name, "source_name is missing or empty"
    print(f"  ✓ Source documented: {source_type} — {source_name}")


def test_tags_include_recipe_meal_type(fm):
    """Check tags include a recipe/{{meal_type}} tag."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    meal_types = fm.get("meal_type", [])
    if isinstance(meal_types, str):
        meal_types = [meal_types]

    has_recipe_tag = any("recipe/" in t for t in tags)
    assert has_recipe_tag, (
        f"Expected a 'recipe/...' tag, got {tags}"
    )
    print(f"  ✓ Tags include recipe/meal_type reference")


def test_base_servings(fm):
    """Check base_servings is populated."""
    bs = fm.get("base_servings")
    assert bs is not None, "base_servings is missing"
    assert bs != "", "base_servings is empty"
    print(f"  ✓ base_servings: {bs}")


def test_serving_unit(fm):
    """Check serving_unit is populated."""
    su = fm.get("serving_unit")
    assert su is not None, "serving_unit is missing"
    assert su != "", "serving_unit is empty"
    print(f"  ✓ serving_unit: {su}")


def test_key_equipment(fm):
    """Check key_equipment is populated."""
    ke = fm.get("key_equipment")
    assert ke is not None, "key_equipment is missing"
    assert len(ke) > 0, "key_equipment is empty"
    print(f"  ✓ key_equipment: {ke}")


def test_difficulty_set(fm):
    """Check difficulty is populated."""
    diff = fm.get("difficulty")
    assert diff, f"difficulty is missing or empty"
    assert diff in ["easy", "medium", "hard", "professional"], (
        f"difficulty should be easy/medium/hard/professional, got '{diff}'"
    )
    print(f"  ✓ difficulty: {diff}")


def test_origin_notes_present(fm):
    """Check origin_notes is populated."""
    on = fm.get("origin_notes", "")
    assert on, "origin_notes is missing or empty"
    print(f"  ✓ origin_notes: '{on[:60]}...'")


def test_content_structure(content):
    """Check the overall content structure has required sections."""
    required_headings = [
        "## Ingredients",
        "## Instructions",
        "## Notes & Variations",
        "### Cook's Notes",
        "### Variations",
        "### Make-Ahead",
        "### Storage",
        "### Scaling",
    ]
    for heading in required_headings:
        assert heading in content, f"Missing heading: '{heading}'"
    print(f"  ✓ All required sections present ({len(required_headings)} headings)")


def run_all_tests():
    """Run all test functions and report results."""
    tests = [
        ("File exists", test_file_exists),
    ]

    passed = 0
    failed = 0
    failures = []

    for name, test_fn in tests:
        try:
            test_fn()
            passed += 1
        except AssertionError as e:
            failed += 1
            failures.append((name, str(e)))
            print(f"  ✗ {name}: FAILED")
            print(f"    {e}")

    # If file exists, run all other tests
    if os.path.exists(RECIPE_PATH):
        fm, content = test_frontmatter_present()

        details_tests = [
            ("All frontmatter fields", lambda: test_frontmatter_all_fields_present(fm)),
            ("Title", lambda: test_title(fm)),
            ("Status reviewed", lambda: test_status_reviewed(fm)),
            ("date_modified", lambda: test_date_modified(fm)),
            ("Cuisine", lambda: test_cuisine(fm)),
            ("Dietary tags", lambda: test_dietary_tags(fm)),
            ("Tags", lambda: test_tags(fm)),
            ("Slug", lambda: test_slug(RECIPE_PATH)),
            ("Source documented", lambda: test_source_documented(fm)),
            ("meal_type tag", lambda: test_tags_include_recipe_meal_type(fm)),
            ("base_servings", lambda: test_base_servings(fm)),
            ("serving_unit", lambda: test_serving_unit(fm)),
            ("key_equipment", lambda: test_key_equipment(fm)),
            ("difficulty", lambda: test_difficulty_set(fm)),
            ("origin_notes", lambda: test_origin_notes_present(fm)),
            ("Notebook ingredients", lambda: test_ingredients_notebook_specified(content)),
            ("Ingredient format", lambda: test_ingredients_format(content)),
            ("Instruction count", lambda: test_instructions_count(content)),
            ("Bolded titles", lambda: test_instructions_bolded_titles(content)),
            ("Sensory cues", lambda: test_instructions_sensory_cues(content)),
            ("Inline timing", lambda: test_instructions_inline_timing(content)),
            ("Cook's Notes", lambda: test_cooks_notes(content)),
            ("Variations", lambda: test_variations(content)),
            ("Make-Ahead/Storage", lambda: test_make_ahead_storage(content)),
            ("Scaling", lambda: test_scaling(content)),
            ("Content structure", lambda: test_content_structure(content)),
        ]

        for name, test_fn in details_tests:
            try:
                test_fn()
                passed += 1
            except AssertionError as e:
                failed += 1
                failures.append((name, str(e)))
                print(f"  ✗ {name}: FAILED")
                print(f"    {e}")

    print(f"\n{'='*60}")
    print(f"RESULTS: {passed} passed, {failed} failed")
    if failures:
        print(f"FAILURES:")
        for name, msg in failures:
            print(f"  - {name}: {msg}")
    print(f"{'='*60}")

    return passed, failed, failures


if __name__ == "__main__":
    try:
        import yaml
    except ImportError:
        print("Installing PyYAML...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
        import yaml

    passed, failed, failures = run_all_tests()
    sys.exit(1 if failed > 0 else 0)
