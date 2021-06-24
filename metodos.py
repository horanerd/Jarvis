import speech_recognition as sr #importa a biblioteca
import pyttsx3

engine = pyttsx3.init()
listener = sr.Recognizer() #configurar reconhecimento

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:  # inicia o microfone
            print('listen....')  # imprime que esta escutando
            voice = listener.listen(source)  # salva o que foi dito
            command = listener.recognize_google(voice, language='pt-BR')  # fala o que foi dito
            command = command.lower()  # deixa tudo em caixa alta

    except:
        pass
    return command

def Repet_command():
    try:
        with sr.Microphone() as source: #inicia o microfone
            print('listen....') #imprime que esta escutando
            voice = listener.listen(source) #salva o que foi dito
            command = listener.recognize_google(voice, language='pt-BR') #fala o que foi dito
            command = command.lower() #deixa tudo em caixa alta

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    if 'jarvis' in command:  # ativa o jarvis
        # command = command.replace('jarvis', '')
        # a = "command javis que horas é"
        # teste = a.sprit("jarvis")
        a = "Hello World! jarvis como estamos"
        b = command.split("jarvis")
        print (b[1])

run_jarvis()

# a = "Hello World! jarvis como estamos"
# b = a.split("jarvis")
# print(b[1])