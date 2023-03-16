FROM python:3.10.9

#Create and make the API folder the working directory
WORKDIR /api

#clone the kinyarwanda tts repo into the tts folder
RUN git clone https://huggingface.co/DigitalUmuganda/Kinyarwanda_YourTTS tts

#Copy all the files
COPY . . 

#create a temp folder to store the audio files
RUN mkdir tts/sounds

#Create a temp folder to store the audio files
RUN mkdir stt/sounds

#upgrade pip
RUN pip install --no-cache-dir --upgrade pip

#Install the cython package
RUN pip install --no-cache-dir cython

#Install all the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#install the package using apt with packages.txt file
RUN apt-get update && cat packages.txt | xargs apt-get install -y

#Expose the port
EXPOSE 8000

#Run the app
CMD ["uvicorn", "main:api", "--host=0.0.0.0", "--port=8000", "--reload"]

