prompt = input('Enter file name ')
try: 
    handle = open(prompt)
except:
    print('File cannot be opened:', prompt)
    exit()
#handle = open('mbox-short.txt')
temail = dict()
for line in handle :
    if line.startswith('From ') :
        words = line.split()
        #print(words)
        emails = words[1]
        #print(emails)
        temail[emails] = temail.get(emails,0) +1

maximum = None
maxword = None
for email,count in temail.items() :
    if maximum is None or count > maximum:
        maximum = count
        maxword = email

print(maxword, maximum)

#print(temail)