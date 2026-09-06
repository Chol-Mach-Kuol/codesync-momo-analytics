from etl.clean_normalize import clean_amount, clean_phone, clean_date, clean_record


def test_clean_amount_strips_commas():
    assert clean_amount("5,000 RWF") == 5000.0


def test_clean_amount_none():
    assert clean_amount("") is None


def test_clean_phone_valid():
    assert clean_phone("+250788000001") == "250788000001"


def test_clean_phone_short():
    assert clean_phone("123") is None


def test_clean_date_iso():
    result = clean_date("Jan 1, 2024 10:00:00")
    assert result.startswith("2024-01-01")


def test_clean_record_drops_empty_body():
    assert clean_record({"body": "", "amount": "100", "date": "2024-01-01"}) is None


def test_clean_record_valid():
    r = clean_record({"_id": "1", "body": "received 500", "amount": "500", "date": "2024-01-01", "address": "+250788000001"})
    assert r is not None
    assert r["amount"] == 500.0
