<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project  a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS  -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/agent87/RW-DEEPSPEECH-API">
  </a>

  <h3 align="center">RW DEEPSPEECH API</h3>

  <p align="center">
    A Kinyarwanda based end to end deepspeech with speech to text and text to speech services!
    <br />
    <a href="https://github.com/agent87/RW-DEEPSPEECH-API"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/agent87/RW-DEEPSPEECH-API">View Demo</a>
    ·
    <a href="https://github.com/agent87/RW-DEEPSPEECH-API/issues">Report Bug</a>
    ·
    <a href="https://github.com/agent87/RW-DEEPSPEECH-API/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->

  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>




<!-- ABOUT THE PROJECT -->
## About The Project

Welcome to the Kinyarwanda DeepSpeech API repository! This comprehensive guide provides an in-depth exploration of this powerful end-to-end solution for speech processing in Kinyarwanda. With our DeepSpeech API, you can effortlessly convert spoken Kinyarwanda into text and transform text into natural-sounding Kinyarwanda speech.
Introduction

In today's digital age, seamless communication across diverse languages is crucial. Our DeepSpeech API for Kinyarwanda bridges language barriers by offering robust speech-to-text and text-to-speech capabilities tailored specifically for the Kinyarwanda language. Whether you are building interactive voice applications, transcribing audio content, or enhancing accessibility features, our API empowers you to achieve your goals with ease.
Key Features

    Accurate Speech-to-Text Conversion: Leverage our advanced deep learning models to accurately transcribe spoken Kinyarwanda into written text. Our models have been trained on extensive Kinyarwanda speech datasets, ensuring high accuracy and reliability.

    Natural Text-to-Speech Synthesis: Generate lifelike Kinyarwanda speech from textual input. Our text-to-speech engine produces natural intonation, rhythm, and pronunciation, creating a seamless and engaging user experience.

    End-to-End Processing: Perform both speech-to-text and text-to-speech operations within a single API, streamlining your workflow and saving development time.

    Customization: Fine-tune our models to adapt them to specific accents, dialects, or domains, ensuring optimal performance for your unique use case.

    Scalability: Our API is designed to handle a high volume of requests, making it suitable for applications ranging from small-scale projects to large-scale enterprise solutions.



