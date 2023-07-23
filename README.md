# Voice-Driven-BI
Hands-free way to interact with Power BI reports




The script starts by importing the necessary libraries:

1. speech_recognition-  Recognises audio input from the micro and converts it into text
2. pyttsx3 (Text to speech) -  allows the code to provide feedback and confirm the execution of commands. Allowing the program to speak to the user.
3. subprocess to  interact with external applications. It is used to open the Power BI application with a specific file.


Then initialization of the speech recognition and text-to-speech components:

1. Recognizer: This object  allows the program to recognize speech from the user's microphone.
2. Microphone: This object represents the microphone used for speech input.
3. Engine: This object  enables the program to generate spoken output.


Defining the wake word. I have named it  name "Alex". We did it so  that we can prevent the voice assistant from constantly listening and consuming system resources and it only processes voice commands when the wake word is spoken.

Defining Voice Commands and File Paths
1. The command_mapping  is a dictionary used  to provide a mapping between recognized voice commands and the corresponding actions to be performed. 
2. We know that a dictionary is a key-value pair. Now here the key is the voice command
3. For example, we want to open the sales dashboard. For that the voice command will be the "Alex open sales dashboard" and this is a key and value will be the file path where the power-bi dashboard file is saved.
4. When a user speaks a voice command, the code checks if the recognized command matches any of the keys in the command_mapping. It retrieves the corresponding file path from the dictionary if it finds a match.  If it finds a match with the key "open sales dashboard," it knows that the user wants to open the sales dashboard file. 
5 It uses a subprocess. Popen function to open that file.


while True loop is an infinite loop. Within the loop, the code captures audio input from the user through the microphone and performs speech recognition to convert the spoken words into text to recognize the voice command. After recognizing the voice command, the script checks if the command matches any of the predefined voice commands in the command_mapping dictionary. If there is a match and the recognized command corresponds to a valid action, the script executes the associated function, such as opening a Power BI file. The loop will keep running indefinitely until a valid voice command is executed and a break statement is encountered to stop the loop.

Exception Handling: 
1. Unknown value error = This error occurs when the code fails to recognize the user voice input. It considers it as an unknown value. It gives the output "Sorry, I didn't catch that. Can you please repeat?". It is converted into voice output by pyttx3 library.

2. Request error = This error occurs when there is a problem with the speech recognition service, such as issues with the internet connection or service availability.
