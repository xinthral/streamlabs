try:
    import clr
    clr.AddReference("IronPython.SQLite.dll")
    clr.AddReference("IronPython.Modules.dll")
except:
    pass
finally:
    import os
    import random
    import re
    import sqlite3
    import sys
    import time
    sys.path.append(os.path.dirname(__file__))
    from settings import MySettings
    from xsql import Database

""" Globals """
random.seed(time.time())
Options = MySettings._Options
Version = MySettings._Version
versionRegex = re.compile(r"(\d\.\d\.\d)")
versionURL = 'https://raw.githubusercontent.com/xinthral/streamlabs/main/version.txt'
Facts = list()
Fortunes = list()
Jokes = list()
Phrases = list()
Rathers = list()

def checkVersion(Parent):
    """ Call back function to check github version """
    # '{\n "code": 200,\n "response": "0.0.1\n"\n}'
    req = Parent.GetRequest(versionURL, {})
    latestVersion = versionRegex.search(req).group(0)
    updateMessage = "xBot has an update pending : {}".format(latestVersion)
    if latestVersion != Version:
        Log(Parent, 'VersionCheck', updateMessage)
        send_message(Parent, updateMessage + ': https://github.com/xinthral/streamlabs/blob/main/xbot.zip')

def getFact(Parent):
    """ Randomly Query a fact from the internets """
    url = 'http://randomfactgenerator.net/'
    raw_html = Parent.GetRequest(url, {})
    fact = raw_html.split("<div id='z'>")[1].split('<br/>')[0]
    Database.insertFact((fact, 'random', 1))
    return(fact)

def getRepo(SQLTable):
    """ Select active repository """
    global Facts, Fortunes, Jokes, Phrases, Rathers
    responseRepo = None
    if SQLTable == 'facts':
        responseRepo = Facts
    if SQLTable == 'fortunes':
        responseRepo = Fortunes
    if SQLTable == 'jokes':
        responseRepo = Jokes
    if SQLTable == 'phrases':
        responseRepo = Phrases
    if SQLTable == 'rather':
        responseRepo = Rathers
    return(responseRepo)

def getText(Parent, SQLTable):
    """ Return output text for given input command """
    TextRepo = getRepo(SQLTable)
    responseText = None

    if SQLTable == 'facts':
        responseText = (0, getFact(Parent),)
    elif SQLTable == 'admin':
        responseText = (0, 'Session Lock Complete...',)
        os.system('python2 ./Services/Scripts/xbot/dbtables.py')
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
        # checkVersion(Parent)
        if data.GetParam(1).lower() not in Options:
            for line in getText(Parent, SQLTable)[1].split(Database._delim):
                Log(Parent, Command, line)
                send_message(Parent, line)
                time.sleep(2)
        else:
            """ handle options """
            send_message('Your command shall not pass.')