### [Speech to Text Model by Nvidia](https://huggingface.co/nvidia/stt_rw_conformer_ctc_large)
This model transcribes speech into lowercase Latin alphabet including spaces, and apostroph, and is trained on around 2000 hours of Kinyarwanda speech data by Nvidia. It is a non-autoregressive "large" variant of Conformer, with around 120 million parameters. See the [model architecture](https://huggingface.co/nvidia/stt_rw_conformer_ctc_large#model-architecture) and NeMo documentation for complete architecture details. 

### [Text to Speech Model by Digital Umuganda](https://huggingface.co/DigitalUmuganda/Kinyarwanda_YourTTS)
This model is an end-to-end deep-learning-based Kinyarwanda Text-to-Speech (TTS) developed by Digital Umuganda. Due to its zero-shot learning capabilities, new voices can be introduced with 1min speech. The model was trained using the Coqui's TTS library, and the YourTTS[1] architecture. It was trained on 67 hours of Kinyarwanda bible data, for 100 epochs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
* [![WebSockets](https://img.shields.io/badge/WebSockets-4DC0B5?style=for-the-badge&logo=websocket&logoColor=white)](https://en.wikipedia.org/wiki/WebSocket)
* [![Transformers](https://img.shields.io/badge/Transformers-FFA100?style=for-the-badge&logo=huggingface&logoColor=white)](https://huggingface.co/transformers/)
* [![TTS](https://img.shields.io/badge/TTS-000000?style=for-the-badge&logo=readthedocs&logoColor=white)](https://tts.readthedocs.io/en/latest/index.html)
* [![Uvicorn](https://img.shields.io/badge/Uvicorn-3F3F3F?style=for-the-badge&logo=fastapi&logoColor=white)](https://www.uvicorn.org/)
* [![Nemo](https://img.shields.io/badge/Nemo-2590F7?style=for-the-badge&logo=apachenemo&logoColor=white)](https://github.com/nvidia/nemo)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is a simpple implmentation requiring few lines of code to run.

### Prerequisites

It is highly recomended to run the application in docker container to avoid dependency errors but it also possible to run it without docker
In terms of specifications needed

* With Docker:
    - DISK SPACE >= 10GB
    - RAM >= 2GB
* Without Docker:
    - RAM >= 2GB free/spare


### Installation with docker

Follow the steps bellow to set up your project on server/machine running docker.


1. Clone the repo
   ```sh
   git clone https://github.com/agent87/RW-DEEPSPEECH-API.git
   ```
2. Pull the large files with git lfs. Make sure you have git lfs installed or refer to [git lfs](https://git-lfs.github.com/) for installation instructions
   ```sh
   git lfs pull
   ```
2. create an environment file named as ".env" with "touch .env" and paste the variables. Make sure the file is in the root directory of the project
    ```sh
    MONGO_USERNAME=myuser
    MONGO_PASSWORD=mypassword
    MONGO_HOST=localhost
    MONGO_PORT=27017
    MONGO_DATABASE=feedback
    MONGO_COLLECTION=logs
    ```
    NOTE: For security purposes, make sure to change the variables above!
3. build the docker image
   ```sh
   docker compose build
   ```
   Note: if you have an earlier docker version use "docker-compose build"
4. Start the docker containers and let the magic begin
   ```sh
   docker compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

If you happen not to have speciazed hardware(GPU) you can run the application on Google Colab. Use the following link to open the notebook and follow the instructions in the notebook to run the application.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RBi0M27eMuRq9InGDpK9nZlV0kem4iCt?usp=sharing)

### Speech to Text (STT) usage
```sh
curl -X POST "http://server_url/stt" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "file=@/path/to/audio/file"
```

### Text to Speech (TTS) usage
```sh
curl -X POST "http://server_url/tts" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"text\":\"string\"}"
``` 



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add database
- [ ] Add Authentication
- [ ] Testing
- [ ] CI/CD Setup tutorial
- [ ] Automated audio conversion
- [ ] OpenAPI Documentation/ Swagger
- [ ] Usage Feedback incorporation into the readme.MD

See the [open issues](https://github.com/agent87/RW-DEEPSPEECH-API/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arnaud Kayonga - [@kayarn](https://www.kayarn.co) - arnauldkayonga1@gmail.com

Project Link: [https://github.com/agent87/RW-DEEPSPEECH-API](https://github.com/agent87/RW-DEEPSPEECH-API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Nvidia STT RW Conformer CTC Large](https://huggingface.co/nvidia/stt_rw_conformer_ctc_large)
* [Digital Umuganda Kinyarwanda YourTTS](https://huggingface.co/DigitalUmuganda/Kinyarwanda_YourTTS)
* [TTS Paper](https://arxiv.org/pdf/2112.02418.pdf)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/agent87/RW-DEEPSPEECH-API
[contributors-url]: https://github.com/agent87/RW-DEEPSPEECH-API/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/agent87/RW-DEEPSPEECH-API
[forks-url]: agent87/RW-DEEPSPEECH-API
[stars-shield]: https://img.shields.io/github/stars/agent87/RW-DEEPSPEECH-API
[stars-url]: agent87/RW-DEEPSPEECH-API
[issues-shield]: https://img.shields.io/github/issues/agent87/RW-DEEPSPEECH-API
[issues-url]: https://github.com/agent87/RW-DEEPSPEECH-API/issues

[Python.py]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=pythondotpy&logoColor=white
[Python-url]: https://python.com/

[FastAPI.py]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white
[FastAPI-url]: https://fastapi.tiangolo.com/

[Nemo.py]: https://img.shields.io/badge/Nemo-0077B5?style=for-the-badge&logo=Nemo&logoColor=white
[Nemo-url]: https://nemo.apache.org/

[Websocket.py]: https://img.shields.io/badge/Websocket-000000?style=for-the-badge&logo=websocket&logoColor=white
[Websocket-url]: https://websocket.org/

