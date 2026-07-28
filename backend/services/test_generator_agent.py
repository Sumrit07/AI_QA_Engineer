class TestGeneratorAgent:

    def generate_tests(self, code: str) -> str:
        """
        Generate simple pytest test template.
        """

        return '''import pytest


def test_sample():
    assert True
'''
