FROM python:3.7
COPY requirements.txt /tmp
COPY arxiv_db_ai.py /tmp
COPY subject_ai.csv /tmp
WORKDIR /tmp
RUN pip3 install -r requirements.txt
CMD ["python3","arxiv_db_ai.py"]