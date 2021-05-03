handle = open('mbox-short.txt')

domains = dict()
for line in handle :
    if line.startswith('From ') :
        words = line.split()
        email = words[1]
        splitdomain = email.split('@')
        domain = splitdomain[1]
        domains[domain] = domains.get(domain,0) + 1

print(domains)

#maximum = None
#bigdomain = None 
#for d,c in domains.items() :
#    if maximum is None or c > maximum :
#        maximum = c
#        bigdomain = d

#print(bigdomain, maximum)
