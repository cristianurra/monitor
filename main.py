import gspread
import datetime 
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
    now=datetime.now()
    if True: #int(now.minute)==00:
        print("Registrando datos")
        sheet.update_cell(hora_absoluta()-1620,2 , "aaa") #fila,columna
        time.sleep(5)
