FROM python:3.9.6-slim-buster as base 

RUN apt-get update \ 
    && apt-get -y install make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
    
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

COPY . /app

WORKDIR /app 

ENV PATH "$PATH:/root/.poetry/bin"

RUN poetry install 

EXPOSE 5000

FROM base as development 
CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]


FROM base as production 
ENV FLASK_ENV=production
CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:5000", "todo_app.app:create_app()"]