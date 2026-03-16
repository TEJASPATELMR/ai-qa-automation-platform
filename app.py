import os
import glob
from loaders.word_loader import load_word_document
from loaders.excel_loader import load_excel_mapping

from ai_engine.test_generator import generate_test_cases
from ai_engine.script_generator import generate_playwright_script, save_playwright_script


def _find_first_or_default(path, pattern):
	if os.path.exists(path):
		return path
	# search for matching files in the same folder
	folder = os.path.dirname(path)
	candidates = glob.glob(os.path.join(folder, pattern))
	return candidates[0] if candidates else None


print("Loading requirement document...")

req_path = _find_first_or_default("data/requirements/requirement.docx", "*.docx")
if not req_path:
	raise FileNotFoundError("No requirement document found in data/requirements/")

requirement = load_word_document(req_path)
print(f"Using requirement: {req_path}")


print("Loading API mapping...")

map_path = _find_first_or_default("data/mappings/api_mapping.xlsx", "*.xlsx")
mapping = ""
if map_path:
	try:
		mapping = load_excel_mapping(map_path)
		print(f"Using mapping: {map_path}")
	except Exception as e:
		print(f"Warning: failed to load mapping {map_path}: {e}\nContinuing without mapping.")
		mapping = ""
else:
	print("No mapping file found in data/mappings/; continuing without mapping.")


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