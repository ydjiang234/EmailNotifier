from UnreadChecker import UnreadChecker
'''
EmailName = 'FEUP'
host='imap.fe.up.pt'
port=993
user = 'yjiang'
pw = 'Iao901011'
a = UnreadChecker(EmailName, host, port, user, pw)
a.login()
a.setBox('INBOX')
out = a.RenderOutput()
print(out)
a.logout()
'''
f = open('Profiles/163.txt')
content = f.read()
f.close()
contents = content.split('\n')
dict1 = {}
for item in contents:
    temp = item.split(':')
    dict1[temp[0]] = temp[1]

b = UnreadChecker(dict1['EmailName'], dict1['host'], dict1['port'], dict1['user'], dict1['pw'])
b.login()
b.setBox('INBOX')
out = b.RenderOutput()
print(out)
b.logout()
