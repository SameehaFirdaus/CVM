import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Coffee options
coffee_options = {
    "1": "Espresso",
    "2": "Latte",
    "3": "Cappuccino",
    "4": "Americano",
    "5": "Mocha"
}

def speak(text):
   engine.say(text)
   engine.runAndWait()

def listen():
    with sr.Microphone() as source:
       print("Listening...")
       audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        return ""

def display_menu():
   print("Welcome to the Coffee Vending Machine!")
   speak("Welcome to the Coffee Vending Machine!")
   print("Please choose your coffee:")
   for key, value in coffee_options.items():
        print(f"{key}: {value}")
        speak("Please choose your coffee by saying the number.")

def process_order(order):
    if order in coffee_options:
       coffee = coffee_options[order]
       print(f"Preparing your {coffee}...")
       speak(f"Preparing your {coffee}. Enjoy!")
    else:
       print("Invalid choice. Please try again.")
       speak("Invalid choice. Please try again.")

def main():
    display_menu()
    order = listen()
    process_order(order)

if __name__ == "__main__":
   main()