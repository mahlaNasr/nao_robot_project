

<!-- PROJECT LOGO -->

<p align="center">
  <a href="https://github.com/mahlaNasr/nao_robot_project">
    <img src="nao_logo.png" alt="Logo" width="150" height="150">
  </a>
  <h3 align="center">NGX NAO Robot Project</h3>
  <p align="center">
    Final Year 3 BEng Individual Project
  </p>
</p>


<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li>
      <a href="#a-booking-web-page-folder">Booking Web Page folder</a>
      <ul>
        <li><a href="#demo-video-for-section-a">Demo Video for Section (a)</a></li>
      </ul>
    </li>
    <li>
      <a href="#b-scripts-english-folder">Scripts (English) folder</a>
      <ul>
        <li><a href="#demo-video-for-section-b">Demo Video for Section (b)</a></li>
      </ul>
    </li>
    <li>
      <a href="#c-scripts-french-folder">Scripts (French) folder</a>
      <ul>
        <li><a href="#demo-video-for-section-c">Demo Video for Section (c)</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started-for-virtual-nao">Getting Started for Virtual NAO</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#d-analysing-qr-codes-folder">Analysing Qr Codes folder</a></li>
    <li>
      <a href="#getting-started-for-analysing-qr-codes">Getting Started for Analysing QR Codes</a></li> 
      <ul>
        <li><a href="#prerequisites-1">Prerequisites</a></li>
        <li><a href="#installation-1">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

 Getting Started for Virtual NAO 

<!-- ABOUT THE PROJECT -->
## About The Project

This project proposes a system where humanoid robot, NAO, uses scanned QR code ticket information to form simple conversations with the visitors at the [**the National Portrait Gallery**](https://www.nationalgallery.org.uk/whats-on/national-gallery-x) art museum.

There are three folders that are in this repository:
* (a) booking_website
* (b) scripts_enu
* (c) scripts_frf
* (d) analyse_qrcode



### [(a)](https://github.com/mahlaNasr/nao_robot_project/tree/master/booking_website) Booking Web Page folder
To book a ticket for one of the gallery's events, I made a webpage where it generates a QR code with all the input parameters that you enter. This QR code then gets scanned by the robot to read the JSON file information inside the code. To run the scripts in this folder, [XAMPP](https://www.apachefriends.org/index.html) needs to be set up to run a local server. Write the IP address of your local server along with the directory of where the scripts are saved in the search bar of any search engine. In my case it was: `http://192.168.64.2/booking_website/index.php`.
Make sure that this folder (a) gets saved inside `htdocs` folder in XAMPP.


#### Demo Video for Section (a) 
[Booking a Ticket for National Gallery Museum Demo](https://youtu.be/mtQ_YTJ_wK8)


### [(b)](https://github.com/mahlaNasr/nao_robot_project/tree/master/scripts_enu) Scripts (English) folder 
This folder consists of all the codes that were written for the robot to scan QR codes and interact with the visitors.
To run the whole system, write 
    `
    python nao_project.py
    `
command in the terminal. A few libraries are needed to be installed in order to run the scripts which are listed below. 
Make sure that you are in the same directory as the python file (i.e. `nao_robot_project/scripts_enu`).

#### Demo Video for Section (b)
[Retrieving QR code Data to Form Personalised Speeches](https://youtu.be/nI8LN00qGhE)


### [(c)](https://github.com/mahlaNasr/nao_robot_project/tree/master/scripts_frf) Scripts (French) folder
These sets of scripts were added to show future possibilities that can be done with the built system. NAO retrieves  the language parameter within a pre-generated JSON file from a pre-scanned QR code that is inside the folder. It then asks the visitors to ask if NAO can speak in French or not. This program is very small and it is recorded below to show how it works. To run this program write
    `
    python nao_french_project.py
    `
command in the terminal. Make sure that you are in the same directory as the python file (i.e. `nao_robot_project/scripts_frf`).

#### Demo Video for Section (c)
[Personalised Speech Based on the 'Language' Parameter of a QR Code](https://youtu.be/HNX2OmFoa7k)



<!-- GETTING STARTED -->
## Getting Started for Virtual NAO 

To be able to run folders (2) and (3), follow these steps below to set up the neccessary applications. 

#### Prerequisites 

The older version of python is needed in order to run the software.
1. Get Python 2.7 from [python official website](https://www.python.org/about/)
2. Get Choregraphe installed from [ALDebaran documentations](http://doc.aldebaran.com/2-4/software/choregraphe/installing.html)
3. Get python SDK from [ALDebaran documentations](http://doc.aldebaran.com/2-4/dev/python/install_guide.html)

#### Installation 

A few libraries are also needed.

1. Install Computer Vision tools for OpenCV
    ```sh
    pip install opencv-python
    ```
2. If your python package does not have TKinter pre-installed for the Graphical User Interface (GUI), run this command to install for python 2.7 on Linux
   ```sh
   sudo apt-get install python-tk
   ```
3. Install pyzbar for reading barcodes using zbar library
   ```sh
   pip install pyzbar
   ```
Other libraries such as JSON, time, os, argparse, random and qi were imported.




### [(d)](https://github.com/mahlaNasr/nao_robot_project/tree/master/analyse_qrcode) Analysing Qr Codes folder 
This folder was added to show how the images were analysed and decoded using a few other libraries. The results were then stored onto an Excel sheet.

There was two ways:
1. [Real-time scanning](https://github.com/mahlaNasr/nao_robot_project/tree/master/analyse_qrcode/take_process_img) -> `take_process_img` folder
2. [Analysing images that are already taken](https://github.com/mahlaNasr/nao_robot_project/tree/master/analyse_qrcode/opencv_image_analyse) -> `opencv_image_analyse` folder
 
 

<!-- GETTING STARTED -->
## Getting Started for Analysing QR Codes

#### Prerequisites 
These files in this folder were run and tested using python 3.8. 
1. Get Python 3.8 from [python official website](https://www.python.org/about/)


#### Installation 
Extra libraries are needed to run this section of scripts as well as comparing the obtained results of images from Excel file.

1. Install Anaconda which comes with a lot of pre-installed libraries. Instruction found in [Anadonda Documentations](https://docs.continuum.io/anaconda/install/).

  Alternative method can be found here [through miniconda](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).
2. We also need ZBar and OpenCV tools here as well.




<!-- CONTRIBUTING -->
## Contributing 
This project was a contributed to help the National Gallery in order to make their ticket scan system automated through using a humanoid robot, NAO.



<!-- LICENSE -->
## License 

For distribution, please reference my [code](https://github.com/mahlaNasr/nao_robot_project) and cite my [report](https://drive.google.com/file/d/1tI2FzyNm9XHmyPpshxGPi-ilAd05Y5fe/view?usp=sharing) :)





<!-- CONTACT -->
## Contact 

Links to: 
* [My LinkedIn](https://www.linkedin.com/in/mahla-nasrollahi-0bb679163)
* [My GitHub](https://github.com/mahlaNasr/) 
* [NAO Project](https://github.com/mahlaNasr/nao_robot_project)
* [YouTube Videos for Sections (a), (b) and (c)](https://www.youtube.com/watch?v=nI8LN00qGhE&list=PL7HjjvER6Zg1OaPwt4OcNtcNmq3_RAi9l&index=1&ab_channel=MahlaNasrollahi)
* Project Presentation (coming soon!)


