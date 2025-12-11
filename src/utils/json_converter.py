import json
from pathlib import Path

def save_json_document(doc: dict, out_path: Path):
    out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False))
