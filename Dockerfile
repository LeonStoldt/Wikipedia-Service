FROM python:3-onbuild
COPY ./service /usr/src/app
CMD ["python", "wikipedia.py"]
