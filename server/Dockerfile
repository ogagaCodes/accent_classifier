FROM public.ecr.aws/lambda/python:3.10

COPY requirements.txt   .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt
COPY index.py           .
COPY app/               app/
CMD [ "index.handler" ]
