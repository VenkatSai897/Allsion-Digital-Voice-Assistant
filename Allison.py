import os
# os.environ["HTTPS_PROXY"] = "http://user:pass@192.168.1.107:3128"

from gtts import gTTS
import datetime
import geocoder
import calendar
import time
import webbrowser
import winshell

import ctypes
import random
import speech_recognition as sr


def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio = r.listen(source)
    try:
        data = r.recognize_google(audio)
        print("You Said :" + data)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print("Couldnt get what u requested" + e)
    return data


def assistantresponse(text):
    print(text)
    my_obj = gTTS(text=text, lang='en', slow=False)
    my_obj.save('response.mp3')
    os.system('start response.mp3')


x = record_audio()


def get_date():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()

    weekday = calendar.day_name[my_date.weekday()]
    Month = now.month
    day = now.day
    month_array = ["January", "Febuary", "March", "April", "June", "July", "August", "September", "October", "November",
                   "December"]
    day_array = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th',
                 '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th',
                 '28th', '29th', '30th', '31st']
    return " Today is " + weekday + ' ' + day_array[day - 1] + ' of ' + month_array[Month - 1]


def get_time():
    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    return "Current Time is " + current_time


if "location" in x.lower():
    g = geocoder.ip('me')
    assistantresponse("Your Location is " + str(g.latlng[0]) + " degree " + " latitude " + " and " + str(
        g.latlng[1]) + "degree " + "longetude")
elif "date" and "time" in x.lower():
    assistantresponse(get_date() + " and " + get_time())
elif "time" in x.lower():
    assistantresponse(get_time())
elif "date" in x.lower():
    assistantresponse(get_date())
elif "Youtube".lower() in x.lower():
    assistantresponse("Playing Youtube")
    Youtube_Sites = ['https://www.youtube.com/watch?v=Du__JfXqsAs',
                     'https://www.youtube.com/watch?v=uAVUl0cAKpo',
                     'https://www.youtube.com/watch?v=ldONzfNw660',
                     'https://www.youtube.com/watch?v=gJY8D468Jv0',
                     'https://www.youtube.com/watch?v=P1doPpgVLNs',
                     'https://www.youtube.com/watch?v=qz9tKlF431k',
                     'https://www.youtube.com/watch?v=60ItHLz5WEA']
    webbrowser.open(Youtube_Sites[random.randint(0, len(Youtube_Sites))])

elif "lock" in x.lower():
    assistantresponse("Locking your PC")
    import ctypes

    user32 = ctypes.cdll.LoadLibrary("user32.dll")
    user32.LockWorkStation()
elif "website" in x.lower():
    assistantresponse("Opening a Website")
    Web_sites = ["www.google.com", "www.youtube.com", "www.github.com", "www.twitter.com"]
    rand_web = Web_sites[random.randint(0, len(Web_sites) - 1)]
    webbrowser.open(rand_web)
elif "hi" or "hello" in x.lower():
    assistantresponse("Hi there ! I am Allison How can I help You ?")

elif "empty" in x.lower():
    winshell.recycle_bin().empty(confirm=False,
                                 show_progress=False, sound=True)
    print("Recycle Bin Empty!!")



