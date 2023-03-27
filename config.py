import mysql.connector


is_production = False
debug_mode = False



log_level = "DEBUG"
LOGFILENAME = "error.log"
dict_Config = {
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] {(%(threadName)-9s) %(pathname)s:%(funcName)s:%(lineno)d} %(levelname)s - %(message)s',
    }},
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': LOGFILENAME,
            'encoding': 'utf-8',
            'when': 'midnight',
            'interval': 1,
            'backupCount': 5
        },

        'graypy': {
            'level': 'DEBUG',
            'class': 'graypy.GELFUDPHandler',
            'host': 'graylog.rezo.ai',
            'port': 9515,
        }

        # ,
        #
        # 'console': {
        #     'level': 'DEBUG',
        #     'formatter': 'detailed',
        #     'class': 'logging.StreamHandler',
        #     'stream': 'ext://sys.stdout'
        # }
    },
    'root': {
        'level': log_level,
        'handlers': ['default','graypy']
    },
}


app_password = 'awseadfasdfkajsklfadslfkadsjklafladjljadsflkads'
app_write_password = 'nasklfjkdasjflkjadslkfoi2uerioaslkfdnklasnfahudof'


def getConnection():
    mydb = mysql.connector.connect(host='localhost',
                                   user='rezoadmin',
                                   password='Rezo#!54312aI',
                                   db='helper_db')

    return mydb


def closeConnection(mydb):
    if mydb is not None:
        mydb.close()
