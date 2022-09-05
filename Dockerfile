FROM python:3.8-slim 

WORKDIR /app

RUN pip install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install flask flask_restful requests

RUN pipenv install --deploy --ignore-pipfile

COPY . .

CMD [ "python", "./main.py" ]
