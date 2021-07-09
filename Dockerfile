FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8-slim
# ARG FUNCTION_DIR="/app"

COPY . /app

WORKDIR /app

# RUN mkdir -p ${FUNCTION_DIR}

# COPY src ${FUNCTION_DIR}/go

# COPY main.py ${FUNCTION_DIR}

# COPY requirements.txt ${FUNCTION_DIR}

# COPY settings.py ${FUNCTION_DIR}

RUN pip3 install -r requirements.txt

EXPOSE 80

# CMD ["cd", "app"]

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]