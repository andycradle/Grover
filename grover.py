from pyrogram import * 
import time
import pyfiglet
import os
from colorama import Fore

os.clear()
print(Fore.GREEN)
print(pyfiglet.figlet_format("Grover"))
print('-------------------------------')
print("Create by ELVIN\nИнструкция по импользыванию: https://telegra.ph/Rassylka-soobshchenij-telegram-01-10")
print('-------------------------------')

# Твои данные
api_id = input("Введите api_id: ")
api_hash = input("Введите api_hash: ")
print('-------------------------------')

session_name='save'
app = Client(session_name, api_id, api_hash)
app.start()
 
# текст
text = input("Введите текст: ")
print('-------------------------------')

# ид чатов
id1 = input('Введите ID чата: ')
id2 = input('Введите ID чата 2(если нет введите: n): ')
id3 = input('Введите ID чата 3(если нет введите: n): ')
id4 = input('Введите ID чата 4(если нет введите: n): ')
id5 = input('Введите ID чата 5(если нет введите: n): ')
id6 = input('Введите ID чата 6(если нет введите: n): ')
id7 = input('Введите ID чата 7(если нет введите: n): ')
id8 = input('Введите ID чата 8(если нет введите: n): ')
id9 = input('Введите ID чата 9(если нет введите: n): ')
id10 = input('Введите ID чата 10(если нет введите: n): ')
print('-------------------------------')

# Время слоумода
try:
    slowmode = int(input("Введите время слоумода(в секундах): "))
except:
    slowmode = int(input("Введите время слоумода(в секундах,не используйте буквы!): "))
print('-------------------------------')
    
# Отправка сообщений
print("Рассылка началась")
while True:
    app.send_message(id1,text)
    if id2 != "n":
    	app.send_message(id2,text)
    elif id3 != "n":
    	app.send_message(id3,text)
    elif id4 != "n":
    	app.send_message(id4,text)
    elif id5 != "n":
    	app.send_message(id5,text)
    elif id6 != "n":
    	app.send_message(id6,text)
    elif id7 != "n":
    	app.send_message(id7,text)
    elif id8 != "n":
    	app.send_message(id8,text)
    elif id9 != "n":
    	app.send_message(id9,text)
    elif id10 != "n":
    	app.send_message(id10,text)
    
    # Слоумод
    time.sleep(slowmode)
    
app.stop()
