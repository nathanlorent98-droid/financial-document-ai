import re
from typing import Any


PATTERNS = {
    "revenue": [
        r"(?:revenue|turnover|chiffre d[’']affaires|chiffre d'affaires|ca)\s*[:=]?\s*€?\s*([\d\s.,]+)\s*(m|million|millions|k|thousand)?",
    ],
    "ebitda": [
        r"(?:ebitda|ebe|ebit)\s*[:=]?\s*€?\s*([\d\s.,]+)\s*(m|million|millions|k|thousand)?",
    ],
    "debt": [
        r"(?:net debt|debt|dette)\s*[:=]?\s*€?\s*([\d\s.,]+)\s*(m|million|millions|k|thousand)?",
    ],
    "headcount": [
        r"(?:headcount|employees|effectif|salariés)\s*[:=]?\s*(\d+)",
    ],
}


def _number(value: str, unit: str | None) -> float:
    cleaned = value.replace(" ", "").replace("\u202f", "")
    if "," in cleaned and "." in cleaned:
        cleaned = cleaned.replace(".", "").replace(",", ".")
    elif "," in cleaned:
        cleaned = cleaned.replace(",", ".")
    number = float(cleaned)

    if unit:
        unit = unit.lower()
        if unit in {"m", "million", "millions"}:
            number *= 1_000_000
        elif unit in {"k", "thousand"}:
            number *= 1_000
    return number


def extract_metrics(text: str) -> dict[str, Any]:
    result: dict[str, Any] = {}

    for metric, patterns in PATTERNS.items():
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.IGNORECASE)
            if not match:
                continue

            value = match.group(1)
            unit = match.group(2) if match.lastindex and match.lastindex >= 2 else None

            if metric == "headcount":
                result[metric] = int(value)
            else:
                result[metric] = _number(value, unit)
            break

    return result
