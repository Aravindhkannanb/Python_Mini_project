import pyttsx3
engine=pyttsx3.init()
input=input("Enter the text to say:")
engine.say(input)
engine.runAndWait()