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
import nao_talk as talk
import nao_scan as scan
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
        self.dialogs = talk.NaoDialogs()

         # Getting the service ALDialog
        self.ALDialog = session.service("ALDialog")
        self.ALDialog.setLanguage("English")

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
            # Greet users to start the system
            hello = ["hi", "hello", "hey", "greetings"]
            self.tts.say(random.choice(hello))

            # >>> Load ticket scan dialogue
            try:
                qrcode_content = self.ALDialog.loadTopic(os.path.abspath("ticket_scan_enu.top"))
            except:
                qrcode_content = "ticket_scan"
            print "[INFO] English loaded topics:", self.ALDialog.getLoadedTopics("English")
            # Activating the loaded topic
            self.ALDialog.activateTopic(qrcode_content)
            self.ALDialog.subscribe('nao_conversation')

            try:
                # Enable GUI button for users to press for scanning
                def yes():
                    self.ALDialog.forceInput("have_ticket")
                    self.window.destroy()
                # User has no ticket
                def no():
                    self.ALDialog.forceInput("no_ticket")
                self.gui()
                self.window.title("Ticket Check")
                # Label of the box
                label = tk.Label(self.window, fg="white", bg='#4a536b',
                                text = "Do you have a ticket?",
                                font = ('calibri', 12, 'bold'),
                                borderwidth = '3')
                # Yes Button
                yes_btn = tk.Button(self.window,
                                    text ="Yes - Ready for Scanning QR Code",
                                    command = yes, bg='#9bc472',
                                    height=2, width=30,
                                    font = ('calibri', 10, 'bold'),
                                    borderwidth = '3')
                # No button
                no_btn = Button(self.window, text = "No",
                    		    command = no, bg='#ff9a8d',
                                height=2, width=30,
                                font = ('calibri', 10, 'bold'),
                                borderwidth = '3')

                # Load 4 seconds amount after conversation with NAO is done.
                wait_time = 4000
                self.window.after(wait_time,
                                  label.grid(row=0, column=5, padx=40, pady=50))
                self.window.after(wait_time,
                                  yes_btn.grid(row=1, column=5, padx=40, pady=10))
                self.window.after(wait_time,
                                  no_btn.grid(row=2, column=5, padx=40, pady=10))
                mainloop()

            finally:
                # stopping the dialog engine
                self.ALDialog.unsubscribe('nao_conversation')
                # Deactivating topic
                self.ALDialog.deactivateTopic(qrcode_content)
                self.ALDialog.unloadTopic(qrcode_content)

            try_again = ["Sorry I couldn't read that. Can I see your ticket again?",
                        "Let me scan again, try to keep your hand steady.",
                        "Please scan again, try to come closer to the camera.",
                        "That was blurry, please try again.",
                        "Please make sure that your brightness is about 50% then try again."]

            scan_again = True
            while(scan_again):
                # Check if barcode is clear and can be decoded
                self.scan_code.scan_qrcode()

                # Check of barcode is readable and clear
                if self.scan_code.check_readable() is True:
                    print "[INFO] Done scanning."
                    self.tts.say("Thank you. Your barcode has been successfully scanned.")
                    cv.destroyAllWindows()
                    #Get specific values from the json file
                    return_interest = self.scan_code.json_data("Interest")

                    # Getting random conversation strings from NaoDialogs class
                    interest_option = self.dialogs.intro_interest()
                    speech = self.dialogs.interest_talk(return_interest)

                    # Check if the QR code is a valid one
                    if return_interest == "Artist" or return_interest == "History" or return_interest == "Culture":
                        self.tts.say(interest_option + str(return_interest) + ". " + speech)
                        scan_again = False
                    else:
                        self.tts.say("Your barcode is invalid. Please try again.")
                        scan_again = True
                else:
                    self.tts.say(random.choice(try_again))
            # Close scanning window
            cv.destroyAllWindows()
            cv.waitKey(1)

            # Checking if a visitor has membership or not
            return_tickType = self.scan_code.json_data("ticket_type")

            # >>> Load the welcome talk dialogs
            self.tts.say("Anyway, now you know something about what you were interested in!")
            try:
                welcome_content = self.ALDialog.loadTopic(os.path.abspath("welcome_talk_enu.top"))
            except:
                welcome_content = "welcome_talk"
            print "[INFO] English loaded topics:", self.ALDialog.getLoadedTopics("English")

            # Activating the loaded topic
            self.ALDialog.activateTopic(welcome_content)
            self.ALDialog.subscribe('welcome_visitor')

            if return_tickType != "Member":
                self.ALDialog.forceInput("no_membership")
            else:
                self.ALDialog.forceInput("yes_membership")

            try:
                # Delete the JSON file and its information from system when
                # finished talking to a visitor
                self.scan_code.remove_json()
                # Enable the GUI button to move on to next visitor
                self.next_visitor()
                print "[INFO] Waiting for next visitor..."
            finally:
                # stopping the dialog engine
                self.ALDialog.unsubscribe('welcome_visitor')
                # Deactivating topic
                self.ALDialog.deactivateTopic(welcome_content)
                self.ALDialog.unloadTopic(welcome_content)

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

        self.window.title("Next Visitor")
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
        wait_time = 10000
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
