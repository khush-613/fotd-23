# NoteForge

Tiny internal notes service for the team. Flask + in-memory storage.

## Run

    pip install -r requirements.txt
    python app.py

Open http://localhost:5000.

## API

- `GET /notes` list notes
- `POST /notes` create a note (`{"title": "...", "body": "..."}`)
- `DELETE /notes/<id>` remove a note
