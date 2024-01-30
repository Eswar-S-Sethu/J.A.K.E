import wikipedia
import win32com.client
import speech_recognition as sr
import os,sys
import itertools
import string
import time
import pywhatkit as pywht
from screen_brightness_control import set_brightness
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from datetime import datetime,timezone

speaker = win32com.client.Dispatch("SAPI.SpVoice")
sp_recognizer=sr.Recognizer()
desired_voice = "Microsoft Eva - English (United States)"
followup=False


def voice_check(speaker, desired_voice):
    for voice in speaker.GetVoices():
        if desired_voice in voice.GetDescription():
            speaker.Voice = voice
            return True
    return False

def recognize_speech_with_whisper(audio_data):
    result=sp_recognizer.recognize_whisper(audio_data,model="small",language='en')
    return result
def passwordCracker(): # need to work more on it
    chars = string.printable

    # Define the password to be cracked
    password = "echu" # make a guess based on the minimum length of passwords
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
def textToMorseCodeAndBack(inputValue):
    morse_code={"A":"._","B":"_...","C":"_._.","D":"_..","E":".",
                "F":".._.","G":"__.","H":"....","I":"..","J":".___",
                "K":"_._","L":"_..","M":"__","N":"_.","O":"___",
                "P":".__.","Q":"__._","R":"._.","S":"...","T":"_",
                "U":".._","W":".__","X":"_.._","Y":"_.__","Z":"__..",
                "1":".____","2":"..___","3":"...__","4":"...._",
                "5":".....","6":"_....","7":"__...","8":"___..","0":"_____",
                "?":"..__..","!":"_._.__"}
