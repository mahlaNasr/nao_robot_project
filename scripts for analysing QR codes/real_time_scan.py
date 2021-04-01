#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

##########################################################################
# Author: Mahla Nasrollahi
# Last Updated: 28/03/2021
# File Name: quick_scan.py
#
# This script scans QR code in real-time and creats a json file with the
# decoded data.
############################################################################


# Imprting related libraries
from pyzbar.pyzbar import decode, pyzbar
from pyzbar import pyzbar
import numpy as np
import cv2 as cv
import json
import os

json_filename= 'json_qrdata'
json_path = "{}.json".format(json_filename)

#image = cv2.imread('1.png')
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

scanned = True
print('Please scan your QR code...')
while(scanned):
    success, image = cap.read()
    # find the barcodes in the image and decode if possible
    barcodes = pyzbar.decode(image)

    # if no barcode is detected
    if not barcodes :
        if os.path.exists(json_path):
            os.remove(json_path)
        else:
            pass
    else:
        pass

    # loop over the detected barcodes
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        with open(json_path, 'w') as scanned_data:
            scanned_data.write(barcodeData)

        # Green colour
        myColor = (0, 255, 0)
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv.polylines(image,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv.putText(image,"myOutput",(pts2[0],pts2[1]),cv.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)

        print('scanned')
        ##To stop the real-time streming when a barcode is presented, uncomment
        ## the following command
        # scanned = False

    cv.imshow('Show QR Code Here',image)
    cv.waitKey(1)


# Create a Json file of the scanned barcode
def json_data(parameter):
    if os.path.exists(json_path):
        with open(json_path, 'r') as jfile:
            data = json.load(jfile)
            for item in data:
                if parameter == "Name" or parameter == "name":
                    name = data["Name"]
                    return name
                if parameter == "Ticket_type" or parameter == "ticket_type" or parameter == "ticket_Type":
                    tick_type = data["Ticket_type"]
                    return tick_type
                if parameter == "Interest" or parameter == "interest":
                    interest = data["Interest"]
                    return interest
    else:
        print("[INFO] Barcode is not clear")
        return None
