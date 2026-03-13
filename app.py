from loaders.word_loader import load_word_document
from loaders.excel_loader import load_excel_mapping

from ai_engine.test_generator import generate_test_cases
from ai_engine.script_generator import generate_playwright_script, save_playwright_script


print("Loading requirement document...")

requirement = load_word_document("data/requirements/requirement.docx")


print("Loading API mapping...")

mapping = load_excel_mapping("data/mappings/api_mapping.xlsx")


context = requirement + "\n" + mapping


print("Generating test cases using AI...")

test_cases = generate_test_cases(context)

print("\nGenerated Test Cases:\n")
print(test_cases)


print("\nGenerating Playwright automation script...")

script = generate_playwright_script(test_cases)

print(script)


print("\nSaving Playwright test script...")

save_playwright_script(script)