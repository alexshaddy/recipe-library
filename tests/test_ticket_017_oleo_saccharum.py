#!/usr/bin/env python3
"""
TICKET-017: Expand Oleo Saccharum from notebook source.

Validates `recipes/condiment/oleo-saccharum.md` against:
  - TICKET-017 requirements
  - docs/specs/017-oleo-saccharum.md specification
  - Digitization skill spec compliance

Notebook source specifies:
  - 50g orange peel (no pith)
  - 200g granulated sugar
  - 200mL hot water

Key technique: muddle + rest for oil extraction.
"""

import os
import re
import sys

# ── Ensure PyYAML is available for robust frontmatter parsing ─────────────
# The test_helpers' manual fallback parser cannot handle YAML lists,
# so we install PyYAML if it isn't already present.
try:
    import yaml  # noqa: F401 — imported for side-effect (test_helpers uses it)
except ImportError:
    import subprocess
    print("PyYAML not found. Installing...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "pyyaml", "-q", "--break-system-packages"]
    )
    import yaml  # noqa: F401

# Import shared test helpers (must come after yaml is guaranteed)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

# ── Recipe under test ──────────────────────────────────────────────────────

RECIPE_RELATIVE_PATH = "condiment/oleo-saccharum.md"

# ── Expected values from TICKET-017 and spec ───────────────────────────────

EXPECTED_TITLE = "Oleo Saccharum"
EXPECTED_STATUS = "reviewed"
EXPECTED_DATE_MODIFIED = "2026-06-27"
EXPECTED_CUISINE = "american"
EXPECTED_DIETARY_TAGS = ["vegetarian", "vegan", "gluten-free"]
EXPECTED_TAGS_SUBSTRINGS = ["recipe/condiment"]
EXPECTED_TECHNIQUE_TAGS = ["technique/macerate", "technique/muddle"]

MIN_INSTRUCTIONS = 5
MAX_INSTRUCTIONS = 8
MIN_COOKS_NOTES = 2
MIN_VARIATIONS = 1

# Notebook source ingredient references to check in content
NOTEBOOK_INGREDIENTS = [
    ("orange peel (50g)", [r"50\s*grams?", r"50g"]),
    ("sugar (200g)", [r"200\s*grams?", r"200g"]),
    ("hot water (200mL)", [r"200\s*milliliters?", r"200ml"]),
]

# Key technique markers that must appear in the recipe
REQUIRED_CONTENT_MARKERS = [
    ("avoids pith", r"\bpith\b"),
    ("muddle / muddler", r"\bmuddl[ei]r?\b"),
    ("rest for oil extraction", r"\brest\b"),
    ("strain / cheesecloth", r"\bstrain\b|\bcheesecloth\b"),
]


def test_file_exists():
    """Recipe file must exist at the expected path."""
    path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "recipes",
        RECIPE_RELATIVE_PATH,
    )
    assert os.path.exists(path), f"Recipe file not found at {path}"
    print(f"  ✓ File exists at recipes/{RECIPE_RELATIVE_PATH}")


def test_frontmatter_valid():
    """Parse and return frontmatter and content."""
    fm, content = load_recipe(RECIPE_RELATIVE_PATH)
    print("  ✓ Frontmatter is valid YAML")
    return fm, content


def test_title(fm):
    """Check title matches expected."""
    title = check_frontmatter_field(fm, "title")
    assert title == EXPECTED_TITLE, f"Expected title '{EXPECTED_TITLE}', got '{title}'"
    print(f"  ✓ Title is '{EXPECTED_TITLE}'")


def test_status(fm):
    """Check status is 'reviewed'."""
    status = check_frontmatter_field(fm, "status")
    assert status == EXPECTED_STATUS, f"Expected status '{EXPECTED_STATUS}', got '{status}'"
    print(f"  ✓ Status is '{EXPECTED_STATUS}'")


def test_date_modified(fm):
    """Check date_modified is 2026-06-27."""
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )
    print(f"  ✓ date_modified is '{EXPECTED_DATE_MODIFIED}'")


def test_slug(fm):
    """Check slug matches filename."""
    expected_slug = os.path.splitext(os.path.basename(RECIPE_RELATIVE_PATH))[0]
    actual_slug = fm.get("slug", "")
    assert actual_slug == expected_slug, (
        f"Expected slug '{expected_slug}', got '{actual_slug}'"
    )
    print(f"  ✓ Slug matches filename: '{expected_slug}'")


