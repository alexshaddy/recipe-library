#!/usr/bin/env python3
"""Shared test utilities for recipe validation tests."""

import os
import re
import sys

try:
    import yaml
except ImportError:
    yaml = None

RECIPES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recipes")


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
    # fallback manual parse
    fm = {}
    for line in fm_text.strip().split("\n"):
        line = line.strip()
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, content


def load_recipe(relative_path):
    """Load a recipe file and return (frontmatter dict, content string)."""
    path = os.path.join(RECIPES_DIR, relative_path)
    assert os.path.exists(path), f"Recipe file not found at {path}"
    with open(path) as f:
        content = f.read()
    fm, content = parse_frontmatter(content)
    assert fm is not None, f"Could not parse YAML frontmatter in {path}"
    return fm, content


def fmt_date(dm):
    """Convert YAML date object to string for comparison."""
    if hasattr(dm, "isoformat"):
        return dm.isoformat()
    return str(dm)


def check_frontmatter_field(fm, field):
    """Assert a frontmatter field exists and is non-empty."""
    val = fm.get(field)
    assert val is not None and val != "", f"{field} is missing or empty"
    return val


def check_instructions(content, min_steps=5, max_steps=8):
    """Check instructions section meets requirements."""
    instr_match = re.search(r"## Instructions\s*\n(.*?)(?=## Notes|\Z)", content, re.DOTALL)
    assert instr_match, "Could not find Instructions section"
    instr_section = instr_match.group(1)

    steps = re.findall(r"^\d+\.\s+\*\*", instr_section, re.MULTILINE)
    n = len(steps)
    assert min_steps <= n <= max_steps, (
        f"Expected {min_steps}-{max_steps} instructions, found {n}"
    )

    # Check bolded titles
    titles = re.findall(r"^\d+\.\s+\*\*(.+?)\*\*", instr_section, re.MULTILINE)
    assert len(titles) >= 1, "No bolded action titles found"

    # Check sensory cues
    sensory = ["sizzle", "brown", "golden", "fragrant", "smooth", "creamy",
               "glossy", "aroma", "bubbly", "melt", "soft", "warm", "tender",
               "crisp", "pink", "wilt", "translucent", "thick"]
    found = [t for t in sensory if t in instr_section.lower()]
    assert len(found) >= 1, f"No sensory cues found: found {found}"

    # Check inline timing
    timing = re.findall(r"\d+[–\-]?\d*\s*(?:min|hour|hr|sec|second|minute)s?(?=\)|\s)",
                        instr_section, re.IGNORECASE)
    assert len(timing) >= 2, f"Too few inline timings: {len(timing)}"

    return n, titles, found


def check_notes(content, min_cooks=2, min_variations=1):
    """Check Notes & Variations section."""
    notes = re.search(r"### Cook's Notes\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert notes, "Missing Cook's Notes section"
    nb = len(re.findall(r"^- ", notes.group(1), re.MULTILINE))
    assert nb >= min_cooks, f"Expected ≥{min_cooks} cook's notes, got {nb}"

    var = re.search(r"### Variations\s*\n(.*?)(?=###|\Z)", content, re.DOTALL)
    assert var, "Missing Variations section"
    vb = len(re.findall(r"^- \*\*", var.group(1), re.MULTILINE))
    assert vb >= min_variations, f"Expected ≥{min_variations} variation(s), got {vb}"

    assert "Make-Ahead" in content or "Make Ahead" in content, "Missing Make-Ahead"
    assert "Storage" in content or "storage" in content, "Missing Storage"
    assert "### Scaling" in content, "Missing Scaling section"

    return nb, vb


def run_tests(name, tests):
    """Run a list of (name, callable) tests and print results."""
    passed = 0
    failed = 0
    failures = []
    print(f"\n{'='*60}")
    print(f"TICKET: {name}")
    print(f"{'='*60}")

    for test_name, test_fn in tests:
        try:
            test_fn()
            passed += 1
            print(f"  ✓ {test_name}")
        except AssertionError as e:
            failed += 1
            failures.append((test_name, str(e)))
            print(f"  ✗ {test_name}: FAILED")
            print(f"    {e}")
        except Exception as e:
            failed += 1
            failures.append((test_name, str(e)))
            print(f"  ✗ {test_name}: ERROR")
            print(f"    {e}")

    print(f"\n{'─'*60}")
    print(f"RESULTS: {passed} passed, {failed} failed")
    if failures:
        print("FAILURES:")
        for tn, msg in failures:
            print(f"  - {tn}: {msg}")
    print(f"{'─'*60}")
    return passed, failed, failures
