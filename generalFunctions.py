# all general functions which any voice assistant can do will be here.
# Author : Eswar Sivan Sethu
'''These are the things which any voice assistant can do like - telling the time and date-done, keeping
    reminders, accessing the calendar data and letting user know about the events, making a phone
    call, doing a Google search-done, opening a webpage, opening a YT video-done, recognizing a song-done,
    key logging, face and object recognition, file format conversions, scheduling your day, getting the
    news, taking notes, taking printouts, controlling brightness and audio-done, playing a song, getting jokes from the internet-done,
    automating keyboard shortcuts, controlling Wi-Fi and
    bluetooth, opening and closing apps, taking screenshots, recording sound, setting alarms and timers,
    mini-games, getting weather info, getting info from wikipedia-done, cracking a password-done, calculator,
    wikiHow integration, morse and binary conversions- almost done, language translations'''

import wikipedia
import os,sys,json
import string,time
import pywhatkit as pywht
from screen_brightness_control import set_brightness
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime,timezone,date
import newspaper as newspr
import itertools,pyjokes,asyncio,keyboard,folium,requests,geocoder,nltk
import pyautogui
import aspose.words as aw
from geopy.geocoders import Nominatim
from shazamio import Shazam
import tkinter as tk
import pygame,serial
import spotipy
from pywikihow import RandomHowTo,search_wikihow
from sinch import SinchClient
from dotenv import load_dotenv


newsList={"AU":["https://www.news.com.au/","https://www.9news.com.au/","https://www.abc.net.au/news/australia"],
          "IN":["https://timesofindia.indiatimes.com/","https://www.thehindu.com/news/national/","https://www.indiatoday.in/"],
          "GLOBAL":["https://www.indiatoday.in/","https://www.reuters.com/world/","https://www.bbc.com/"],
          "SPORTS":["https://www.bbc.com/sport","https://7news.com.au/sport","https://sports.ndtv.com/"]}


