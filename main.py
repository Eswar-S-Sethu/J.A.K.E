
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




def main():
    if voice_check(speaker, desired_voice):
        print(f"Voice set to: {desired_voice}")

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