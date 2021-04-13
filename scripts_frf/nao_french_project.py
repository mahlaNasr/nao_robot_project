#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################################
# Author: Mahla Nasrollahi
# Last Updated: 06/04/2021
# File Name: nao_project.py
#
# This program with the help of other classes, asks visitors to scan their
# QR code. Based on whether their barcode is valid or not, the robot
# extracts its information and gives out personalised responses.
############################################################################


#--------------------------------------------------------------------------
# Importing necessary packages and files
#--------------------------------------------------------------------------
import nao_scan_lang as scan
from Tkinter import *
import Tkinter as tk
import cv2 as cv
import argparse
import random
import time
import json
import os
import qi




class NaoProject():
    def __init__(self):
        # Text To Speech (tts) service
        self.tts = session.service('ALTextToSpeech')
        # Calling and creating objects for external classes
        self.scan_code = scan.NaoScanBarcode()

         # Getting the service ALDialog
        self.ALDialog = session.service("ALDialog")
        self.ALDialog.setLanguage("French")

    #---------------------------------------------------------------------------
    # This is the main function of this class where the robot interacts with
    # the visitors and asks them to scan their QR code. It also checks the
    # parameters that are inside the QR code and gives out specific feedback
    # regardng the inputs.
    # Argument: None
    #---------------------------------------------------------------------------
    def nao_dialog(self):
        scanning = True
        while scanning:
            # Get visitor's name
            return_name = self.scan_code.json_data("Name")
            # Greet users to start the system
            hello = ["hi", "hello", "hey", "greetings"]
            self.tts.say(random.choice(hello) + " " + return_name)

            # Get specific values from the json file
            return_language = self.scan_code.json_data("Language")

            # Check if NAO can speak the language that is picked
            if return_language == "French":
                self.tts.say("You can speak " + return_language + ". Very cool!!")
            else:
                self.tts.say("I havn't learnt that language yet. Sorry... )")

            # >>> Load the french talk dialogs
            try:
                french_content = self.ALDialog.loadTopic(os.path.abspath("french_talk_frf.top"))
            except:
                french_content = "french_talk"
            print "[INFO] French loaded topics:", self.ALDialog.getLoadedTopics("French")

            # Activating the loaded topic
            self.ALDialog.activateTopic(french_content)
            self.ALDialog.subscribe('visitor_language')

            try:
                self.ALDialog.forceOutput()
                # Enable the GUI button to move on to next visitor
                self.next_visitor()
                print "[INFO] Waiting for next visitor..."
            finally:
                # stopping the dialog engine
                self.ALDialog.unsubscribe('visitor_language')
                # Deactivating topic
                self.ALDialog.deactivateTopic(french_content)
                self.ALDialog.unloadTopic(french_content)


            # Keep Running the Loop
            scanning = True


    #---------------------------------------------------------------------------
    # GUI Button to start conversation with the next visitor
    # Agument: None
    #---------------------------------------------------------------------------
    def next_visitor(self):
        def next():
            self.window.destroy()
        self.gui()

        self.window.title("Speak Again")
        label = tk.Label(self.window,fg="white", bg='#4a536b',
                        text="Press Start To Talk To NAO",
                        font = ('calibri', 12, 'bold'),
                        borderwidth = '3')
        # start button
        next_person = tk.Button(self.window, text ="Start",
                                command = next, bg='#cbf6db',
                                height=2, width=30,
                                font = ('calibri', 10, 'bold'),
                                borderwidth = '3')
        # To be able to exit the whole system,
        quit_btn = tk.Button(self.window, text ="Quit",
                                command = quit, bg='#CD5C5C',
                                height=2, width=30,
                                font = ('calibri', 10, 'bold'),
                                borderwidth = '3')

        # Load 10 seconds after conversation with NAO is done.
        wait_time = 5000
        self.window.after(wait_time,
                          label.grid(row=0, column=5, padx=40, pady=50))
        self.window.after(wait_time,
                          next_person.grid(row=1, column=5, padx=40, pady=10))
        self.window.after(wait_time,
                          quit_btn.grid(row=2, column=5, padx=40, pady=10))
        mainloop()



    #---------------------------------------------------------------------------
    # Initialising Graphical User Interface(GUI) for scanning qr code and moving
    # on to next customer using Tkinter
    # Argument: None
    #---------------------------------------------------------------------------
    def gui(self):
        # For GUI input buttons create a window
        self.window = Tk()
        self.window.geometry("300x400")
        self.window.configure(background='#4a536b')

#---------------------------------------------------------------------------
# Main function to start module sessions
# Agument: Session
#---------------------------------------------------------------------------
def main(session):
    # Creating an object of NaoProject class
    main_obj = NaoProject()
    # Calling main function of the class
    main_obj.nao_dialog()

if __name__ == "__main__":
    # Connecting to the Choregraphe simulated robot (from Robotic Platform)
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="desktop-6d4cqe5.local",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("\nCan't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.\n".format(args.ip, args.port))
        sys.exit(1)
    main(session)
