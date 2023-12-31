# using the model on our data

# import libraries
from fastai.vision.all import (
    load_learner,
    PILImage,
)

learn = load_learner("model.pkl")

is_bird, _, probs = learn.predict(PILImage.create("bird.jpg"))
print(f"Probability it's a bird: {probs[0]:.4f}")
print(f"This is a {is_bird}.")

is_bird, _, probs = learn.predict(PILImage.create("forest.jpg"))
print(f"Probability it's a bird: {probs[0]:.4f}")
print(f"This is a {is_bird}.")
