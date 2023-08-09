# training the model on our data

# import libraries
from fastai.vision.all import (
    Path,
    DataBlock,
    ImageBlock,
    CategoryBlock,
    get_image_files,
    RandomSplitter,
    parent_label,
    Resize,
    vision_learner,
    resnet18,
    error_rate,
)

path = Path("bird_or_not")

dls = DataBlock(
    blocks=(ImageBlock, CategoryBlock),
    get_items=get_image_files,
    splitter=RandomSplitter(valid_pct=0.2, seed=42),
    get_y=parent_label,
    item_tfms=[Resize(192, method="squish")],
).dataloaders(path, bs=32)

learn = vision_learner(dls, resnet18, metrics=error_rate)
learn.fine_tune(3)

# export the model as a pkl file
learn.export(fname="model.pkl")
