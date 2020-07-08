FROM python:3-onbuild

# Copying source in current directory into the image
# python:3-onbuild expects the source in /usr/src/app
RUN pip install -r requirements.txt
COPY . /usr/src/app
CMD ["python", "app.py"]
