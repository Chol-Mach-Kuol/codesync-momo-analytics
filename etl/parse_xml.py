import xml.etree.ElementTree as ET
import logging

logger = logging.getLogger(__name__)


def parse_xml(xml_path: str) -> list[dict]:
    """Parse MoMo XML file and return a list of raw transaction dicts."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    records = []
    for sms in root.findall("sms"):
        records.append(sms.attrib)
    logger.info(f"Parsed {len(records)} records from {xml_path}")
    return records
