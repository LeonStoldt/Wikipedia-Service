FROM python:3-onbuild
COPY . /usr/src/app
EXPOSE 8080
CMD ["python", "wikipedia.py"]