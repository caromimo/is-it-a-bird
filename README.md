# Is it a bird?

Build a machine learning model to classify pictures as bird or not bird (following tutorial from fastai) and expose through it via an API.

## How to run the API

This uses [PDM](https://pdm.fming.dev/latest/). Clone this directory and: 

```bash
# this installs all the packages in pdm.lock
pdm install
# this starts the API which uses the model to classify images as bird or not-bird
pdm start
```
Connect to the API on localhost:8000

## How to get data and train a model

```bash
# this installs all the packages in pdm.lock
pdm install
# this downloads the data from the internet
pdm data
# this trains your model on the data and exports it as model.pkl
pdm train
```
