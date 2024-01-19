import win32com.client


def set_voice(speaker, desired_voice):
    for voice in speaker.GetVoices():
        if desired_voice in voice.GetDescription():
            speaker.Voice = voice
            return True
    return False


def main():
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    # Set the desired voice (replace with your desired voice description)
    desired_voice = "Microsoft Eva - English (Canada)"

    if set_voice(speaker, desired_voice):
        print(f"Voice set to: {desired_voice}")
        message_to_speak = "Hi, I am JAKE, a one of a kind voice assistant with some brains. My name sounds like a guy's name but it has a meaning just like edith and jarvis in the marvel universe"
        speaker.Speak(message_to_speak)
    else:
        print(f"Voice '{desired_voice}' not found.")


if __name__ == "__main__":
    main()