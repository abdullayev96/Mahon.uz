# FROM python:3.9
#
# WORKDIR /app
#
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
#
# COPY . .
#
#
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]
#
#



FROM python:3.11


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
