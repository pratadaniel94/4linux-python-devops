FROM python:3.10
WORKDIR /app
COPY . /app

# Installs poetry and pip
RUN pip install --upgrade pip && \
    pip install poetry

# Installs projects dependencies as a separate layer
RUN poetry export -f requirements.txt -o requirements.txt && \
    pip uninstall --yes poetry && \
    pip install --require-hashes -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]