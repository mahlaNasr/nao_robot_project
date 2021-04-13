#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################################
# Author: Mahla Nasrollahi
# Last Updated: 25/03/2021
# File Name: nao_scan.py
#
# This class scans a QR code and checks if it is decodable or not. If it
# is decodable, the program stores the QR code information into a json file.
############################################################################

#--------------------------------------------------------------------------
# Importing necessary packages
#--------------------------------------------------------------------------
from pyzbar import pyzbar
import cv2 as cv
import json
import os


class NaoScanBarcode:
    def __init__(self):
        # Json file path and direction
        self.json_filename= 'json_qrdata'
        self.json_path = "{}.json".format(self.json_filename)

    #---------------------------------------------------------------------------
    # Open a window frame for the camera to scan QR code. Also, check if the
    # barcode is decodable or not.
    # Argument: None
    #---------------------------------------------------------------------------
    def scan_qrcode(self):
        # Record whether a QR code is decodable or not in lists
        self.decode_result = []

        try:
            # Initialise camera video
            vidStream = cv.VideoCapture(0, cv.CAP_DSHOW)
            vidStream.set(3,640)
            vidStream.set(4,480)
        except:
            print ("problem opening input stream")
            sys.exit(1)

        print "[INFO] Scanning QR code..."
        scanned = True
        while(scanned):
            success, image = vidStream.read()
            # Decode if possible
            barcodes = pyzbar.decode(image)

            # if no barcode information is detected
            if not barcodes :
                # Remove old json files
                if os.path.exists(self.json_path):
                    os.remove(self.json_path)
                else:
                    pass
                self.decode_result.append("Decoding Failed")
            else:
                pass

            # loop over the detected barcodes
            for barcode in barcodes:
                barcodeData = barcode.data.decode("utf-8")
                # Save barcode information insidea new json file
                with open(self.json_path, 'w') as scanned_data:
                    scanned_data.write(barcodeData)
                self.decode_result.append("Decoding Passed")
                scanned = False

            # Show scanning window
            cv.imshow('Show QR Code Here',image)
            cv.waitKey(1)

    #---------------------------------------------------------------------------
    # Check if the detected barcode is clear and readable by the camera. If
    # it is clear enough, its values is saved as passed. Otherwise, it is failed.
    # Argument: None
    #---------------------------------------------------------------------------
    def check_readable(self):
        for i in range(len(self.decode_result)):
            if self.decode_result[i] == "Decoding Passed":
                return True
            else:
                return False

    #---------------------------------------------------------------------------
    # Check if a json file exists first. If file exists, find all parameters
    # and data and save save them.
    # Argument: Parameter, type=string, it is the value of the key elements
    # in the json file
    #---------------------------------------------------------------------------
    def json_data(self, parameter):
        if os.path.exists(self.json_path):
            # Read existing json file
            with open(self.json_path, 'r' ) as jfile:
                data = json.load(jfile)

            # Loop through all the data inside json file and return them
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
                if parameter == "Language" or parameter == "language":
                    language = data["Language"]
                    return language
        else:
            print("[INFO] Barcode is not clear and no json file found")
            return None

    #---------------------------------------------------------------------------
    # Check if a json file exists first. If file exists, delete it along with
    # information inside it when a visitor finishes his/her talk session.
    # Argument: None
    #---------------------------------------------------------------------------
    def remove_json(self):
        if os.path.exists(self.json_path):
            os.remove(self.json_path)
        else:
            pass
