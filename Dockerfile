FROM python:3.10

ENV SECRET_KEY=hdhgasjkienxc

WORKDIR /code

COPY ./entrypoint.sh /code/entrypoint.sh

COPY ./configure_app.py /code/configure_app.py

COPY ./database /code/database

RUN chmod +x entrypoint.sh

COPY ./requirements-prod.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

ENTRYPOINT /code/entrypoint.sh