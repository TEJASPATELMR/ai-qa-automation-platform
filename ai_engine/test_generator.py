import ollama

def generate_test_cases(context):

    prompt = f"""
You are a senior QA engineer.

Analyze the requirement and mapping sheet.

Generate:
- Test scenarios
- Detailed test cases
- Edge cases

Format:

Test Case ID | Scenario | Steps | Expected Result

Requirement:
{context}
"""

    response = ollama.chat(
        model="deepseek-coder",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]