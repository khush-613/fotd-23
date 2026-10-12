"""Export notes to JSON."""
import json

import store


def export_json():
    return json.dumps(store.all_notes(), indent=2)
