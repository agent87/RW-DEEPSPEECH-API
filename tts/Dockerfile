FROM python:3.10.9

#Create and make the API folder the working directory
WORKDIR /api

#Copy the requirments and packages file
COPY requirements.txt .

#upgrade pip
RUN pip install --no-cache-dir --upgrade pip

#Install the cython package
RUN pip install --no-cache-dir cython

#Install all the dependencies
RUN pip install --no-cache-dir -r requirements.txt  

#Install Google Protobuf
RUN pip install protobuf==4.21.1

#Expose the port
EXPOSE 8000

#Run the app
CMD ["uvicorn", "api:api", "--host=0.0.0.0", "--port=8000", "--reload"]

