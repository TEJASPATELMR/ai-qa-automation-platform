import re
from typing import Optional


def _count(locator) -> int:
    try:
        return locator.count()
    except Exception:
        return 0


def find_alternative_locator(page, original_selector: str, max_words: int = 5):
    """Try multiple strategies to locate an element when the original selector fails.

    Strategies (in order):
    - try the original selector with `page.locator`
    - try `page.get_by_text(original_selector)`
    - try searching for longer words from the selector via `get_by_text`
    - try xpath search for nodes containing those words

    Returns a Playwright Locator or raises an Exception if none found.
    """

    # 1) original selector
    try:
        loc = page.locator(original_selector)
        if _count(loc) > 0:
            return loc
    except Exception:
        pass

    # 2) try exact text match
    try:
        loc = page.get_by_text(original_selector)
        if _count(loc) > 0:
            return loc
    except Exception:
        pass

    # 3) try words extracted from selector (prefer longer words)
    words = re.findall(r"\w{4,}", original_selector)
    words = sorted(set(words), key=lambda w: -len(w))[:max_words]

    for w in words:
        try:
            loc = page.get_by_text(w)
            if _count(loc) > 0:
                return loc
        except Exception:
            pass

    # 4) try xpath contains(normalize-space(.), word)
    for w in words:
        try:
            escaped = w.replace('"', '\\"')
            xpath = f'xpath=//*[contains(normalize-space(.), "{escaped}")]'
            loc = page.locator(xpath)
            if _count(loc) > 0:
                return loc
        except Exception:
            pass

    raise RuntimeError(f"No alternative locator found for: {original_selector}")


def safe_click(page, selector: str, **kwargs):
    """Attempt to click using `selector`. If that fails, search for alternatives and click the first found."""
    try:
        loc = page.locator(selector)
        loc.click(**kwargs)
        return loc
    except Exception as e:
        print(f"[self-heal] Original click failed for '{selector}': {e}")
        alt = find_alternative_locator(page, selector)
        print(f"[self-heal] Found alternative locator, clicking it.")
        alt.click(**kwargs)
        return alt


def safe_fill(page, selector: str, value: str, **kwargs):
    """Attempt to fill using `selector`. If that fails, search for an alternative input and fill it."""
    try:
        page.fill(selector, value, **kwargs)
        return page.locator(selector)
    except Exception as e:
        print(f"[self-heal] Original fill failed for '{selector}': {e}")
        alt = find_alternative_locator(page, selector)
        try:
            alt.fill(value)
            return alt
        except Exception as e2:
            raise RuntimeError(f"Alternative locator found but fill failed: {e2}")


__all__ = ["find_alternative_locator", "safe_click", "safe_fill"]
