import win32com.client
import speech_recognition as sr

speaker = win32com.client.Dispatch("SAPI.SpVoice")
desired_voice = "Microsoft Eva - English (Canada)"

def voice_check(speaker, desired_voice):
    for voice in speaker.GetVoices():
        if desired_voice in voice.GetDescription():
            speaker.Voice = voice
            return True
    return False

def speechToText():
    # working on it
    pass
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
def getDateAndTime():
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
def speechRecognition():
    # working on it
    pass
def doYTsearch(query):
    # working on it
    pass
def moderationSystem():
    # working on it
    pass
def main():

    if voice_check(speaker, desired_voice):
        print(f"Voice set to: {desired_voice}")
        #message_to_speak = "Hi, I am JAKE, a one of a kind voice assistant with some brains. My name sounds like a guy's name but it has a meaning just like edith and jarvis in the marvel universe"
        #speaker.Speak(message_to_speak)
        speaker.Speak("i am having difficulty understanding you. can you please speak up?")
    else:
        print(f"Voice '{desired_voice}' not found.")


if __name__ == "__main__":
    main()