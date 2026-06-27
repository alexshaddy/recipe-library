#!/usr/bin/env python3
"""Test suite for TICKET-011: Miso Ramen recipe.

Validates the recipe at recipes/dinner/miso-ramen.md against all
requirements in the ticket: file existence, ingredient groupings,
instruction structure, frontmatter metadata, and content keywords.
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *


def test_file_exists():
    """Verify the Miso Ramen recipe file exists at the expected path."""
    recipe = load_recipe("dinner/miso-ramen.md")
    assert recipe is not None, "Recipe file not found at recipes/dinner/miso-ramen.md"
    return True


def test_frontmatter_present():
    """Verify frontmatter metadata exists and has required fields."""
    recipe = load_recipe("dinner/miso-ramen.md")
    fm = recipe.get("frontmatter", recipe.get("metadata", {}))
    required_keys = ["cuisine", "tags", "technique", "protein", "status", "date_modified"]
    for key in required_keys:
        assert key in fm, f"Missing frontmatter key: {key}"
    return fm


def test_frontmatter_cuisine():
    """Verify cuisine is Japanese."""
    fm = test_frontmatter_present()
    assert "japanese" in str(fm.get("cuisine", "")).lower(), \
        "Cuisine must include 'Japanese'"
    return True


def test_frontmatter_tags():
    """Verify tags include dinner, ramen, and noodles."""
    fm = test_frontmatter_present()
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",")]
    for expected in ["dinner", "ramen", "noodles"]:
        assert expected in tags, f"Missing tag: {expected}"
    return True


def test_frontmatter_technique():
    """Verify technique includes broth-making and tare."""
    fm = test_frontmatter_present()
    technique = fm.get("technique", [])
    if isinstance(technique, str):
        technique = [t.strip() for t in technique.split(",")]
    for expected in ["broth-making", "tare"]:
        assert expected in technique, f"Missing technique: {expected}"
    return True


def test_frontmatter_protein():
    """Verify protein includes chicken and pork."""
    fm = test_frontmatter_present()
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [p.strip() for p in protein.split(",")]
    for expected in ["chicken", "pork"]:
        assert expected in protein, f"Missing protein: {expected}"
    return True


def test_frontmatter_status():
    """Verify status is 'reviewed' and date_modified is 2026-06-27."""
    fm = test_frontmatter_present()
    assert fm.get("status") == "reviewed", \
        f"Expected status 'reviewed', got '{fm.get('status')}'"
    modified = fm.get("date_modified", fm.get("date-modified", ""))
    assert str(modified) == "2026-06-27", \
        f"Expected date_modified '2026-06-27', got '{modified}'"
    return True


def test_ingredient_groups_present():
    """Verify the ingredient section contains the required groups.

    Required groups: broth (chicken/pork), miso tare, noodles, toppings.
    """
    recipe = load_recipe("dinner/miso-ramen.md")
    content = recipe.get("content", recipe.get("body", ""))
    if not content:
        if "sections" in recipe:
            content = "\n".join(
                s.get("body", "") if isinstance(s, dict) else str(s)
                for s in recipe["sections"]
            )
        else:
            content = str(recipe)

    content_lower = content.lower()

    # Check group headers or mentions
    groups = ["broth", "miso tare", "tare", "noodles", "toppings"]
    found = [g for g in groups if g in content_lower]
    # "tare" alone should count if "miso tare" isn't present as a literal heading
    assert "miso tare" in content_lower or "tare" in content_lower, \
        "Missing 'miso tare' or 'tare' in ingredients"
    assert "broth" in content_lower, "Missing 'broth' in ingredients"
    assert "noodles" in content_lower, "Missing 'noodles' in ingredients"
    assert "toppings" in content_lower, "Missing 'toppings' in ingredients"
    return True


def test_ingredient_group_broth_details():
    """Verify broth mentions chicken and/or pork."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    assert "chicken" in content or "pork" in content, \
        "Broth group should mention chicken or pork"
    return True


