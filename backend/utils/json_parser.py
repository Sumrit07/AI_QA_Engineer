import json
import re


def parse_json(text: str):

    if not text:
        return {}

    text = text.strip()

    # -------------------------
    # Direct JSON
    # -------------------------
    try:
        return json.loads(text)
    except:
        pass

    # -------------------------
    # JSON Array
    # -------------------------
    try:

        match = re.search(
            r"\[.*\]",
            text,
            re.DOTALL
        )

        if match:
            return json.loads(match.group())

    except:
        pass

    # -------------------------
    # JSON Object
    # -------------------------
    try:

        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL
        )

        if match:
            return json.loads(match.group())

    except:
        pass

    return {}