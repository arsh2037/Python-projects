import requests
import json
import time
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=9779f694971549808edf026b10058eb0")

result = data.json()
print(result['status'])
print(result)

news = result['articles']

speak("Welcome to the  News Channel")
speak("Here are the top  news of  India")
speak("So our first news is ")
for i  in range(1,10):
    print(i)
    print(news[i]['description'])
    speak(news[i]['description'])
    if i>=9:
        break
    time.sleep(2)
    if i == 8:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")
speak("Keep coding")
