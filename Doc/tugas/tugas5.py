import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Katakan sesuatu!")
    audio = r.listen(source)

try:
    print("Anda berkata: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition tidak mengerti yang anda katakan")
except sr.RequestError as e:
print("Tidak ada perkataan dari Google Speech Recognition service; {0}".format(e))