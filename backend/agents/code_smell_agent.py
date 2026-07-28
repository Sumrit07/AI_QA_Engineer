from backend.services.gemini_service import GeminiService


class CodeSmellAgent:

    def __init__(self):
        self.gemini = GeminiService()

    def analyze(self, code: str):

        prompt = f"""
You are a Senior Software Architect and Clean Code Reviewer.

Analyze the following Python code and identify all Code Smells and Maintainability Issues.

For every issue provide:

1. Code Smell
2. Severity (Critical / High / Medium / Low)
3. Description
4. Why it is a problem
5. Refactoring Suggestion
6. Improved Code Example (if possible)

Check especially for:

- Duplicate Code
- Long Functions
- Large Classes
- Dead Code
- Unused Variables
- Unused Imports
- Magic Numbers
- Poor Naming
- Deep Nesting
- High Coupling
- Low Cohesion
- SOLID Principle Violations
- DRY Principle Violations
- Single Responsibility Principle
- Poor Exception Handling
- Hardcoded Values
- Poor Readability
- Maintainability Problems

Return the report in clean markdown.

Python Code:

{code}
"""

        return self.gemini.generate(prompt)