import speech_recognition as sr

listner = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listning....')
        voice = listner.listen(source)
        command = listner.recognize_google(voice)
        command =  command.lower()
        if 'alexa' in command:
            print(command)
except:
    pass