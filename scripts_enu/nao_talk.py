#!/usr/bin/python
# -*- coding: utf-8 -*-

##########################################################################
# Author: Mahla Nasrollahi
# Last Updated: 25/03/2021
# File Name: nao_talk.py
#
# This class stores some string dialogs with regards to the different
# interests inputs that the visitors choose when they book their tickets.
# The strings are returned randomly for the robot to talk back at the
# visitors.
############################################################################

#--------------------------------------------------------------------------
# Importing necessary packages
#--------------------------------------------------------------------------
import random
import json



class NaoDialogs:
    def __init__(self):
        pass

    #---------------------------------------------------------------------------
    # Introduction on what the NAO is going to talk about next for different
    # interest input values.
    # Argument: None
    #---------------------------------------------------------------------------
    def intro_interest(self):
        speech_interests = ["I see that you are interested in the ",
                            "Oh you have a fascinating interest in the ",
                            "So your interest lies within the "]
        return random.choice(speech_interests)

    #---------------------------------------------------------------------------
    # This function returns a random string based on what interest parameter
    # visitors have chosen. There are 3 different interest choices:
    # Artist, History and Culture
    # Argument: json_value, type=string, it is the interest choice of the
    # visitor based on their QR code
    #---------------------------------------------------------------------------
    def interest_talk(self, json_value):
            # Based on json file data value from user inputs, choose one statement
            if json_value == "Artist":
                about_artist = [
                "Let me tell you something about Jan Matejko’s Copernicus."\
                " He was a Polish painter who lived and worked in Kraków. He"\
                " was considered the finest representative of historicism in"\
                " Polish painting and founder of the national school of"\
                " historical painting.",
                "Did you know that Jan Matejko’s Copernicus won international"\
                " fame and recognition before he turned thirty? He was mostly"\
                " known for being a Polish history painter. If you ever visit"\
                " the capital of Poland, Krakow, don't forget to visit the"\
                " beautiful monument of Jan Matejko",
                "Jan Matejko’s Copernicus had ten siblings and he was the ninth"\
                " from the eleven that his parents had. This Polish painter"\
                " was mostly known for his drawings of notable historical"\
                " Polish political and military events."
                ]
                # Pick a random dialog from above list and send it to the robot
                return random.choice(about_artist)

            elif json_value == "History":
                about_history =[
                "I will tell you a little history about Matejko. He has won two"\
                " gold medals of 1st classes at the Universal Exhibition in"\
                " Paris one of which was for Rejtan painting in 1867. That"\
                " painting was later bought by the Emperor of Austria",
                "Jan Matejk was at a very young age when Kraków was during its"\
                " revolution of 1846 and also witnessed the siege of Kraków in"\
                " 1848 by the Austrians which did not end up being so great for"\
                " the Free City of Kraków.",
                "Did you know that Matejk attended St. Ann's High School in"\
                " Kraków, Poland, but since he was not performing well, he"\
                " dropped out of school in 1851. However, getting low grades"\
                " in other subjects did not stop him from developing artistic talent."
                ]
                return random.choice(about_history)

            elif json_value == "Culture":
                about_culture = [
                "According to my research, Polish food, specially the one that"\
                " is called pierogi is very delicious and must be tried at least"\
                " once. Pierogies is kind of a dough filled with different fillings."\
                " It is usually cooked or baked and is served with the greaves,"\
                " onion or sour cream. I will most likely cook that today when"\
                " I go home.",
                "As far as I know, Poland has long winter seasons. So, to"\
                " celebrate the first day of spring, children usually go to"\
                " truancy or make a straw doll with colourful ribbons called"\
                " Marzanna. Adults on the other hand help in setting Marzanna"\
                " on fire and then dropping the doll into the local river."\
                " This Polish tradition is a peculiar way of saying goodbye to winter.",
                "Did you know that Polish people have a popular saying, which"\
                " rougly translates to having a guest in the house is like"\
                " having a God in the house. So you enter a Polish home, expect"\
                " to be treated like a member of the royalty!"
                ]
                return random.choice(about_culture)
