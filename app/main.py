import os
import shutil

from fastapi import FastAPI, File, Request, UploadFile
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request
    })

@app.post("/upload_file")
async def upload_file(my_file: UploadFile):
    upload_dir = open(os.path.join("./files", my_file.filename), "wb+")
    shutil.copyfileobj(my_file.file, upload_dir)
    upload_dir.close()
    return {"filename": my_file.filename}
    