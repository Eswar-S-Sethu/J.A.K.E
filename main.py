import win32com.client
import speech_recognition as sr
import os,sys,vosk

model_path="C:\\Users\\eswar\\PycharmProject\\J.A.K.E\\vosk-model-en-us-0.22"
model=vosk.Model(model_path)
recognizer=vosk.KaldiRecognizer(model,16000)
speaker = win32com.client.Dispatch("SAPI.SpVoice")
sp_recognizer=sr.Recognizer()
desired_voice = "Microsoft Eva - English (United States)"

def voice_check(speaker, desired_voice):
    for voice in speaker.GetVoices():
        if desired_voice in voice.GetDescription():
            speaker.Voice = voice
            return True
    return False

def recognize_speech_with_vosk(audio_data):
    recognizer.AcceptWaveform(audio_data)
    result=recognizer.Result()
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
        message_to_speak = "Hi, I am JAKE, a one of a kind voice assistant with some brains. My name sounds like a guy's name but it has a meaning just like edith and jarvis in the marvel universe"
        speaker.Speak(message_to_speak)
    else:
        print(f"Voice '{desired_voice}' not found.")

    print("Going to listen to your voice now...")


    with sr.Microphone() as source:
        sp_recognizer.adjust_for_ambient_noise(source)
        print("Say something..")
        audio_data=sp_recognizer.listen(source)

    try:
        vosk_result=recognize_speech_with_vosk(audio_data.frame_data)
        print("Vosk result:"+vosk_result)
    except sr.UnknownValueError:
        speaker.Speak("I'm having difficulty understanding you, please speak up!")
    except sr.RequestError as e:
        speaker.Speak("I'm sorry, offline speech recognition is not available at the moment, try again later")


if __name__ == "__main__":
    main()