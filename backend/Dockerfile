# build stage
FROM python:slim

# install PDM
RUN pip install pdm

# change the working directory
WORKDIR /app

# copy files
COPY . .

# install dependencies and project into the local packages directory
RUN pdm sync --prod --no-editable

# set command/entrypoint, adapt to fit your needs
CMD ["pdm", "start"]