def searchAFile(name,path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
def binaryToTextAndBack(textOrBinary):
    if set(textOrBinary).issubset({'0','1'}):
        textOrBinary = textOrBinary[:len(textOrBinary) - (len(textOrBinary) % 8)]

        text = ""
        for i in range(0, len(textOrBinary), 8):
            byte = textOrBinary[i:i + 8]
            text += chr(int(byte, 2))
        return text
    else:
        return ''.join(format(ord(char), '08b') for char in textOrBinary)

def getDateAndTime(timeOnly,singleDigit=False):
    if timeOnly:
        getDateTime = datetime.now(timezone.utc)
        the_time=getDateTime.strftime("%I:%M %p")
        return the_time
    elif timeOnly==False:
        the_date=datetime.now().strftime("%d %B, %Y, %A")
        return the_date
    elif timeOnly==True and singleDigit==True:
        getTime=datetime.now(timezone.utc)
        the_time_num=getTime.strftime("%H")
        return the_time_num
def setReminder():
    # working on it
    pass
def doAGoogleSearch(query):
    pywht.search(query)
    speaker.Speak("found this one on google")

def doAWikiSearch(query):
    speaker.Speak(wikipedia.search(query,results=4))

def takeANote(query):
    # working on it
    pass
def getNews():
    news_agencies={"9 news":"https://www.9news.com.au/",
                "times of india":"https://timesofindia.indiatimes.com/",
                "abc australia":"https://www.abc.net.au/news",
                "bbc":"https://www.bbc.com/"}
    newsSummary=""

    pass
def planADay():
    # working on it
    pass
def adjustScreenBrightness(adjustValue):
    set_brightness(adjustValue)
def adjustSystemVolume(adjustValue):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume_object = cast(interface, POINTER(IAudioEndpointVolume))
    # Set the volume (0.0 to 1.0)
    volume_object.SetMasterVolumeLevelScalar(adjustValue, None)
def greetingOnBootup():
    res=int(getDateAndTime(timeOnly=True,singleDigit=True))
    if (res>=0 or res>=00) and res<12:
        speaker.Speak("Good morning")
    elif res>=12 and res<=15:
        speaker.Speak("Good afternoon")
    elif res>15 and res<=21:
        speaker.Speak("Good evening")
    else:
        speaker.Speak("Good night")
def doYTsearch(query):
    pywht.playonyt(query)
def moderationSystem():
    # working on it
    pass
def contextAnalyser(sentence):
    # this function analyses the context of a sentence and takes appropriate action and action here means it runs a specific function
    volume_adjust_value=0
    digit=""
    sentence.lower()
    if "time" and "now" and "what" in sentence:
        res=getDateAndTime(timeOnly=True)
        speaker.Speak(res)
    elif "date" and "today" and "what" in sentence:
        res=getDateAndTime(timeOnly=False)
        speaker.Speak(res)
    elif "do" and "google search" in sentence:
        sentence=sentence.replace('google search','')
        doAGoogleSearch(sentence)
    elif "youtube" and "search" in sentence:
        sentence=sentence.replace('youtube search','')
        doAGoogleSearch(sentence)
        speaker.Speak("result will open in youtube")
    elif "news" and "today" in sentence:
        getNews()
    elif "increase volume" in sentence:
        volume_adjust_value=volume_adjust_value+20
        float(volume_adjust_value)
        volume_adjust_value=volume_adjust_value/10
        adjustSystemVolume(volume_adjust_value)
        speaker.Speak("i increased the speaker volume")
        followup=True
    elif "decrease volume" in sentence:
        volume_adjust_value=volume_adjust_value-20
        float(volume_adjust_value)
        volume_adjust_value=volume_adjust_value/10
        adjustSystemVolume(volume_adjust_value)
        speaker.Speak("i decreased the speaker volume")
        followup=True
    elif "adjust volume" and "percent" in sentence:
        for i in sentence:
            if i.isDigit():
                digit=digit+""+i
        float(digit)
        digit=digit/10.0
        adjustSystemVolume(digit)
        speaker.Speak("adjusted the volume by "+digit+" percent")
    elif "increase screen brightness" in sentence:
        volume_adjust_value=volume_adjust_value+20
        adjustScreenBrightness(volume_adjust_value)
        speaker.Speak("increased screen brightness")
    elif "decreased screen brightness" in sentence:
        volume_adjust_value=volume_adjust_value-20
        adjustScreenBrightness(volume_adjust_value)
        speaker.Speak("decreased screen brightness")
    elif "adjust brightness" and "percent" in sentence:
        for j in sentence:
            if j.isDigit():
                digit=digit+""+j
        int(digit)
        adjustScreenBrightness(digit)
        speaker.Speak("adjusted the brightness by "+digit+" percent")
    elif "do" and "wikipedia search" in sentence:
        sentence=sentence.replace('wikipedia search','')
        doAWikiSearch(sentence)


class Automations(automations=False):
    # JAKE will adjust screen brightness and volume automatically after checking the ambient sound and light.
    # it will tell you when it does this. this action can be reversed.
    # JAKE will tell you when it's time to sleep, drink water, eat food, workout and other day-to-day activities
    # working on it
    def screen_brightness_adjustment(self):
        pass
    def speaker_volume_adjustment(self):
        pass
    def water_reminder(self):
        pass
    def food_reminder(self):
        pass
    def workout_reminder(self):
        pass
    def sleep_check(self):
        pass

def main():
    if voice_check(speaker, desired_voice):
        print(f"Voice set to: {desired_voice}")
    greetingOnBootup()

    print("Going to listen to your voice now...")


    with sr.Microphone() as source:
        sp_recognizer.adjust_for_ambient_noise(source)
        print("Say something..")
        audio_data=sp_recognizer.listen(source)
    try:
        print("done listening")
        result=recognize_speech_with_whisper(audio_data)
        print(result)
    except sr.UnknownValueError:
        speaker.Speak("I'm having difficulty understanding you, please speak up!")
    except sr.RequestError as e:
        speaker.Speak("I'm sorry, offline speech recognition is not available at the moment, try again later")


if __name__ == "__main__":
    main()