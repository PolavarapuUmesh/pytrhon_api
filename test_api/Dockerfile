# FROM python:3.10.12
# WORKDIR /app/api
# COPY requirements.txt /app/api/requirements.txt
# RUN pip install --upgrde pip
# RUN pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt]
# COPY . .
# Expose 8000
# CMD ["python3","test.py","uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10.12
WORKDIR /app/api
COPY requirements.txt /app/api/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/api/requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]
