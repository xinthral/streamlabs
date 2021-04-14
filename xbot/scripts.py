try:
    import clr
    clr.AddReference("IronPython.SQLite.dll")
    clr.AddReference("IronPython.Modules.dll")
except:
    pass
finally:
    import os
    import random
    import sqlite3
    import sys
    import time
    sys.path.append(os.path.dirname(__file__))
    from settings import MySettings
    from xsql import Database

random.seed(time.time())
Options = MySettings._Options
Facts = list()
Jokes = list()
Phrases = list()
Rathers = list()

def getFact(Parent):
    """ Randomly Query a fact from the internets """
    url = "http://randomfactgenerator.net/"
    fact = Parent.GetRequest(url, {})
    return(fact.split("<div id='z'>")[1].split("<br/>")[0])

def getRepo(SQLTable):
    """ Select active repository """
    global Facts, Jokes, Phrases, Rathers
    responseRepo = None
    if SQLTable == 'facts':
        responseRepo = Facts
    if SQLTable == 'jokes':
        responseRepo = Jokes
    if SQLTable == 'phrases':
        responseRepo = Phrases
    if SQLTable == 'wur':
        responseRepo = Rathers
    return(responseRepo)

def getText(Parent, SQLTable):
    """ Return output text for given input command """
    TextRepo = getRepo(SQLTable)
    responseText = None

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
    # global Options
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
