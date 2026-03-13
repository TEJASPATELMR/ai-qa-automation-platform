import ollama

response = ollama.chat(
    model="deepseek-coder",
    messages=[{"role": "user", "content": "Generate login API test cases"}]
)

print(response["message"]["content"])