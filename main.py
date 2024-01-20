import win32com.client
import speech_recognition as sr
import os,sys,vosk

speaker = win32com.client.Dispatch("SAPI.SpVoice")
sp_recognizer=sr.Recognizer()
desired_voice = "Microsoft Eva - English (United States)"

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
    # working on it
    pass
def doYTsearch(query):
    # working on it
    pass
def moderationSystem():
    # working on it
    pass
def contextAnalyser(sentence):
    # this function analyses the context of a sentence and takes appropriate action
    sentence.lower()
    if "time" and "now" and "what" in sentence:
        res=getDateAndTime(timeOnly=True)
        speaker.Speak(res)
    elif "date" and "today" and "what" in sentence:
        res=getDateAndTime(timeOnly=False)
        speaker.Speak(res)
    elif "do" and "google search" in sentence:
        # continue from here
        res=doAGoogleSearch(sentence)
    pass
def main():
    if voice_check(speaker, desired_voice):
        print(f"Voice set to: {desired_voice}")

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