# Action Tracker

A small desktop dashboard for daily action items. It displays each task's status and priority, along with the current time in India and Dallas.

## Requirements

- Python 3.9 or later
- Tkinter (included with most Python installations)

## Run

```powershell
py -3 app.py
```

The app loads `tasks.json` when present. If it is absent, it loads the generic `tasks.example.json` starter list. The local `tasks.json` file is ignored by Git so personal task data is not published.

Task files are JSON arrays with `task`, `status`, and `priority` fields.