# Is it a bird?

This project is about building a machine learning model to classify pictures as bird or not-bird following the [fastai tutorial](https://youtu.be/8SF_h3xF3cE) and wrapping the model in an API. This project uses [PDM](https://pdm.fming.dev/latest/). 

## How to run the API

Clone this directory and: 

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
