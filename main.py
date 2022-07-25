import speech_recognition  # Importing required Python Packages
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

receiver = speech_recognition.Recognizer()  # Recognizing your speech and assigning it to receiver
assistant = pyttsx3.init()  # Initializing Python text to speech and assigning it to an assistant
change_voice = assistant.getProperty('voices')  # importing voices from package
assistant.setProperty('voice', change_voice[1].id)  # Assigning a new voice to the assistant


def speak(text):  # Defining a function 'speech' with input 'text'
    assistant.say(text)  # Text to Speech
    assistant.runAndWait()


def take_command():  # Defining a function 'take_command'
    with speech_recognition.Microphone() as source:
        speak('I am listening')
        speech = receiver.listen(source)
        command = receiver.recognize_google(speech)
        command = command.lower()
    return command


def run_praveen():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing the song')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
    elif 'date' in command:
        speak('sorry, I have a headache')
    elif 'are you single' in command:
        speak('I am in a relationship with wifi')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    else:
        info = wikipedia.summary(command, 1)
        print(info)
        speak('This is what I found on Internet ' + info)


while True:
    run_praveen()
