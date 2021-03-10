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


def hora_absoluta():
    now = datetime.now()
    date_val = date(now.year, now.month, now.day)
    day_of_year = date_val.strftime('%j')
    hour_of_year=int(day_of_year)*24+int(now.hour)
    return(hour_of_year)

def minuto_absoluto():
    return(int(hora_absoluta*60))
    
st="Null"
dt="Null"
ot="Null"
it="Null"
c1="Null"
c2="Null"
c3="Null"
c4="Null"
while True:

    os.system("reset")
    try:
        dataserial = serial.Serial('/dev/ttyUSB0', baudrate=500000, timeout=1)
        time.sleep(1)
        elementos=dataserial.readline().split()
    except:
        pass

    try:
        dataserial = serial.Serial('/dev/ttyUSB1', baudrate=500000, timeout=1)
        time.sleep(1)
        elementos=dataserial.readline().split()
    except:
        pass
   
   
    for entrada in elementos:
        if "t0f" in entrada:
            entrada=entrada.replace("t0f","")
            entrada=float(entrada)
            st=entrada

    for entrada in elementos:
        if "t1f" in entrada:
            entrada=entrada.replace("t1f","")
            entrada=float(entrada)
            dt=entrada

    for entrada in elementos:
        if "t2f" in entrada:
            entrada=entrada.replace("t2f","")
            entrada=float(entrada)
            ot=entrada

    for entrada in elementos:
        if "t3f" in entrada:
            entrada=entrada.replace("t3f","")
            entrada=float(entrada)
            it=entrada           
            
    for entrada in elementos:
        if "t4f" in entrada:
            entrada=entrada.replace("t4f","")
            entrada=float(entrada)
            c1=entrada
            
    for entrada in elementos:
        if "t5f" in entrada:
            entrada=entrada.replace("t5f","")
            entrada=float(entrada)
            c2=entrada            

    for entrada in elementos:
        if "t6f" in entrada:
            entrada=entrada.replace("t6f","")
            entrada=float(entrada)
            c3=entrada              
            
    for entrada in elementos:
        if "t7f" in entrada:
            entrada=entrada.replace("t7f","")
            entrada=float(entrada)
            c4=entrada   

    for entrada in elementos:
        if "t8f" in entrada:
            entrada=entrada.replace("t8f","")
            entrada=float(entrada)
            hhh=entrada   

    for entrada in elementos:
        if "t9f" in entrada:
            entrada=entrada.replace("t9f","")
            entrada=float(entrada)
            hhh=entrada               
                       
    now=datetime.now()
    if True: #int(now.minute)==00:
        fecha="{}-{}-{}".format(now.year,now.month,now.day)
        hora="{}:{}:{}".format(now.hour,now.minute,now.second)

        print(hora_absoluta())
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
