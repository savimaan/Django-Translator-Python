from django.shortcuts import render
from django.http import HttpResponse
import pip
from tkinter import *
from playsound import playsound
import pyttsx3 as pt
import os
from time import sleep
import tkinter as tk
from tkinter import ttk
from translate import Translator
from tkinter import *
from langdetect import detect

# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'SAVITA'})


def add(request):
    val1 = (request.GET['num1'])
    val2 = (request.GET['num2'])
    val3 =(request.GET['result'])
    translator= Translator(from_lang=val1,to_lang=val2)
    translation = translator.translate(val3)
    print(translation)
    return render(request, "result.html", {'result': translation}) 

import gtts  
import os
def play(request):    
    language = (request.GET['num1'])
    text_user= (request.GET['num2'])
    tts = gtts.gTTS(text =text_user,
                lang =language, 
                slow = False)
    tts.save("hello.mp3")
    os.system("start hello.mp3") 
    return render(request, "result.html", {'result': tts}) 

import speech_recognition as SRG 
def speak(request):
    import time 
    store = SRG.Recognizer()
    with SRG.Microphone() as s:
        print("Speak...")
        audio_input = store.record(s, duration=7)
        print("Recording time:",time.strftime("%I:%M:%S"))
        text_output = store.recognize_google(audio_input)
        try:
            text_output = store.recognize_google(audio_input)
            print("Text converted from audio:\n")
        except:
            print("Sorry, I did not get that")   
    return render(request,"result.html",{'result':text_output})      