#!/usr/bin/env python3
"""
TICKET-006: Fix Yakiniku Salt Slab ingredient mismatch vs notebook source.

Validates `recipes/dinner/yakiniku-salt-slab.md` against:
  - TICKET-006 requirements
  - docs/specs/006-yakiniku-salt-slab-fix.md specification
  - Digitization skill spec compliance

Notebook source (p.23 of 5.13 Kat Dinner):
  - A5 Wagyu on Himalayan salt slab
  - Bordelaise (¾ cup), thyme (¼ tsp)
  - Nori bordelaise variant
  - Negi bed, 2 cups beef stock, shallots
"""

import os
import re
import sys

RECIPE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recipes")
RECIPE_PATH = os.path.join(RECIPE_DIR, "dinner", "yakiniku-salt-slab.md")

try:
    import yaml
except ImportError:
    print("PyYAML not available. Will parse frontmatter manually.")
    yaml = None


def parse_frontmatter(content):
    """Parse YAML frontmatter from a markdown file."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None, content
    fm_text = match.group(1)
    if yaml:
        try:
            return yaml.safe_load(fm_text), content
        except yaml.YAMLError:
            return None, content
    else:
        # Manual parsing for basic fields
        fm = {}
        for line in fm_text.strip().split("\n"):
            line = line.strip()
            if ":" in line:
                key, _, val = line.partition(":")
                fm[key.strip()] = val.strip().strip('"').strip("'")
        return fm, content


# ── Requirements from TICKET-006 and spec ──────────────────────────────────

NOTEBOOK_INGREDIENTS = [
    "wagyu",
    "himalayan salt slab",
    "bordelaise",
    "red wine",
    "beef stock",
    "shallot",
    "thyme",
    "butter",
    "negi",
    "nori",
]

EXPECTED_FRONTMATTER = {
    "title": "Yakiniku Salt Slab",
    "slug": "yakiniku-salt-slab",
    "status": "reviewed",
    "date_modified": "2026-06-27",
}

REQUIRED_FRONTMATTER_FIELDS = [
    "title", "aliases", "slug", "meal_type", "cuisine", "course",
    "dietary_tags", "season",
    "prep_time", "cook_time", "inactive_time", "total_time",
    "base_servings", "serving_unit", "scaling_notes",
    "source_type", "source_name", "source_url", "source_page", "origin_notes",
    "difficulty", "key_equipment",
    "tags", "status",
    "date_added", "date_modified",
]

EXPECTED_CUISINE = "japanese"
EXPECTED_DIETARY_TAGS = ["gluten-free"]
EXPECTED_TAGS_SUBSTRINGS = ["grill", "sauce"]
EXPECTED_TECHNIQUE_TAGS = ["technique/grill", "technique/sauce"]
EXPECTED_PROTEIN_TAGS = ["protein/beef"]

MIN_INSTRUCTIONS = 5
MAX_INSTRUCTIONS = 8

MIN_COOKS_NOTES = 2
MIN_VARIATIONS = 1

EXPECTED_DATE_MODIFIED = "2026-06-27"


def fmt_date(dm):
    """Convert YAML date object to string if needed."""
    if hasattr(dm, "isoformat"):
        return dm.isoformat()
    return str(dm)


def test_file_exists():
    assert os.path.exists(RECIPE_PATH), (
        f"Recipe file not found at {RECIPE_PATH}"
    )
    print(f"  ✓ File exists at {RECIPE_PATH}")


def test_frontmatter_present():
    with open(RECIPE_PATH) as f:
        content = f.read()
    fm, content = parse_frontmatter(content)
    assert fm is not None, "Could not parse YAML frontmatter"
    print("  ✓ Frontmatter is valid YAML")
    return fm, content


def test_frontmatter_all_fields(fm):
    missing = [f for f in REQUIRED_FRONTMATTER_FIELDS if f not in fm]
    assert not missing, f"Missing frontmatter fields: {missing}"
    print("  ✓ All required frontmatter fields present")


def test_title(fm):
    assert fm.get("title") == EXPECTED_FRONTMATTER["title"], (
        f"Expected title '{EXPECTED_FRONTMATTER['title']}', got '{fm.get('title')}'"
    )
    print(f"  ✓ Title is '{EXPECTED_FRONTMATTER['title']}'")


def test_status(fm):
    assert fm.get("status") == EXPECTED_FRONTMATTER["status"], (
        f"Expected status '{EXPECTED_FRONTMATTER['status']}', got '{fm.get('status')}'"
    )
    print(f"  ✓ Status is '{EXPECTED_FRONTMATTER['status']}'")


def test_date_modified(fm):
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, (
        f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    )
    print(f"  ✓ date_modified is '{EXPECTED_DATE_MODIFIED}'")


def test_slug(fm):
    expected_slug = os.path.splitext(os.path.basename(RECIPE_PATH))[0]
    actual_slug = fm.get("slug", "")
    assert actual_slug == expected_slug, (
        f"Expected slug '{expected_slug}', got '{actual_slug}'"
    )
    print(f"  ✓ Slug matches filename: '{expected_slug}'")


def test_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    assert any(EXPECTED_CUISINE in c.lower() for c in cuisines), (
        f"Expected cuisine to include '{EXPECTED_CUISINE}', got {cuisines}"
    )
    print(f"  ✓ Cuisine includes '{EXPECTED_CUISINE}'")


def test_dietary_tags(fm):
    tags = fm.get("dietary_tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in EXPECTED_DIETARY_TAGS:
        assert any(exp in t.lower() for t in tags), (
            f"Expected dietary_tags to include '{exp}', got {tags}"
        )
    print(f"  ✓ dietary_tags includes {EXPECTED_DIETARY_TAGS}")


def test_frontmatter_times(fm):
    """Check that time fields are populated."""
    for field in ["prep_time", "cook_time", "inactive_time", "total_time"]:
        val = fm.get(field, "")
        assert val, f"{field} is missing or empty"
    print(f"  ✓ All time fields populated: prep={fm.get('prep_time')}, cook={fm.get('cook_time')}, "
          f"inactive={fm.get('inactive_time')}, total={fm.get('total_time')}")


def test_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    tags_lower = [t.lower() for t in tags]

    # Check for recipe/ tag
    assert any("recipe/" in t for t in tags_lower), (
        f"Expected a 'recipe/...' tag, got {tags}"
    )
    print("  ✓ Tags include recipe/meal_type tag")

    # Check technique tags
    for exp in EXPECTED_TECHNIQUE_TAGS:
        assert any(exp in t for t in tags_lower), (
            f"Expected technique tag containing '{exp}', got {tags}"
        )
    print(f"  ✓ Technique tags include {EXPECTED_TECHNIQUE_TAGS}")

    # Check protein tags
    protein_tags = [t for t in tags_lower if "protein" in t]
    if protein_tags:
        assert any("beef" in t for t in protein_tags), (
            f"Expected protein:beef tag, got {protein_tags}"
        )
        print("  ✓ Protein tag is 'beef'")


def test_source_documented(fm):
    assert fm.get("source_type"), "source_type is missing or empty"
    assert fm.get("source_name"), "source_name is missing or empty"
    assert fm.get("source_page"), "source_page is missing or empty"
    print(f"  ✓ Source documented: {fm.get('source_type')} — {fm.get('source_name')}, p.{fm.get('source_page')}")


def test_difficulty(fm):
    diff = fm.get("difficulty")
    assert diff in ["easy", "medium", "hard", "professional"], (
        f"Expected easy/medium/hard/professional, got '{diff}'"
    )
    print(f"  ✓ difficulty: {diff}")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    assert len(ke) > 0, "key_equipment is empty"
    has_slab = any("salt" in e.lower() for e in ke)
    has_grill = any("grill" in e.lower() for e in ke)
    assert has_slab, f"Expected key_equipment to reference salt slab, got {ke}"
    print(f"  ✓ key_equipment includes salt slab: {ke}")


def test_ingredients_notebook_specified(content):
    """Check that notebook-specified ingredients are present."""
    content_lower = content.lower()
    for ing in NOTEBOOK_INGREDIENTS:
        assert ing in content_lower, (
            f"Missing notebook-specified ingredient: '{ing}'"
        )
    print(f"  ✓ All notebook ingredients found in recipe")


def test_ingredients_grouped(content):
    """Check ingredients are grouped by component sub-headings."""
    ing_match = re.search(r"## Ingredients\s*\n(.*?)(?=## Instructions|\Z)", content, re.DOTALL)
    assert ing_match, "Could not find Ingredients section"
    ing_section = ing_match.group(1)

    # Check for group headings
    group_headings = re.findall(r"### (For the .+)", ing_section)
    assert len(group_headings) >= 3, (
        f"Expected grouped ingredients with sub-headings, found {len(group_headings)} groups: {group_headings}"
    )
    print(f"  ✓ Ingredients grouped ({len(group_headings)} groups): {group_headings}")


def test_ingredients_checkbox_format(content):
    """Check ingredients use checkbox format."""
    ing_match = re.search(r"## Ingredients\s*\n(.*?)(?=## Instructions|\Z)", content, re.DOTALL)
    ing_section = ing_match.group(1)
    checkbox_lines = re.findall(r"- \[ \].*", ing_section)
    assert len(checkbox_lines) >= 5, (
        f"Expected checkbox format ingredients, found {len(checkbox_lines)} checkbox lines"
    )
    print(f"  ✓ Ingredients use checkbox format ({len(checkbox_lines)} items)")


def test_instructions_count(content):
    """Check instructions have 5-8 steps."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n_steps = len(steps)
    assert MIN_INSTRUCTIONS <= n_steps <= MAX_INSTRUCTIONS, (
        f"Expected {MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS} instructions, found {n_steps}"
    )
    print(f"  ✓ Instructions count: {n_steps} ({MIN_INSTRUCTIONS}-{MAX_INSTRUCTIONS})")


