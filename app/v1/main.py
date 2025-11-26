from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pathlib

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    html_file = pathlib.Path(__file__).parent / "index.html"
    return html_file.read_text()
