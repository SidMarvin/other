# -*- coding: utf-8 -*-

"""
sudo apt install -y python3-pip && sudo apt-get install -y minicom && sudo apt-get install -y portaudio19-dev && sudo apt install -y espeak&& sudo apt-get install scons gcc flite flite1-dev expat libunistring-dev libsox-dev && sudo apt-get install -y libasound-dev && sudo apt-get install -y libpulse-dev libao-dev && apt-get install -y scons && apt-get install -y git && pip3 install pyserial && pip3 install SpeechRecognition && pip3 install pyttsx3 && pip3 install pyaudio && sudo git clone --recursive https://github.com/Olga-Yakovleva/RHVoice && cd RHVoice && sudo scons && sudo scons install && sudo ldconfig
"""

import serial
import pyttsx3
import pyaudio
import speech_recognition
import speech_recognition as sr
import os
import threading
import subprocess

#инициация списка с именами
#тут могла бы быть база данных
names = []
with open("bd.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line)
names = [str[:-1] for str in names]
#print(names)

#настройки COM-порта
ser = serial.Serial("/dev/ttyACM0")
ser.baudrate = 115200

#АТ-команды
msg1 = "AT+FCLASS=8\r\n" #перевод модема в голосовой режим
msg2 = "AT+VLS=13\r\n" #поднять трубку
msg3 = "ATZ\r\n" #положить трубку
msg4 = "AT\r\n" #проверочная команда

#голосовые ответы
echo = "echo "
command = "| RHVoice-test -p anna"
message_1 = "Здравствуйте. Вас приветствует справочная компании ЧТК. Громко и ч>
message_2 = "Вы сказали "
message_3 = "Телефон "
message_4 = "Данный человек не найдет в базе данных. Повторите запрос четчте"

#ser.write(msg1.encode())
#print("Модем переведен в голосовй режим")

#настройка озвучивания речи
#tts = pyttsx3.init()
#voices = tts.getProperty('voices')
#tts.setProperty('voice', 'ru') #язык
#tts.setProperty('volume', 5.0) #громкость

#функция распознавани речи
def call():
    while True:
        m = sr.Microphone()
        r = sr.Recognizer()
        with m as source:
            print("Скажи что-нибудь")
            audio = r.listen(source)
        query = r.recognize_google(audio, language="ru-RU")
        query_min = query.lower()
        print("Вы сказали " + query_min)
        message = echo + message_2 + query_min + command
        print(message)
        os.system(message)

        if query_min == "алло":
            message = echo + "ну тебе тоже алло тогда" + command 
            print(message)
            os.system(message)

        elif query_min == "привет":
            message = echo + "привет в ответ" + command
            print("Собеседник поприветствовал вас")
            os.system(message)

        elif query_min in names:
            tel_index = names.index(query_min) + 1
            tel_number = names[tel_index]
            print(tel_number)
            message = echo + message_3 + tel_number + command
            print(message)
            os.system(message)

        else:
            print("Сообщение не распознано")
            message = echo + message_4 + command
            os.system(message)

#for voice in voices:
#    ru = voice.id.find('RHVoice\Anna')
#   if ru > -1:
#        tts.setProperty('voice', voice.id)

def main_function():
    try:
        print("Инициация...")
        while True:
            line = ser.readline()
            print(line)
            if line == b'RING\r\n':
                print("Вам звонят!")
                ser.write(msg1.encode())
                print("Модем переведен в голосовой режим")
                break
        while True:
            line = ser.readline()
            print(line)
            if line == b'\x10R\r\n':
                ser.write(msg2.encode())
                print("Трубка поднята")
                message = echo + message_1 + command
                print(message)
                os.system(message)
                # tts.say("Здравствуйте. Вас приветствует электронная справочна>
                print("Произнесена фраза")
                call()
    except speech_recognition.UnknownValueError:
        print("Кладу трубку")
        ser.write(msg3.encode())
        main_function()



subprocess.Popen(["pulseaudio"]) # запуск команды в фоновом режиме
main_function()
