try:
    import sqlite3
except:
    import clr
    clr.AddReference("IronPython.SQLite.dll")
    clr.AddReference("IronPython.Modules.dll")
finally:
    import os
    import random
    import sys
    import time
    sys.path.append(os.path.dirname(__file__))
    from settings import MySettings
    from xsql import Database

random.seed(time.time())
Options = ['add', 'del', 'rem' ,'list', 'search', 'find']
Facts = list()
Jokes = list()
Phrases = list()
Rathers = list()

def getFact(Parent):
    """ Randomly Query a fact from the internets """
    url = "http://randomfactgenerator.net/"
    fact = Parent.GetRequest(url, {})
    # Log(Parent, '!fact', fact.split("<div id='z'>")[1].split("<br/>")[0])
    return(fact.split("<div id='z'>")[1].split("<br/>")[0])

def getText(Parent, SQLTable):
    global Facts, Jokes, Phrases, Rathers
    responseText = None
    TextRepo = None

    if SQLTable == 'facts':
        TextRepo = Facts
    if SQLTable == 'jokes':
        TextRepo = Jokes
    if SQLTable == 'phrases':
        TextRepo = Phrases
    if SQLTable == 'wur':
        TextRepo = Rathers

    if SQLTable == 'facts':
        responseText = (0, getFact(Parent),)
    elif len(TextRepo) == 0:
        TextRepo = Database.queryTableAll(SQLTable)
    elif len(TextRepo) == 1:
        responseText = TextRepo.pop(0)
        TextRepo = Database.queryTableAll(SQLTable)

    if responseText == None:
        responseText = TextRepo.pop(random.randrange(0, len(TextRepo)))

    return(responseText)

def Log(Parent, Command, message):
    """ Log output to Built-in Logfile """
    Parent.Log(Command, message)
    return

def send_message(Parent, message):
    """ Send Message to Channel """
    Parent.SendStreamMessage(message)
    return

def Skits(Command, SQLTable, Parent, data):
    global Options
    Settings = MySettings(Command, 'settings.json')
    if data.GetParam(0).lower() == Command:
        if data.GetParam(1).lower() not in Options:
            for line in getText(Parent, SQLTable)[1].split(Database._delim):
                Log(Parent, Command, line)
                send_message(Parent, line)
                time.sleep(2)
        else:
            """ handle options """
            send_message('Your command shall not pass.')
