FROM python:3.12-slim

WORKDIR /tasks

COPY requirements.txt /tasks/

RUN python -m pip install --no-cache --upgrade -r requirements.txt

COPY . /tasks

CMD [ "python", "-m", "pytest" ]