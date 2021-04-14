"""
SLCB runs on IronPython, those cheeky whores:
https://stackoverflow.com/a/66794423/13825434
"""
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

ScriptName = "Joke"
Website = "https://www.lmgtfy.com"
Description = "Joke Script for the lulz"
Creator = "Xinthral"
Version = "0.0.3"
Command = "!joke"
SQLTable = 'jokes'
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
