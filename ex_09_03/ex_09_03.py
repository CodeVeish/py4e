prompt = input('Enter file name ')
try: 
    handle = open(prompt)
except:
    print('File cannot be opened:', prompt)
    exit()

temail = dict()
for line in handle :
    if line.startswith('From ') :
        words = line.split()
        #print(words)
        emails = words[1]
        #print(emails)
        temail[emails] = temail.get(emails,0) +1

print(temail)