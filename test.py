from UnreadChecker import UnreadChecker
import time
import numpy as np
import threading

def DictReader(path):
    f = open(path)
    contents = f.read().split('\n')
    f.close()
    EmailDict = {}
    for item in contents:
        temp = item.split(':')
        if len(temp) == 2:
            EmailDict[temp[0]] = temp[1]
    return EmailDict

def ReadEmail(EmailDict, boxName = 'INBOX'):
    checker = UnreadChecker(EmailDict['EmailName'], EmailDict['host'], EmailDict['port'], EmailDict['user'], EmailDict['pw'])
    checker.login()
    checker.setBox(boxName)
    out = checker.RenderOutput()
    checker.logout()
    return out

def ReadAllEmail():
    EmailNames = np.loadtxt('Profiles/EmailList.txt', dtype=str)
    outputs = []
    for i in range(len(EmailNames)):
        EmailName = EmailNames[i]
        EmailDict = DictReader('Profiles/' + EmailName + '.txt')
        temp = ReadEmail(EmailDict)
        if temp != None:
            outputs.append(temp)
    if len(outputs) != 0:
        return ''.join(outputs)
    else:
        return 'No Mail'

def RepeatCheck():
    threading.Timer(60.0, RepeatCheck).start()
    print(ReadEmail())

RepeatCheck()

