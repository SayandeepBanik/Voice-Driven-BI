import pyttsx3
import speech_recognition as sr
import subprocess

# Set up speech recognition
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Set up text-to-speech engine
engine = pyttsx3.init()

# Define the wake word or trigger phrase
wake_word = "Alexa"

# Define voice commands and corresponding file paths
command_mapping = {
    "open sales dashboard": r"C:\Users\banik\OneDrive\Documents\powerbiprojects\sales dashboard.pbix",
    "open marketing dashboard": r"C:\path\to\marketing.pbix",
    "open finance dashboard": r"C:\path\to\finance.pbix",
    # Add more command-file path mappings as needed
}

# Function to open a Power BI file based on the command
def open_powerbi_file(command):
    if command in command_mapping:
        file_path = command_mapping[command]

        # Open the file in Power BI using subprocess
        subprocess.Popen([r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe", file_path])

        engine.say("File opened successfully.")
        engine.runAndWait()
    else:
        engine.say("Unknown command: " + command)
        engine.runAndWait()

while True:
    with microphone as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("Command:", command)

        if wake_word in command:
            # Remove the wake word from the command
            command = command.replace(wake_word, "").strip()

            if command in command_mapping:
                open_powerbi_file(command)

                engine.say("Command executed: " + command)
                engine.runAndWait()
            else:
                engine.say("Unknown command: " + command)
                engine.runAndWait()

    except sr.UnknownValueError:
        engine.say("Sorry, I didn't catch that. Can you please repeat?")
        engine.runAndWait()
    except sr.RequestError:
        engine.say("Sorry, there was an issue with the speech recognition service.")
        engine.runAndWait()