class General:
    def __init__(self):
        load_dotenv()
        self.shazam = Shazam()
        self.geolocator = Nominatim(user_agent="geoapi")
        self.sinchAppkey=os.getenv("SINCH_APPLICATION_KEY")
        self.sinchAppSecret=os.getenv("SINCH_APPLICATION_SECRET")
        self.openweatherAPIKey=os.getenv("OPENWEATHER_API_KEY")
        self.sinch_client = SinchClient(application_key=os.getenv(self.sinchAppkey),
                                        application_secret=os.getenv(self.sinchAppSecret))

    def song_identification(self, song=None):
        async def recognise_song(song):
            song=await self.shazam.recognize_song(song)
            if song.get('track') != None:
                print(song['track']['title'] + '\t' + song['track']['subtitle'])

        asyncio.run(recognise_song(song))

    def get_news(self,topgoogletrends=False,today=True,sportsnewsonly=False,currentCountry=False):
        pass

    def takeNote(self,note):
        now = datetime.now()
        dt_string = now.strftime("%H:%M")

        dictionary = {
            "Date": str(date.today()),
            "Time": str(dt_string),
            "Content": note,
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent=3)

        # Writing to sample.json
        with open("usernotes.json", "a") as outfile:
            outfile.write(json_object)

        return



    def takeAScreenShot(self):
        im1 = pyautogui.screenshot()
        im1.save(r"C:\Users\Eswar\PycharmProjects\J.A.K.E\temp\screenshot.png")
        return

    def getCurrentLocation(self):
        g = geocoder.ip('me')  # this function is used to find the current information using our IP Add
        latitude, longitude = g.latlng
        print(latitude)
        print(longitude)

        location = self.geolocator.reverse([latitude, longitude])

        address = location.raw['address']

        # traverse the data
        city = address.get('city', '')
        state = address.get('state', '')
        country = address.get('country', '')
        code = address.get('country_code')
        zipcode = address.get('postcode')

        return city


    def getWeatherInfo(self):
        city = self.getCurrentLocation()

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(
            city,self.openweatherAPIKey)

        res = requests.get(url)
        data = res.json()

        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        temp = data['main']['temp']

        temp="Temperature: "+temp+"°C"
        wind="Wind: "+wind
        pressure="Pressure: "+pressure
        humidity="Humidity: "+humidity

        return (temp,wind,pressure,humidity,description)

    def dialNumberOnline(self,phonenumber):
        # uses internet for making the phone call
        response = self.sinch_client.voice.callouts.text_to_speech(
            destination={
                "type": "number",
                "endpoint": phonenumber
            },
            text="")

        return response

    def play_song(self,songname):
        pass

    def get_a_joke(self):
        My_joke = pyjokes.get_joke(language="en", category="all")
        return My_joke

    def textToMorseCodeAndBack(inputValue):

        # still needs work - come back later
        morse_code_list = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "_..", "__",
                           "_.", "___",
                           ".__.", "__._", "._.", "...", "_", ".._", "..._", ".__", "_.._", "_.__", "__..", ".____",
                           "..___", "...__",
                           "...._", ".....", "_....", "__...", "___..", "____.", "_____", "..__..", "_._.__"]
        letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                        "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                        "?", "!"]

        morse = None
        flag = 0

        for i in inputValue:
            if i == "." or i == "_":
                flag += 1
            elif i.isalpha():
                flag -= 1

        if flag > 1:
            morse = True
        elif flag < -1:
            morse = False
        elif flag == 0:
            morse = False

        inputValue = inputValue.upper()
        converted = ""

        # convert text to morse
        if not morse:
            for j in inputValue:
                for a in range(len(letters_list)):
                    if j == letters_list[a]:
                        converted = converted + morse_code_list[a] + " "

        elif morse:
            inputValue = inputValue.split()
            for k in inputValue:
                for b in range(len(morse_code_list)):
                    if k == morse_code_list[b]:
                        converted = converted + letters_list[b]

        return converted

    def binaryToTextAndBack(textOrBinary):
        # needs to work on it
        # probably needs work as i never tested it
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

    def wikiHowRandom(self):
        how_to = RandomHowTo()
        return how_to.print() # a string value

    def wikiHowSpecific(self,query):
        max_results = 1  # default for optional argument is 10
        how_tos = search_wikihow(query, max_results)
        assert len(how_tos) == 1
        return how_tos[0].print()

    def openAWindow(self,dimensionX,dimensionY):
        window=tk.Tk()
        window.title("Info Screen")
        window.geometry(dimensionX+"x"+dimensionY)
        window.mainloop()

    class FormatFactory:
        # need to work on this further
        # to convert files to various file formats
        def __init__(self, filepath, filename):
            self.filepath = filepath
            self.filename = filename

        def ToDOCX(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.docx")

        def ToPDF(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.pdf")

        def ToMD(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.md")

        def ToTXT(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.txt")

        def ToDOC(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.doc")

        def ToDOT(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.dot")

        def ToDOCM(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.docm")

        def ToDOTX(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.dotx")

        def ToDOTM(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.dotm")

        def ToRTF(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.rtf")

        def ToEPUB(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.epub")

        def ToPS(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.ps")

        def ToPCL(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.pcl")

        def ToMHTML(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.mhtml")

        def ToXHTML(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.xhtml")

        def ToODT(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.odt")

        def ToOTT(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.ott")

        def ToXPS(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)
            doc.save("Output.xps")

        def ToPNG(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.png")

        def ToBMP(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.bmp")

        def ToEMF(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.emf")

        def ToGIF(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.gif")

        def ToSVG(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.svg")

        def ToTIFF(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.tiff")

        def ToJPG(self):
            file = self.filepath + self.filename
            doc = aw.Document(file)

            for page in range(0, doc.page_count):
                extractedPage = doc.extract_pages(page, 1)
                extractedPage.save(f"Output_{page + 1}.jpg")

    class KeyLogger:

        # needs more work

        def __init__(self):
            self.log = ""
            self.start_date = datetime.now()
            self.end_date = datetime.now()

        def callback(self, event):
            name = event.name

            if len(name) > 1:
                if name == "space":
                    name = "  "
                elif name == "enter":
                    name = "[ ENTER ]\n"
                elif name == "decimal":
                    name = " . "
                else:
                    name = name.replace(" ", "_")
                    name = f"[{name.upper()}]"

            self.log += name

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

    class PhoneCall:

        """
        This is meant to make phone call from any device but it only uses GSM for now. Raspberry Pi will have a SIM card
        to make the said phone call.
        """
        def __init__(self,phnumber):
            self.ser = serial.Serial('COM3', 9600, timeout=5)  # Windows
            self.phnumber=phnumber
            self.make_call(phone_number=self.phnumber)

        def make_call(self,phone_number):
            self.ser.write(b'ATD' + phone_number.encode() + b';\r')  # Send call command
            time.sleep(5)  # Wait for a few seconds (adjust as necessary)

        def hangup(self):
            # Hang up the call (if necessary)
            self.ser.write(b'ATH\r')  # Send hang-up command

            self.ser.close()  # Close the serial connection



    def __del__(self):
        # cleanup functions
        pass


