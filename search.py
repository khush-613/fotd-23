"""Naive note search."""
import store


def search(term):
    term = term.lower()
    return [n for n in store.all_notes()
            if term in n["title"].lower() or term in n["body"].lower()]
