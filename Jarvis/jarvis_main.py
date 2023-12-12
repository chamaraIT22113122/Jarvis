import os
import time
import webbrowser
import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import requests
import bs4


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning, sir")
    elif 12 <= hour < 18:
        speak("Good Afternoon, sir")
    else:
        speak("Good Evening, sir")

    speak("Please tell me, how can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again, please.")
        return "None"
    return query.lower()

if __name__ == "__main__":
    while True:
        query = take_command()
        if "wake up" in query:
            greet_me()

            while True:
                query = take_command()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime")
                    break
                elif "hello" in query:
                            speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                            speak("that's great, sir")
                elif "how are you" in query:
                            speak("Perfect, sir")
                elif "thank you" in query:
                            speak("you are welcome, sir")

                elif "who are you" in query:
                    speak('My Name Is jrvis')
                    print('I can Do Everything that my creator programmed me to do')
                    speak('I can Do Everything that my creator programmed me to do')
 
                elif "who created you" in query:
                    speak('My creater is Master chamara nuwan bandara')

############################ ((desktop shortcuts)) ################################

############################ IP Address ################################
                        
                elif "what is my ip address" in query:
                    speak("Checking")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text
                        print(ipAdd)
                        speak("your ip adress is")
                        speak(ipAdd)
                    except Exception as e:
                        speak("network is weak, please try again some time later")

############################ VOLUME UP/DOWN/MUTE ################################

                elif "volume up" in query:
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        pyautogui.press("volumeup")
                        
                elif "volume down" in query:
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        pyautogui.press("volumedown")
                        
                elif "mute" in query:
                        pyautogui.press("volumemute")
                        speak("volume is mute")

############################ REFRESH ################################

                elif "refresh the desktop" in query:
                       pyautogui.hotkey('win', 'f5')
############################   CLEAR DESKTOP ################################

                elif "clear the desktop" in query:
                       pyautogui.hotkey('win', 'd')
                       

############################   SWITCH APPS ################################

                elif "switch app" in query:
                       speak("switching")
                       pyautogui.hotkey('alt', 'tab')

############################   SWITCH APPS ################################

                elif "switch tab" in query:
                       speak("switching tabs")
                       pyautogui.hotkey('ctrl', 'tab')

############################  Save  ################################

                elif "save" in query:
                       speak("saving the project")
                       pyautogui.hotkey('ctrl', 's')

############################  PRINT  ################################

                elif "print" in query:
                       pyautogui.hotkey('ctrl', 'p')

############################  SELLECT ALL  ################################

                elif "select all " in query:
                       pyautogui.hotkey('ctrl', 'a')

############################  TYPING  ################################

                elif 'type' in query:
                      speak("typing")
                      query=query.replace("type","")
                      pyautogui.typewrite(f"{query}",0.1) 

############################  ENTER  ################################

                elif "press enter" in query.lower():
                       pyautogui.press('enter')

############################  WINDOW LEFT/RIGHT  ################################

                elif "window left " in query:
                       pyautogui.hotkey('win', 'left')


############################  OPENING APPS  ################################
                ##PHOTOSHOP##
                elif'open photoshop' in query:
                     speak("Launching, sir")
                     os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 2022')
                elif 'close photoshop' in query:
                     speak("Closing,sir")
                     os.system("taskkill /f /im Photoshop.exe")

                elif 'open chat gpt' in query:
                    speak("opening chatgtp")
                    url = 'https://chat.openai.com'  # Replace this with your desired URL
                    webbrowser.open(url)


                ##Downloads##
                elif 'open download folder' in query.lower():
                    speak("Launching, sir")
                    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
                    os.startfile(downloads_path)



                ##OTHER##

                elif 'google search' in query:
                    query = query.replace("google search", "")
                    pyautogui.hotkey('alt', 'd')
                    pyautogui.write(f"{query}", 0.1)
                    pyautogui.press('enter')

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                
                elif "google" in query:
                            from SearchNow import searchGoogle
                            searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

############################ TEMPERATURE/WEATHER ################################

                elif "temperature" in query:
                    search = "temperature is"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = bs4.BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")


                elif "weather" in query:
                    search = "temperature is"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = bs4.BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")




                elif "find" in query.lower():
                    query = query.replace("find", "").strip()
                    os.startfile('::{20D04FE0-3AEA-1069-A2D8-08002B30309D}')
                    time.sleep(1)  # Wait for the File Explorer to open
                    pyautogui.hotkey('F3',)  # Open File Explorer (Windows + E)
                    time.sleep(1)  # Wait for the File Explorer to open
                    pyautogui.write(query)  # Type the folder name to search
                    time.sleep(1)  # Wait for typing
                    pyautogui.press('enter')  # Perform the search by pressing Enter 

 ############################ Chrome Automation ################################
                
                elif 'get new window' in query:
                     pyautogui.hotkey('ctrl', 'n')

                elif 'get incognito window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'n')

                elif 'get history' in query:
                    pyautogui.hotkey('ctrl', 'h')

                elif 'g downloads' in query:
                    pyautogui.hotkey('ctrl', 'j')

                elif 'previous tab' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'tab')

                elif 'next tab' in query:
                    pyautogui.hotkey('ctrl', 'tab')

                elif 'close tab' in query:
                    pyautogui.hotkey('ctrl', 'w')

                elif 'close window' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'w')

                elif 'clear browsing history' in query:
                    pyautogui.hotkey('ctrl', 'shift', 'delete')
               
############################ Exit ################################

                elif "jarvis sleep" in query:
                    speak("Going to sleep,sir")
                    exit()


