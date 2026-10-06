"""In-memory note storage."""
_notes = {}
_next_id = 1


def all_notes():
    return list(_notes.values())


def add_note(title, body):
    global _next_id
    note = {"id": _next_id, "title": title, "body": body}
    _notes[_next_id] = note
    _next_id += 1
    return note
