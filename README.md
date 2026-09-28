# Financial Document AI

Open-source toolkit for extracting and structuring financial information from business documents.

The project focuses on practical automation for knowledge-intensive workflows: extracting text from PDFs, identifying common financial metrics, and exporting structured data that can be reused in analysis workflows.

## Current features

- PDF text extraction
- Extraction of common financial metrics such as revenue, EBITDA/EBE, debt and headcount
- Structured JSON output
- Simple command-line interface
- Unit tests

## Example

```bash
pip install -e .
financial-document-ai extract-report ./examples/sample_report.txt
```

The project is intentionally generic and does not contain confidential client information or proprietary documents.

## Roadmap

- Better multilingual financial terminology
- Table extraction
- Excel export
- Document classification
- Optional LLM-assisted extraction
- Confidence scores and validation
- Support for additional document formats

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT
