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
    import os
    import sys
    sys.path.append(os.path.dirname(__file__))
    from scripts import Skits

ScriptName = "Phrase"
Website = "https://www.lmgtfy.com"
Description = "Phrase Script for the feelz"
Creator = "Xinthral"
Version = "0.0.3"
Command = "!phrase"
SQLTable = 'phrases'

# def send_message(message):
#     Parent.SendStreamMessage(message)
#     return

# def Log(message):
#     """ Log output to Built-in Logfile """
#     Parent.Log(Command, message)
#     return

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
