from UnreadChecker import UnreadChecker
from tkinter import Tk, Label, Button
from InfoWindow import InfoWindow
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
        output =  ''.join(outputs)
        return output
    else:
        return None

def showNotification(msg):
    root = Tk()
    iw = InfoWindow(root, msg)
    root.mainloop()

def RepeatCheck():
    out = ReadAllEmail()
    while True:
        if out!=None:
            #t2 = threading.Thread(target=showNotification, name="InfoWindow", args=(out,))
            #t2.run()
            print(out)
        else:
            curTime = time.localtime()
            print('{0}-{1}-{2}, {3}:{4} -- No new Email.'.format(curTime[0], curTime[1], curTime[2], curTime[3], curTime[4]))
        #threading.Timer(20.0, RepeatCheck).start()
        time.sleep(1800.0)
        out = ReadAllEmail()
t1 = threading.Thread(target=RepeatCheck, name="Checker")
global t2
t2 = threading.Thread(target=showNotification, name="InfoWindow")
t1.run()