def test_ingredient_group_miso_tare_details():
    """Verify miso tare mentions white miso and red miso."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    assert "white miso" in content, "Missing 'white miso' in miso tare"
    assert "red miso" in content, "Missing 'red miso' in miso tare"
    return True


def test_ingredient_group_tare_components():
    """Verify miso tare mentions mirin, sake, garlic, and ginger."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    for component in ["mirin", "sake", "garlic", "ginger"]:
        assert component in content, f"Missing tare component: {component}"
    return True


def test_toppings_present():
    """Verify all required toppings are mentioned.

    Required toppings: chashu, nori, corn, butter
    """
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    for topping in ["chashu", "nori", "corn", "butter"]:
        assert topping in content, f"Missing required topping: {topping}"
    return True


def test_instructions_structure():
    """Verify instructions have 7-9 steps with bolded titles and sensory cues.

    Uses the shared check_instructions helper.
    """
    recipe = load_recipe("dinner/miso-ramen.md")
    instruction_text = _get_instructions(recipe)
    assert instruction_text, "No instructions section found in recipe"

    steps = _split_steps(instruction_text)
    step_count = len(steps)
    assert 7 <= step_count <= 9, \
        f"Expected 7-9 instruction steps, got {step_count}"

    # Every step should have a bolded title (marked by **...**)
    for i, step in enumerate(steps):
        assert "**" in step, f"Step {i+1} is missing a bolded title"

    # At least some steps should contain sensory cues
    sensory_keywords = [
        "until", "fragrant", "golden", "brown", "bubbly",
        "soft", "tender", "simmer", "boil", "sizzl",
        "thickened", "caramelized", "translucent", "aromatic",
    ]
    sensory_count = sum(
        1 for step in steps
        if any(kw in step.lower() for kw in sensory_keywords)
    )
    assert sensory_count >= 3, \
        f"Expected at least 3 steps with sensory cues, found {sensory_count}"

    return True


def test_instructions_inline_timing():
    """Verify instructions contain inline timing cues (e.g. '5 minutes', '10 min')."""
    recipe = load_recipe("dinner/miso-ramen.md")
    instruction_text = _get_instructions(recipe)
    assert instruction_text, "No instructions section found"

    # Look for patterns like "X minutes" or "X min" or "X-hour"
    import re
    timing_pattern = r'\d+\s*(?:min(?:ute)?s?|hour|hr)s?'
    matches = re.findall(timing_pattern, instruction_text.lower())
    assert len(matches) >= 2, \
        f"Expected at least 2 inline timing cues, found {len(matches)}: {matches}"
    return True


def test_cooks_notes():
    """Verify there are at least 2 cook's notes."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe)
    notes = _extract_section(content, "cook's notes", "notes")
    if not notes:
        notes = _extract_section(content, "cook's note", "note")
    assert notes, "No 'Cook's Notes' section found"
    # Count bullet points or numbered items as individual notes
    note_items = _count_list_items(notes)
    assert note_items >= 2, \
        f"Expected at least 2 cook's notes, found {note_items}"
    return True


def test_variations():
    """Verify there is at least 1 variation."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe)
    variation_section = _extract_section(content, "variation", "variations")
    assert variation_section, "No 'Variations' section found"
    return True


