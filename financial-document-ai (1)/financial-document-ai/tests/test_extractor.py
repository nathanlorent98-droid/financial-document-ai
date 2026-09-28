from financial_document_ai.extractor import extract_metrics


def test_extracts_common_financial_metrics():
    text = '''
    Revenue: €4.1 million
    EBITDA: €1.1 million
    Net debt: €500k
    Employees: 24
    '''

    assert extract_metrics(text) == {
        "revenue": 4_100_000.0,
        "ebitda": 1_100_000.0,
        "debt": 500_000.0,
        "headcount": 24,
    }
