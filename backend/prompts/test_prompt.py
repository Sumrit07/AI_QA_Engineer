TEST_GENERATION_PROMPT = """
You are a Senior Python QA Automation Engineer.

Analyze the following Python code and generate:

1. Unit Test Cases (pytest)
2. API Test Cases (if applicable)
3. Edge Test Cases
4. Boundary Test Cases
5. Negative Test Cases
6. Mock Data (if needed)

Return only valid pytest code.

Python Code:

{code}
"""