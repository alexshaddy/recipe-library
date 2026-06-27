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


def load_recipe(relative_path):
    """Load a recipe file and return (frontmatter dict, content string)."""
    path = os.path.join(RECIPE_DIR, relative_path)
    assert os.path.exists(path), f"Recipe file not found at {path}"
    with open(path) as f:
        content = f.read()
    fm = parse_frontmatter(content)
    assert fm is not None, f"Could not parse YAML frontmatter in {path}"
    return fm, content


@pytest.fixture
def fm(request):
    """Fixture that loads the recipe file and returns parsed frontmatter."""
    # Get the recipe path from the test module
    if hasattr(request.module, 'RECIPE_PATH'):
        path = request.module.RECIPE_PATH
    else:
        pytest.skip("Test module must define RECIPE_PATH")
    
    fm, content = load_recipe(path)
    return fm


@pytest.fixture
def content(request):
    """Fixture that returns the full recipe content."""
    if hasattr(request.module, 'RECIPE_PATH'):
        path = request.module.RECIPE_PATH
    else:
        pytest.skip("Test module must define RECIPE_PATH")
    
    with open(path) as f:
        return f.read()


@pytest.fixture
def filename(request):
    """Fixture that returns the recipe filename."""
    if hasattr(request.module, 'RECIPE_PATH'):
        return os.path.basename(request.module.RECIPE_PATH)
    pytest.skip("Test module must define RECIPE_PATH")
