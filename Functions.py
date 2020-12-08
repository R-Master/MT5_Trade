from datetime import datetime,timedelta
import pandas, pytz, Configs
from Tikers import tiker_list as tiker_list_file
from time import sleep
from os import system

if Configs.region_timezone != "":
    timezone = pytz.timezone("Etc/" + Configs.region_timezone)
else:
    timezone = pytz.timezone("Etc/GMT")

def get_dates():

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    return today, yesterday, tomorrow


def get_closing_value(mt, *tikers):

    today, yesterday, tomorrow = get_dates()

    close_hour = Configs.market_closing_hour
    close_minute = Configs.market_closing_minutes

    if tikers:
        tiker_list = tikers[0]
        timer = 0
    else:
        tiker_list = tiker_list_file
        timer = 0.2

    closing_yesterday_rate = {}

    closing_time = datetime(yesterday.year,
                            yesterday.month,
                            yesterday.day,
                            close_hour + 1,
                            close_minute + 20,
                            tzinfo=timezone)

    for tiker in tiker_list:

        closing_rate = mt.copy_rates_from(tiker, mt.TIMEFRAME_M1, closing_time, 1)
        if closing_rate is None:
            print(tiker)
        else:
            closing_rate = list(closing_rate)
            closing_yesterday_rate[tiker] = closing_rate[0][4]
        sleep(timer)

    return closing_yesterday_rate



def get_current_value(mt, *tikers):

    current_tiker = {}

    today = datetime.today() - timedelta(seconds=2)
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    minute = today.minute
    second = today.second

    if tikers:
        tiker_list = tikers[0]
        timer = 0
    else:
        tiker_list = tiker_list_file
        timer = 1

    date_time = datetime(year,
                         month,
                         day,
                         hour,
                         minute,
                         second,
                         tzinfo=timezone)

    for tiker in tiker_list:
        tik_value = mt.copy_ticks_from(tiker, date_time, 1, mt.COPY_TICKS_ALL)
        if tik_value is None:
            print("Error! Tiker {} is not valid." . format(tiker))
        else:
            tik_value = list(tik_value)
            current_tiker[tiker] = tik_value[0][3]

            sleep(timer)

    return current_tiker

def show_variation_porcentage(closing_prices, mt5, *tikers):

    variation_porcentage_value = {}
    variation_porcentage_dataframe = []

    if tikers:
        tiker_list = tikers[0]
        curr_value = get_current_value(mt5, tiker_list)
    else:
        tiker_list = tiker_list_file
        curr_value = get_current_value(mt5)

    for tiker in tiker_list:

        temp = curr_value[tiker]/closing_prices[tiker]
        variation_porcentage_value[tiker] = temp

        if temp == 0.0 or temp == 1.0:
            temp = "{:.2f} %" .format(0.00)
            index = 1000
        elif temp < 1.0:
            temp = 1 - temp
            index = 1000 - temp
            temp = "- {:.2f} %" .format(round(temp * 100, 2))
        elif temp > 1.0:
            temp = temp - 1
            index = 1000 + temp
            temp = "+ {:.2f} %" .format(round(temp * 100, 2))


        variation_porcentage_dataframe.append((index, tiker, temp,(curr_value[tiker]), (closing_prices[tiker])))
        variation_porcentage_dataframe.sort(reverse=True)

    DF = pandas.DataFrame(variation_porcentage_dataframe).drop(columns=0)

    clear = lambda: system('cls')
    clear()

    print('')
    print('-------------------------------')
    print(DF)

