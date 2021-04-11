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
    from xsql import Database
    import random
    import sqlite3
    import time

ScriptName = "Joke"
Website = "https://www.lmgtfy.com"
Description = "Joke Script for the lulz"
Creator = "Xinthral"
Version = "0.0.1"
Command = "!joke"
SQLTable = 'jokes'
TextRepo = list()

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
    Parent.log(Command, message)
    return

def Init():
    """ Constructor API Method """
    global TextRepo
    TextRepo = Database.queryTableAll(SQLTable)
    random.seed(time.time())
    return

def Execute(data):
    """ Command Execution Method """
    if data.GetParam(0) != Command:
        return

    Log(data.getParam(1))
    for line in getText()[1].split(Database._delim):
        send_message(line)
        time.sleep(2)
    return

def Tick():
    """ Timed Event Loop Method """
    return

# Xinthral's Sql Handler file
