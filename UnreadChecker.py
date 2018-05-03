import imaplib
from email.parser import HeaderParser
from DecodeUser import usercode
import codecs

class UnreadChecker:
    def __init__(self, EmailName, host, port, user, pw):
        self.EmailName = EmailName
        self.host = host
        self.port = port
        self.user = user
        self.pw = pw
        
    def login(self):
        uc = usercode()
        pw1 = uc.decode(self.pw)
        self.M = imaplib.IMAP4_SSL(host=self.host, port=self.port)
        self.M.login(self.user, pw1)
        
    def logout(self):
        self.M.logout()
    
    def setBox(self, boxName):
        self.M.select(boxName, True)
    
    def UnreadName(self):
        typ, data = self.M.search(None, '(UNSEEN)')
        return data[0].split()
    
    def UnreadList(self):
        nameList = self.UnreadName()
        subjectList = []
        fromList = []
        if len(nameList) != 0:
            for name in nameList:
                typ, data = self.M.fetch(name, '(BODY[HEADER])')
                header = data[0][1]
                parser = HeaderParser()
                msg = parser.parsestr(header.decode("utf-8") )
                subjectList.append(msg['Subject'])
                fromList.append(msg['From'])
            return fromList, subjectList
        else:
            return [], [] 
        
    def RenderOutput(self):
        spliter = '#############'
        fromList, subjectList = self.UnreadList()
        if len(fromList) != 0:
            output = spliter + '\n'
            output = output + '#' + self.EmailName + ':\n'
            for i in range(len(fromList)):
                output = output + '#' + fromList[i] + ': ' + subjectList[i] + '.\n'
            output = output + spliter + '\n'
        else:
            output = None
        return output
        
        
    
