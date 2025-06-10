import json
# Placeholder for actual EchoNet processing
def process_echo(dicom_path: str) -> str:
    # TODO: integrate real EchoNet inference here
    # For now, return a mock result
    result = {
        "ejection_fraction": 55.2,
        "lv_volume": 120,
        "rv_volume": 100
    }
    return json.dumps(result)
