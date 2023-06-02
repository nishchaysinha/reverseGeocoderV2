#write a dockerfile to create a docker image on alpine linux that runs the main.py file

FROM alpine:latest
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip
WORKDIR /app
COPY . /app
RUN pip3 --no-cache-dir install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]

