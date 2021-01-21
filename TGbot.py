import telebot
import pyowm
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("1113752141:AAEA0gXmn4LrQtgDx1smCsNocZ80KPZtshI")
owm = OWM('f4d76c17533dc5e00068faffb70afb12')
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru' 

@bot.message_handler(content_types=['text'])
def echo_all(message):
	#bot.reply_to(message, message.text)
        observation = mgr.weather_at_place( message.text )
        w = observation.weather
        temp = w.temperature('celsius')["temp"]
        wind = w.wind() ["speed"]

        answer = "В городе " + message.text + " сейчас: " + w.detailed_status + "\n"
        answer += "Температура воздуха: " + "℃ "+str(temp) + "" + "\n"
        answer += "Скорость ветра " + str(wind) + " м/с" + "\n\n"
	
        if temp < 10:
            answer += "Сейчас холодно"
        elif temp < 20:
            answer += "Прохладно"
        else:
            answer += "Температура нормальная"
        bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)
