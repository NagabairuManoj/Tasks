import speech_recognition as sr
import os
import webbrowser as wb
import pyttsx3 as pt

def sp() :
	a = sr.Recognizer()
	with sr.Microphone() as source:
		print("start saying")
		a.adjust_for_ambient_noise(source)
		audio = a.listen(source)
		print("OK I got it")
	 
		ch = a.recognize_google(audio,show_all=True)
		X = ch['alternative']
		ch = X[0]['transcript']
		return(ch)

pt.speak("Welcome to Kiti")
pt.speak("please enter ur name")
a = input()
pt.speak("Hello %s" %(a))
pt.speak("How are you")
b = sp()
if "good" in b or "fine" in b :
	pt.speak("I will keep that smile on ur face in the same way all over my work")
else:
	pt.speak("I will try to relax u with my work")
pt.speak("where do u want to work either in local or remote")
c = sp()
if "local" in c :
	print("local")
	while True:
		pt.speak("How can I help you")
		d = sp()
		if "thanks" in d:
			break
		elif ("show" or "what") and "date" in d :
			os.system("date")
		elif "search" in d :
			wb.open("https://www.google.com/search?q={}&oq={}&aqs=chrome..69i57j69i65l3j5l3.703j0j7&sourceid=chrome&ie=UTF-8".format(d[13:-11],d[13:-11]))


elif "remote" in c :
	print("remote")
	pt.speak("enter the ip where u want to work")
	ip = input()
	pt.speak("How can I help you")
	e = sp()
	if ("show" or "what") and "date" in e :
		os.system('"ssh root@%s "espeak-ng `date +%A` ""  %(ip)')
		os.system('"ssh root@%s "espeak-ng `date +%d` ""  %(ip)')
		os.system('"ssh root@%s "espeak-ng `date +%B` ""  %(ip)')
		os.system('"ssh root@%s "espeak-ng `date +%Y` ""  %(ip)')
	elif "open" and "firefox" :
		os.system("ssh root@{} 'firefox'".format(ip))
			
else :
	print("not supported")

