import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import urllib.parse
import os

# Text-to-speech setup
engine = pyttsx3.init()

# Speech recognition setup
recognizer = sr.Recognizer()


def speak(text):
    """Print and speak the assistant response."""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen through the microphone and return spoken text."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=6,
                phrase_time_limit=10
            )

        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        speak("I could not understand that. Please repeat.")

    except sr.WaitTimeoutError:
        speak("I did not hear anything. Please try again.")

    except sr.RequestError:
        speak("Speech recognition is unavailable right now.")

    except OSError as error:
        speak(f"I cannot access the microphone: {error}")

    return ""


def handle_command(command):
    """Choose an action based on the spoken command."""

    if "goodbye" in command or "exit" in command or "stop listening" in command:
        speak("Goodbye. Have a nice day.")
        return False

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"It is {current_time}")

    elif "date" in command:
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        speak(f"Today is {current_date}")

    elif command.startswith("search for "):
        topic = command.replace("search for ", "", 1)

        search_url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(topic)
        )

        webbrowser.open(search_url)
        speak(f"Searching for {topic}")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open files" in command or "open file explorer" in command:
        os.startfile(os.path.expanduser("~"))
        speak("Opening your files.")

    else:
        speak("I do not understand that command yet.")

    return True


# Start the assistant
speak(
    "Voice assistant ready. You can say hello, ask for time or date, "
    "search, open Google, open YouTube, open files, or say goodbye."
)

while True:
    command = listen()

    if command:
        should_continue = handle_command(command)

        if should_continue is False:
            break