def test_instructions_bolded_titles(content):
    """Check each instruction step starts with a bolded title."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)
    steps = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(steps) >= 1, "No bolded action titles found"
    print(f"  ✓ Bolded action titles: {[s.strip() for s in steps]}")


def test_instructions_sensory_cues(content):
    """Check instructions contain sensory cues."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)
    instr_lower = instr_section.lower()

    sensory_terms = ["sizzle", "brown", "aroma", "glossy", "fragrant", "pink",
                     "wilt", "tender", "golden", "crisp", "soft"]
    found = [t for t in sensory_terms if t in instr_lower]
    assert len(found) >= 2, (
        f"Few sensory cues found: {found}"
    )
    print(f"  ✓ Sensory cues: {found}")


def test_instructions_inline_timing(content):
    """Check instructions contain inline timing."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1)

    timing_matches = re.findall(r"\(~?\s*\d+[\s-]*\d*\s*(?:min|hour|hr|sec|second|minute)s?\)",
                                instr_section, re.IGNORECASE)
    # Also match unbracketed timing
    timing_matches += re.findall(r"\d+[–\-]\d+\s*(?:min|hour|hr|sec|second|minute)s?",
                                 instr_section, re.IGNORECASE)
    assert len(timing_matches) >= 3, (
        f"Expected ≥3 inline timings, found {len(timing_matches)}"
    )
    print(f"  ✓ Inline timing: {len(timing_matches)} instance(s)")


def test_cooks_notes(content):
    """Check for ≥2 cook's notes."""
    notes_match = re.search(r"### Cook's Notes\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert notes_match, "Missing 'Cook's Notes' section"
    notes_section = notes_match.group(1)
    bullets = re.findall(r"^- ", notes_section, re.MULTILINE)
    assert len(bullets) >= MIN_COOKS_NOTES, (
        f"Expected ≥{MIN_COOKS_NOTES} cook's notes, found {len(bullets)}"
    )
    print(f"  ✓ Cook's Notes: {len(bullets)} entries (≥{MIN_COOKS_NOTES})")


def test_variations(content):
    """Check for ≥1 variation."""
    var_match = re.search(r"### Variations\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert var_match, "Missing 'Variations' section"
    var_section = var_match.group(1)
    variations = re.findall(r"^- \*\*", var_section, re.MULTILINE)
    assert len(variations) >= MIN_VARIATIONS, (
        f"Expected ≥{MIN_VARIATIONS} variation(s), found {len(variations)}"
    )
    print(f"  ✓ Variations: {len(variations)} entries (≥{MIN_VARIATIONS})")


def test_make_ahead_storage(content):
    """Check Make-Ahead and Storage sections."""
    assert "### Make-Ahead" in content or "Make-Ahead" in content, "Missing Make-Ahead section"
    assert "### Storage" in content or "Storage" in content, "Missing Storage section"
    print("  ✓ Make-Ahead / Storage sections present")


def test_scaling(content):
    """Check Scaling section with substantive content."""
    assert "### Scaling" in content, "Missing Scaling section"
    scaling_match = re.search(r"### Scaling\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    if scaling_match:
        text = scaling_match.group(1).strip()
        assert len(text) > 10, "Scaling section is empty or too short"
        print(f"  ✓ Scaling guidance present")
    else:
        # Could be end of file
        assert True


def test_content_sections(content):
    """Check all required sections exist."""
    required = [
        "## Ingredients",
        "## Instructions",
        "## Notes & Variations",
        "### Cook's Notes",
        "### Variations",
        "### Scaling",
    ]
    for h in required:
        assert h in content, f"Missing heading: '{h}'"
    has_make_ahead = "### Make-Ahead" in content
    has_storage = "### Storage" in content
    assert has_make_ahead, "Missing '### Make-Ahead' heading"
    assert has_storage, "Missing '### Storage' heading"
    print(f"  ✓ All required sections present")


def test_bordelaise_specifics(content):
    """Check bordelaise-specific requirements from spec."""
    content_lower = content.lower()
    # The spec says bordelaise should have: red wine, beef stock, shallot, thyme, butter
    bordelaise_items = ["red wine", "beef stock", "shallot", "thyme", "butter"]
    for item in bordelaise_items:
        assert item in content_lower, f"Missing bordelaise component: '{item}'"
    print(f"  ✓ Bordelaise components all present: {bordelaise_items}")


def test_negi_bed(content):
    """Check negi bed is specified."""
    content_lower = content.lower()
    assert "negi" in content_lower or "scallion" in content_lower, "Missing negi/scallion reference"
    print("  ✓ Negi bed present")


def test_salt_slab_heating(content):
    """Check salt slab heating instructions include gradual preheat caution."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    instr_section = instr_match.group(1).lower()
    has_gradual = "gradual" in instr_section
    has_crack = "crack" in instr_section
    assert has_gradual or has_crack, (
        "Salt slab heating should mention gradual preheat to prevent cracking"
    )
    print("  ✓ Salt slab heating includes gradual preheat guidance")


def test_origin_notes(fm):
    on = fm.get("origin_notes", "")
    assert on, "origin_notes is missing or empty"
    has_kat = "kat" in on.lower() or "5.13" in on
    assert has_kat, "origin_notes should reference 5.13 Kat dinner context"
    print(f"  ✓ origin_notes references notebook context")


def test_meal_type(fm):
    mt = fm.get("meal_type", [])
    if isinstance(mt, str):
        mt = [mt]
    assert "dinner" in [m.lower() for m in mt], f"Expected meal_type dinner, got {mt}"
    print("  ✓ meal_type includes dinner")


def run_all_tests():
    tests = [
        ("File exists", lambda: test_file_exists()),
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

    if os.path.exists(RECIPE_PATH):
        fm, content = test_frontmatter_present()

        details_tests = [
            ("All frontmatter fields", lambda: test_frontmatter_all_fields(fm)),
            ("Title", lambda: test_title(fm)),
            ("Status reviewed", lambda: test_status(fm)),
            ("date_modified", lambda: test_date_modified(fm)),
            ("Slug", lambda: test_slug(fm)),
            ("Cuisine", lambda: test_cuisine(fm)),
            ("Dietary tags", lambda: test_dietary_tags(fm)),
            ("Time fields", lambda: test_frontmatter_times(fm)),
            ("Tags", lambda: test_tags(fm)),
            ("Source documented", lambda: test_source_documented(fm)),
            ("Difficulty", lambda: test_difficulty(fm)),
            ("Key equipment", lambda: test_key_equipment(fm)),
            ("Origin notes", lambda: test_origin_notes(fm)),
            ("Meal type", lambda: test_meal_type(fm)),
            ("Notebook ingredients", lambda: test_ingredients_notebook_specified(content)),
            ("Ingredient groups", lambda: test_ingredients_grouped(content)),
            ("Ingredient format", lambda: test_ingredients_checkbox_format(content)),
            ("Instruction count", lambda: test_instructions_count(content)),
            ("Bolded titles", lambda: test_instructions_bolded_titles(content)),
            ("Sensory cues", lambda: test_instructions_sensory_cues(content)),
            ("Inline timing", lambda: test_instructions_inline_timing(content)),
            ("Bordelaise components", lambda: test_bordelaise_specifics(content)),
            ("Negi bed", lambda: test_negi_bed(content)),
            ("Salt slab heating", lambda: test_salt_slab_heating(content)),
            ("Cook's Notes", lambda: test_cooks_notes(content)),
            ("Variations", lambda: test_variations(content)),
            ("Make-Ahead/Storage", lambda: test_make_ahead_storage(content)),
            ("Scaling", lambda: test_scaling(content)),
            ("Content sections", lambda: test_content_sections(content)),
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
        print("FAILURES:")
        for name, msg in failures:
            print(f"  - {name}: {msg}")
    print(f"{'='*60}")

    return passed, failed, failures


if __name__ == "__main__":
    passed, failed, failures = run_all_tests()
    sys.exit(1 if failed > 0 else 0)
