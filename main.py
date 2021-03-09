import gspread
import datetime 
from datetime import datetime
from datetime import date
from datetime import datetime, timedelta 
from oauth2client.service_account import ServiceAccountCredentials


# use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
#creds = ServiceAccountCredentials.from_json_keyfile_name('key.json', scope)
#client = gspread.authorize(creds)
#sheet = client.open("friser2").sheet1


#list_of_hashes = sheet.get_all_records()
#sheet.update_cell(12, 12, "aaa")

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



