# Project vasr
import speech_recognition as sr
import datetime
import wikipedia
import pyttsx3
import webbrowser
import random
import os


# Text To Speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
# to change the rate of spoken words per minute
engine.setProperty('rate', 200)


def speak(audio):  # here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning sir i am virtual assistent vasr how may i assist you")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir i am virtual assistent vasr how may i assist you")
    else:
        speak("good evening sir i am virtual assistent vasr how may i assist you")

# now convert audio to text


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening....")
        print("Listening....")
        audio = r.record(source, duration=3)
    try:
        print("Recognising.")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:  # For Error handling
        speak("unable to execute make sure your internet is connected")
        print("Network connection error")
        return "none"
    return text


# for main function
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()

        if "wikipedia" in query:
            speak("searching details....Wait")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)
        elif 'play my song' in query:
            speak("plz say video name")
            k = takecom().lower()
            # l = "https://www.youtube.com/results?search_query="
            # d = l+k
            webbrowser.open(
                f'https://www.youtube.com/results?search_query={k}')
        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com")
            speak("opening github")
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")
        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")
        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")
        elif 'play  music' in query or "music" in query:

            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, musics[0]))
        elif 'play video' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir, videos[0]))
        elif 'good bye' in query:
            speak("good bye")
            exit()
        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!',
                      'I am nice and full of energy', 'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')
        elif 'who make you' in query or 'who created you' in query or 'who is your developer' in query:
            ans_m = " For your information team suraj Created me as a mini project of college! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "tell me about yourself" in query or "your details" in query:
            about = "I am vasr a virtual assistant speech recognizer based computer program but i can help you lot like a your close friend ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you !thanku sir "
            print(about)
            speak(about)
        elif "hello" in query or "hello vars" in query:
            hel = "Hello sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "tell me your name" in query or "what is your name" in query:
            na_me = "Thanks for Asking my name my self ! vasr ! a virtual assistant speech recognizer"
            print(na_me)
            speak(na_me)
        elif "who you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")
        elif query == 'none':
            continue
        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query:
            break
            # ex_exit = 'I feeling very sweet after meeting with you ! thankyou sir'
            # speak(ex_exit)
            # exit()
        else:

            temp = query.replace(' ', '+')
            g_url = "https://www.google.com/search?q="
            res_g = 'sorry! i cant understand but i search from internet to give your answer ! okay'
            print(res_g)
            speak(res_g)
            webbrowser.open(g_url+temp)
        print("press enter to search again")
        ok = input()
