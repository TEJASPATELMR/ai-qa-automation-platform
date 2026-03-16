import pytest


@pytest.fixture
def self_heal_helpers():
    """Fixture that provides access to the self-heal helper functions.

    Usage in tests:
        def test_x(self_heal_helpers, page):
            safe_click = self_heal_helpers['safe_click']
            safe_click(page, "#some-btn")
    """
    from playwright.helpers.self_heal import safe_click, safe_fill, find_alternative_locator

    return {
        'safe_click': safe_click,
        'safe_fill': safe_fill,
        'find_alternative_locator': find_alternative_locator,
    }
