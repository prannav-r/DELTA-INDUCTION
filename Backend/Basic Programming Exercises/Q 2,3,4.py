# Program to implement language translator program

import googletrans
lng=googletrans.LANGUAGES
from googletrans import Translator
translator = Translator()


def toeng():
    x=input("Enter your sentence: ")
    y=translator.translate(x)
    print("This sentence translates to: ",y.text)

def src():
    x=input("Enter your sentence: ")
    a=input("Enter the code of your preferred language: ")
    y=translator.translate(x, dest = a)
    print("The sentence in",lng[a],"is: ",y.text)

def detect():
    x=input("Enter your sentence: ")
    y=translator.detect(x)
    print("This sentence is in: ",lng[y.lang])

#Main Program

while True:
    print("Main Menu")
    print("1.Translate to English")
    print("2.Translate to your preferred language")
    print("3.Detect the language of the sentence")
    x=int(input("Enter the number of your choice:"))
    if x==1:
        toeng()
    elif x==2:
        src()
    elif x==3:
        detect()
    else:
        print("Invalid Choice!")

    ch=input("Do you want to continue?(y/n)")
    if ch.lower()=='y':
        continue
    else:
        break