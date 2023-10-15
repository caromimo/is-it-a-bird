# import libraries
from typing import Annotated
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastai.vision.all import *
import io


from fastapi.middleware.cors import CORSMiddleware

learn = load_learner("model.pkl")

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
)


@app.post("/")
async def create_upload_file(file: UploadFile):
    print(f"looking good {file.filename} and {file.size}")
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    # XXX: Fix this:
    # TypeError: Image.frombytes() missing 1 required positional argument: 'data'
    is_bird, _, probs = learn.predict(PILImage.frombytes(img))  # <--- img is None?
    return {"probability": probs.tolist()[0], "answer": is_bird}


@app.get("/")
async def root():
    is_bird, _, probs = learn.predict(PILImage.create("forest.jpg"))
    return {"probability": probs.tolist()[0], "answer": is_bird}
