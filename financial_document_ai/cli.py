import argparse
import json
from pathlib import Path

from .extractor import extract_metrics
from .pdf import extract_pdf_text


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract financial metrics from a document.")
    parser.add_argument("command", choices=["extract-report"])
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if args.path.suffix.lower() == ".pdf":
        text = extract_pdf_text(args.path)
    else:
        text = args.path.read_text(encoding="utf-8")

    result = extract_metrics(text)
    print(json.dumps(result, indent=2, ensure_ascii=False))
