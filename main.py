import pyttsx3, speech_recognition as sr
import time, pytz, subprocess, os
import datetime, pickle, os.path
import wikipedia, pyjokes, random
import webbrowser

class pith:
    def __init__(self):
        self.master = 'Pradeep  Raj'
        self.wake = 'hey pith'
        self.google = ['open chrome','open google','open browser']
        self.telljoke = ['ok tell me a joke','tell me a joke','one more joke','joke']
        self.TakeNotes = ['take notes',"make a note", "write this down", "remember this"]
        self.ready = ['Yes','I am there']
        self.time = ['What is the time now','time','what\'s the time']
        self.song = ['play song','play music']
        self.wiki = ['according to wikipedia','tell about']
        self.inquire = ["whats up" , 'what about you' , 'how are you' , 'how about you' , 'how was your day' , 'are you worrying']
        self.jsttalk = ['do you eat' , 'do you want food' , 'do you want coffee' , 'take a tea' , 'do you want tea','do you have a girlfriend']
        self.hi = ['hi' , 'hi pic' , 'hi pit' , 'hi pith' , 'hello']
        self.gotHi = ['nice' , 'i am fine' , 'fine']
        self.here = ['what are you doing','are you there',]
        self.name = ['you name','tell me your name' , 'what is your name']
        self.stop = ['take rest','ok take rest','shutdown program pith','break yourself']
    
    def speak(self,text,rate=200): 
        engine = pyttsx3.init()
        # id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
        # engine.setProperty('voices', id)
        engine.setProperty('rate', rate)
        engine.say(text)
        engine.runAndWait()
        
    def getAudio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print('[LISTENING] >> ')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print('[RECOGNIZING] :) ')
            text = r.recognize_google(audio)
            print(f'[IP] : {text}\n')
        except Exception as e:
            print('[RECOGNITION ERROR] :(' + str(e)) 
            return 'none'
            
        return text.lower()    
        
    def welcome(self):
        master = 'Pradeep Sir'  
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak('Good Morning' + master)
        elif hour >= 12 and hour <= 16:
            self.speak('Good Afternoon' + master)
        else:
            self.speak('Good Evening' + master)
        self.speak('Your System is ready to access...')
        
    def joke(self):
        joke = pyjokes.get_joke(language='en')
        print(joke)
        self.speak(joke,rate=140)
        time.sleep(2)
        ee = ['ha ha, I think it was hilarious', 'Nice joke yaar']
        self.speak(random.choice(ee),rate=145)
        
    def takeNotesOnPad(self,notes):
        date = datetime.datetime.now()
        file = str(date).replace(":", "-") + "-notes.txt"
        with open(file,'w') as f:
            f.write(notes)
        subprocess.Popen(['notepad.exe',file])
        
    def start(self):
        start = 'Initializing Pith..,'
        print(start)
        self.speak(start)
        self.welcome()
        while True:
            command = self.getAudio()
                
            if command in self.TakeNotes:
                self.speak('Sir,What would you like me to write down?')
                notes = self.getAudio()
                self.takeNotesOnPad(notes)
                self.speak("I've made a note of that.")
                
            if command in self.wiki:
                result = wikipedia.summary(command,sentences=3)
                wiki = 'According to wikipedia..,'
                print(wiki)
                self.speak('Sir' + wiki)
                print(result)
                self.speak(result)
                
            if command in self.google:
                webbrowser.open("google.com")
                self.speak('Sir,Opening Chrome')
            
            if command in self.telljoke:
                self.joke()
        
            if command in self.inquire:
                msg = ['Just doing my thing!', 'I am fine !', 'Nice!', 'I am nice sir and full of energy']
                self.speak(random.choice(msg))
            
            elif command in self.jsttalk:
                self.speak('No..,')
                
            elif command in self.hi:
                msga = ['hi' , 'hi,how about you','hi,how was your day']
                self.speak(random.choice(msga))
                
            elif command in self.gotHi:
                self.speak('Nice to hear.,')
                
            elif command in self.time:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                self.speak(f"Sir, the time is {strTime}")
                
            elif command in self.here:
                self.speak('Yeah, I am waiting for your command')
                
            elif command in self.name:
                print('P.I.T.H')
                self.speak('I am Pith')
                
            elif command in self.song:
                dir = "P:/Songs"
                songs = os.listdir(dir)
                os.startfile(os.path.join(dir,songs[random.randint(1, 10)]))
                self.speak('Sir,Playing Songs')
                
            elif command in self.stop:
                self.speak('Ok Sir I am going down')
                self.speak('Bye')
                break
                
            elif 'none' in command:
                print('-'*8)
                
pith().start()