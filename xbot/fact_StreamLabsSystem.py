try:
    import clr
    clr.AddReference("IronPython.Modules.dll")
except:
    pass
finally:
    import os
    import sys
    sys.path.append(os.path.dirname(__file__))
    from settings import MySettings
    from scripts import Skits

ScriptName = "Fact"
Website = "https://www.lmgtfy.com"
Description = "Fact Script for the infoz"
Creator = "Xinthral"
Version = "0.0.3"
Command = "!fact"
SQLTable = 'facts'
Options = MySettings._Options

def Init():
    """ Constructor API Method """
    return

def Execute(data):
    """ Command Execution Method """
    Skits(Command, SQLTable, Parent, data)
    return

def Tick():
    """ Timed Event Loop Method """
    return

# Xinthral's Sql Handler file

# def send_message(message):
#     Parent.SendStreamMessage(message)
#     return

# def Log(message):
#     """ Log output to Built-in Logfile """
#     Parent.Log(Command, message)
#     return

# def getFact():
#     """ Randomly Query a fact from the internets """
#     url = "http://randomfactgenerator.net/"
#     fact = Parent.GetRequest(url, {})
#     return(fact.split("id='z'>")[1].split("<br/>")[0])
