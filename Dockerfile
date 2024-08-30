#Use official Python base image
FROM python:3.9-slim

#set working dir
WORKDIR /app

#Copy app and requirements
COPY src/ /app/

#Install required packages from requirements
RUN pip install --no-cache-dir -r requirements.txt

#Expose port from container 
EXPOSE 8080

#Run app.py when container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]