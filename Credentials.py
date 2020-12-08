
 --------------- CONTA DEMO -------------------------
import os

conn_type = "demo"

if conn_type == "demo":

   directory = os.path.join(os.path.expanduser("~"), "Desktop")
   login = ***  #int type
   password = '***' #str type
   server = 'CLEAR-Demo'
   timeout = ''
   portable = ''

log_info = {
   'path': directory,
   'login': login,
   'password': password,
   'server': server,
   'timeout': timeout,
   'portable': portable
            }