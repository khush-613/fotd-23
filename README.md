# NoteForge

> **Note:** This is not a real project or product. It is a Capture The Flag (CTF)
> challenge. A flag is hidden somewhere in this repository for you to find. The app
> code below is just set dressing, it does not need to run. Flag format:
> `INFOSEC_SIG{...}`. Happy hunting.

Tiny internal notes service for the team. Flask + in-memory storage.

## Run

    pip install -r requirements.txt
    python app.py

Open http://localhost:5000.

## API

- `GET /notes` list notes
- `POST /notes` create a note (`{"title": "...", "body": "..."}`)
- `DELETE /notes/<id>` remove a note

## Configuration

Copy `.env.example` and set the variables in your environment before running.
