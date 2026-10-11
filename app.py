from flask import Flask, jsonify, request

import config
import search
import store

app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.get("/")
def index():
    return "NoteForge is running"


@app.get("/notes")
def list_notes():
    return jsonify(store.all_notes())


@app.post("/notes")
def create_note():
    data = request.get_json(force=True)
    return jsonify(store.add_note(data["title"], data["body"])), 201


@app.get("/search")
def search_notes():
    return jsonify(search.search(request.args.get("q", "")))


@app.delete("/notes/<int:note_id>")
def delete_note(note_id):
    if store.delete_note(note_id) is None:
        return jsonify({"error": "not found"}), 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=config.DEBUG)
