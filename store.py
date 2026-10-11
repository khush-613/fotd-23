"""In-memory note storage."""
_notes = {}
_next_id = 1


def all_notes():
    return list(_notes.values())


def add_note(title, body):
    global _next_id
    note = {"id": _next_id, "title": title, "body": body, "tags": []}
    _notes[_next_id] = note
    _next_id += 1
    return note


def delete_note(note_id):
    return _notes.pop(note_id, None)


def tag_note(note_id, tag):
    note = _notes.get(note_id)
    if note is None:
        return None
    note["tags"].append(tag)
    return note
