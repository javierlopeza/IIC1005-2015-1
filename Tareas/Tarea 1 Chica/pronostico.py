import  pywapi
import datetime
import smtplib
weather_com_result = pywapi.get_weather_from_weather_com('CIXX0020')
dia = str(datetime.date.today())[8:]
mes = str(datetime.date.today())[5:7]
a = str(datetime.date.today())[:4]
hoy = "Fecha de hoy: "+dia+"/"+mes+"/"+a+"\n"
ciudad = "Pronostico para la ciudad de Santiago, Chile.\n"
minima = ("Temperatura minima pronosticada: " + (weather_com_result['forecasts'][0]['low']) + "C\n")
maxima = ("Temperatura maxima pronosticada: " + (weather_com_result['forecasts'][0]['high']) + "C")
archivo = open("pronostico.txt","w")
archivo.write(hoy)
archivo.write(minima)
archivo.write(maxima)
archivo.close()

import email
import smtplib
msg = email.message_from_string(hoy+ciudad+minima+maxima)
msg['From'] = "javierlopez_iic1005@hotmail.com"
msg['To'] = "javierlopez_iic1005@hotmail.com"
msg['Subject'] = "Aviso Temperaturas ("+(dia+"/"+mes+"/"+a)+")"
s = smtplib.SMTP("smtp.live.com",587)
s.ehlo()
s.starttls() 
s.ehlo()
s.login('javierlopez_iic1005@hotmail.com', 'Javieriic1005')
s.sendmail("javierlopez_iic1005@hotmail.com","javierlopez_iic1005@hotmail.com", msg.as_string())
s.quit()
