# import libraries
from fastapi import FastAPI
from fastai.vision.all import (
    load_learner,
    PILImage,
)

learn = load_learner("model.pkl")

app = FastAPI()


@app.get("/")
async def root():
    is_bird, _, probs = learn.predict(PILImage.create("forest.jpg"))
    return {"Probability it's a bird": probs.tolist()[0], "This is a ": is_bird}
