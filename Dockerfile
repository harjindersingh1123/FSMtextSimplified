# Use an official Python runtime as a parent image
FROM python:3

#Add files
ADD src/app.py /
ADD src/templates/index.html /templates/index.html
ADD requirement.txt /

# Install any needed packages specified in requirements.txt
RUN pip install -r requirement.txt
#run command
ENTRYPOINT ["python", "app.py"]