def test_make_ahead_storage():
    """Verify make-ahead or storage instructions exist."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    assert ("make-ahead" in content or "make ahead" in content
            or "storage" in content or "store" in content), \
        "Missing make-ahead or storage instructions"
    return True


def test_scaling():
    """Verify scaling information exists."""
    recipe = load_recipe("dinner/miso-ramen.md")
    content = _get_content(recipe).lower()
    assert ("scaling" in content or "scale" in content
            or "double" in content or "halve" in content
            or "adjust" in content), \
        "Missing scaling information"
    return True


def test_date_modified_format():
    """Verify date_modified uses the shared fmt_date helper format."""
    fm = test_frontmatter_present()
    modified = fm.get("date_modified", fm.get("date-modified", ""))
    formatted = fmt_date(str(modified))
    assert formatted is not None, f"date_modified '{modified}' could not be formatted"
    return True


# ---------------------------------------------------------------------------
# Internal helpers (operate on the dict returned by load_recipe)
# ---------------------------------------------------------------------------

def _get_content(recipe):
    """Extract full recipe text from the parsed recipe dict."""
    content = recipe.get("content", recipe.get("body", ""))
    if not content:
        if "sections" in recipe:
            content = "\n".join(
                s.get("body", "") if isinstance(s, dict) else str(s)
                for s in recipe["sections"]
            )
        else:
            content = str(recipe)
    return content


def _get_instructions(recipe):
    """Extract the instructions section text."""
    content = _get_content(recipe)
    return _extract_section(content, "instructions", "directions", "method")


def _extract_section(content, *section_names):
    """Return the text of the first section found matching any of the names."""
    lines = content.split("\n")
    in_section = False
    section_lines = []
    section_headers = set()

    for name in section_names:
        section_headers.add(f"## {name.lower()}")
        section_headers.add(f"##{name.lower()}")
        section_headers.add(f"# {name.lower()}")
        section_headers.add(name.lower())

    for line in lines:
        stripped = line.strip().lower()
        if stripped in section_headers or any(
            stripped.startswith(h) for h in section_headers
        ):
            in_section = True
            continue
        if in_section:
            # Stop at the next top-level or second-level heading
            if stripped.startswith("## ") or stripped.startswith("# "):
                break
            section_lines.append(line)

    return "\n".join(section_lines).strip()


def _split_steps(text):
    """Split instruction text into individual steps.

    Steps may be numbered (1., 2., etc.) or separated by blank lines.
    """
    lines = text.split("\n")
    steps = []
    current_step = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current_step:
                steps.append("\n".join(current_step))
                current_step = []
            continue
        # Detect numbered step markers
        import re
        if re.match(r'^\d+[\.\)]\s', stripped):
            if current_step:
                steps.append("\n".join(current_step))
            current_step = [stripped]
        else:
            current_step.append(stripped)
    if current_step:
        steps.append("\n".join(current_step))
    return steps


def _count_list_items(text):
    """Count bullet or numbered items in text."""
    import re
    bullets = re.findall(r'^[\s]*[-*]\s', text, re.MULTILINE)
    numbers = re.findall(r'^\s*\d+[\.\)]\s', text, re.MULTILINE)
    return max(len(bullets), len(numbers), 1 if text.strip() else 0)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    tests = [
        ("File exists", test_file_exists),
        ("Frontmatter: cuisine is Japanese", test_frontmatter_cuisine),
        ("Frontmatter: tags include dinner, ramen, noodles", test_frontmatter_tags),
        ("Frontmatter: technique includes broth-making, tare", test_frontmatter_technique),
        ("Frontmatter: protein includes chicken, pork", test_frontmatter_protein),
        ("Frontmatter: status reviewed, date 2026-06-27", test_frontmatter_status),
        ("Ingredient groups present (broth, tare, noodles, toppings)", test_ingredient_groups_present),
        ("Ingredient: broth mentions chicken/pork", test_ingredient_group_broth_details),
        ("Ingredient: miso tare includes white and red miso", test_ingredient_group_miso_tare_details),
        ("Ingredient: tare components (mirin, sake, garlic, ginger)", test_ingredient_group_tare_components),
        ("Toppings: chashu, nori, corn, butter", test_toppings_present),
        ("Instructions: 7-9 steps with bold titles & sensory cues", test_instructions_structure),
        ("Instructions: inline timing cues", test_instructions_inline_timing),
        ("Cook's notes: ≥2", test_cooks_notes),
        ("Variations: ≥1", test_variations),
        ("Make-ahead / storage", test_make_ahead_storage),
        ("Scaling", test_scaling),
        ("Date format via fmt_date", test_date_modified_format),
    ]

    run_tests("TICKET-011", tests)
