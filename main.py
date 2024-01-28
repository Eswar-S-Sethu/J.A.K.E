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
def passwordCracker():
    chars = string.printable

    # Define the password to be cracked
    password = "echu" # make a guess based on the minimum length of passwords

    # Define the maximum password length to try
    max_length = len(password)

    # Track the start time of the password cracking process
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
def textToMorseCodeAndBack():
    morse_code={"A":"._","B":"_...","C":"_._.","D":"_..","E":".",
                "F":".._.","G":"__.","H":"....","I":"..","J":".___",
                "K":"_._","L":"_..","M":"__","N":"_.","O":"___",
                "P":".__.","Q":"__._","R":"._.","S":"...","T":"_",
                "U":".._","W":".__","X":"_.._","Y":"_.__","Z":"__..",
                "1":".____","2":"..___","3":"...__","4":"...._",
                "5":".....","6":"_....","7":"__...","8":"___..","0":"_____",
                "?":"..__..","!":"_._.__"}
    pass
def searchAFile():
    # working on it
    pass
def binaryToTextAndBack():
    binary_text={"A":"01000001","B":"01000010","C":"01000011","D":"01000100","E":"01000101","F":"01000110",
                 "G":"01000111","H":"01001000","I":"01001001","J":"01001010","K":"01001011","L":"01001100",
                 "M":"01001101","N":"01001110","O":"01001111","P":"01010000","Q":"01010001",
                 "R":"01010001","S":"01010011","T":"01010100","U":"01010101","V":"01010110",
                 "W":"01010111","X":"01011000","Y":"01011001","Z":"01011010","a":"01100001","b":"01100010","c":"01100011",
                 "d":"01100100","e":"01100101","f":"01100110","g":"01100111","h":"01101000","i":"01101001",
                 "j":"01101010","k":"01101011","l":"01101100","m":"01101101","n":"01101110","o":"01101111",
                 "p":"01110000","q":"01110001","r":"01110010","s":"01110011","t":"01110100","u":"01110101",
                 "v":"01110110","w":"01110111","x":"01111000","y":"01111001","z":"01111010"}
    pass
def getDateAndTime(timeOnly):
    # working on it
    pass
def setReminder():
    # working on it
    pass
def doAGoogleSearch(query):
    # working on it
    pass
def takeANote(query):
    # working on it
    pass
def getNews():
    # working on it
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
    res=getDateAndTime(timeOnly=True)
    pass
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
        res=doAGoogleSearch(sentence)
        speaker.Speak(res)
    elif "youtube" and "search" in sentence:
        sentence=sentence.replace('youtube search','')
        doAGoogleSearch(sentence)
        speaker.Speak("result will open in youtube")
    elif "news" and "today" in sentence:
        getNews()
    elif "increase volume" in sentence:
        volume_adjust_value=volume_adjust_value+20
        adjustSystemVolume(volume_adjust_value)
        speaker.Speak("i increased the speaker volume")
        followup=True
    elif "decrease volume" in sentence:
        volume_adjust_value=volume_adjust_value-20
        adjustSystemVolume(volume_adjust_value)
        speaker.Speak("i decreased the speaker volume")
        followup=True
    elif "adjust volume" and "percent" in sentence:
        for i in sentence:
            if i.isDigit():
                digit=digit+""+i
        int(digit)
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
        sp_recognizer.adjust_for_ambient_noise(source,duration=1)
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