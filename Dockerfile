FROM python:3.8-slim 

WORKDIR /app

RUN pip install --upgrade pip && pip install pipenv flask flask_restful requests

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv install --deploy --ignore-pipfile

COPY . .
RUN chmod +x ./main.sh

CMD [ "main.sh" ]
