import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Tarvis Sir. Please tell me how may I help you")       

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    flag = False
    while (not flag):
        input_=input("Please Enter the command: ")
        query = input_.lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        elif 'movies' in query:
            select= input("Enter Holly for Holleywood bolly for Bolleywood south for South indian and web for Webseries: ").lower()
            if 'holly' in select:
                path1= "F:\Config\HOLLYWOOD"
                os.startfile(path1)
            elif 'bolly' in select:
                path2 = "F:\Config\BOLLYWOOD"
                os.startfile(path2)
            elif 'south' in select:
                path3 = "F:\Config\SOUTH"
                os.startfile(path3)

            elif 'web' in select:
                path4 = "F:\Config\Web Series"
                os.startfile(path4)

            else:
                speak("Sorry, i can find that")

        elif 'iic' in query:
            path4 = "G:\IIC"
            os.startfile(path4)

        

        elif 'music' in query:
            select1 = input("Enter the eng for English song hin for Hindi song nep for Nepali song ply for plylists: ").lower()
            if 'eng' in select1:
                music_dir = 'E:\Music\English_song'
                songs = os.listdir(music_dir)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
            elif 'hin' in select1:
                music_dir = 'E:\Music\Hindi_song'
                songs = os.listdir(music_dir)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                
            elif 'nep' in select1:
                speak("i cannot able to play nepali song because of langauge but i can able to open the folder of nepali song.")
                path = "E:\Music"
                os.startfile(path)
           
            elif 'ply' in select1:
                music_dir = 'E:\Music\Playlists'
                songs = os.listdir(music_dir)    
                os.startfile(os.path.join(music_dir, songs[0]))
                             
            else:
                speak("sorry the command you enter is not found")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "G:\IIC\Code"
            os.startfile(codePath)

        
        elif 'exit' in query:
            speak("Thanks for using our service Tarvis")
            flag = True

        elif 'list' in query:
            print(" wikipedia\n music\n time\n open code\n exit\n iic\n email\n movies\n youtube\n google\n stackoverflow\n")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = input("Enter the content: ")
                to = input("Enter the email address: ")    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry i cannot able to send this email")    

        else:
            speak("The command you enter is not found")
        
        
