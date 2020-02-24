# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:34:53 2020

@author: vaish
"""

import speech_recognition as sr
from gtts import gTTS 
  
# import Os module to start the audio file
import os
import socket


r = sr.Recognizer()
with sr.Microphone() as source:
    print("        Welcome to the Voice Recognition Module!")
    print("Speak Anything:")
    print("Give a try")
   
    audio = r.listen(source)
    
    try:
        
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        port = 3
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.43.51",50001))
        
        new=text
        
        s.send(bytes(text, 'UTF-8'))
        
        print(" Here are my commands: You can tell:\n 1.Turn left \n 2.Turn Right \n 3.Move Forward \n 4.Move Backward")
        while text!='quit':
             audio = r.listen(source)
             try:
                 text = r.recognize_google(audio)
                 if text=='turn left':
                     new1=text
                     s.send(bytes(text, 'UTF-8'))
                     print("Your car will turn left!")
                     fh = open("leftturn.txt", "r")
                     myText = fh.read().replace("\n", " ")
                     language = 'en'
                     output = gTTS(text=myText, lang=language, slow=False)
                     output.save("output.mp3")
                     os.system("start output.mp3")
                     fh.close()
                 elif text=='turn right':
                     new2=text
                     s.send(bytes(text, 'UTF-8'))
                     print("Your car will turn right!")
                     fh = open("rightturn.txt", "r")
                     myText = fh.read().replace("\n", " ")
                     language = 'en'
                     output = gTTS(text=myText, lang=language, slow=False)
                     output.save("output.mp3")
                     os.system("start output.mp3")
                     fh.close()
                 elif text=='move forward':
                     new3=text
                     s.send(bytes(text, 'UTF-8'))
                     print("Your car will move forward!")
                     fh = open("forward.txt", "r")
                     myText = fh.read().replace("\n", " ")
                     language = 'en'
                     output = gTTS(text=myText, lang=language, slow=False)
                     output.save("output.mp3")
                     os.system("start output.mp3")
                     fh.close()
                 elif text=='move backward':
                     new4=text
                     s.send(bytes(text, 'UTF-8'))
                     print("Your car will move backward!")
                     fh = open("backward.txt", "r")
                     myText = fh.read().replace("\n", " ")
                     language = 'en'
                     output = gTTS(text=myText, lang=language, slow=False)
                     output.save("output.mp3")
                     os.system("start output.mp3")
                     fh.close()
                     
                 else:
                     fh = open("nocommand.txt", "r")
                     myText = fh.read().replace("\n", " ")
                     language = 'en'
                     output = gTTS(text=myText, lang=language, slow=False)
                     output.save("output.mp3")
                     os.system("start output.mp3")
                     fh.close()
                     print("You said : {}\n which is not in my command list!".format(text))
             except:
                 s.close()
                 exit()
                 
    except:
         print("I couldn't recognise what you are telling")
        
                
        
                
       
    
            
        
        
    

