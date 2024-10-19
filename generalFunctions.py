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
    wikiHow integration, morse and binary conversions- done, language translations'''

import wikipedia
import os,sys,json
import string,time
import pywhatkit as pywht
from screen_brightness_control import set_brightness
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime,timezone,date
import itertools,pyjokes,asyncio,keyboard,folium,requests,geocoder,nltk,smtplib
from itertools import product
import pyautogui
import aspose.words as aw
from geopy.geocoders import Nominatim
from shazamio import Shazam
import tkinter as tk
import pygame,serial,cv2
from pywikihow import RandomHowTo,search_wikihow
from sinch import SinchClient
from dotenv import load_dotenv
from gnews import GNews


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

    def get_news(self):
        gnews = GNews(language='en', country='AU')
        top_news = gnews.get_top_news()
        summaries = []
        for article in top_news[:5]:
            summaries.append({
                'headline': article['title'],
                'summary': article['description']
            })
        return summaries # returns a list


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
        morse_code_list = ["._", "_...", "_._.", "_..", ".", ".._.", "__.", "....", "..", ".___", "_._", "._..", "__",
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

    def brute_force_pin_combination(target_pin):
        """Brute-force the target PIN by generating and checking all possible combinations."""
        pin_length = len(target_pin)  # Automatically determine the PIN length
        for pin_tuple in product("0123456789", repeat=pin_length):
            generated_pin = ''.join(pin_tuple)  # Form the PIN string

            print(f'Trying PIN: {generated_pin}')

            if generated_pin == target_pin:  # Check if the generated PIN matches the target
                print(f'Success! The PIN is: {generated_pin}')
                return generated_pin

        print('Failed to find the PIN within the specified length.')
        return None

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
        # needs more work
        window=tk.Tk()
        window.title("Info Screen")
        window.geometry(dimensionX+"x"+dimensionY)
        window.mainloop()

    def blurAnImage(self,imagename=None):
        imagename=self.searchAFile()
        try:
            image = cv2.imread('image.jpg')
            blurred = cv2.GaussianBlur(image, (15, 15), 0)
            cv2.imwrite('blurred.jpg', blurred)
            return "Done"
        except Exception:
            return "No can do"


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


    # more functions will be added later


    def __del__(self):
        # cleanup functions
        pass


