

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




<br />


<!-- ABOUT THE PROJECT -->
## About The Project

This project proposes a system where humanoid robot, NAO, is used to scan QR code tickets in the National Gallery art museum.

There are two folders that are in this repository:
* nao_scan_qrcode
* scripts for analysing qrcodes

<br />
### Nao Scan Qr Code folder

This folder consists of all the codes that were written for the robot to scan QR codes and interact with the visiotrs.
To run the whole system, execute `nao_project.py` python file. A few libraries are needed to be installed in order to run the scripts.



<br />
<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The older version of python is needed in order to run the software.
1. Get Python 2.7 from [python official website](https://www.python.org/about/)
2. Get Choregraphe installed from [ALDebaran documentations](http://doc.aldebaran.com/2-4/software/choregraphe/installing.html)
3. Get python SDK from [ALDebaran documentations](http://doc.aldebaran.com/2-4/dev/python/install_guide.html)


<br />
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


<br />
<br />
### Scripts for Analysing Qr Codes folder

This folder was added to show how the images were analysed and decoded using a few other libraries. The results were then stored onto an Excel sheet.

There was two ways:
1. Real-time scanning -> `take_process_img` folder
2. Analysing images that are already taken -> `opencv_image_analyse` folder
 

<br />
### Prerequisites

These files in this folder were run and tested using python 3.8. 
1. Get Python 3.8 from [python official website](https://www.python.org/about/)


<br />
### Installation

Extra libraries are needed to run this section of scripts as well as comparing the obtained results of images from Excel file.

1. Install Anaconda which comes with a lot of pre-installed libraries. Instruction found in [Anadonda Documentations](https://docs.continuum.io/anaconda/install/).

  Alternative method can be found here [through miniconda](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html).
2. We also need ZBar and OpenCV tools here as well.



<br />
<!-- CONTRIBUTING -->
## Contributing

This project was a contributed to help the National Gallery in order to make their ticket scan system automated through using a humanoid robot, NAO.


<br />
<!-- LICENSE -->
## License

For distribution, please reference my code :)

<br />
<!-- CONTACT -->
## Contact

My LinkedIn - [Link to LinkedIn] (https://www.linkedin.com/in/mahla-nasrollahi-0bb679163)

Project Link:  [Link to NAO robot project github](https://github.com/mahlaNasr/nao_robot_project)


