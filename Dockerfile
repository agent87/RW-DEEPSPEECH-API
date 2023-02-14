FROM python:3.10.9

#Create and make the API folder the working directory
WORKDIR /API

#Copy all the files
COPY . . 

#clone the kinyarwanda tts repo into the tts folder
RUN git clone https://huggingface.co/DigitalUmuganda/Kinyarwanda_YourTTS tts

#create a temp folder to store the audio files
RUN mkdir tts/sounds

#Create a temp folder to store the audio files
RUN mkdir tts/sounds

#create temp folder to store audio files
RUN mkdir tmp

#upgrade pip
RUN pip install --upgrade pip

#Install the cython package
RUN pip install cython

#Install all the dependencies
RUN pip install -r requirements.txt

#Install python-multipart
RUN pip install python-multipart

#install the package using apt with packages.txt file
RUN apt-get update && cat packages.txt | xargs apt-get install -y

#Expose the port
EXPOSE 8000

#Run the app
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=8000"]

