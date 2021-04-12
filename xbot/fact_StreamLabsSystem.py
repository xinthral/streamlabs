"""
SLCB runs on IronPython, those cheeky whores:
https://stackoverflow.com/a/66794423/13825434
"""
try:
    import sqlite3
except:
    import clr
    clr.AddReference("IronPython.SQLite.dll")
    clr.AddReference("IronPython.Modules.dll")
finally:
    import sys
    import nt
    sys.path.insert(1, nt.getcwd() + "\\Services\\Scripts\\xbot")
    from settings import MySettings
    from xsql import Database
    import random
    import sqlite3
    import time

ScriptName = "Fact"
Website = "https://www.lmgtfy.com"
Description = "Fact Script for the infoz"
Creator = "Xinthral"
Version = "0.0.2"
Command = "!fact"
SQLTable = 'facts'
TextRepo = list()
Options = list()
Settings = dict()

def getText():
    global TextRepo
    if len(TextRepo) <= 1:
        lastValue = TextRepo.pop(0)
        TextRepo = Database.queryTableAll(SQLTable)
        return(lastValue)
    return(TextRepo.pop(random.randrange(0, len(TextRepo))))

def send_message(message):
    Parent.SendStreamMessage(message)
    return

def Log(message):
    """ Log output to Built-in Logfile """
    Parent.Log(Command, message)
    return

def getFact():
    """ Randomly Query a fact from the internets """
    url = "http://randomfactgenerator.net/"
    fact = Parent.GetRequest(url, {})
    return(fact.split("id='z'>")[1].split("<br/>")[0])

def Init():
    """ Constructor API Method """
    global Options, Settings, TextRepo
    Options = ['add', 'del', 'rem' ,'list', 'search', 'find']
    Settings = MySettings(Command, 'settings.json')
    TextRepo = Database.queryTableAll(SQLTable)
    random.seed(time.time())
    return

def Execute(data):
    """ Command Execution Method """
    global Options, Settings
    if data.GetParam(0).lower() == Command:
        if data.GetParam(1).lower() not in Options:
            Log(data.GetParam(1))
            send_message(getFact())
            # for line in getText()[1].split(Database._delim):
            #     send_message(line)
            #     time.sleep(2)
        else:
            """ handle options """
            send_message('Your command shall not pass.')
    return

def Tick():
    """ Timed Event Loop Method """
    return

# Xinthral's Sql Handler file
