import Credentials as credentials

def meta5_close_conn(mt):

    mt.shutdown()

def conn_status(mt):

    print("Connection Status: {}".format(mt.terminal_info()._asdict()["connected"]))

def meta5_release(mt):

    print("MetaTrader5 package author: ", mt.__author__)
    print("MetaTrader5 package version: ", mt.__version__)

def meta5_info(mt):

    print(mt.terminal_info())

def meta5_connect(mt):

    if not mt.initialize(login=credentials.log_info['login'],
                         server=credentials.log_info['server'],
                         password=credentials.log_info['password']):

        print("initialize() failed, error code =", mt.last_error())
        quit()


