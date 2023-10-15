# import libraries
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastai.vision.all import *
import io


learn = load_learner("model/model.pkl")

app = FastAPI(title="app")
api = FastAPI(title="api")


@api.post("/")
async def create_upload_file(file: UploadFile):
    print(f"looking good {file.filename} and {file.size}")
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    # XXX: Fix this:
    # TypeError: Image.frombytes() missing 1 required positional argument: 'data'
    is_bird, _, probs = learn.predict(PILImage.frombytes(img))  # <--- img is None?
    return {"probability": probs.tolist()[0], "answer": is_bird}


app.mount("/classify", api)
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")
