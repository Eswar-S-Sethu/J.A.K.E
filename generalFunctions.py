# all general functions which any voice assistant can do will be here.
# Author : Eswar Sivan Sethu
'''These are the things which any voice assistant can do like - telling the time and date, keeping
    reminders, accessing the calendar data and letting user know about the events, making a phone
    call, doing a Google search, opening a webpage, opening a YT video, recognizing a song,
    key logging, face and object recognition, file format conversions, scheduling your day, getting the
    news, taking notes, taking printouts, controlling brightness and audio, playing a song, random
    questions, getting jokes from the internet, automating keyboard shortcuts, controlling Wi-Fi and
    bluetooth, opening and closing apps, taking screenshots, recording sound, setting alarms and timers,
    mini-games, getting weather info, getting info from wikipedia, cracking a password, calculator,
    wikiHow integration, morse and binary conversions, language translations'''

import wikipedia
import os,sys
import string,time
import pywhatkit as pywht
from screen_brightness_control import set_brightness
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime,timezone
import newspaper as newspr
import itertools,pyjokes,asyncio,keyboard,folium
from shazamio import Shazam
import pygame
import spotipy

shazam=Shazam()
newsList={"AU":["https://www.news.com.au/","https://www.9news.com.au/","https://www.abc.net.au/news/australia"],
          "IN":["https://timesofindia.indiatimes.com/","https://www.thehindu.com/news/national/","https://www.indiatoday.in/"],
          "GLOBAL":["https://www.indiatoday.in/","https://www.reuters.com/world/","https://www.bbc.com/"],
          "SPORTS":["https://www.bbc.com/sport","https://7news.com.au/sport","https://sports.ndtv.com/"]}


class General:
    def __init__(self):
        pass

    def song_identification(self, song=None):
        async def recognise_song(song):
            song=await shazam.recognize_song(song)
            if song.get('track') != None:
                print(song['track']['title'] + '\t' + song['track']['subtitle'])

        asyncio.run(recognise_song(song))

    def get_news(self,topgoogletrends=False,today=True,sportsnewsonly=False,currentCountry=False):
        pass

    def take_new_note(self,note):
        pass

    def dial_a_number(self):
        pass

    def play_song(self,songname):
        pass

    def get_a_joke(self):
        pass

    def textToMorseCodeAndBack(inputValue):

        # in tests.py - working on it

        morse_code = {"A": "._", "B": "_...", "C": "_._.", "D": "_..", "E": ".",
                      "F": ".._.", "G": "__.", "H": "....", "I": "..", "J": ".___",
                      "K": "_._", "L": "_..", "M": "__", "N": "_.", "O": "___",
                      "P": ".__.", "Q": "__._", "R": "._.", "S": "...", "T": "_",
                      "U": ".._", "W": ".__", "X": "_.._", "Y": "_.__", "Z": "__..",
                      "1": ".____", "2": "..___", "3": "...__", "4": "...._",
                      "5": ".....", "6": "_....", "7": "__...", "8": "___..", "0": "_____",
                      "?": "..__..", "!": "_._.__"}

        morse=None
        flag=0

        for i in len(inputValue):
            if i=="." or i=="_":
                flag+=1
            else:
                pass

        if flag==len(inputValue):
            morse=True

        # convert morse to text
        if morse:
            pass



    def binaryToTextAndBack(textOrBinary):
        if set(textOrBinary).issubset({'0', '1'}):
            textOrBinary = textOrBinary[:len(textOrBinary) - (len(textOrBinary) % 8)]

            text = ""
            for i in range(0, len(textOrBinary), 8):
                byte = textOrBinary[i:i + 8]
                text += chr(int(byte, 2))
            return text
        else:
            return ''.join(format(ord(char), '08b') for char in textOrBinary)

    def searchAFile(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    def passwordCracker(self):  # need to work more on it
        chars = string.printable

        # Define the password to be cracked
        password = "echu"  # make a guess based on the minimum length of passwords
        max_length = len(password)
        start_time = time.time()

        # Try all possible combinations of characters up to max_length
        for length in range(1, max_length + 1):
            for combination in itertools.product(chars, repeat=length):
                # Join the characters in the combination to form a password candidate
                candidate = "".join(combination)
                print("Trying password:", candidate)
                # Check if the candidate matches the password
                if candidate == password:
                    # Track the end time of the password cracking process
                    end_time = time.time()
                    print("Password found:", candidate)
                    # Calculate the time taken to crack the password
                    time_taken = end_time - start_time
                    print("Time taken:", time_taken, "seconds")
                    # Terminate the password cracking process
                    raise SystemExit

    def getDateAndTime(timeOnly, singleDigit=False):
        if timeOnly:
            getDateTime = datetime.now(timezone.utc)
            the_time = getDateTime.strftime("%I:%M %p")
            return the_time
        elif timeOnly == False:
            the_date = datetime.now().strftime("%d %B, %Y, %A")
            return the_date
        elif timeOnly == True and singleDigit == True:
            getTime = datetime.now(timezone.utc)
            the_time_num = getTime.strftime("%H")
            return the_time_num

    def doAGoogleSearch(query):
        pywht.search(query)

    def doAWikiSearch(query):
        wikipedia.search(query, results=4)

    def adjustScreenBrightness(adjustValue):
        set_brightness(adjustValue)

    def adjustSystemVolume(adjustValue):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume_object = cast(interface, POINTER(IAudioEndpointVolume))
        # Set the volume (0.0 to 1.0)
        volume_object.SetMasterVolumeLevelScalar(adjustValue, None)

    def doYTsearch(query):
        pywht.playonyt(query)


class FormatFactory:

    # to convert files to various file formats

    def __init__(self):
        pass


class KeyLogger:

    # needs more work

    def __init__(self):
        self.log=""
        self.start_date=datetime.now()
        self.end_date=datetime.now()

    def callback(self,event):
        name=event.name

        if len(name)>1:
            if name=="space":
                name="  "
            elif name=="enter":
                name="[ ENTER ]\n"
            elif name=="decimal":
                name=" . "
            else:
                name=name.replace(" ","_")
                name=f"[{name.upper()}]"

        self.log+=name

    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"keylog-{start_dt_str}_{end_dt_str}"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
