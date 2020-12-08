conn_type = "demo"

import MetaTrader5 as mt5
import Connection as conn
import Functions as func
from time import sleep

tt = ['VVAR3', 'CIEL3']

conn.meta5_connect(mt5)

closing_values = func.get_closing_value(mt5, tt)

while True:
	func.show_variation_porcentage(closing_values, mt5, tt)
	sleep(.5)


while True:
    func.show_variation_porcentage(closing_values, mt5)

