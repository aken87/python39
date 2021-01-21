import pyowm

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

# ---------- FREE API KEY examples ---------------------
owm = OWM('f4d76c17533dc5e00068faffb70afb12')
mgr = owm.weather_manager()

place = input("В каком городе/стране? ")

observation = mgr.weather_at_place(place)
w = observation.weather


temp = w.temperature('celsius')["temp"]

print("В городе " + place + " сейчас: " + w.detailed_status)
print("Температура воздуха: " + "℃"+str(temp) + " По цельсию")

if temp < 10:
    print("Сейчас холодно, оденься теплее.")
elif temp < 20:
    print("Прохладно.")
else:
    print("Температура нормальная")
