FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

Run mkdir /code
workdir /code

Add App/requirements.txt /code/

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000