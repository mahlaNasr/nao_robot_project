# nao_robot_project


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
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/mahlaNasr/nao_robot_project">
    <img src="nao_logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">NAO Robot Project</h3>

  <p align="center">
    Final Year 3 BEng Individual Project
    <br />
  </p>
</p>




<!-- ABOUT THE PROJECT -->
## About The Project

This project proposes a system where humanoid robot, NAO, is used to scan QR code tickets in the National Gallery art museum.

There are two folders that are in this repository:
* nao_scan_qrcode
* scripts for analysing qrcodes


### Nao Scan Qr Code folder

This folder consists of all the codes that were written for the robot to scan QR codes and interact with the visiotrs.
To run the whole system, execute `nao_project.py` python file. A few libraries are needed to be installed in order to run the scripts.




<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The older version of python is needed in order to run the software.
1. Get Python 2.7 from [https://www.python.org/about/](python official website)
2. Get Choregraphe installed from [http://doc.aldebaran.com/2-4/software/choregraphe/installing.html](ALDebaran documentations)
3. Get python SDK from [http://doc.aldebaran.com/2-4/dev/python/install_guide.html](ALDebaran documentations)



### Installation

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




### Scripts for Analysing Qr Codes folder

This folder was added to show how the images were analysed and decoded using a few other libraries. The results were then stored onto an Excel sheet.

There was two ways:
1. Real-time scanning -> `take_process_img` folder
2. Analysing images that are already taken -> `opencv_image_analyse` folder
 


### Prerequisites

These files in this folder were run and tested using python 3.8. 
1. Get Python 3.8 from [https://www.python.org/about/](python official website)



### Installation

Extra libraries are needed to run this section of scripts as well as comparing the obtained results of images from Excel file.

1. Install Anaconda which comes with a lot of pre-installed libraries. Instruction found in [https://docs.continuum.io/anaconda/install/](Anadonda Documentations)

  Alternative method can be found here [https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html](through miniconda).
2. We also need ZBar and OpenCV tools here as well.




<!-- CONTRIBUTING -->
## Contributing

This project was a contributed to help the National Gallery in order to make their ticket scan system automated through using a humanoid robot, NAO.



<!-- LICENSE -->
## License

For distribution, please reference my code :)


<!-- CONTACT -->
## Contact

My LinkedIn - [https://www.linkedin.com/in/mahla-nasrollahi-0bb679163/](Link to LinkedIn)

Project Link: [https://github.com/mahlaNasr/nao_robot_project](Link to NAO robot project github)