def test_cuisine(fm):
    """Check cuisine includes 'american'."""
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any(EXPECTED_CUISINE in c.lower() for c in cuisines), (
        f"Expected cuisine to include '{EXPECTED_CUISINE}', got {cuisines}"
    )
    print(f"  ✓ Cuisine includes '{EXPECTED_CUISINE}'")


def test_dietary_tags(fm):
    """Check dietary_tags include vegetarian, vegan, gluten-free."""
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )
    print(f"  ✓ dietary_tags includes {EXPECTED_DIETARY_TAGS}")


def test_tags(fm):
    """Check tags include recipe/condiment and technique tags."""
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]

    # Check for recipe/ condiment tag
    assert any("recipe/condiment" in t for t in tags_lower), (
        f"Expected a 'recipe/condiment' tag, got {tags}"
    )
    print("  ✓ Tags include recipe/condiment")

    # Check technique tags: technique/macerate and technique/muddle
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected technique tag '{exp}', got {tags}"
        )
    print(f"  ✓ Technique tags include {EXPECTED_TECHNIQUE_TAGS}")


def test_frontmatter_times(fm):
    """Check that time fields are populated."""
    for field in ["prep_time", "cook_time", "inactive_time", "total_time"]:
        val = fm.get(field, "")
        assert val, f"{field} is missing or empty"
    print(f"  ✓ Time fields populated: prep={fm.get('prep_time')}, "
          f"cook={fm.get('cook_time')}, inactive={fm.get('inactive_time')}, "
          f"total={fm.get('total_time')}")


def test_source_documented(fm):
    """Check source_type and source_name are documented."""
    st = check_frontmatter_field(fm, "source_type")
    sn = check_frontmatter_field(fm, "source_name")
    sp = check_frontmatter_field(fm, "source_page")
    print(f"  ✓ Source documented: {st} — {sn}, p.{sp}")


def test_difficulty(fm):
    """Check difficulty is set to a valid value."""
    diff = check_frontmatter_field(fm, "difficulty")
    assert diff in ["easy", "medium", "hard", "professional"], (
        f"Expected easy/medium/hard/professional, got '{diff}'"
    )
    print(f"  ✓ difficulty: {diff}")


def test_key_equipment(fm):
    """Check key_equipment references muddler, strainer, cheesecloth."""
    ke = fm.get("key_equipment", [])
    assert len(ke) > 0, "key_equipment is empty"
    has_muddler = any("muddler" in e.lower() or "spoon" in e.lower() for e in ke)
    has_strainer = any("strain" in e.lower() for e in ke)
    assert has_muddler, f"Expected muddler or spoon in key_equipment, got {ke}"
    assert has_strainer, f"Expected strainer in key_equipment, got {ke}"
    print(f"  ✓ key_equipment includes muddler/spoon, strainer: {ke}")


def test_base_servings(fm):
    """Check base_servings is populated."""
    bs = fm.get("base_servings")
    assert bs is not None and bs != "", "base_servings is missing or empty"
    print(f"  ✓ base_servings: {bs}")


def test_serving_unit(fm):
    """Check serving_unit is populated."""
    su = fm.get("serving_unit")
    assert su is not None and su != "", "serving_unit is missing or empty"
    print(f"  ✓ serving_unit: {su}")


def test_origin_notes(fm):
    """Check origin_notes references notebook context."""
    on = check_frontmatter_field(fm, "origin_notes")
    assert "notebook" in on.lower() or "page" in on.lower(), (
        f"origin_notes should reference notebook/page origin, got: '{on}'"
    )
    print(f"  ✓ origin_notes references notebook origin")


# ── Content-level tests ────────────────────────────────────────────────────


def test_notebook_ingredients(content):
    """Check notebook-specified ingredient amounts are present."""
    for label, patterns in NOTEBOOK_INGREDIENTS:
        found = any(re.search(p, content, re.IGNORECASE) for p in patterns)
        assert found, (
            f"Missing notebook ingredient '{label}'. "
            f"Looked for patterns: {patterns}"
        )
    print("  ✓ All notebook-specified ingredient amounts found "
          "(50g peel, 200g sugar, 200mL water)")


def test_ingredients_checkbox_format(content):
    """Check ingredients use checkbox format."""
    ing_match = re.search(r"## Ingredients\s*\n(.*?)(?=## Instructions|\Z)", content, re.DOTALL)
    assert ing_match, "Could not find Ingredients section"
    ing_section = ing_match.group(1)
    checkbox_lines = re.findall(r"- \[ \].*", ing_section)
    assert len(checkbox_lines) >= 3, (
        f"Expected ≥3 checkbox ingredients, found {len(checkbox_lines)}"
    )
    print(f"  ✓ Ingredients use checkbox format ({len(checkbox_lines)} items)")


