import win32com.client
import speech_recognition as sr
import os,sys

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
    # working on it
    pass
def textToMorseCode():
    # working on it
    pass
def morseCodeToText():
    # working on it
    pass
def searchAFile():
    # working on it
    pass
def textToBinary():
    # working on it
    pass
def binaryToText():
    # working on it
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
    # working on it
    pass
def adjustSystemVolume(adjustValue):
    # working on it
    pass
def greetingOnBootup():
    res=getDateAndTime(timeOnly=True)
    pass
def doYTsearch(query):
    # working on it
    pass
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

    pass

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