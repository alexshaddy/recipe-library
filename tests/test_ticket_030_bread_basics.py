#!/usr/bin/env python3
"""
TICKET-030: Expand Bread Basics Golden Ratio from notebook source.

Validates `recipes/side/bread-basics-golden-ratio.md` against:
  - TICKET-030 requirements
  - Notebook p.25 source (5:3 flour:water ratio)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from test_helpers import *

RECIPE = "side/bread-basics-golden-ratio.md"
EXPECTED_DATE_MODIFIED = "2026-06-27"


def test_file_exists():
    fm, content = load_recipe(RECIPE)
    print("  ✓ File exists at recipes/side/bread-basics-golden-ratio.md")
    return fm, content


def test_frontmatter_cuisine(fm):
    cuisines = fm.get("cuisine", [])
    if isinstance(cuisines, str):
        cuisines = [cuisines]
    cuisines_lower = [c.lower() for c in cuisines]
    assert any("artisan" in c for c in cuisines_lower), \
        f"Expected cuisine Artisan bread, got {cuisines}"
    print("  ✓ Cuisine: Artisan bread")


def test_frontmatter_dietary_tags(fm):
    dt = fm.get("dietary_tags", [])
    if isinstance(dt, str):
        dt = [dt]
    for tag in ["vegan", "vegetarian"]:
        assert tag in dt, f"Expected dietary_tags to contain '{tag}', got {dt}"
    print("  ✓ Dietary tags: vegan, vegetarian")


def test_frontmatter_tags(fm):
    tags = fm.get("tags", [])
    if isinstance(tags, str):
        tags = [tags]
    for exp in ["bread", "basic", "yeast", "technique-mixing", "technique-fermentation",
                "technique-shaping", "technique-baking"]:
        assert any(exp in t.lower() for t in tags), f"Missing tag containing '{exp}', got {tags}"
    print("  ✓ Tags: bread, basic, yeast, technique tags")


def test_frontmatter_protein(fm):
    """Protein should be [none] for bread."""
    protein = fm.get("protein", [])
    if isinstance(protein, str):
        protein = [protein]
    assert len(protein) == 0, f"Expected protein to be empty, got {protein}"
    print("  ✓ Protein: [none]")


def test_frontmatter_status(fm):
    assert fm.get("status") == "reviewed", f"Expected status 'reviewed', got '{fm.get('status')}'"
    dm = fmt_date(fm.get("date_modified", ""))
    assert dm == EXPECTED_DATE_MODIFIED, f"Expected date_modified '{EXPECTED_DATE_MODIFIED}', got '{dm}'"
    print("  ✓ Status reviewed, date_modified 2026-06-27")


def test_frontmatter_fields(fm):
    for field in ["title", "slug", "meal_type", "cuisine", "course",
                  "dietary_tags", "season",
                  "prep_time", "cook_time", "inactive_time", "total_time",
                  "base_servings", "serving_unit", "scaling_notes",
                  "source_type", "source_name", "origin_notes",
                  "difficulty", "key_equipment", "tags", "protein",
                  "status", "date_added", "date_modified"]:
        check_frontmatter_field(fm, field)
    print("  ✓ All required frontmatter fields present")


def test_source_documented(fm):
    assert fm.get("source_type") == "handwritten", \
        f"Expected source_type 'handwritten', got '{fm.get('source_type')}'"
    assert "Notebook" in fm.get("source_name", ""), \
        f"Expected source_name containing 'Notebook', got '{fm.get('source_name')}'"
    assert fm.get("source_page") == "25", \
        f"Expected source_page '25', got '{fm.get('source_page')}'"
    print("  ✓ Source documented: handwritten — Chef's Recipe Notebook p.25")


def test_golden_ratio(content):
    """Verify the 5:3 flour:water ratio is prominently documented."""
    assert "5:3" in content, "Missing 5:3 ratio reference"
    assert "60%" in content or "60%" in content, "Missing 60% hydration reference"
    print("  ✓ Golden Ratio 5:3 (60% hydration) documented")


def test_yeast_resolved(content):
    """Verify the [TO VERIFY] on yeast is resolved — no [TO VERIFY] in ingredient section."""
    # Check only between ## Ingredients and ## Instructions
    ingr_section = content.split("## Ingredients")[1].split("## Instructions")[0] if "## Ingredients" in content and "## Instructions" in content else ""
    assert "[TO VERIFY]" not in ingr_section, \
        "Yeast still has [TO VERIFY] in ingredient list"
    assert "0.7%" in content or "0.7" in content, "Missing yeast percentage"
    print("  ✓ Yeast [TO VERIFY] resolved")


def test_instructions(content):
    n, titles, sensory = check_instructions(content, min_steps=8, max_steps=11)
    print(f"  ✓ Instructions: {n} steps, {len(titles)} bolded titles, {len(sensory)} sensory cues")


def test_inline_timing(content):
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)
    timing = re.findall(r"\d+\s*(?:min(?:ute)?s?|hour|hr|sec)s?", instr_section, re.IGNORECASE)
    assert len(timing) >= 4, f"Too few timing cues: {len(timing)}"
    print(f"  ✓ Inline timing: {len(timing)} instances")


def test_notes(content):
    nb, vb = check_notes(content, min_cooks=2, min_variations=1)
    print(f"  ✓ Notes: {nb} cook's notes, {vb} variations, make-ahead, storage, scaling")


def test_sections(content):
    required = ["## Ingredients", "## Instructions", "## Notes & Variations",
                "### Cook's Notes", "### Variations", "### Scaling"]
    for h in required:
        assert h in content, f"Missing heading: {h}"
    assert "Make-Ahead" in content, "Missing Make-Ahead"
    assert "Storage" in content, "Missing Storage"
    print("  ✓ All required sections present")


def test_key_steps_present(content):
    """Verify key bread-making steps are present."""
    lower = content.lower()
    for step in ["autolyse", "knead", "bulk ferment", "stretch", "fold",
                 "shape", "proof", "score", "steam"]:
        assert step in lower, f"Missing key step: {step}"
    print("  ✓ Key bread steps: autolyse, knead, bulk ferment, stretch & fold, shape, proof, score, steam")


def test_origin_note(content):
    assert "Notebook" in content and "p. 25" in content, \
        "Missing notebook origin reference"
    print("  ✓ Origin note references notebook page 25")


def test_key_equipment(fm):
    ke = fm.get("key_equipment", [])
    if isinstance(ke, str):
        ke = [ke]
    for tool in ["dutch-oven", "scale", "proofing-basket"]:
        assert any(tool in eq for eq in ke), f"Missing required equipment '{tool}', got {ke}"
    print("  ✓ Key equipment: dutch-oven, scale, proofing-basket")


def test_by_weight(content):
    """Verify ingredients are listed by weight with percentages."""
    assert "500 g" in content, "Missing 500g flour by weight"
    assert "300 g" in content, "Missing 300g water by weight"
    assert "100%" in content, "Missing baker's percentage reference"
    print("  ✓ Ingredients by weight with baker's percentages")


def test_no_estimated_values(content):
    """Verify no [ESTIMATED] values remain."""
    assert "[ESTIMATED]" not in content, "Still has unresolved [ESTIMATED] values"
    print("  ✓ No [ESTIMATED] values remain")


def run():
    fm, content = load_recipe(RECIPE)

    tests = [
        ("File exists", lambda: None),
        ("Frontmatter: cuisine", lambda: test_frontmatter_cuisine(fm)),
        ("Frontmatter: dietary tags", lambda: test_frontmatter_dietary_tags(fm)),
        ("Frontmatter: tags", lambda: test_frontmatter_tags(fm)),
        ("Frontmatter: protein [none]", lambda: test_frontmatter_protein(fm)),
        ("Frontmatter: status/date", lambda: test_frontmatter_status(fm)),
        ("Frontmatter: all fields", lambda: test_frontmatter_fields(fm)),
        ("Source documented", lambda: test_source_documented(fm)),
        ("Key equipment", lambda: test_key_equipment(fm)),
        ("Golden Ratio 5:3 documented", lambda: test_golden_ratio(content)),
        ("Yeast [TO VERIFY] resolved", lambda: test_yeast_resolved(content)),
        ("Ingredients by weight", lambda: test_by_weight(content)),
        ("Instructions", lambda: test_instructions(content)),
        ("Inline timing", lambda: test_inline_timing(content)),
        ("Key bread steps present", lambda: test_key_steps_present(content)),
        ("Cook's notes & variations", lambda: test_notes(content)),
        ("Sections", lambda: test_sections(content)),
        ("Origin note", lambda: test_origin_note(content)),
        ("No [ESTIMATED] values", lambda: test_no_estimated_values(content)),
    ]

    run_tests("TICKET-030", tests)


if __name__ == "__main__":
    run()
