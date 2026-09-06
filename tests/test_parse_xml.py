import os
import tempfile
import pytest
from etl.parse_xml import parse_xml

SAMPLE_XML = """<?xml version="1.0"?>
<smses>
  <sms _id="1" address="+250788000001" date="2024-01-01" body="You have received 5,000 RWF" />
  <sms _id="2" address="+250788000002" date="2024-01-02" body="You have transferred 2,000 RWF" />
</smses>"""


@pytest.fixture
def xml_file(tmp_path):
    f = tmp_path / "test.xml"
    f.write_text(SAMPLE_XML)
    return str(f)


def test_parse_returns_list(xml_file):
    records = parse_xml(xml_file)
    assert isinstance(records, list)


def test_parse_count(xml_file):
    records = parse_xml(xml_file)
    assert len(records) == 2


def test_parse_fields(xml_file):
    records = parse_xml(xml_file)
    assert records[0]["_id"] == "1"
    assert "body" in records[0]
