import speech_recognition as sr #importa a biblioteca
import pyttsx3

listener = sr.Recognizer() #configurar reconhecimento
engine = pyttsx3.init()
voices = engine.getProperty('voices') #define a voz jarvis
def talk(text):
    engine.setProperty('voice', voices[1].id) #altera a voz do jarvis
    engine.say(text)
    engine.runAndWait()
try:
    with sr.Microphone() as source: #inicia o microfone
        print('listen....') #imprime que esta escutando
        voice = listener.listen(source) #salva o que foi dito
        command = listener.recognize_google(voice) #fala o que foi dito
        command = command.lower() #deixa tudo em caixa alta
        if 'mark' in command: #ativa o jarvis

            talk(command) #repete o que foi dito
except:
    pass