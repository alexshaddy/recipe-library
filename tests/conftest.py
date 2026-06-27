#!/usr/bin/env python3
"""Pytest fixtures for recipe validation tests."""

import os
import re
import yaml
import pytest

RECIPE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "recipes")


def parse_frontmatter(content):
    """Parse YAML frontmatter from a markdown file."""
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None
    try:
        return yaml.safe_load(match.group(1))
    except yaml.YAMLError:
        return None


@pytest.fixture
def fm(request):
    """Fixture that loads the recipe file and returns parsed frontmatter and content."""
    # Get the recipe path from the test module
    test_file = request.module.__file__
    # Extract ticket number from test file name
    match = re.search(r'test_ticket_(\d+)', test_file)
    if not match:
        pytest.skip("Could not determine ticket number from test file")
    
    # We need to know which recipe file to load - this varies by ticket
    # The test module should define RECIPE_PATH
    if hasattr(request.module, 'RECIPE_PATH'):
        path = request.module.RECIPE_PATH
    else:
        pytest.skip("Test module must define RECIPE_PATH")
    
    with open(path) as f:
        content = f.read()
    fm = parse_frontmatter(content)
    assert fm is not None, f"Could not parse YAML frontmatter in {path}"
    return fm, content


@pytest.fixture
def content(fm):
    """Fixture that returns the full recipe content."""
    return fm[1]


@pytest.fixture
def frontmatter(fm):
    """Fixture that returns just the frontmatter dict."""
    return fm[0]
