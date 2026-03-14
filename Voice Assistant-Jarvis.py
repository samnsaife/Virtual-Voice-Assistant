import wolframalpha
import wikipedia
client=wolframalpha.Client("6HUYPY-KA2RXHHV27")

import PySimpleGUI as sg
import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.say("Hello Sir, My Name Is Jarvis, What Can I Do For You?")
engine.runAndWait()

sg.theme('DarkRed')
layout=[[sg.Text("ENTER COMMAND"), sg.InputText()],[sg.Button('OK'),sg.Button('Cancel')]]
window=sg.Window("JARVIS",layout)


while True:
    event,values=window.read()
    if event in (None,'Cancel'):
        engine.say("Have A Good Day Sir.")
        engine.runAndWait()
        break
    try:
        res=client.query(values[0])
        wolfram_res=next(res.results).text
        engine.say("Result Is, "+wolfram_res)
        engine.runAndWait()
        sg.Popup(wolfram_res)


    except:
        wiki_res=wikipedia.summary(values[0],sentences=2)
        engine.say(" Result Is, "+wiki_res)
        engine.runAndWait()
        sg.Popup(wiki_res)
window.close()
