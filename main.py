import gspread
import serial
import datetime 
import os
import time
from datetime import datetime
from datetime import date
from datetime import datetime, timedelta 
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
client = gspread.authorize(creds)
sheet = client.open("friser2").sheet1


#list_of_hashes = sheet.get_all_records()


def registrar_now(compresor,dato,tipo):  #recibe del tipo (int,x,n) y lo registra en la tabla correspondiente
    now = datetime.now()
    current_hour = int(now.strftime("%H"))
    columna=current_hour+2
    sett=(compresor*12)-7
    fila=sett+dato
    sheet.update_cell(fila,columna,"hola")
    print(fila,columna)

def hora_absoluta():
    now = datetime.now()
    date_val = date(now.year, now.month, now.day)
    day_of_year = date_val.strftime('%j')
    hour_of_year=int(day_of_year)*24
    return(hour_of_year)


while True:
    os.system("reset")
    try:
        dataserial = serial.Serial('/dev/ttyUSB0', baudrate=500000, timeout=1)
        time.sleep(1)
        elemento=dataserial.readline().split()
    except:
        pass

    try:
        dataserial = serial.Serial('/dev/ttyUSB1', baudrate=500000, timeout=1)
        time.sleep(1)
        elemento=dataserial.readline().split()
    except:
        pass
        
    print(elemento)
    now=datetime.now()
    if True: #int(now.minute)==00:
        fecha="{}-{}-{}".format(now.year,now.month,now.day)
        hora="{}:{}:{}".format(now.hour,now.minute,now.second)
        st=0
        dt=0
        ot=0
        it=0
        c1=0
        c2=0
        c3=0
        c4=0
        
        print("Registrando datos")
        
        sheet.update_cell(hora_absoluta()-1648,2 , fecha) #fila,columna
        sheet.update_cell(hora_absoluta()-1648,3 , hora)
        sheet.update_cell(hora_absoluta()-1648,4 , st)
        sheet.update_cell(hora_absoluta()-1648,5 , dt)
        sheet.update_cell(hora_absoluta()-1648,6 , ot)
        sheet.update_cell(hora_absoluta()-1648,7 , it)
        sheet.update_cell(hora_absoluta()-1648,8 , c1)
        sheet.update_cell(hora_absoluta()-1648,9 , c2)
        sheet.update_cell(hora_absoluta()-1648,10 , c3)
        sheet.update_cell(hora_absoluta()-1648,11, c4)
        print("Ultimo registro: {}-{}-{} a las {}:{}:{}".format(now.year,now.month,now.day,now.hour,now.minute,now.second))
        time.sleep(20)
