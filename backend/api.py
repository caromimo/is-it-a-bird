# import libraries
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastai.vision.all import (
    load_learner,
    PILImage,
)
from fastapi.middleware.cors import CORSMiddleware

learn = load_learner("model.pkl")

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


@app.get("/")
async def root():
    is_bird, _, probs = learn.predict(PILImage.create("forest.jpg"))
    return {"probability": probs.tolist()[0], "answer": is_bird}
