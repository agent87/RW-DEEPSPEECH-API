<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
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


There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!



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

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

It is highly recomended to run the application in docker container to avoid dependency erros but it also possible to run it without docker
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
2. create an environment file named as ".env" and paste the variables
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
4. Start the docker containers
   ```sh
   docker compose up
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage



<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add database
- [ ] Add Authentication
- [ ] Additional testing
- [ ] 

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

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

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Arnaud Kayonga - [@kayarn_](https://twitter.com/kayarn) - arnauldkayonga1@gmail.com

Project Link: [https://github.com/agent87/RW-DEEPSPEECH-API](https://github.com/agent87/RW-DEEPSPEECH-API)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

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

