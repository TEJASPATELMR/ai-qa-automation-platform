from loaders.word_loader import load_word_document
from loaders.excel_loader import load_excel_mapping
import os

REQ_PATH = "data/requirements/requirement.docx"
MAPPING_PATH = "data/mappings/api_mapping.xlsx"
OUT_PATH = "playwright/tests/test_ai_generated.py"


def short_snippet(text, length=80):
    s = " ".join(text.split())
    return (s[:length] + "...") if len(s) > length else s


def generate_tests(requirement_text, mapping_text):
    lines = [l.strip() for l in requirement_text.splitlines() if l.strip()]
    snippets = []
    if lines:
        snippets.append(("title", short_snippet(lines[0], 100)))
    if len(lines) > 1:
        snippets.append(("first_paragraph", short_snippet(lines[1], 120)))
    if len(lines) > 2:
        snippets.append(("second_paragraph", short_snippet(lines[2], 120)))

    # add a mapping-based test placeholder
    mapping_snippet = short_snippet(mapping_text or "", 100)
    if mapping_snippet:
        snippets.append(("api_mapping_snippet", mapping_snippet))

    header = (
        "import pytest\n"
        "from playwright.sync_api import sync_playwright\n\n"
        "# Auto-generated Playwright pytest file.\n"
        "# Replace `http://your-app-url` and the `assert` placeholders with real checks.\n\n"
    )

    body = ""
    for i, (name, snippet) in enumerate(snippets, start=1):
        func = f"def test_{name}_{i}():\n"
        func += f"    \"\"\"Generated from requirement: {snippet}\"\"\"\n"
        func += "    with sync_playwright() as p:\n"
        func += "        browser = p.chromium.launch()\n"
        func += "        page = browser.new_page()\n"
        func += "        page.goto(\"http://your-app-url\")\n"
        func += f"        # TODO: verify presence/behavior related to: {snippet}\n"
        func += "        assert True  # replace with real assertions\n"
        func += "        browser.close()\n\n"
        body += func

    return header + body


def main():
    if not os.path.exists(REQ_PATH):
        print(f"Requirement file not found: {REQ_PATH}")
        return

    requirement = load_word_document(REQ_PATH)

    mapping = ""
    try:
        mapping = load_excel_mapping(MAPPING_PATH)
    except Exception:
        mapping = ""

    script = generate_tests(requirement, mapping)

    out_dir = os.path.dirname(OUT_PATH)
    os.makedirs(out_dir, exist_ok=True)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(script)

    print(f"Generated Playwright tests saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
