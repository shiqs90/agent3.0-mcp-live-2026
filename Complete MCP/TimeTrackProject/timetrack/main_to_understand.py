from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles



import database as db
from pydantic import BaseModel

db.init_db() # Initialize the database and seed it with initial data if empty


app = FastAPI(title="TimeTrack", description="A simple time tracking app with REST and MCP endpoints.", version="1.0.0")

@app.get("/api/entries")
def api_list_all_entries():
    """List all time entries in the database."""
    return db.list_all_entries()


@app.get("/api/projects")
def api_list_projects():
    return db.list_projects()


@app.get("/api/projects/{project}/summary")
def api_project_summary(project: str):
    return db.get_project_summary(project)


@app.get("/api/timesheet/{employee_name}")
def api_get_timesheet(employee_name: str, start_date: str = None, end_date: str = None):
    return db.get_timesheet(employee_name, start_date, end_date)



class NewEntry(BaseModel):
    employee_name: str
    project: str
    entry_date: str
    hours: float
    description: str = ""

@app.post("/api/entries")
def api_log_entry(entry: NewEntry):
    return db.log_time(entry.employee_name, entry.project, entry.entry_date, entry.hours, entry.description)


# uvicorn main_to_understand:app --port 9998

# uv run uvicorn main_to_understand:app --port 9998 -reload
# http://127.0.0.1:9998/docs ------> Open swagger page, port should be right.


## MCP Server 