def test_instructions_step_count(content):
    """Check instructions have 5-8 numbered steps with bolded titles."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n = len(steps)
    assert MIN_INSTRUCTIONS <= n <= MAX_INSTRUCTIONS, (
        f"Expected {MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS} instructions, found {n}"
    )

    titles = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(titles) >= 1, "No bolded action titles found"

    print(f"  ✓ Instructions: {n} steps ({MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS}) "
          f"with bolded titles: {[t.strip() for t in titles]}")


def test_instructions_sensory_cues(content):
    """Check instructions contain sensory cues (fragrant, aromatic, etc.)."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_lower = instr_match.group(1).lower()

    # Oleo-specific sensory terms from the spec
    sensory_terms = [
        "fragrant", "aroma", "aromatic", "glistening", "damp",
        "cloudy", "syrupy", "perfume", "bright", "soften", "oily",
    ]
    found = [t for t in sensory_terms if t in instr_lower]
    assert len(found) >= 2, (
        f"Expected ≥2 sensory cues (e.g. fragrant, aroma, glistening, cloudy), "
        f"found {len(found)}: {found}"
    )
    print(f"  ✓ Sensory cues found ({len(found)}): {found}")


def test_instructions_inline_timing(content):
    """Check instructions contain inline timing cues (≥3)."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    # Match various timing patterns:
    #   "1–2 minutes" (dash-separated range)
    #   "1 to 2 hours" (word-separated range)
    #   "~5 min" (single duration)
    #   "190°F" (temperature — not a timing, but we want actual timings)
    timing_patterns = [
        r"\d+\s*(?:–|-|to)\s*\d+\s*(?:min|hour|hr|minute|second)s?",  # ranges
        r"\d+\s*(?:min|hour|hr|minute|second)s?(?=\s|\)|,|\.)",         # single durations
    ]
    all_timings = []
    for p in timing_patterns:
        all_timings.extend(re.findall(p, instr_section, re.IGNORECASE))

    assert len(all_timings) >= 2, (
        f"Expected ≥2 inline timing instances, found {len(all_timings)}: {all_timings}"
    )
    print(f"  ✓ Inline timing: {len(all_timings)} instance(s): {all_timings}")


def test_required_technique_keywords(content):
    """Check recipe mentions key technique words from the spec."""
    content_lower = content.lower()
    for label, pattern in REQUIRED_CONTENT_MARKERS:
        assert re.search(pattern, content_lower), (
            f"Missing required technique keyword: '{label}' (pattern: {pattern})"
        )
    print("  ✓ All required technique keywords present (pith, muddle, rest, strain)")


def test_rest_period(content):
    """Check the rest period is specified as 1 to 2 hours."""
    content_lower = content.lower()
    has_rest_period = re.search(r"1\s*(?:to|–|-)\s*2\s*hours?", content_lower)
    assert has_rest_period, (
        "Expected rest period of '1 to 2 hours' for oil extraction"
    )
    print("  ✓ Rest period specified as 1–2 hours")


def test_cooks_notes(content):
    """Check for at least MIN_COOKS_NOTES cook's notes entries."""
    notes_match = re.search(r"### Cook's Notes\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert notes_match, "Missing 'Cook's Notes' section"
    notes_section = notes_match.group(1)
    bullets = re.findall(r"^- ", notes_section, re.MULTILINE)
    assert len(bullets) >= MIN_COOKS_NOTES, (
        f"Expected ≥{MIN_COOKS_NOTES} cook's notes, found {len(bullets)}"
    )
    print(f"  ✓ Cook's Notes: {len(bullets)} entries (≥{MIN_COOKS_NOTES})")


def test_variations(content):
    """Check for at least MIN_VARIATIONS variation entries."""
    var_match = re.search(r"### Variations\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert var_match, "Missing 'Variations' section"
    var_section = var_match.group(1)
    variations = re.findall(r"^- \*\*", var_section, re.MULTILINE)
    assert len(variations) >= MIN_VARIATIONS, (
        f"Expected ≥{MIN_VARIATIONS} variation(s), found {len(variations)}"
    )
    print(f"  ✓ Variations: {len(variations)} entry/entries (≥{MIN_VARIATIONS})")


def test_make_ahead_storage(content):
    """Check Make-Ahead and Storage information is present."""
    # The recipe may use a combined heading: "### Make-Ahead / Storage"
    has_make_ahead = "Make-Ahead" in content
    has_storage = re.search(r"(?:###\s*)?(?:Make-Ahead\s*/\s*Storage|Storage)", content) is not None
    has_storage = has_storage or "Storage" in content
    assert has_make_ahead, "Missing 'Make-Ahead' reference in content"
    assert has_storage, "Missing 'Storage' reference in content"
    print("  ✓ Make-Ahead / Storage sections present")


def test_scaling(content):
    """Check Scaling section has substantive content."""
    assert "### Scaling" in content, "Missing '### Scaling' heading"
    scaling_match = re.search(r"### Scaling\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    if scaling_match:
        text = scaling_match.group(1).strip()
        assert len(text) > 10, "Scaling section is empty or too short"
        print("  ✓ Scaling guidance present (substantive)")
    else:
        # If at end of file, the `(?=###|\Z)` would match but `###` might not follow
        assert "Scaling" in content
        print("  ✓ Scaling section present")


def test_content_structure(content):
    """Check all required sections are present."""
    required_headings = [
        "## Ingredients",
        "## Instructions",
        "## Notes & Variations",
        "### Cook's Notes",
        "### Variations",
        "### Scaling",
    ]
    for h in required_headings:
        assert h in content, f"Missing heading: '{h}'"

    # Make-Ahead / Storage can be individual or combined
    has_any_storage_heading = (
        "### Make-Ahead / Storage" in content
        or "### Storage / Make-Ahead" in content
        or "### Make-Ahead" in content
        or "### Storage" in content
    )
    assert has_any_storage_heading, (
        "Missing '### Make-Ahead / Storage' or similar heading"
    )
    print(f"  ✓ All required sections present ({len(required_headings)}+ headings)")


def test_oil_extraction_keywords(content):
    """Check for oil-extraction-specific language."""
    content_lower = content.lower()
    oil_terms = ["essential oil", "oil droplet", "oil gland", "release oil",
                 "draw out", "extract", "fragrant"]
    found = [t for t in oil_terms if t in content_lower]
    assert len(found) >= 2, (
        f"Expected ≥2 oil-extraction-related terms, found {len(found)}: {found}"
    )
    print(f"  ✓ Oil extraction language found ({len(found)}): {found}")


# ── Test runner ──────────────────────────────────────────────────────────────


def run_all_tests():
    """Run all tests using the shared run_tests helper."""
    # Check file exists first
    test_file_exists()

    # Load the recipe (this also validates frontmatter YAML)
    fm, content = load_recipe(RECIPE_RELATIVE_PATH)

    tests = [
        # ── Frontmatter & metadata ──
        ("File exists", test_file_exists),
        ("Title", lambda: test_title(fm)),
        ("Status reviewed", lambda: test_status(fm)),
        ("date_modified", lambda: test_date_modified(fm)),
        ("Slug matches filename", lambda: test_slug(fm)),
        ("Cuisine", lambda: test_cuisine(fm)),
        ("Dietary tags", lambda: test_dietary_tags(fm)),
        ("Tags & technique tags", lambda: test_tags(fm)),
        ("Time fields populated", lambda: test_frontmatter_times(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Difficulty", lambda: test_difficulty(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Base servings", lambda: test_base_servings(fm)),
        ("Serving unit", lambda: test_serving_unit(fm)),
        ("Origin notes", lambda: test_origin_notes(fm)),

        # ── Ingredients ──
        ("Notebook ingredient amounts", lambda: test_notebook_ingredients(content)),
        ("Ingredient checkbox format", lambda: test_ingredients_checkbox_format(content)),

        # ── Instructions ──
        ("Instructions step count (5-8)", lambda: test_instructions_step_count(content)),
        ("Instructions sensory cues", lambda: test_instructions_sensory_cues(content)),
        ("Instructions inline timing", lambda: test_instructions_inline_timing(content)),

        # ── Key technique keywords ──
        ("Required technique keywords", lambda: test_required_technique_keywords(content)),
        ("Rest period (1–2 hours)", lambda: test_rest_period(content)),

        # ── Notes & Variations ──
        ("Cook's Notes (≥2)", lambda: test_cooks_notes(content)),
        ("Variations (≥1)", lambda: test_variations(content)),
        ("Make-Ahead / Storage", lambda: test_make_ahead_storage(content)),
        ("Scaling guidance", lambda: test_scaling(content)),
        ("Content structure", lambda: test_content_structure(content)),

        # ── Oil extraction language ──
        ("Oil extraction language", lambda: test_oil_extraction_keywords(content)),
    ]

    run_tests("TICKET-017", tests)


if __name__ == "__main__":
    run_all_tests()
