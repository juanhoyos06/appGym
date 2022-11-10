from datetime import date
"""from datetime import datetime
from datetime import timedelta
import calendar
from deep_translator import GoogleTranslator


#Obtener numero del dia actual
today = date.today()
#Obtener numero del dia siguiente
new_day = today + timedelta(days=1)
#print("El día actual es {}".format(today.day))
#print("El día de mañana es {}".format(new_day.day))
#
#print("El mes actual es {}".format(today.month))
#Dia en letras
traductor = GoogleTranslator(source='en', target='es')
nombre_dia = traductor.translate(calendar.day_name[today.weekday()])
mesActual = traductor.translate(calendar.month_name[today.month])
nombreDiaSiguiente = traductor.translate(calendar.day_name[new_day.weekday()])


#print(mesActual)
#print(nombreDiaSiguiente)
fecha = datetime.now()
print(fecha+timedelta(days=1))
print(datetime.strftime(datetime.now(),"%d-%m-%y"))
"""
usuario = []

if usuario:
    print("hi")
else:
    print("Error")