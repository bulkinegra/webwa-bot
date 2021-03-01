# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# COPY requirements to /app dir
COPY /webwa-master/ /app/api-setup/
COPY /app/ /app/

# Install any needed packages specified in base.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r api-setup/requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.python.org pygsheets
RUN cd api-setup; python setup.py install
RUN rm -r api-setup
