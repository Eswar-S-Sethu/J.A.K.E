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

import wikipedia as wk
import os,sys
import string,time
import pywhatkit as pywht
from screen_brightness_control import set_brightness
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime,timezone

